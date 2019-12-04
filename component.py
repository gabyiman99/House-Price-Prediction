import dash
import json
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc

from model_predictor import Predictor

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

body = dbc.Container(
    html.Div(children=[
    html.Div(children=[
        html.H1('House Price Prediction Using Random Forest')
    ]),
    html.H4('In this app, we will try to predict the price of your dream house. So input the desired values of each feature that you want, or you can leave it in its deafult value. Make sure that your inputs are within the range of each feature.'),
    html.H6('Note that this app only predicts houses in the Washington, USA area so the predictions will only be accurate to houses in that area.'),
    html.Div(id = "madeby", children=[
        html.P('Made by: Licyawati Dewi, Gabriella')
    ]),
    dbc.Container(children=[
        html.P('Total bedroom: (Input the total of bedrooms that you want!)'),
    dbc.Input(id='input-1-state', type='number', value='3', placeholder='>=1'),
    html.P('Total bathroom: (Input the total of bathrooms that you want!)'),
    dbc.Input(id='input-2-state', type='number', value='2.5', placeholder='>=1'),
    html.P('Floor: (Input the total stories that you want! Add a half if you want an attic!)'),
    dbc.Input(id='input-3-state', type='number', value='1', placeholder='>1'),
    html.P('Waterfront: (Input 0 for no waterfront and 1 for a waterfront!)'),
    dbc.Input(id='input-4-state', type='number', value='0', placeholder='0 or 1'),
    html.P('View: (Input a number from 0-4! 0 for no view at all and 4 for the best view you can get!)'),
    dbc.Input(id='input-5-state', type='number', value='0', placeholder='0 - 4'),
    html.P('Condition: (Input a number from 1-5! 1 for the lowest condition and 5 for the best condition!)'),
    dbc.Input(id='input-6-state', type='number', value='3', placeholder='1-5'),
    html.P('Grade: (Input a number from 1-10! 1 for the lowest grade and 10 for the best grade!)'),
    dbc.Input(id='input-7-state', type='number', value='7', placeholder='1-10'),
    html.P('Square Feet of Above: (Input your desired size of upper floor!)'),
    dbc.Input(id='input-8-state', type='number', value='1570'),
    html.P('Square Feet of Basement: (Input your desired size of your basement, 0 if you do not desire basement!)'),
    dbc.Input(id='input-9-state', type='number', value='0', placeholder='>=0'),
    html.P('Year Built: (Input the year your desired house was built!)'),
    dbc.Input(id='input-10-state', type='number', value='2014'),
    html.P('Year Renovated: (Input the year your desired house was renovated, 0 if you do not want renovated house!)'),
    dbc.Input(id='input-11-state', type='number', value='0'),
    html.P('Zip Code: (Input the Zip Code of Washington area from between 98001 and 98199!)'),
    dbc.Input(id='input-12-state', type='number', value='98115', placeholder='98001 - 98199'),
    html.P('Latitude: (Input the latitude of your desired house!)'),
    dbc.Input(id='input-13-state', type='number', value='47.5491'),
    html.P('Longitude: (Input the longitude of your desired house!)'),
    dbc.Input(id='input-14-state', type='number', value='-122.29'),
    html.P('Square Feet of Living Room: (Input the desired size of your living room!)'),
    dbc.Input(id='input-15-state', type='number', value='1840', placeholder='>=0'),
    html.P('Square Feet of Lot: (Input the desired size of your lot!)'),
    dbc.Input(id='input-16-state', type='number', value='7620')
    ]),
    html.Div(children=[
        dbc.Button(id='submit-button', n_clicks=0, children='Predict!'),
        dbc.Alert(children=[
            html.H4(id = 'output-state')
        ])
    ])
])
)

app.layout = html.Div([body])

model_predictor = Predictor()

@app.callback(Output('output-state', 'children'),
              [Input(component_id='submit-button', component_property='n_clicks')],
              [State('input-1-state', 'value'),
               State('input-2-state', 'value'),
               State('input-3-state', 'value'),
               State('input-4-state', 'value'),
               State('input-5-state', 'value'),
               State('input-6-state', 'value'),
               State('input-7-state', 'value'),
               State('input-8-state', 'value'),
               State('input-9-state', 'value'),
               State('input-10-state', 'value'),
               State('input-11-state', 'value'),
               State('input-12-state', 'value'),
               State('input-13-state', 'value'),
               State('input-14-state', 'value'),
               State('input-15-state', 'value'),
               State('input-16-state', 'value')
               ])
def update_output(n_clicks: int,
                     bed: float, bath: float, floor: float, wf: float,
                     view: float, cond: float, grade: float, sabv: float, sbst: float,
                     yblt: float, yrnv: float, zipc: float, lat: float, lng: float, 
                     sliv15: float, slot15: float
                     ):
    if n_clicks is None:
        raise PreventUpdate
    else:
        data1 = model_predictor.predict(
            bed = bed,
            bath = bath,
            floor = floor,
            wf = wf,
            view = view,
            cond = cond,
            grade = grade,
            sabv = sabv,
            sbst = sbst,
            yblt = yblt,
            yrnv = yrnv,
            zipc = zipc,
            lat = lat,
            lng = lng,
            sliv15 = sliv15,
            slot15 = slot15
        )
        data = {
            'prediction': data1
        }
        
        return u'''
        The house price prediction is USD {},
        '''.format(data["prediction"])

if __name__ == '__main__':
    app.run_server(debug=True)