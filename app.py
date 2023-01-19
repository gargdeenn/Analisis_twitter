from dash import Dash, dcc, html, Input, Output
import plotly.express as px
from Conn.conn import conn
import plotly.graph_objects as go
import plotly.figure_factory as ff
import pandas as pd
import geopandas as gpd
import numpy as np
# from geopandas import GeoDataFrame
# from shapely.geometry import Point

import folium
from folium import Choropleth
from folium.plugins import HeatMap
import json
from urllib.request import urlopen
with urlopen('https://gist.githubusercontent.com/john-guerra/43c7656821069d00dcbc/raw/be6a6e239cd5b5b803c6e7c2ec405b793a9064dd/Colombia.geo.json') as response:
    counties = json.load(response)
app = Dash(__name__)




conexion = conn()
tweets = conexion.get_tweets()
cities = conexion.get_cities()
tweetsTemas = []
ciudades = []
union = []
departamentos = ['CESAR','ATLANTICO','VALLE DEL CAUCA','CUNDINAMARCA','ANTIOQUIA']

app.layout = html.Div([
    dcc.Dropdown(['inseguridad', 'corrupción', 'educacion'], value='inseguridad',id='demo-dropdown'),
    
    html.Div(style={}, children=[
        html.Div(style={'display':'flex'}, children=[
            dcc.Graph(
                id='graph_map', 
                figure={},
                style={'width':'650px','height':'500px'},
                ),
            dcc.Graph(
                id='graph_pie',
                figure={},
                style={'width':'650px','height':'500'},
            ),    
        ]),
        dcc.Graph(
                id='graph_bar', 
                figure={},
                style={'width':'650px','height':'500'},
                ),
    ]),

])

@app.callback(
    Output('graph_bar', 'figure'),
    [Input('demo-dropdown', 'value')]
)

def graph_bar_output(value):
    tweetsTemas.clear()
    ciudades.clear()
    tweetsTemasaux = []
    for city in range(len(cities)):
        contador: int = 0
        for i in range(len(tweets)):
            if tweets[i][4] in cities[city][0].__str__():
                if tweets[i][3] in value:
                            contador = contador + 1
        tweetsTemas.append(contador)
        tweetsTemasaux.append(contador)
        ciudades.append(cities[city][1])
    union = (tweetsTemas, ciudades)
    tweetsTemasaux.sort(reverse=True)
    ciudadesaux= []
    posicion=[1,2,3,4,5]

    #print(tweetsTemas)
    for t in range(5):
        for u in range(5):
            if union[0][u] == tweetsTemasaux[t]:
                ciudadesaux.append(union[1][u])
    todo = (posicion,tweetsTemasaux,ciudadesaux)
    #print(tweetsTemasaux,ciudadesaux)
    print( np.ravel(todo, order='F'))
    tode = ( np.reshape(np.ravel(todo, order='F'), (5,3)) )
    print(tode)
    fig = ff.create_table(tode)
    trace1 = go.Bar(x=ciudades, y=tweetsTemas, xaxis='x2', yaxis='y2',
                marker=dict(color='#9CCC65'),
                name=f'{value}')
    fig.add_traces([trace1])
    fig['layout']['xaxis2'] = {}
    fig['layout']['yaxis2'] = {}
    fig.layout.yaxis.update({'domain': [0, .45]})
    fig.layout.yaxis2.update({'domain': [.6, 1]})
# The graph's yaxis2 MUST BE anchored to the graph's xaxis2 and vice versa
    fig.layout.yaxis2.update({'anchor': 'x2'})
    fig.layout.xaxis2.update({'anchor': 'y2'})
    fig.layout.yaxis2.update({'title': 'Numero de tweets'})
# Update the margins to add a title and see graph x-labels.
    fig.layout.margin.update({'t':75, 'l':50})
    fig.layout.update({'title': f'{value} en las ciudades principales del país'})
    fig.layout.update({'height':800})
    return fig

@app.callback(
    Output('graph_pie', 'figure'),
    [Input('demo-dropdown', 'value')]
)

def graph_pie_output(value):
    fig_pie = go.Figure(data=[go.Pie(labels=ciudades, values=tweetsTemas)])
    return fig_pie

@app.callback(
    Output('graph_map', 'figure'),
    [Input('demo-dropdown', 'value')]
)

def graph_mapp(value):
    for loc in counties['features']:
        loc['id'] = loc['properties']['NOMBRE_DPT']
    fig = go.Figure(go.Choroplethmapbox(
                    geojson=counties,
                    locations=departamentos,
                    z=tweetsTemas,
                    colorscale='Viridis',
                    colorbar_title="Número"))
    fig.update_layout(mapbox_style="carto-positron",
                        mapbox_zoom=3.5,
                        mapbox_center = {"lat": 4.570868, "lon": -74.2973328})
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)