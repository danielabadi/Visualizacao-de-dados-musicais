from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc

import datas_lancamentos
import imports_datasets
import mapa
import distribuicoes

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = dbc.Container(children=[
    dbc.Row([
        html.H1("Distribuições das características das músicas", style={'text-align': 'center'}),
        dbc.Row([
            dbc.Col([
                dcc.Graph(id='caracteristicas1', figure=distribuicoes.charts[0])
            ]),
            dbc.Col([
                dcc.Graph(id='caracteristicas2', figure=distribuicoes.charts[1])
            ])
        ]),
        dbc.Row([
            dbc.Col([
                dcc.Graph(id='caracteristicas3', figure=distribuicoes.charts[2])
            ]),
            dbc.Col([
                dcc.Graph(id='caracteristicas4', figure=distribuicoes.charts[3])
            ])
        ]),
        dbc.Row([
            dbc.Col([
                dcc.Graph(id='caracteristicas5', figure=distribuicoes.charts[4])
            ]),
            dbc.Col([
                dcc.Graph(id='caracteristicas6', figure=distribuicoes.charts[5])
            ])
        ]),
        dbc.Row([
            dbc.Col([
                dcc.Graph(id='caracteristicas7', figure=distribuicoes.charts[6])
            ]),
            dbc.Col([
                dcc.Graph(id='caracteristicas8', figure=distribuicoes.charts[7])
            ])
        ]),
        dbc.Row([
            dbc.Col([
                dcc.Graph(id='caracteristicas9', figure=distribuicoes.charts[8])
            ]),
            dbc.Col([
                dcc.Graph(id='caracteristicas10', figure=distribuicoes.charts[9])
            ])
        ]),


    ]),
    dbc.Row([
            html.H1("Distribuições temporais do lançamento das músicas", style={'text-align': 'center'}),

            dcc.Graph(id='datas_lancamentos', figure=datas_lancamentos.fig)
    ]),
    dbc.Row([
        html.H1("Distribuição de artistas pelo mundo", style={'text-align': 'center'}),

        dcc.Graph(id='mapa', figure=mapa.fig)
    ])
])


if __name__ == '__main__':
    app.run_server(debug=True)