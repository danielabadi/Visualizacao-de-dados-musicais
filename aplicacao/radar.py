import imports_datasets as imports

musicas = []
categories = ['mode','acousticness','danceability',
              'energy', 'instrumentalness', 'liveness', 'speechiness', 'valence', 'mode']

def atribute_radar(value):
    fig = imports.go.Figure()

    for i in range(len(value)):
        fig.add_trace(imports.go.Scatterpolar(r=imports.pd.DataFrame(imports.dataset_radar[imports.dataset_radar["song_name"]==value[i]][['mode', 'acousticness', 'danceability', 'energy', 
            'instrumentalness', 'liveness', 'speechiness', 'valence', 'mode']]).mean(), theta=categories, name='Música: '+ value[i]))

    return fig