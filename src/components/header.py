from dash import html


def header(title=''):
    return html.Header([
        html.Button(html.Span("\u2630"), id="toggleSidebar", className="icon-button"),
        html.H1(title)

    ], className="row_1")