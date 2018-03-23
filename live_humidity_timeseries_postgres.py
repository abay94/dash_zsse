from dash.dependencies import Input, Output, State, Event
import plotly.plotly as py
from plotly.graph_objs import *
from scipy.stats import rayleigh
from flask import Flask
import numpy as np
import pandas as pd
import os
import sqlite3
import datetime as dt
import psycopg2
import dash
import dash_html_components as html
import dash_core_components as dcc
app = dash.Dash('streaming-wind-app')
server = app.server

app.layout = html.Div([
    html.Div([
        html.H2("Humidity warehouse"),
        html.Img(src="http://3sc.kz/ru/page/nashi-klienty"),
    ], className='banner'),
    html.Div([
        html.Div([
            html.H3("Humidity (percentage)")
        ], className='Title'),
        html.Div([
            dcc.Graph(id='wind-speed'),
        ], className='twelve columns wind-speed'),
        dcc.Interval(id='wind-speed-update', interval=60000, n_intervals=0),
    ], className='row wind-speed-row'),
], style={'padding': '0px 10px 15px 10px',
          'marginLeft': 'auto', 'marginRight': 'auto', "width": "900px",
          'boxShadow': '0px 0px 5px 5px rgba(204,204,204,0.4)'})
@app.callback(Output('wind-speed', 'figure'), [Input('wind-speed-update', 'n_intervals')])
def gen_wind_speed(value):
    conn = psycopg2.connect("dbname='zsse' user='postgres' host='192.168.1.92' password='postgres'")
    df1 = pd.read_sql_query('select * from "warehouse_ana"', con = conn)
    df = df1.iloc[-200:]
    trace = Scatter(
        y=df['rasp_temp'],
        line=Line(
            color='#42C4F7'
        ),
        hoverinfo='skip',
        error_y=ErrorY(
            type='data',
            array=df['rasp_temp'],
            thickness=1.5,
            width=2,
            color='#B4E8FC'
        ),
        mode='lines'
    )

    layout = Layout(
        height=450,
        xaxis=dict(
            range=[0, 200],
            showgrid=False,
            showline=False,
            zeroline=False,
            fixedrange=True,
            tickvals=[0, 50, 100, 150, 200],
            ticktext=['0', '50', '100', '150', '200'],
            title='Time Elapsed (sec)'
        ),
        yaxis=dict(
            range=[min(0, min(df['rasp_temp'])),
                   max(45, max(df['rasp_temp'])+max(df['rasp_temp']))],
            showline=False,
            fixedrange=True,
            zeroline=False,
            nticks=max(6, round(df['rasp_temp'].iloc[-1]/10))
        ),
        margin=Margin(
            t=45,
            l=50,
            r=50
        )
    )

    return Figure(data=[trace], layout=layout)


if __name__ == '__main__':
    app.run_server()