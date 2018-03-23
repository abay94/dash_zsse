import dash
import dash_core_components as dcc
import dash_html_components as html
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
from sqlalchemy import create_engine
now = dt.datetime.now()
sec = now.second
minute = now.minute
hour = now.hour

total_time = ((hour - 10) * 3600) + ((minute - 10) * 60) + (sec)
# engine = create_engine(
#     'postgresql://' + os.environ['postgres'] + ':' + os.environ['postgres'] + '@' + os.environ['192.168.1.92'] + ':' + os.environ['5432'] + '/' + os.environ['zsse'],
#     echo=False)
conn = psycopg2.connect("dbname='zsse' user='postgres' host='192.168.1.92' password='postgres'")
# cur = conn.cursor()
df = pd.read_sql_query('select * from "warehouse_ana"', con = conn)
# rows = cur.fetchall()
# df = pd.DataFrame(rows)
# con = sqlite3.connect("./Data/wind-data.db")
# df = pd.read_sql_query('SELECT Speed, SpeedError, Direction from Wind where\
#                         rowid > "{}" AND rowid <= "{}";'
#                         .format(total_time-200, total_time), con)

print(df['power'].iloc[-200:])