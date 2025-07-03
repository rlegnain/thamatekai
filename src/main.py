"""Main app."""


import dash
from dash import dcc, html, no_update, Patch
from dash_extensions import Keyboard
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

# from pages import chatbot

# ##############################################################################
#                                Init and Config
# ##############################################################################
# Initialize the Dash app
app = dash.Dash(
    __name__,
    pages_folder="pages",
    use_pages=True,
    assets_folder="assets",
    external_stylesheets=[
        # dbc.themes.BOOTSTRAP, 
        "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css"]
)


# ======================================================================
#                                 Layout
# ======================================================================
app.layout = html.Div(dash.page_container)


# ##############################################################################
#                            Run The app
# ##############################################################################
if __name__ == '__main__':
    app.run_server(debug=True, port=8060)

