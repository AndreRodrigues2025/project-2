# -*- coding: utf-8 -*-
"""
Created on Sun Mar 16 15:31:48 2025

@author: afa.rodrigues
"""

import dash
import dash_core_components as dcc
import dash_html_components as html

# Initialize Dash app
app = dash.Dash(__name__)

# Define Layout
app.layout = html.Div(children=[
    html.H1(children='IST Energy Monitor'),

    html.Div(children='''
        Visualization of total electricity consumption at IST over the last years
    '''),

    dcc.Graph(
        id='yearly-data',
        figure={
            'data': [
                {'x': [2017, 2018, 2019], 'y': [9709, 0, 0], 'type': 'bar', 'name': 'Total'},
                {'x': [2017, 2018, 2019], 'y': [1440, 1695, 0], 'type': 'bar', 'name': 'Civil'},
                {'x': [2017, 2018, 2019], 'y': [1658, 1598, 0], 'type': 'bar', 'name': 'Central'},
                {'x': [2017, 2018, 2019], 'y': [898, 1022, 0], 'type': 'bar', 'name': 'North Tower'},
                {'x': [2017, 2018, 2019], 'y': [1555, 1523, 0], 'type': 'bar', 'name': 'South Tower'},
            ],
            'layout': {
                'title': 'IST yearly electricity consumption (MWh)'
            }
        }
    )
])

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)
