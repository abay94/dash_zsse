#!/usr/bin/python2.4
#
# Small script to show PostgreSQL and Pyscopg together
#

import psycopg2
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State, Event

app = dash.Dash()

app.layout = html.Div([
    html.Label('Enter the db name'),
    html.Div(dcc.Input(id='db_name', type='text')),

    html.Label('Enter user name'),
    html.Div(dcc.Input(id='db_user', type='text')),

    html.Label('Enter the password'),
    html.Div(dcc.Input(id='db_passw', type='text')),

    html.Label('Enter the Host'),
    html.Div(dcc.Input(id='db_host', type='text')),

    html.Button('Submit', id='button'),

    html.Div([
            dcc.Markdown(("""
                **ALL TAGS**
                """))]),
    html.Div(dcc.Dropdown(
        id='dropdown_example',
        multi=True
        # options=[
        #     {'label': 'Coke', 'value': 'COKE'},
        #     {'label': 'Tesla', 'value': 'TSLA'},
        #     {'label': 'Apple', 'value': 'AAPL'}
        # ],
        # value='COKE'
    ))
])




@app.callback(
    Output('dropdown_example', 'options'),
    inputs=[Input('button', 'n_clicks')],
    state=[State('db_name', 'value'),
           State('db_user', 'value'),
           State('db_passw', 'value'),
           State('db_host', 'value')])
def pull_all_tags(numb_clicks, name, name1, passw, host):
    connection_string = "dbname=" + str(name) + " " + "user=" + str(name1) + " " + "host=" + str(host)+ " password="+ passw

    if (name is not None) and (name1 is not None):
        # conn = psycopg2.connect("dbname='zsse' user='postgres' host='192.168.1.92' password='postgres'")
        conn = psycopg2.connect(connection_string)
        cur = conn.cursor()
        cur.execute("""SELECT * from warehouse_ana""")
        colnames = [desc[0] for desc in cur.description]
    # dropdown_list = []
    # element = []
    # for i in range(len(colnames)):
    #     s = "{'label':" + colnames[i] + ", 'value': " + colnames[i]+"}"
    #     # element[i] = s
    #     dropdown_list.append(s)

    return [{
                    'label': i,
                    'value': i
                } for i in colnames]

if __name__ == '__main__':
    app.run_server(debug=True)



