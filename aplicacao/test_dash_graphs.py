from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc

import datas_lancamentos
import imports_datasets as imports
import distribuicoes
import distribuicoes_popularidades
import correlacao
import weeks_on_chart
import atributos_popularidade
import radar

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = dbc.Container(children=[
    dbc.Row([
        html.H2("Núvens de palavras", style={'text-align': 'center'}),
        dbc.Col([
            html.H3("Títulos das músicas", style={'text-align': 'center'}),
            html.Img(src=app.get_asset_url("titles.png"), style={"width": "100%"}),
    ]),
        dbc.Col([
            html.H3("Letras das músicas", style={'text-align': 'center'}),
            html.Img(src=app.get_asset_url("lyrics.png"), style={"width": "100%"})
        ])
    ]),
    dbc.Row([
        html.H2("Distribuições das características das músicas", style={'text-align': 'center'}),
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
        html.H2("Distribuição dos álbuns, artistas e músicas populares versus o total", style={'text-align': 'center'}),

        dbc.Row([
            html.H3("Álbuns", style={'text-align': 'center'}),
            dcc.Graph(id='albumsPopularidade', figure=distribuicoes_popularidades.charts[0])
        ]),
        dbc.Row([
            html.H3("Artistas", style={'text-align': 'center'}),
            dcc.Graph(id='artistasPopularidade', figure=distribuicoes_popularidades.charts[1])
        ]),
        dbc.Row([
            html.H3("Músicas", style={'text-align': 'center'}),
            dcc.Graph(id='musicasPopularidade', figure=distribuicoes_popularidades.charts[2])
        ]),
    ]),
    dbc.Row([
        html.H2("Correlações entre atributos musicais", style={'text-align': 'center'}),

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
            html.H2("Distribuições temporais do lançamento das músicas", style={'text-align': 'center'}),
            dcc.Graph(id='datas_lancamentos', figure=datas_lancamentos.fig)
    ]),
    dbc.Row([
            html.H2("Distribuição de semanas que as músicas permanecem na Billboard 100", style={'text-align': 'center'}),
            dcc.Graph(id='weeks_on_chart', figure=weeks_on_chart.weeks_on_chart)
    ]),
    dbc.Row([
            html.H2("Relação entre o número de semanas que a música permaneceu na Billboard 100, sua posição máxima no ranking e sua popularidade", style={'text-align': 'center'}),
            dcc.Graph(id='weeks_on_chart_peak_position', figure=weeks_on_chart.weeks_on_chart_peak_position)
    ]),
    dbc.Row([
            html.H2("Atributos médios por popularidade", style={'text-align': 'center'}),
            dcc.Graph(id='atributos_popularidade', figure=atributos_popularidade.fig)
    ]),
    dbc.Row([
        dcc.Dropdown(id='musics',
            options=imports.df_metadata_songs['song_name'], value = ['thank u, next', 'Sunflower - Spider-Man: Into the Spider-Verse'],
            multi=True
        ),
        dcc.Graph(id='radar', figure=radar.atribute_radar([]))
    ]),
    dbc.Row([
        html.H2("Distribuição de artistas pelo mundo", style={'text-align': 'center'}),

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

@app.callback(
    Output("radar", "figure"),
    Input("musics", "value"),
)
def update_radar(value):
    return radar.atribute_radar(value)


if __name__ == '__main__':
    app.run_server(debug=True)
