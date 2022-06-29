from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc

import datas_lancamentos
import imports_datasets
import distribuicoes
import correlacao

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
        html.H1("Correlações entre atributos musicais", style={'text-align': 'center'}),

        dbc.Row([
                html.H3("Correlações entre atributos relacionados à expressividade das músicas", style={'text-align': 'center'}),
                html.P("A característica valência mede a positividade da música, a\
                    'danceabilidade' mede o quão dançante uma música é, já a energia representa uma medida perceptiva de intensidade e atividade de uma música.\
                    Todas essas caracterpisticas estão em um intervalo de 0 a 1. A característica tempo é relacionada ao ritmo da música, ela é medida em batidas\
                    por minuto.", style={'text-align': 'center'}),
                dcc.Graph(id='correlacao1', figure=correlacao.fig_1)
            ]),
            dbc.Row([
                html.H3("Correlações entre atributos relacionados a alguma coisa (arrumar palavra boa)", style={'text-align': 'center'}),
                html.P("A característica 'instrumentalness' prevê se uma música não contém vocais, a característica 'acousticness' é uma medida de confiança se a música\
                    é acústica e 'speechiness' detecta a presença de palavras faladas em uma música. Todas essas caracterpisticas estão em um intervalo de 0 a 1. \
                    Já a característica 'loudness' é o volume geral de uma faixa em decibéis", style={'text-align': 'center'}),
                dcc.Graph(id='correlacao2', figure=correlacao.fig_2)
            ])
    ]),
    dbc.Row([
            html.H1("Distribuições temporais do lançamento das músicas", style={'text-align': 'center'}),
            html.P("AAAAAAAAAAAA"),
            dcc.Graph(id='datas_lancamentos', figure=datas_lancamentos.fig)
    ]),
    dbc.Row([
        html.H1("Distribuição de artistas pelo mundo", style={'text-align': 'center'}),

        html.Div(
            children=[
                html.Iframe(
                    src="assets/mapa.html",
                    style={"width": "100%", "min-height": "640px", "background":"url(assets/loading.gif) center center no-repeat"},
                )
            ]
        )
    ])
])


if __name__ == '__main__':
    app.run_server(debug=True)