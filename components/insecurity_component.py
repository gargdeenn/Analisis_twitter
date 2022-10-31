from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
app = Dash(__name__)

def graph_map(year_selected):
	fig = px.choropleth(
			location_mode='COP_colombia',
			locations='colombia',
			scope='cop',
			template='plotly_white'
		)