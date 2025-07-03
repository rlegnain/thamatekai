"""Main app."""


import dash
from dash import dcc, html, no_update, Patch
from dash_extensions import Keyboard
from dash.dependencies import Input, Output, State
from dash_extensions import Keyboard

# import dash_bootstrap_components as dbc

import components as ui
from utils import ai_llm_langchain as ullm
from utils import helper as uhf

# ##############################################################################
#                                Init and Config
# ##############################################################################
dash.register_page(
    __name__, 
    title="AI Chatbot", 
    path="/",
    redirect_from=["/chatbot"]    )
app = dash.get_app()

# ======================================================================
#                                 Layout
# ======================================================================

left_column = ui.sidebar([{"name": "AI Chatbot", "path": "/"}, {"name": "Ask PDF", "path": "/ask-pdf"}])
right_coulumn = html.Div(children=[ui.header("Chatbot"), ui.chat_box()], className="col_2")


# App layout
layout = html.Div([
    html.Div([ 
        left_column,
        right_coulumn,
        dcc.Store(id="chat-history-id", data=[],),
        dcc.Store(id="query-storage-id", data=""),
        Keyboard(id="keyboard"),
        dcc.Store(id="selected-llm-id", data="llama3.2:3b")
    ], className="container")
])


# ##############################################################################
#                            Callbacks
# ##############################################################################

#"""Toggles the sidebar visibility based on the click count."""
@app.callback(
    Output("sidebar", "style"),
    Input("toggleSidebar", "n_clicks")
)
def on_toggle_sidebar_clicked(n_clicks: int):
    if n_clicks and n_clicks % 2 == 1:
        return {"display": "none"}
    return {"display": "block"}


# Send query when you left-clicked on send button.
@app.callback(
    Output("query-storage-id", "data", allow_duplicate=True),
    Input("send-button-id", "n_clicks"),
    State("input-textarea-id", "value"),
    prevent_initial_call=True,)
def on_send_btn_clicked(n_clicks, text):
    if not text:
        return no_update
    return {'prompt': text, 'file_data': "", 'file_icon': ""}


# """Handle the input and model selection, and update the output"""
@app.callback(
    Output("chat-history-id", "data",  allow_duplicate=True),
    Output("input-textarea-id", "value", allow_duplicate=True),
    Output("chat-messages-container-id", "children", allow_duplicate=True),
    Input("query-storage-id", "data"),
    State("chat-history-id", "data"),
    prevent_initial_call=True,)
def new_human_message(data_dict, chat_history):
    chat_box = Patch()
    if len(chat_history) > 0:
        chat_history = ullm.loads(chat_history) # de-serialize the chat_history
    
    user_msg = data_dict["prompt"]
    chat_history.append(ullm.HumanMessage(content=user_msg))
    chat_box.append(ui.human_message(chat_history[-1].content, uid=uhf.generate_id()))
    history = ullm.dumps(chat_history)
    return history, "", chat_box
    

# """Handle the input and model selection, and update the output"""
@app.callback(
    Output("chat-history-id", "data"),
    Output("chat-messages-container-id", "children", allow_duplicate=True),
    Output('app-status-id', 'children'),
    Input("chat-history-id", "data"),
    State("query-storage-id", "data"),
    State("selected-llm-id", "data"), 
    prevent_initial_call=True,)
def get_ai_message(chat_history, data_dict, model):
    chat_box = Patch()
    if len(chat_history) > 0:
        chat_history = ullm.loads(chat_history) # de-serialize the chat_history
    
    user_msg = data_dict["prompt"]
    ai_msg = ullm.invoke(user_msg, chat_history[-4::], model)
    chat_history.append(ullm.AIMessage(content=ai_msg))
    chat_box.append(ui.ai_message(ai_msg, uid=uhf.generate_id()))
    history = ullm.dumps(chat_history)
    return history, chat_box, ""


@app.callback(
    Output("send-button-id", "n_clicks"),
    Input("keyboard", "keydown"),
    Input("send-button-id", "n_clicks"),
    prevent_initial_call=True,)
def on_keyboard_pressed(keyEvent, n_click):
    if n_click is None:
        n_click = 0
    is_enter = uhf.is_enterKey(keyEvent)
    return n_click+1 if is_enter else no_update


@app.callback(
    Output('input-textarea-id', 'rows'),
    Input('input-textarea-id', 'value'),
    State('input-textarea-id', 'rows'),
    State('input-textarea-id', 'cols')
)
def adjust_textarea_rows(value, current_rows, cols ):
    print(cols)
    if value:
        print(len(value))
    if value:
        # Estimate rows based on the number of newlines and content length
        lines = value.split('\n')
        new_rows = len(lines) + 2  # Add extra row for spacing
        return max(new_rows, 2)  # Minimum of 2 rows
    return 2  # Default if empty



# ##############################################################################
#                            Run The app
# ##############################################################################
# if __name__ == '__main__':
#     app.layout = layout
#     app.run_server(debug=True, port=8060)

