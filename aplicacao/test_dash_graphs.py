from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc

import datas_lancamentos
import imports_datasets
import mapa
import distribuicoes

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = html.Div(children=[
    html.Div([
        html.H1("Distribuições das características das músicas", style={'text-align': 'center'}),
        html.Div([
            dcc.Graph(id='caracteristicas1', figure=distribuicoes.charts[0])
        ]),
        html.Div([
            dcc.Graph(id='caracteristicas2', figure=distribuicoes.charts[1])
        ])

    ]),
    html.Div([
            html.H1("Distribuições temporais do lançamento das músicas", style={'text-align': 'center'}),

            dcc.Graph(id='datas_lancamentos', figure=datas_lancamentos.fig)
    ]),
    html.Div([
        html.H1("Distribuição de artistas pelo mundo", style={'text-align': 'center'}),

        dcc.Graph(id='mapa', figure=mapa.fig)
    ])
])


if __name__ == '__main__':
    app.run_server(debug=True)