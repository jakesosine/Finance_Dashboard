# importing libraries
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html
from datetime import datetime, timedelta
from dash.dependencies import Output, Input

reimbursement_df = pd.read_excel(
    '../data/Names.xlsx', sheet_name='Reimbursement Rates')
names_df = pd.read_excel(
    '../data/Names.xlsx', sheet_name='names')

supervisor_df = pd.read_excel(
    '../data/Names.xlsx', sheet_name='Supervisor_Salary')


print(names_df.head())

colors = ['rgba(32, 105, 224,.1)', 'rgba(244, 212, 124,.1)', 'rgba(8, 44, 108,.1)',
          'rgba(135, 134, 131,.1)', 'rgb(190, 190, 190,.1)',  'rgba(68, 68, 68,.1)',
          'rgba(32, 105, 224,.5)', 'rgba(244, 212, 124,.5)', 'rgba(8, 44, 108,.5)',
          'rgba(135, 134, 131,.5)', 'rgb(190, 190, 190,.5)',  'rgba(68, 68, 68,.5)'
          'rgba(32, 105, 224,1)', 'rgba(244, 212, 124,1)', 'rgba(8, 44, 108,1)',
          'rgba(135, 134, 131,1)', 'rgb(190, 190, 190,1)',  'rgba(68, 68, 68,1)']

external_stylesheets = [
    'https://codepen.io/chriddyp/pen/bW LwgP.css',
    {
        'href': 'https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css',
        'rel': 'stylesheet',
        'integrity': 'sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO',
        'crossorigin': 'anonymous'
    }
]


# Figures
fig_1 = go.Figure()


fig_1.add_trace(go.Bar(
    x=reimbursement_df['BT_Reimbursement_Rate'],
    y=reimbursement_df['Insurance_Provider'],
    name='BT Reimbursement Rates',
    orientation='h',
    marker=dict(
        color='rgba(58, 71, 80, 0.6)',
        line=dict(color='rgba(58, 71, 80, 1.0)', width=1)
    )))


fig_1.add_trace(go.Bar(
    x=reimbursement_df['BCBA_Reimbursement_Rate'],
    y=reimbursement_df['Insurance_Provider'],
    name='Clinical Director',
    orientation='h',
    textposition='inside',
    marker=dict(color='rgba(85, 78, 43, 0.6)',
                line=dict(color='rgba(85, 78, 23, 1.0)',
                          width=1)),

)),
fig_1.update_layout(barmode='stack')
fig_1.update_xaxes(title_text="Reimbursement Rates")
fig_1.update_yaxes(title_text="Insurance Provider")
fig_1.update_layout(paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)')


fig_2 = go.Figure(data=[go.Pie(labels=names_df['Insurance Funding'],
                               values=names_df['Authorized Weekly Direct Hours'])])
fig_2.update_traces(hoverinfo='label+percent', textinfo='percent', textfont_size=10,
                    marker=dict(colors=colors, line=dict(color='#000000', width=1)))
fig_2.update_layout(paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)')


fig_3 = go.Figure()

diagnosis = names_df
freq = diagnosis.Diagnosis.value_counts()

fig_3.add_trace(go.Bar(
    x=['Autism', 'Down Syndrome', 'other'],
    y=freq,
    name='BT Reimbursement Rates',
    marker=dict(
        color=['red', colors[4], colors[4]],
        line=dict(color=['red', colors[4], colors[4]], width=1)
    )))
fig_3.update_layout(paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)',
                    title_text='Diagnosis')

fig_4 = go.Figure(data=[go.Table(
    columnwidth=[80, 40, 40],
    header=dict(values=['<b>Insurance Funder</b>', '<b>BCBA Reimbursement Rate</b>', '<b>BT reimbursement rate</b>'],
                fill_color='grey',
                align=['center', 'center', 'right'],
                font=dict(color='white', size=10)),
    cells=dict(values=[reimbursement_df.Insurance_Provider, reimbursement_df.BCBA_Reimbursement_Rate, reimbursement_df.BT_Reimbursement_Rate],
               line_color='darkslategray',
               fill_color=[
                   ['rgba(255,255,255,1)', 'rgba(211,211,211,.5)'] * 15],
               align=['left', 'center'],
               font=dict(color='black', size=11)))
])

fig_4.update_layout(paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)')


fig_5 = go.Figure()


fig_5.add_trace(go.Bar(
    y=names_df['Client'],
    x=names_df['Authorized Clinical Supervisor Hours'],
    name='Authorized Supervision Hours',
    orientation='h',
    marker=dict(
        color='rgba(58, 71, 80, 0.6)',
        line=dict(color='rgba(58, 71, 80, 1.0)', width=1)
    )))


fig_5.add_trace(go.Bar(
    y=names_df['Client'],
    x=names_df['Scheduled Weekly Direct Hours'],
    name='Scheduled Supervision Hours',
    orientation='h',
    textposition='inside',
    marker=dict(color='rgba(85, 78, 43, 0.6)',
                line=dict(color='rgba(85, 78, 23, 1.0)',
                          width=1)),
))

fig_5.update_layout(paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)')


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.Div([
        html.H1(
            children="Dashboard",
            style={
                'color': colors[13],
                'backgroundColor': "#18191c",
            }
        )
    ], className='row'),
    html.Div([
        html.Div([
            dcc.Graph(figure=fig_1),
            dcc.Interval(id='fig_1_update', interval=360 * 1000, n_intervals=0)
        ], className='six columns'),
        html.Div([
            dcc.Graph(figure=fig_2),
            dcc.Interval(id='fig_2_update', interval=360 * 1000, n_intervals=0)
        ], className='six columns')
    ], className='row'),
    html.Div([
        html.Div([
            dcc.Graph(figure=fig_3),
            dcc.Interval(id='fig_3_update', interval=360 * 1000, n_intervals=0)
        ], className='four columns'),
        html.Div([
            dcc.Graph(figure=fig_4),
            dcc.Interval(id='fig_4_update', interval=360 * 1000, n_intervals=0)
        ], className='four columns'),
    ], className='row'),
    html.Div([
        html.Div([
            html.H4(children='Clinical Dashboard', style={
                    'color': colors[13], 'backgroundColor': "#18191c"}),
            html.Div(id='table_data'),
            dcc.Interval(id='update_table', interval=480 * 1000, n_intervals=0)
        ], className='container')
    ], className='row'),
    html.Div([
        html.Div([
            'Resources', html.Br(),
            html.A("Tableau Clinical Dashboard",
                   href='https://public.tableau.com/profile/jacob.sosine1#!/'), html.Br(),
            html.A(
                'Jakesosine github', href='https://github.com/jakesosine'), html.Br(), html.Br(),
            'Created by ',
            html.A('@87JTS', href='https://twitter.com/87Jts')
        ], className='container', style={'color': colors[13]}, id='footer')
    ], className='row')
], style={
    'backgroundColor': "#18191c"
}, className='container-fluid')


if __name__ == '__main__':
    app.run_server(debug=True)
