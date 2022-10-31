from dash import Dash, dcc, html
from dash.dependencies import Input, Output
from components.insecurity_component import graph_map
import plotly.express as px
app = Dash(__name__)

app.layout = html.Div(style={},children=[
    dcc.Tabs(id="tabs-with-props", value='tab-1', style={'color':'white'},children=[
        dcc.Tab(label='Inseguridad', value='tab-1'),
        dcc.Tab(label='Corrupción', value='tab-2'),
        dcc.Tab(label='Educación', value='tab-3'),
    ], colors={
        "border": "white",
        "primary": "#2d2d2d",
        "background": "#2d2d2d"
    }),
    html.Div(id='tabs-content-props-4'),
    dcc.Dropdown(
                    id='year_selected',
                    options=[
                        {"label":"joly", "value":"joly"},
                        {"label":"Coderre", "value":"Coderre"},
                        {"label":"Bergeron", "value":"Bergeron"},
                    ],
                    multi=False,value=2018,
                ),
            html.Div(id='output_container', children=[]),
            html.Br(),

            dcc.Graph(id='my_map', figure={})
])

@app.callback(Output('tabs-content-props-4', 'children'),
              Input('tabs-with-props', 'value'))
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([

        ])
    elif tab == 'tab-2':
        return html.Div([
            html.H3('Tab content 2')
        ])
    elif tab == 'tab-3':
        return html.Div([
            html.H3('Tab content 3')
        ])

@app.callback(
    [Output(component_id='output_container', component_property='children'),
    Output(component_id='my_map', component_property='figure')],
    [Input(component_id='year_selected', component_property='value')]
    )

def graph_map(year_selected):
    df = px.data.election() # replace with your own data source
    geojson = px.data.election_geojson()
    fig = px.choropleth(
            df, geojson=geojson, color=candidate,
            locations="district", featureidkey="properties.district",
            projection="mercator", range_color=[0, 6500]
        )
    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)