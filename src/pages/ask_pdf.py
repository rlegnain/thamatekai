"""Main app."""


import dash
from dash import dcc, html, no_update, Patch
from dash_extensions import Keyboard
from dash.dependencies import Input, Output, State
# import dash_bootstrap_components as dbc

import components as ui
from utils import ai_llm_langchain as ullm
from utils import helper as uhf

# ##############################################################################
#                                Init and Config
# ##############################################################################
dash.register_page(
    __name__, 
    title="Ask PDF", 
    path="/ask-pdf",)
app = dash.get_app()

# ======================================================================
#                                 Layout
# ======================================================================
left_column = ui.sidebar([{"name": "AI Chatbot", "path": "/"}, {"name": "Ask PDF", "path": "/ask-pdf"}])

right_coulumn = html.Div(children=[ui.header("Ask PDF"), ui.chat_box()], className="col_2")


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

#"