from dash import Dash, html, dcc, Input, Output, State, no_update
import dash_bootstrap_components as dbc
import plotly.express as px

import aplicacao.datas_lancamentos as datas_lancamentos
import aplicacao.imports_datasets as imports
import aplicacao.distribuicoes as distribuicoes
import aplicacao.distribuicoes_popularidades as distribuicoes_popularidades
import aplicacao.correlacao as correlacao
import aplicacao.weeks_on_chart as weeks_on_chart
import aplicacao.atributos_popularidade as atributos_popularidade
import aplicacao.radar as radar
import aplicacao.radar_medio as radar_medio
import aplicacao.evolucao_generos as evolucao_generos
import aplicacao.popularidade_generos as popularidade_generos
import aplicacao.coordenadas_paralelas as coordenadas_paralelas

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

server = app.server

app.layout = dbc.Container(children=[
    dbc.Row([
        html.H1("Visualizações de Dados Musicais", style={'text-align': 'center'}),
        html.P("André Ribeiro, Caio Campos, Daniel Abadi, Igor Castejon e \
            Pedro Geovanni", style={'text-align': 'center', 'font-weight': 'bold'}),
        html.P("A música pode ser definida como uma importante expressão cultural, \
            ela pode refletir a sociedade e seu povo no momento em que foi criada. \
            Um exemplo claro deste fato é em relação ao período da ditadura militar \
            brasileira, instaurada em 1964 e que durou até 1985, onde havia forte \
            censura relacionada a arte. E, para driblar a opressão, os artistas que \
            desejavam, por meio da música, fazer alguma crítica ao atual regime \
            precisavam alterar as letras de modo que estas passassem uma mensagem de forma \
            subliminar para que não fossem classificadas como ativismo político."),
        html.P("Outro fator importante relacionado as músicas é o fator comercial. \
            Atualmente, a indústria musical mundial movimenta bilhões de dólares, portanto \
            criar visualizações que permitam dar uma noção, mesmo que pequena e informal, \
            sobre o que torna uma música popular é algo bem importante, além de ser uma boa \
            curiosidade. Nosso trabalho, portanto, consiste na criação de visualizações de \
            dados musicais provenientes do conjunto de dados MusicOset, que contém dados \
            relacionados a popularidade das músicas, características acústicas e líricas, \
            e metadados, que são informações textuais e numéricas sobre as músicas, com \
            foco em explorar a seguinte pergunta 'Como determinar o que torna uma música popular?'.")
    ]),
    dbc.Row([
        html.H2("Nuvens de palavras", style={'text-align': 'center'}),
        dbc.Col([
            html.H3("Títulos das músicas", style={'text-align': 'center'}),
            html.Img(src=app.get_asset_url("titles.png"), style={"width": "100%"}),
    ]),
        dbc.Col([
            html.H3("Letras das músicas", style={'text-align': 'center'}),
            html.Img(src=app.get_asset_url("lyrics.png"), style={"width": "100%"})
        ]),
        html.P("Com o conhecimento das palavras mais comuns nas músicas, podem ser inferidos\
         quais são os temas mais recorrentes no universo musical. Para esse fim, um bom tipo\
          de visualização é uma nuvem de palavras. Sendo assim, apresentamos uma nuvem de\
           palavras para títulos e outra para letras de músicas. Em particular, é notória\
            a recorrência de temas relacionados a amor, com a ocorrencia de palavras como\
             'love', 'heart', 'kissing', entre outras, tanto nas letras quanto nos títulos.")
    ]),
    dbc.Row([
        html.H2("Distribuições das características das músicas", style={'text-align': 'center'}),
        html.P("Uma música pode ser caracterizada por vários atributos. No caso do Spotify, os \
            atributos disponíveis e explorados por este trabalho incluem:"),
        dbc.Row([
            dbc.Col([
                dcc.Graph(id='caracteristicas1', figure=distribuicoes.charts[0]),
                html.P("Duração das músicas dada em minutos", style={'text-align': 'center'})
            ]),
            dbc.Col([
                dcc.Graph(id='caracteristicas2', figure=distribuicoes.charts[1]),
                html.P("Medida de quão acústica é a música, sendo esta uma \
                    medida inversamente proporcional ao quão eletrônica ela seria", style={'text-align': 'center'})
            ])
        ]),
        dbc.Row([
            dbc.Col([
                dcc.Graph(id='caracteristicas3', figure=distribuicoes.charts[2]),
                html.P("O quão dançável é considerada a faixa", style={'text-align': 'center'})
            ]),
            dbc.Col([
                dcc.Graph(id='caracteristicas4', figure=distribuicoes.charts[3]),
                html.P("Atributo relacionado à percepção do quão energética é a música, \
                    geralmente relacionado a alguns tipos de ritmo considerados mais animados", style={'text-align': 'center'})
            ])
        ]),
        dbc.Row([
            dbc.Col([
                dcc.Graph(id='caracteristicas5', figure=distribuicoes.charts[4]),
                html.P("O quão instrumental é a faixa (em \
                    detrimento da presença de mais vocais, por exemplo)", style={'text-align': 'center'})
            ]),
            dbc.Col([
                dcc.Graph(id='caracteristicas6', figure=distribuicoes.charts[5]),
                html.P("Quantifica a sensação passada por uma performance ao vivo", style={'text-align': 'center'})
            ])
        ]),
        dbc.Row([
            dbc.Col([
                dcc.Graph(id='caracteristicas7', figure=distribuicoes.charts[6]),
                html.P("Quantifica a percepção subjetiva de quão \
                    barulhenta é a música, inversamente proporcional à percepção de silêncio, \
                    medida em decibéis (dB)", style={'text-align': 'center'})
            ]),
            dbc.Col([
                dcc.Graph(id='caracteristicas8', figure=distribuicoes.charts[7]),
                html.P("Quanto de fala (trechos não cantados) a música contém", style={'text-align': 'center'})
            ])
        ]),
        dbc.Row([
            dbc.Col([
                dcc.Graph(id='caracteristicas9', figure=distribuicoes.charts[8]),
                html.P("Descreve o quão positiva é considerada a faixa", style={'text-align': 'center'})
            ]),
            dbc.Col([
                dcc.Graph(id='caracteristicas10', figure=distribuicoes.charts[9]),
                html.P("Dado em batidas por minuto, relacionado à velocidade rítmica da música", style={'text-align': 'center'})
            ])
        ]),
        html.P("A análise das distribuições desses atributos permite uma série de inferências a respeito \
            das propriedades musicais mais comuns. Alguns atributos tendem a ser bem concentrados em \
            valores comuns. Isso pode ser observado nos atributos 'speechiness' e 'duration_m', por exemplo, \
            de forma que existem poucas músicas de duração superior a 5 minutos e poucas músicas com um \
            grau de speechiness muito elevado. Por outro lado, alguns atributos possuem faixas mais \
            balanceadas entre as músicas, como é o caso de 'valence', por exemplo. Além disso, no caso \
            geral, boa parte dos atributos aparentam se caracterizar por uma distribuição normal.")
    ]),
    dbc.Row([
        html.H2("Distribuição dos álbuns, artistas e músicas populares versus o total", style={'text-align': 'center'}),
        html.P("A partir de séries temporais, apresentamos o número de músicas, artistas e álbuns lançados a cada ano. \
            Além disso, combinamos essa série com outra que demonstra quantos deles são classificados como populares. \
            Essas visualizações permitem observar uma tendência de crescimento do número de artistas e de álbuns, \
            com uma parcela de popularidade estável no decorrer dos anos. Por outro lado, o número de músicas \
            registradas na base tem caído ao longo dos anos."),
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
                dcc.Graph(id='correlacao1', figure=correlacao.fig_1),
                html.P("Como dito anteriormente nas distribuíções, a característica valência mede a positividade da música, a\
                    'danceabilidade' mede o quão dançante uma música é, já a energia representa uma medida perceptiva de intensidade e atividade de uma música.\
                    Todas essas características estão em um intervalo de 0 a 1. A característica tempo é relacionada ao ritmo da música, ela é medida em batidas\
                    por minuto. É interessante notar que há uma fraca correlação entre algumas variáveis, \
                    porém não conseguimos notar nenhuma combinação que resulte em um número maior de músicas populares."),
            ]),
            dbc.Row([
                html.H3("Correlações entre atributos relacionados à características auditivas", style={'text-align': 'center'}),
                dcc.Graph(id='correlacao2', figure=correlacao.fig_2),
                html.P("Como já mencionado anteriormente, a característica 'instrumentalness' prevê se uma música não contém vocais, \
                    a característica 'acousticness' é uma medida de confiança se a música é acústica e 'speechiness' \
                    detecta a presença de palavras faladas em uma música. Todas essas características estão em um intervalo de 0 a \
                    1. Já a característica 'loudness' é o volume geral de uma faixa em decibéis (dB). Nesse gráfico é \
                    possível perceber alguns padrões interessantes, como a correlação entre 'loudness' e 'instrumentalness'. \
                    Mas, novamente, não é possível identificar uma combinação que produza músicas mais populares."),
            ])
    ]),
    dbc.Row([
            html.H2("Distribuições temporais do lançamento das músicas", style={'text-align': 'center'}),
            dcc.Graph(id='datas_lancamentos', figure=datas_lancamentos.fig),
            html.P("Tentamos também visualizar se existem épocas do ano que concentram lançamentos de \
                músicas. Para isso, utilizamos um mapa de calor. No entanto, nos dados utilizados, mesmo \
                com precisão diária, a maioria das músicas ficam como lançadas no dia 1 de Janeiro ou no \
                dia 1 de cada mês, indicando uma possível inconsistência na base de dados. Para melhor \
                visualização, colocamos o dia 1 de Janeiro como 0 músicas lançadas. Pode-se observar \
                que o número de lançamentos no período natalino e de final de ano é baixo.")
    ]),
    dbc.Row([
            html.H2("Distribuição de semanas que as músicas permanecem na Billboard 100", style={'text-align': 'center'}),
            dcc.Graph(id='weeks_on_chart', figure=weeks_on_chart.weeks_on_chart),
            html.P("Na Billboard 100, músicas são ranqueadas semanalmente a partir de métricas como vendas de discos, \
                número de reproduções, etc. Não é comum que uma música fique muito tempo no ranking, entretanto \
                existem casos em que isso ocorreu, chegando a mais de 80 semanas. Essa música em específico \
                é a Radioactive, da banda Imagine Dragons.")
    ]),
    dbc.Row([
            html.H2("Relação entre o número de semanas que a música permaneceu na Billboard 100, sua posição máxima no ranking e sua popularidade", style={'text-align': 'center'}),
            dcc.Graph(id='weeks_on_chart_peak_position', figure=weeks_on_chart.weeks_on_chart_peak_position),
            html.P("Ao relacionar o tempo de semanas que uma musica permaneceu no chart e seu ranking máximo, \
                observando também sua popularidade, pode ser observado que musicas que alcançam rankings \
                elevados tendem a ficar um menor tempo no chart, enquanto as com ranks mais baixos ficam \
                mais tempo e são até mais populares.")
    ]),
    dbc.Row([
            html.H2("Atributos médios por popularidade", style={'text-align': 'center'}),
            dcc.Graph(id='atributos_popularidade', figure=atributos_popularidade.fig),
            html.P("Outra forma de tentar mensurar quais atributos afetam a popularidade de uma música \
                é através de uma seŕie temporal. Na visualização acima, o eixo X cresce de acordo com \
                a popularidade e o eixo Y representa os valores médios dos atributos para uma dada \
                popularidade. Nesse caso, é possível observar maior variância das séries de atributos \
                para músicas mais populares, também influenciada pela pouca amostragem nessa faixa. A \
                alta variância indica também não ser trivial definir objetivamente quais atributos \
                influenciam na maior popularidade no caso geral.")
    ]),
    dbc.Row([
        html.H2("Comparação de atributos entre músicas", style={'text-align': 'center'}),
        html.H6("Músicas escolhidas:"),
        dcc.Dropdown(id='musics',
            options=imports.df_metadata_songs['song_name'], value = ['thank u, next', 'Sunflower - Spider-Man: Into the Spider-Verse'],
            multi=True
        ),
        dcc.Graph(id='radar', figure=radar.atribute_radar([])),
        html.P("O objetivo deste gráfico é permitir a comparação das características musicais entre duas ou \
            mais músicas, por meio de um Radar Plot. Esse tipo de gráfico foi escolhido com a intenção de ser \
            parecido com um radar de atributos, iguais aqueles que vemos em jogos, onde cada personagem possui \
            características próprias.")
    ]),
    dbc.Row([
        html.H2("Atributos médios entre faixas de popularidade", style={'text-align': 'center'}),
        dcc.Graph(id='radar_medio', figure=radar_medio.fig),
        html.P("Um radar plot também pode ser utilizado para observar os atributos médios por faixa de \
            popularidade. Apesar de ser uma visualização simples e que trabalha com a média, é possível \
            observar alguns padrões de popularidade, por exemplo o fato de músicas mais acústicas no \
            geral não serem muito populares. O mesmo pode ser dito para músicas muito instrumentais.")
    ]),
    dbc.Row([
        html.H2("Gráfico de coordenadas paralelas para os atributos musicais", style={'text-align': 'center'}),
        dcc.Graph(id='coordenadas_paralelas', figure=coordenadas_paralelas.fig),
        html.P("Uma outra forma de comparar atributos no caso geral e relacioná-los à popularidade é através de um gráfico \
            de coordenadas paralelas. Através do gráfico de coordenadas paralelas exibido acima, é possível observar que \
            atributos como loudness e instrumentalness aparentam possuir faixas específicas que concentram as músicas mais \
            populares, ou seja, músicas que fogem muito da faixa média tendem a ser menos populares. Isso também pode ser \
            observado para a duração, que também concentra boa parte das músicas em uma faixa específica como já mencionado \
            anteriormente. É também possível observar que no caso da duração, músicas que fogem a essa faixa geralmente não são muito populares."),
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
        ),
        html.P("A ideia por trás deste gráfico é mostrar a distribuição de artistas/bandas ao redor do \
            mundo no decorrer dos anos (de forma cumulativa). É interessante notar que, nessa base em \
            específico, há um grande desbalanceamento em relação aos países representados, de forma que \
            o país Estados Unidos possui quase metade do número total de artistas/bandas. Outro ponto \
            importante que pode ser observado é a desigualdade relacionada à globalização, visto que \
            apenas um país do continente africano possui dados registrados.")
    ]),
    dbc.Row([
        html.H2("Evolução dos Gêneros", style={'text-align': 'center'}),

        dbc.Col(evolucao_generos.image_card, width=3), dbc.Col(evolucao_generos.graph_card, width=8),

        html.P("Hello boys")
    ], justify="around"),
    dbc.Row([
        html.H2("Pontuação anual dos gêneros", style={'text-align': 'center'}),
        html.H6("Gêneros escolhidos:"),
        dcc.Dropdown(id='music_genres',
            options=popularidade_generos.music_genres, value = ['rock'],
            multi=True
        ),
        dcc.Graph(id='genres_scores', figure=popularidade_generos.compare_genres([])),
        html.P("A Pontuação anual é uma das formas propostas para avaliar a popularidade anual de determinado álbum, artistas ou música, e é uma \
            combinação entre a popularidade máxima alcançada e as semanas que ele ficou nas paradas de sucesso. O objetivo deste gráfico é permitir \
            a comparação entre a pontuação anual de artistas de diferentes gêneros musicais, e observar possíveis padrões na popularidade de determinados \
            gêneros, como anos de alta ou baixa na popularidade. É possível observar, por exemplo, que para o gênero rock, a popularidade diminuiu ao \
            longo dos anos, e na última década sua popularidade voltou a crescer.")
    ]),
    dbc.Row([
        html.H2("Conclusão", style={'text-align': 'center'}),
        html.P("A partir da análise das correlações entre atributos, foi possível perceber alguns padrões interessantes, como a correlação \
            entre 'loudness' e 'instrumentalness', porém não conseguimos notar nenhuma combinação que resulte em um número maior de músicas populares."),
        html.P("Pôde ser observado que musicas que alcançam rankings elevados tendem a ficar um menor tempo no chart, enquanto as com ranks mais baixos \
            tendem a ficar mais tempo e são até mais populares no geral."),
        html.P("Músicas populares costumam ter baixa instrumentalidade e acusticidade, e existe uma grande variância entre os atributos à medida \
            que a popularidade aumenta. Também foi possível observar que músicas populares não são muito longas em duração."),
    ]),
])

@app.callback(
    Output("radar", "figure"),
    Input("musics", "value"),
)
def update_radar(value):
    return radar.atribute_radar(value)

# @app.callback(
#     Output("popover", "is_open"),
#     [Input("popover-bottom-target", "n_clicks")],
#     [State("popover", "is_open")],
# )
# def toggle_popover(n, is_open):
#     if n:
#         return not is_open
#     return is_open

@app.callback(
    [Output("line_chart", "figure"),
     Output("the_alert", "children")],
    [Input("genre_chosen", "value")]
)
def update_graph_card(genres):
    if len(genres) == 0:
        return no_update, evolucao_generos.alert
    else:
        df_filtered = evolucao_generos.df[evolucao_generos.df["Gêneros"].isin(genres)]
        df_filtered = df_filtered.groupby(["ano", "Gêneros"])[['num']].sum().reset_index()
        fig = imports.px.line(df_filtered, x="ano", y="num", color="Gêneros",
                      labels={"ano": "Year", "num": "# Músicas"}).update_traces(mode='lines+markers')
        return fig, no_update

def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@app.callback(
    Output("genres_scores", "figure"),
    Input("music_genres", "value"),
)
def update_genres_scores(value):
    return popularidade_generos.compare_genres(value)

if __name__ == '__main__':
    app.run_server(debug=True)
