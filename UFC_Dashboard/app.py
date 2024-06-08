from flask import Flask, render_template
from dash import Dash, dcc, html
import pandas as pd

# Initialize Flask app
app = Flask(__name__)

# Initialize Dash app
dash_app = Dash(__name__, server=app, url_base_pathname='/dash/')

# Read CSV files
df1 = pd.read_csv('/Users/smallbrain/Desktop/archive/events.csv')
df2 = pd.read_csv('/Users/smallbrain/Desktop/archive/fighters.csv')
df3 = pd.read_csv('/Users/smallbrain/Desktop/archive/fights.csv')
df4 = pd.read_csv('/Users/smallbrain/Desktop/archive/referees.csv')

# Layout for Dash app
dash_app.layout = html.Div([
    dcc.Tabs([
        dcc.Tab(label='Events', children=[
            dcc.Graph(
                figure={
                    'data': [
                        {'x': df1['date'], 'y': df1['title'], 'type': 'bar', 'name': 'Events'}
                    ],
                    'layout': {
                        'title': 'Events Data'
                    }
                }
            )
        ]),
        dcc.Tab(label='Fighters', children=[
            dcc.Graph(
                figure={
                    'data': [
                        {'x': df2['name'], 'y': df2['wins'], 'type': 'bar', 'name': 'Fighters'}
                    ],
                    'layout': {
                        'title': 'Fighters Data'
                    }
                }
            )
        ]),
        dcc.Tab(label='Fights', children=[
            dcc.Graph(
                figure={
                    'data': [
                        {'x': df3['winner_name'], 'y': df3['round'], 'type': 'bar', 'name': 'Fights'}
                    ],
                    'layout': {
                        'title': 'Fights Data'
                    }
                }
            )
        ]),
        dcc.Tab(label='Referees', children=[
            dcc.Graph(
                figure={
                    'data': [
                        {'x': df4['name'], 'y': df4['n_fights'], 'type': 'bar', 'name': 'Referees'}
                    ],
                    'layout': {
                        'title': 'Referees Data'
                    }
                }
            )
        ])
    ])
])

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
