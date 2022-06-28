from dash import Dash, dcc, html, Input, Output

import datas_lancamentos
import imports_datasets
import mapa

app = Dash(__name__)
app.layout = html.Div(children=[
    html.Div([
            html.H1("Distribuições temporais do lançamento das músicas"),

            dcc.Graph(id='datas_lancamentos', figure=datas_lancamentos.fig)
    ]),
    html.Div([
        html.H1("Distribuição de artistas pelo mundo", style={'text-align': 'center'}),

        dcc.Graph(id='my_bee_map', figure=mapa.fig)
    ])#,
    #html.Div([
    #    html.H1("Olá Daniel, estás com frio?", style={'text-align': 'center'}),
    #    dcc.Graph(id='my_bee_map1', figure=fig_2)
    #])
])


if __name__ == '__main__':
    app.run_server(debug=True)