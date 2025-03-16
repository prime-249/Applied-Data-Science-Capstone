# Import required libraries
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go

# Read the airline data into pandas dataframe
df = pd.read_csv("spacex_launch_dash.csv")
max_payload = df['Payload Mass (kg)'].max()
min_payload = df['Payload Mass (kg)'].min()

# Create a dash application
app = dash.Dash(__name__)

# Create an app layout
app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36',
                                               'font-size': 40}),
                                # TASK 1: Add a dropdown list to enable Launch Site selection
                                # The default select value is for ALL sites
                                dcc.Dropdown(id='site-dropdown',
                                             value='ALL',
                                             options=[
                                                  {'label':'All Sites','value':'ALL'},
                                                  {'label':'CCAFS LC-40','value':'CCAFS LC-40'},
                                                  {'label':'VAFB SLC-4E','value':'VAFB SLC-4E'},
                                                  {'label':'KSC LC-39A','value':'KSC LC-39A'},
                                                  {'label':'CCAFS SLC-40','value':'CCAFS SLC-40'}
                                                  ],
                                             placeholder='Choose any or all sites',
                                             searchable=True
                                ),
                                html.Br(),

                                # TASK 2: Add a pie chart to show the total successful launches count for all sites
                                # If a specific launch site was selected, show the Success vs. Failed counts for the site
                                html.Div(dcc.Graph(id='success-pie-chart')),
                                html.Br(),

                                html.P("Payload range (Kg):"),
                                # TASK 3: Add a slider to select payload range
                                dcc.RangeSlider(id='payload-slider',
                                                min=min_payload,
                                                max=max_payload,
                                                marks={0:'0',9600:'9600'},
                                                value=[min_payload,max_payload]
                                ),
                                # TASK 4: Add a scatter chart to show the correlation between payload and launch success
                                html.Div(dcc.Graph(id='success-payload-scatter-chart')),
                                ])

# TASK 2:
@app.callback(
    Output(component_id='success-pie-chart',component_property='figure'),
    Input(component_id='site-dropdown',component_property='value')
    )
def get_pie_chart(selected_site):
    #Check if site-dropdown has a value
    if selected_site:
        if selected_site=='ALL':
            print('ALL sites selected')
            #Filter data by outcome (class == 1) and group it for plotting
            filtered_df = df[df['class']==1].groupby(by='Launch Site')[['class']].count().reset_index()
            #Generate Pie Chart
            pc_fig = px.pie(filtered_df,names='Launch Site',values='class')
            return pc_fig
        else:
                print(selected_site,' selected')
                #Filter data by selected single launch site and group it for plotting
                filtered_df = df[df['Launch Site']==selected_site][['Launch Site','class']].value_counts().to_frame().reset_index()
                #Generate Pie Chart
                pc_fig = px.pie(filtered_df,names='class',values=0)
                return pc_fig
    else:
         #Return empty chart if site-dropdown has no value
         print('NO SITE SELECTED')
         return go.Figure()

# TASK 4:
@app.callback(
    Output(component_id='success-payload-scatter-chart',component_property='figure'),
    [Input(component_id='site-dropdown',component_property='value'),
     Input(component_id='payload-slider',component_property='value')
    ]
    )
def get_scatter_chart(selected_site,selected_payload):
    print('Debug: inside get_scatter_chart')
    #Check if both selectors have a value
    if selected_payload and selected_site:
        print(selected_payload[0],selected_payload[1],selected_site)
        if selected_site == 'ALL':
            #Filter data to get samples within payload range
            scatter_df = df[(df['Payload Mass (kg)']>=selected_payload[0])&(df['Payload Mass (kg)']<=selected_payload[1])]
            #Generate scatterplot
            scat_fig = px.scatter(data_frame=scatter_df,x='Payload Mass (kg)',y='class',color='Booster Version')
            return scat_fig
        else:
            print(selected_site,'single site, nothing yet')
            #Filter data to get samples within payload range and for specific single launch site
            scatter_df = df[(df['Payload Mass (kg)']>=selected_payload[0])&(df['Payload Mass (kg)']<=selected_payload[1])&(df['Launch Site']==selected_site)]
            #Generate scatterplot
            scat_fig = px.scatter(data_frame=scatter_df,x='Payload Mass (kg)',y='class',color='Booster Version')
            return scat_fig
    else:
        #Return empty chart if ANY selector has no value
        print('NO SITE SELECTED')
        return go.Figure()

# Run the app
if __name__ == '__main__':
    app.run_server(port=8085)
