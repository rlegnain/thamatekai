from dash import html, dcc

waiting_response = dcc.Loading(
            className="app-status",
            children=[html.Div(id="app-status-id")],
            type="dot",
            color='#2596be'
        )


def ai_message(msg: str, uid: str):
    return html.Div(
        children=[
            html.I("", className="fas fa-robot", style={"padding-top": "10px"}),
            dcc.Markdown(msg, id=f'msg-{uid}'), 
        ],
        id={
            'type': 'messages-chat-box',
            'index': uid,
        },        
        className="message ai-message")


def human_message(msg:str, uid:str):
    return html.Div(
        children=[
            html.I("", className="fas fa-user", style={"padding-top": "10px"}),
            dcc.Markdown(msg, id=f'msg-{uid}'), 
        ],
        id={
            'type': 'messages-chat-box',
            'index': uid, 
        },
        className="message human-message")


def chat_messages_container():
    return html.Div(
        id="chat-messages-container-id",
        children="",
        style={
            "flex": "1",
            "overflow-y": "auto",
            "padding": "10px",
            "background-color": "rgba(0, 0, 1, .01)",
            "display": "flex",
            "flex-direction": "column",
            "gap": "10px",
            "width":"80%",
        })


# input message box
text_input = dcc.Textarea(
    id="input-textarea-id",
    placeholder="Type your message here...",
    rows=2,
    style={
        "flexGrow": "1", 
        "border": "none",
        "outline": "none", 
        "padding": "10px", 
        "borderRadius": "20px", 
        "overflow": "hidden",
        "resize": "none",
        "font-family": "Arial, sans-serif",
        }
)

send_btn = html.Button(
    html.I(className="fas fa-paper-plane"),
    title="Send Query",
    id="send-button-id",
    style={"backgroundColor": "transparent", "border": "none", "cursor": "pointer", "fontSize": "1.2em", "color": "#4CAF50"}
)

upload_btn = html.Button(
    html.I(className="fas fa-paperclip"),
    title="Upload file",
    id="upload-button-id",
    style={"backgroundColor": "transparent", "border": "none", "cursor": "pointer", "fontSize": "1.2em", "color": "#999"}
)

setting_btn = html.Button(
    html.I(className="fas fa-cogs"),
    title="settings",
    id="settings-button-id",
    style={"backgroundColor": "transparent", "border": "none", "cursor": "pointer", "fontSize": "1.2em", "color": "#288eb4"}
)


history_btn = html.Button(
    html.I(className="fa fa-history"),
    title="history",
    id="history-button-id",
    style={"backgroundColor": "transparent", "border": "none", "cursor": "pointer", "fontSize": "1.2em", "color": "#f7b16c"}
)


def input_message_box():
    return  html.Div( 
        id="input-box", 
        children=[text_input, send_btn, upload_btn, setting_btn, history_btn],
        style={
            "width": "70%", 
            "display": "flex", 
            "alignItems": "flex-end", 
            "gap": "10px", 
            "backgroundColor": "#fff", 
            "border": "1px solid #ccc",
            "borderRadius": "25px",
            "padding": "10px", 
            "boxShadow": "0 0 10px rgba(0, 0, 0, 0.4)"
             } )


def chat_box():
    return html.Div(
        children = [
            chat_messages_container(),
            waiting_response,
            input_message_box()], 
        style={
            "align-items": "center",
            # "justify-content": "center",
            "flex": "1",
            "display": "flex",
            "flex-direction": "column",
            "gap": "10px",
            "background-color": "#fff",
            "overflow": "hidden", # Prevent overflow 
        }
)

