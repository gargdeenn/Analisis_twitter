from dash import Dash, dcc, html, Input, Output
import plotly.express as px
from Conn.conn import conn
import plotly.graph_objects as go
import plotly.figure_factory as ff
app = Dash(__name__)

conexion = conn()
tweets = conexion.get_tweets()
cities = conexion.get_cities()
tweetsTemas = []
ciudades = []
union = []

app.layout = html.Div([
    dcc.Dropdown(['inseguridad', 'corrupción', 'educación'], value='inseguridad',id='demo-dropdown'),
    
    html.Div(style={'display':'flex'}, children=[
            dcc.Graph(id='graph_bar', figure={}),
            dcc.Graph(
                id='graph_pie',
                figure={},
                style={'width':'600px','height':'450px'},
            )

    ]),

])

@app.callback(
    Output('graph_bar', 'figure'),
    [Input('demo-dropdown', 'value')]
)

def graph_bar_output(value):
    tweetsTemas.clear()
    ciudades.clear()
    for city in range(len(cities)):
        contador: int = 0
        for i in range(len(tweets)):
            if tweets[i][5] in cities[city][0]:
                if tweets[i][4] in value:
                            contador = contador + 1
        tweetsTemas.append(contador)
        ciudades.append(cities[city][1])
    union = (tweetsTemas, ciudades)
    fig = ff.create_table(union, height_constant=10)
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

if __name__ == '__main__':
    app.run_server(debug=True)