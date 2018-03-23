import dash
import dash_html_components as html
import datetime
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
app = dash.Dash(__name__)

# list_of_layout_parts = [html.Button('add', id = 'jai_goi'),
#                         html.Div(id='content')]

def serve_layout():
    list_for_content.remove(all(xrange(len(list_for_content))))
    return html.Div([html.Button('add', id = 'jai_goi'),
                        html.Div(id='content')])


app.layout = serve_layout

list_for_content = []


@app.callback(Output('content', 'children'),
    [Input('jai_goi', 'n_clicks')])
def update_layout(i):
    list_for_content.append(html.Button('created' + str(i), id='jai' + str(i)))
    return list_for_content

if __name__ == '__main__':
    app.run_server(debug=True)