import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import time
import logging
import sys
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
import check_cpu
import os
colors = {
    'background': '#000000',
    'text': '#7FDBFF'
}
app = dash.Dash(__name__)
app.layout = html.Div(style={'backgroundcolor':colors['background']},
    children=([
        html.H1('Monitor System'),
        html.Div(id='live-update-text'),
        html.Div(id='sys-space'),
        dcc.Interval(
            id='interval-component',
            interval=1*2000, # in milliseconds
            n_intervals=0
        )
    ])
)
@app.callback(Output('live-update-text','children'),Input('interval-component','n_intervals'))
def cpu(n):
    value = check_cpu.monitor_cpu_usage()
    style = {'padding': '10px', 'fontSize': '32px'}

    ram_value = check_cpu.ram_usage()
    ram_percent = check_cpu.monitor_ram_percent()
    

    return [ html.Span('Cpu usage: {} %'.format(value), style=style),
            html.Span('Ram usage: {} GB {}%'.format(ram_value,ram_percent), style=style),
            
                
                ]
@app.callback(Output('sys-space','children'),Input('interval-component','n_intervals'))
def file_space(n):
    space_value = check_cpu.file_sys_space()
    style = {'padding': '10px', 'fontSize': '32px'}
    return html.Span('File system usage of current disk is : {} %'.format(space_value), style=style)


    
if __name__ == '__main__':
    app.run_server(debug=True)
    time.sleep(20)
