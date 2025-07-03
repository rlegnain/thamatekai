from dash import dcc, html, no_update


def sidebar(links: dict):
    return html.Aside([
        html.P("Sidebar"), 
        navbar(links)
    ], id="sidebar")


def navbar(links: dict):
    if not links:
        links = []
    children = [nav_link(page['name'], page['path']) for page in links]
    return html.Div(
        children=children,
        id="navbar-container",
        style={
            "display": "flex",
            "flex-direction": "column",
            # "background-color": "#000",
            "gap": "5px",
            "padding": "10px",

        }
    )


def nav_link(label:str, href:str):
    return html.Div(
        id=f"container-link-{label}-id",
        children=[
            dcc.Link(
                label,
                href=href,
                id=f"link-{label}-id",
                style={
                    # "padding": "15px 20px",
                    "text-decoration": "none",
                    "font-size":" 14px",
                    "color": "white",
                    # "background-color":"red ",
                    # "border-radius": "10px",
                    "display": "block",


                }
            )
        ],
        style={
            "background-color": '#6496d9',
            "border-radius": "10px",
            "text-align": "center",
            "padding": "10px 10px",

        }
    )
