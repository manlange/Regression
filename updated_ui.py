"""import pandas as pd
import dash
import dash_bootstrap_components as dbc
from dash import html, dcc, dash_table
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)
df = pd.read_excel('/Users/manlange/Desktop/Rishab/17_14_1_Cycle1.xlsx')

# Define the dictionary for validation
validation_dict = {'ABCD': 'manlange'}

html_button = html.Div([
    html.Div([
        dbc.Button("Day 0", id="submit-buton", className="me-2", color="info"),
    ], style={'margin-right': '5px'}),
    html.Div([
        html.Button('Access Tokens', id='unlock-button', n_clicks=0, style={"color": "black", 'textAlign': 'center'}),
        dcc.Input(id='password-input', type='password', placeholder='Enter password', style={'margin-left': '10px'}),
        html.Div(id='output-1', className='py-3', style={'whitespace': 'pre-line', 'textAlign': 'center'}),
        html.Div(id='output-access-tokens', style={'textAlign': 'center', 'margin-top': '5px'}),
    ], style={'display': 'flex', 'align-items': 'center'}),
])

app.layout = html.Div([
    dbc.Card(
        [
            dbc.CardBody(
                [
                    html.H2("Comment Tracker", className="card-text", style={"color": "white", 'textAlign': 'center'}),
                ]
            )
        ],
        color="gray",
        outline=True,
        style={'height': '100px', 'margin-left': '10px', 'margin-right': '10px', 'margin-top': '10px'},
        className="shadow-sm p-3 mb-2 rounded"
    ),
    dbc.Card(
        [
            dbc.CardBody(
                [
                    html.Label('Active Release Cycle:'),
                    dcc.Dropdown(
                        id='dropdown-1',
                        options=[
                            {'label': '17.12.02 - Cycle 1', 'value': '17.12.02 - Cycle 1'},
                            {'label': '17.06.06 - Cycle 1', 'value': '17.06.06 - Cycle 1'},
                            {'label': '17.14.01 - Cycle 1', 'value': '17.14.01 - Cycle 1'},
                            {'label': '17.13.01 - Cycle 4', 'value': '17.13.01 - Cycle 4'}
                        ],
                        style={"color": "black", 'textAlign': 'center'},
                        value='option-1',
                    ),
                ]
            ),
        ],
        color="light",
        outline=True,
        style={'margin-bottom': '10px', 'margin-top': '10px', 'margin-right': '10px', 'margin-left': '10px', 'align-items': 'center'}
    ),
    dbc.Card(
        [
            dbc.CardBody(
                [
                    html.Label('Baseline Release Cycle:'),
                    dcc.Dropdown(
                        id='dropdown-2',
                        options=[
                            {'label': 'ACE', 'value': 'ACE'},
                            {'label': 'ASR1K', 'value': 'ASR1K'},
                            {'label': 'CSR', 'value': 'CSR'},
                            {'label': 'Curie', 'value': 'Curie'},
                            {'label': 'ENCS', 'value': 'ENCS'},
                            {'label': 'Fugazi', 'value': 'Fugazi'},
                            {'label': 'Greenday', 'value': 'Greenday'},
                        ],
                        style={"color": "black", 'textAlign': 'center'},
                        value='option-A'
                    ),
                ]
            ),
        ],
        color="light",
        outline=True,
        style={'margin-bottom': '10px', 'margin-top': '10px', 'margin-right': '10px', 'margin-left': '10px', 'align-items': 'center'}
    ),
    html.Div([
        html_button,  # Include the Access Tokens button here
    ], style={'display': 'flex', 'align-items': 'center', 'margin-top': '5px', 'padding': '5px'}),
    html.Div(id='output-2'),
    html.Div([
        dash_table.DataTable(
            id='table',
            columns=[
                {'name': col, 'id': col, 'editable': True if col == 'Comments' else False}
                for col in df.columns
            ],
            data=df.to_dict('records'),
            sort_action='native',  # Enable native sorting
            sort_mode='multi',     # Allow multi-column sorting
            style_table={'height': '300px', 'overflowY': 'auto'}  # Set a fixed height with scroll for the table
        )
    ]),
])


@app.callback(
    [Output('table', 'editable'),
     Output('output-1', 'children'),
     Output('output-access-tokens', 'children')],
    [Input('unlock-button', 'n_clicks')],
    [State('password-input', 'value')]
)
def update_content(unlock_clicks, password):
    ctx = dash.callback_context
    if not ctx.triggered:
        return False, '', ''

    trigger_id = ctx.triggered[0]['prop_id']

    if trigger_id == 'unlock-button.n_clicks':
        # Validate the access token
        if unlock_clicks > 0 and password in validation_dict:
            return True, f'Created By: {validation_dict[password]}', ''
        else:
            return False, 'Invalid access token', ''
    else:
        return False, '', ''


@app.callback(
    Output('table', 'data'),
    [Input('table', 'data_previous')],
    [State('table', 'data')]
)
def save_changes(previous_data, current_data):
    if previous_data is None:
        raise dash.exceptions.PreventUpdate

    df = pd.DataFrame(previous_data)
    if df.equals(pd.DataFrame(current_data)):
        raise dash.exceptions.PreventUpdate

    # Save the changes to the DataFrame (assuming 'Comments' is the column you want to update)
    df['Comments'] = pd.DataFrame(current_data)['Comments']

    # Save the DataFrame to a CSV file
    df.to_csv('/Users/manlange/Desktop/Rishab/17_14_1_Cycle1_updated.csv', index=False)

    return df.to_dict('records')


if __name__ == '__main__':
    app.run_server(debug=True)"""

#@@@@@@@@@@@@@@

"""import pandas as pd
import dash
import dash_bootstrap_components as dbc
from dash import html, dcc, dash_table
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)
df = pd.read_excel('/Users/manlange/Desktop/Rishab/17_14_1_Cycle1.xlsx')

# Define the dictionary for validation
validation_dict = {'ABCD': 'manlange'}

html_button = html.Div([
    html.Div([
        dbc.Button("Day 0", id="submit-buton", className="me-2", color="info"),
    ], style={'margin-right': '5px'}),
    html.Div([
        html.Button('Access Tokens', id='unlock-button', n_clicks=0, style={"color": "black", 'textAlign': 'center'}),
        dcc.Input(id='password-input', type='password', placeholder='Enter Access Token', style={'margin-left': '10px'}),
        html.Div(id='output-1', className='py-3', style={'whitespace': 'pre-line', 'textAlign': 'center'}),
        html.Div(id='output-access-tokens', style={'textAlign': 'center', 'margin-top': '5px'}),
    ], style={'display': 'flex', 'align-items': 'center'}),
])

app.layout = html.Div([
    dbc.Card(
        [
            dbc.CardBody(
                [
                    html.H2("Comment Tracker", className="card-text", style={"color": "white", 'textAlign': 'center'}),
                ]
            )
        ],
        color="gray",
        outline=True,
        style={'height': '100px', 'margin-left': '10px', 'margin-right': '10px', 'margin-top': '10px'},
        className="shadow-sm p-3 mb-2 rounded"
    ),
    dbc.Card(
        [
            dbc.CardBody(
                [
                    html.Label('Active Release Cycle:'),
                    dcc.Dropdown(
                        id='dropdown-1',
                        options=[
                            {'label': '17.12.02 - Cycle 1', 'value': '17.12.02 - Cycle 1'},
                            {'label': '17.06.06 - Cycle 1', 'value': '17.06.06 - Cycle 1'},
                            {'label': '17.14.01 - Cycle 1', 'value': '17.14.01 - Cycle 1'},
                            {'label': '17.13.01 - Cycle 4', 'value': '17.13.01 - Cycle 4'}
                        ],
                        style={"color": "black", 'textAlign': 'center'},
                        value='option-1',
                    ),
                ]
            ),
        ],
        color="light",
        outline=True,
        style={'margin-bottom': '10px', 'margin-top': '10px', 'margin-right': '10px', 'margin-left': '10px', 'align-items': 'center'}
    ),
    dbc.Card(
        [
            dbc.CardBody(
                [
                    html.Label('Baseline Release Cycle:'),
                    dcc.Dropdown(
                        id='dropdown-2',
                        options=[
                            {'label': 'ACE', 'value': 'ACE'},
                            {'label': 'ASR1K', 'value': 'ASR1K'},
                            {'label': 'CSR', 'value': 'CSR'},
                            {'label': 'Curie', 'value': 'Curie'},
                            {'label': 'ENCS', 'value': 'ENCS'},
                            {'label': 'Fugazi', 'value': 'Fugazi'},
                            {'label': 'Greenday', 'value': 'Greenday'},
                        ],
                        style={"color": "black", 'textAlign': 'center'},
                        value='option-A'
                    ),
                ]
            ),
        ],
        color="light",
        outline=True,
        style={'margin-bottom': '10px', 'margin-top': '10px', 'margin-right': '10px', 'margin-left': '10px', 'align-items': 'center'}
    ),
    html.Div([
        html_button,  # Include the Access Tokens button here
    ], style={'display': 'flex', 'align-items': 'center', 'margin-top': '5px', 'padding': '5px'}),
    html.Div(id='output-2'),
    html.Div([
        dash_table.DataTable(
            id='table',
            columns=[
                {'name': col, 'id': col, 'editable': True if col == 'Comments' else False}
                for col in df.columns
            ],
            data=df.to_dict('records'),
            sort_action='native',  # Enable native sorting
            sort_mode='multi',     # Allow multi-column sorting
            style_table={'height': '300px', 'overflowY': 'auto'}  # Set a fixed height with scroll for the table
        )
    ]),
])


@app.callback(
    [Output('table', 'editable'),
     Output('output-1', 'children'),
     Output('output-access-tokens', 'children')],
    [Input('unlock-button', 'n_clicks')],
    [State('password-input', 'value')]
)
def update_content(unlock_clicks, password):
    ctx = dash.callback_context
    if not ctx.triggered:
        return False, '', ''

    trigger_id = ctx.triggered[0]['prop_id']

    if trigger_id == 'unlock-button.n_clicks':
        # Validate the access token
        if unlock_clicks > 0 and password in validation_dict:
            return True, f'Created By: {validation_dict[password]}', ''
        else:
            return False, 'Invalid access token', ''
    else:
        return False, '', ''


@app.callback(
    Output('table', 'data'),
    [Input('table', 'data_previous')],
    [State('table', 'data')]
)
def save_changes(previous_data, current_data):
    if previous_data is None:
        raise dash.exceptions.PreventUpdate

    df = pd.DataFrame(previous_data)
    if df.equals(pd.DataFrame(current_data)):
        raise dash.exceptions.PreventUpdate

    # Save the changes to the DataFrame (assuming 'Comments' is the column you want to update)
    df['Comments'] = pd.DataFrame(current_data)['Comments']

    # Save the DataFrame to a CSV file
    df.to_csv('/Users/manlange/Desktop/Rishab/17_14_1_Cycle1_updated.csv', index=False)

    return df.to_dict('records')


if __name__ == '__main__':
    app.run_server(debug=True)"""


#$$$$$$$$$$FINAL CODE BELOW

"""import os
import requests
import pandas as pd
import dash
import dash_bootstrap_components as dbc
from dash import html, dcc, dash_table
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

# Define file paths
excel_file_path = '/Users/manlange/Desktop/Rishab/17_14_1_Cycle1.xlsx'
csv_file_path = '/Users/manlange/Desktop/Rishab/17_14_1_Cycle1_updated.csv'

# Define the dictionary for validation
validation_dict = {'ABCD': 'manlange', 'XYZ': 'another_user'}

# Load data from the CSV file if it exists, otherwise load from the Excel file
if os.path.exists(csv_file_path):
    df = pd.read_csv(csv_file_path)
else:
    df = pd.read_excel(excel_file_path)

html_button = html.Div([
    html.Div([
        dbc.Button("Day 4", id="submit-buton-0", className="me-2", color="info"),
        dbc.Button("Day 3", id="submit-buton-1", className="me-2", color="info"),
        dbc.Button("Day 2", id="submit-buton-2", className="me-2", color="info"),
        dbc.Button("Day 1", id="submit-buton-3", className="me-2", color="info"),
        dbc.Button("Day 0", id="submit-buton-4", className="me-2", color="info"),
        dbc.Button("Submit", id="submit-changes", color="success"),
    ], style={'margin-right': '5px'}),
    html.Div([
        dbc.Button('Access Tokens', id='unlock-button', n_clicks=0, color='black', className="mr-2"),
        dcc.Input(id='password-input', type='password', placeholder='Enter Access Token',
                  style={'margin-bottom': '10px', 'margin-top': '10px'}),
        html.Div(id='output-1', className='py-3', style={'whitespace': 'pre-line', 'textAlign': 'center'}),
        html.Div(id='output-access-tokens', style={'textAlign': 'center', 'margin-top': '5px'}),
    ], style={'display': 'flex', 'align-items': 'center'}),
])

# Analysis Card


# Dark Rectangular Text Bar
dark_bar = dbc.Card(
    dbc.CardBody(
        "Analysis",
        style={"color": "white", "background-color": "black", "text-align": "left", "padding": "10px"}
    ),
    className="mb-3",
)

app.layout = html.Div([
    dbc.Card(
        [
            dbc.CardBody(
                [
                    html.H2("Comment Tracker", className="card-text", style={"color": "white", 'textAlign': 'center'}),
                ]
            )
        ],
        color="gray",
        outline=True,
        style={'height': '100px', 'margin-left': '10px', 'margin-right': '10px', 'margin-top': '10px'},
        className="shadow-sm p-3 mb-2 rounded"
    ),
    dbc.Card(
        [
            dbc.CardBody(
                [
                    html.Label('Active Release Cycle:'),
                    dcc.Dropdown(
                        id='dropdown-1',
                        options=[
                            {'label': '17.12.02 - Cycle 1', 'value': '17.12.02 - Cycle 1'},
                            {'label': '17.06.06 - Cycle 1', 'value': '17.06.06 - Cycle 1'},
                            {'label': '17.14.01 - Cycle 1', 'value': '17.14.01 - Cycle 1'},
                            {'label': '17.13.01 - Cycle 4', 'value': '17.13.01 - Cycle 4'}
                        ],
                        style={"color": "black", 'textAlign': 'center'},
                        value='option-1',
                    ),
                ]
            ),
        ],
        color="light",
        outline=True,
        style={'margin-bottom': '10px', 'margin-top': '10px', 'margin-right': '10px', 'margin-left': '10px',
               'align-items': 'center'}
    ),
    dbc.Card(
        [
            dbc.CardBody(
                [
                    html.Label('Baseline Release Cycle:'),
                    dcc.Dropdown(
                        id='dropdown-2',
                        options=[
                            {'label': 'ACE', 'value': 'ACE'},
                            {'label': 'ASR1K', 'value': 'ASR1K'},
                            {'label': 'CSR', 'value': 'CSR'},
                            {'label': 'Curie', 'value': 'Curie'},
                            {'label': 'ENCS', 'value': 'ENCS'},
                            {'label': 'Fugazi', 'value': 'Fugazi'},
                            {'label': 'Greenday', 'value': 'Greenday'},
                        ],
                        style={"color": "black", 'textAlign': 'center'},
                        value='option-A'
                    ),
                ]
            ),
        ],
        color="light",
        outline=True,
        style={'margin-bottom': '10px', 'margin-top': '10px', 'margin-right': '10px', 'margin-left': '10px',
               'align-items': 'center'}
    ),
    html.Div([
        html_button,
    ], style={'display': 'flex', 'align-items': 'center', 'margin-top': '5px', 'padding': '5px'}),
    
    dark_bar,  # Include the Dark Rectangular Text Bar here
    html.Div(id='output-2'),
    html.Div([
        dash_table.DataTable(
            id='table',
            columns=[
                {'name': col, 'id': col, 'editable': True if col == 'Comments' else False}
                for col in df.columns
            ],
            data=df.to_dict('records'),
            sort_action='native',  # Enable native sorting
            sort_mode='multi',  # Allow multi-column sorting
            style_table={
                'height': '300px',
                'overflowY': 'auto',
                'border': 'thin lightgrey solid',
                'fontFamily': 'Arial, sans-serif',  # Specify font family
                'minWidth': '100%',  # Ensure the table takes up the full width
            },
            style_data_conditional=[
                {
                    'if': {'row_index': 'odd'},
                    'backgroundColor': 'rgb(248, 248, 248)'
                },
                {
                    'if': {'column_id': 'Comments'},
                    'textAlign': 'left'
                },
            ],
        )
    ]),
])


@app.callback(
    [Output('table', 'editable'),
     Output('output-1', 'children'),
     Output('output-access-tokens', 'children')],
    [Input('unlock-button', 'n_clicks')],
    [State('password-input', 'value')]
)
def update_content(unlock_clicks, password):
    ctx = dash.callback_context
    if not ctx.triggered:
        return False, '', ''

    trigger_id = ctx.triggered[0]['prop_id']

    if trigger_id == 'unlock-button.n_clicks':
        # Validate the access token
        if unlock_clicks > 0 and password in validation_dict:
            created_by = validation_dict[password]
            return True, f'Created By: {created_by}', ''
        else:
            return False, 'Invalid access token', ''
    else:
        return False, '', ''


@app.callback(
    Output('table', 'data'),
    [Input('table', 'data_previous')],
    [State('table', 'data'),
     State('dropdown-1', 'value'),
     State('dropdown-2', 'value')]
)
def save_changes(previous_data, current_data, active_release_cycle, baseline_release_cycle):
    if previous_data is None:
        raise dash.exceptions.PreventUpdate

    df = pd.DataFrame(previous_data)
    if df.equals(pd.DataFrame(current_data)):
        raise dash.exceptions.PreventUpdate

    # Save the changes to the DataFrame (assuming 'Comments' is the column you want to update)
    df['Comments'] = pd.DataFrame(current_data)['Comments']

    # Save the DataFrame to a CSV file
    df.to_csv(csv_file_path, index=False)

    # Prepare the data to be sent in the PUT request
    payload = {
        'active_release_cycle': active_release_cycle,
        'baseline_release_cycle': baseline_release_cycle,
        'table_data': df.to_dict('records')
    }

    # Send a PUT request with the updated data
    #api_url = 'http://10.65.71.121:5000/fetch_dtdash'
    #headers = {'Content-Type': 'application/json'}  # Adjust the headers as neededS

    # Convert payload to JSON and send the PUT request
    #response = requests.put(api_url, json=payload, headers=headers)

    # Check if the request was successful
    ##   print('PUT request successful')
    #else:
     #   print(f'Error in PUT request. Status code: {response.status_code}')

    return df.to_dict('records')


if __name__ == '__main__':
    app.run_server(debug=True,port = 8051) """
#Tried 

import dash
import dash_bootstrap_components as dbc
from dash import html, dcc, dash_table
from dash.dependencies import Input, Output, State
import requests

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

# Replace 'https://your.api.endpoint/data' with your actual API endpoints
get_api_endpoint = 'http://10.110.147.117:5000/fetch_dtdash'  # Replace with your actual GET API endpoint
post_api_endpoint = 'http://10.110.147.117:5000/send_collections'  # Replace with your actual POST API endpoint

# Define the dictionary for validation
validation_dict = {'ABCD': 'manlange'}

html_button = html.Div([
    html.Div([
        dbc.Button("Day 4", id="submit-buton-4", className="me-2", color="info"),
        dbc.Button("Day 3", id="submit-buton-3", className="me-2", color="info"),
        dbc.Button("Day 2", id="submit-buton-2", className="me-2", color="info"),
        dbc.Button("Day 1", id="submit-buton-1", className="me-2", color="info"),
        dbc.Button("Day 0", id="submit-buton-0", className="me-2", color="info"),
        dbc.Button("Submit", id="submit-changes", color="success"),
    ], style={'margin-right': '5px'}),
    html.Div([
        dbc.Button('Access Tokens', id='unlock-button', n_clicks=0, color='black', className="mr-2"),
        dcc.Input(id='password-input', type='password', placeholder='Enter Access Token..', style={'margin-bottom': '10px', 'margin-top': '10px'}),
        html.Div(id='output-1', className='py-3', style={'whitespace': 'pre-line', 'textAlign': 'center'}),
        html.Div(id='output-access-tokens', style={'textAlign': 'center', 'margin-top': '5px'}),
    ], style={'display': 'flex', 'align-items': 'center'}),
])

# Analysis Card
dark_bar = dbc.Card(
    dbc.CardBody(
        "Analysis",
        style={"color": "white", "background-color": "black", "text-align": "left", "padding": "10px"}
    ),
    className="mb-3",
)

app.layout = html.Div([
    dbc.Card(
        [
            dbc.CardBody(
                [
                    html.H2("Comment Tracker", className="card-text", style={"color": "white", 'textAlign': 'center'}),
                ]
            )
        ],
        color="gray",
        outline=True,
        style={'height': '100px', 'margin-left': '10px', 'margin-right': '10px', 'margin-top': '10px'},
        className="shadow-sm p-3 mb-2 rounded"
    ),
    dbc.Card(
        [
            dbc.CardBody(
                [
                    html.Label('Active Release Cycle:'),
                    dcc.Dropdown(
                        id='dropdown-1',
                        options=[
                            {'label': '17.12.02 - Cycle 1', 'value': '17.12.02 - Cycle 1'},
                            {'label': '17.06.06 - Cycle 1', 'value': '17.06.06 - Cycle 1'},
                            {'label': '17.14.01 - Cycle 1', 'value': '17.14.01 - Cycle 1'},
                            {'label': '17.13.01 - Cycle 4', 'value': '17.13.01 - Cycle 4'}
                        ],
                        style={"color": "black", 'textAlign': 'center'},
                        value='option-1',
                    ),
                ]
            ),
        ],
        color="light",
        outline=True,
        style={'margin-bottom': '10px', 'margin-top': '10px', 'margin-right': '10px', 'margin-left': '10px',
               'align-items': 'center'}
    ),
    dbc.Card(
        [
            dbc.CardBody(
                [
                    html.Label('Baseline Release Cycle:'),
                    dcc.Dropdown(
                        id='dropdown-2',
                        options=[
                            {'label': 'ACE', 'value': 'ACE'},
                            {'label': 'ASR1K', 'value': 'ASR1K'},
                            {'label': 'CSR', 'value': 'CSR'},
                            {'label': 'Curie', 'value': 'Curie'},
                            {'label': 'ENCS', 'value': 'ENCS'},
                            {'label': 'Fugazi', 'value': 'Fugazi'},
                            {'label': 'Greenday', 'value': 'Greenday'},
                        ],
                        style={"color": "black", 'textAlign': 'center'},
                        value='option-A'
                    ),
                ]
            ),
        ],
        color="light",
        outline=True,
        style={'margin-bottom': '10px', 'margin-top': '10px', 'margin-right': '10px', 'margin-left': '10px',
               'align-items': 'center'}
    ),
    html.Div([
        html_button,  # Include the Access Tokens button here
    ], style={'display': 'flex', 'align-items': 'center', 'margin-top': '5px', 'padding': '5px'}),
    dark_bar,
    html.Div(id='output-2'),
    html.Div([
        dash_table.DataTable(
            id='table',
            columns=[],  # No need to initialize columns here
            data=[],
            sort_action='native',  # Enable native sorting
            sort_mode='multi',     # Allow multi-column sorting
            style_table={'height': '300px', 'overflowY': 'auto'}  # Set a fixed height with scroll for the table
        )
    ]),
])


@app.callback(
    [Output('table', 'data'),
     Output('table', 'columns'),
     Output('output-1', 'children'),
     Output('output-access-tokens', 'children')],
    [Input('submit-buton-4', 'n_clicks'),
     Input('submit-buton-3', 'n_clicks'),
     Input('submit-buton-2', 'n_clicks'),
     Input('submit-buton-1', 'n_clicks'),
     Input('submit-buton-0', 'n_clicks'),
     Input('submit-changes', 'n_clicks')],  # Add input for the 'Submit' button
    [State('dropdown-1', 'value'),
     State('dropdown-2', 'value'),
     State('table', 'data')]  # Add State for the table data
)
def fetch_data_from_api(n_clicks_4, n_clicks_3, n_clicks_2, n_clicks_1, n_clicks_0, n_clicks_submit,
                         active_release_cycle, baseline_release_cycle, table_data):
    ctx = dash.callback_context
    if not ctx.triggered:
        raise dash.exceptions.PreventUpdate

    trigger_id = ctx.triggered[0]['prop_id'].split('.')[0]

    # Map the clicked button to the corresponding 'Day' value
    day_mapping = {'submit-buton-4': 4, 'submit-buton-3': 3, 'submit-buton-2': 2, 'submit-buton-1': 1,
                   'submit-buton-0': 0, 'submit-changes': 'submit-changes'}
    selected_day = day_mapping[trigger_id]

    if selected_day == 'submit-changes':
        try:
            # Prepare the data to be sent in the POST request
            post_data = {
                'active_release_cycle': active_release_cycle,
                'baseline_release_cycle': baseline_release_cycle,
                'comments': [row.get('Comments', '') for row in table_data]
            }

            # Make a POST request to send data to the API
            response = requests.post(post_api_endpoint, json=post_data)

            if response.status_code == 200:
                return [], [], 'Data submitted successfully', []
            else:
                return [], [], f'Failed to submit data: {response.status_code}', []
        except Exception as e:
            return [], [], f'Error submitting data: {str(e)}', []
    elif selected_day is not None:
        try:
            # Make a GET request to fetch data for the selected day
            response = requests.get(get_api_endpoint)

            if response.status_code == 200:
                # Parse the API response and update the table
                api_data = response.json()

                # Ensure 'Comments' is included in columns
                columns = [{'name': col, 'id': col, 'editable': True if col == 'Comments' else False} for col in
                           api_data[0].keys()]
                return api_data, columns, '', []
            else:
                return [], [], f'Failed to fetch data from API: {response.status_code}', []
        except Exception as e:
            return [], [], f'Error fetching data from API: {str(e)}', []
    else:
        return [], [], '', []


if __name__ == '__main__':
    app.run_server(debug=True)

#@$@%@^$^@^^@^@^ check 
import dash
import dash_bootstrap_components as dbc
from dash import html, dcc, dash_table
from dash.dependencies import Input, Output, State
import requests

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

# Replace 'https://your.api.endpoint/data' with your actual API endpoint
api_endpoint = 'http://10.110.147.117:5000/fetch_dtdash'

# Define the dictionary for validation
validation_dict = {'ABCD': 'manlange'}

html_button = html.Div([
    html.Div([
        dbc.Button("Day 4", id="submit-buton-4", className="me-2", color="info"),
        dbc.Button("Day 3", id="submit-buton-3", className="me-2", color="info"),
        dbc.Button("Day 2", id="submit-buton-2", className="me-2", color="info"),
        dbc.Button("Day 1", id="submit-buton-1", className="me-2", color="info"),
        dbc.Button("Day 0", id="submit-buton-0", className="me-2", color="info"),
        dbc.Button("Submit", id="submit-changes", color="success"),
    ], style={'margin-right': '5px'}),
    html.Div([
        dbc.Button('Access Tokens', id='unlock-button', n_clicks=0, color='black', className="mr-2"),
        dcc.Input(id='password-input', type='password', placeholder='Enter Access Token..', style={'margin-bottom': '10px', 'margin-top': '10px'}),
        html.Div(id='output-1', className='py-3', style={'whitespace': 'pre-line', 'textAlign': 'center'}),
        html.Div(id='output-access-tokens', style={'textAlign': 'center', 'margin-top': '5px'}),
    ], style={'display': 'flex', 'align-items': 'center'}),
])

# Analysis Card
dark_bar = dbc.Card(
    dbc.CardBody(
        "Analysis",
        style={"color": "white", "background-color": "black", "text-align": "left", "padding": "10px"}
    ),
    className="mb-3",
)

app.layout = html.Div([
    dbc.Card(
        [
            dbc.CardBody(
                [
                    html.H2("Comment Tracker", className="card-text", style={"color": "white", 'textAlign': 'center'}),
                ]
            )
        ],
        color="gray",
        outline=True,
        style={'height': '100px', 'margin-left': '10px', 'margin-right': '10px', 'margin-top': '10px'},
        className="shadow-sm p-3 mb-2 rounded"
    ),
    dbc.Card(
        [
            dbc.CardBody(
                [
                    html.Label('Active Release Cycle:'),
                    dcc.Dropdown(
                        id='dropdown-1',
                        options=[
                            {'label': '17.12.02 - Cycle 1', 'value': '17.12.02 - Cycle 1'},
                            {'label': '17.06.06 - Cycle 1', 'value': '17.06.06 - Cycle 1'},
                            {'label': '17.14.01 - Cycle 1', 'value': '17.14.01 - Cycle 1'},
                            {'label': '17.13.01 - Cycle 4', 'value': '17.13.01 - Cycle 4'}
                        ],
                        style={"color": "black", 'textAlign': 'center'},
                        value='option-1',
                    ),
                ]
            ),
        ],
        color="light",
        outline=True,
        style={'margin-bottom': '10px', 'margin-top': '10px', 'margin-right': '10px', 'margin-left': '10px',
               'align-items': 'center'}
    ),
    dbc.Card(
        [
            dbc.CardBody(
                [
                    html.Label('Baseline Release Cycle:'),
                    dcc.Dropdown(
                        id='dropdown-2',
                        options=[
                            {'label': 'ACE', 'value': 'ACE'},
                            {'label': 'ASR1K', 'value': 'ASR1K'},
                            {'label': 'CSR', 'value': 'CSR'},
                            {'label': 'Curie', 'value': 'Curie'},
                            {'label': 'ENCS', 'value': 'ENCS'},
                            {'label': 'Fugazi', 'value': 'Fugazi'},
                            {'label': 'Greenday', 'value': 'Greenday'},
                        ],
                        style={"color": "black", 'textAlign': 'center'},
                        value='option-A'
                    ),
                ]
            ),
        ],
        color="light",
        outline=True,
        style={'margin-bottom': '10px', 'margin-top': '10px', 'margin-right': '10px', 'margin-left': '10px',
               'align-items': 'center'}
    ),
    html.Div([
        html_button,  # Include the Access Tokens button here
    ], style={'display': 'flex', 'align-items': 'center', 'margin-top': '5px', 'padding': '5px'}),
    dark_bar,
    html.Div(id='output-2'),
    html.Div([
        dash_table.DataTable(
            id='table',
            columns=[],  # No need to initialize columns here
            data=[],
            sort_action='native',  # Enable native sorting
            sort_mode='multi',     # Allow multi-column sorting
            style_table={'height': '300px', 'overflowY': 'auto'}  # Set a fixed height with scroll for the table
        )
    ]),
])


@app.callback(
    [Output('table', 'data'),
     Output('table', 'columns'),
     Output('output-1', 'children'),
     Output('output-access-tokens', 'children')],
    [Input('submit-buton-4', 'n_clicks'),
     Input('submit-buton-3', 'n_clicks'),
     Input('submit-buton-2', 'n_clicks'),
     Input('submit-buton-1', 'n_clicks'),
     Input('submit-buton-0', 'n_clicks')],
    [State('dropdown-1', 'value'),
     State('dropdown-2', 'value')]
)
def fetch_data_from_api(n_clicks_4, n_clicks_3, n_clicks_2, n_clicks_1, n_clicks_0, active_release_cycle, baseline_release_cycle):
    ctx = dash.callback_context
    if not ctx.triggered:
        raise dash.exceptions.PreventUpdate

    trigger_id = ctx.triggered[0]['prop_id'].split('.')[0]

    # Map the clicked button to the corresponding 'Day' value
    day_mapping = {'submit-buton-4': 4, 'submit-buton-3': 3, 'submit-buton-2': 2, 'submit-buton-1': 1, 'submit-buton-0': 0}
    selected_day = day_mapping[trigger_id]

    if selected_day is not None:
        try:
            # Make an API request to fetch data for the selected day
            response = requests.get(f'{api_endpoint}')

            if response.status_code == 200:
                # Parse the API response and update the table
                api_data = response.json()

                # Ensure 'Comments' is included in columns
                columns = [{'name': col, 'id': col, 'editable': True if col == 'Comments' else False} for col in api_data[0].keys()]
                return api_data, columns, '', []
            else:
                return [], [], f'Failed to fetch data from API: {response.status_code}', []
        except Exception as e:
            return [], [], f'Error fetching data from API: {str(e)}', []
    else:
        return [], [], '', []
if __name__ == '__main__':
    app.run_server(debug=True)