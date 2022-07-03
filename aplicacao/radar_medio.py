import aplicacao.imports_datasets as imports

newdf = imports.df_songfeatures_acoustic_features.set_index('song_id').join(imports.df_metadata_songs.set_index('song_id'))

mean_80_up = imports.pd.DataFrame(newdf.query("`popularity` >= 80")[['mode', 'acousticness', 'danceability', 'energy', 
                                                             'instrumentalness', 'liveness', 'speechiness', 'valence', 'mode']])
mean_60_80 = imports.pd.DataFrame(newdf.query("`popularity` >= 60 and `popularity` < 80")[['mode', 'acousticness', 
                                                            'danceability', 'energy', 'instrumentalness', 'liveness', 'speechiness', 'valence', 'mode']])
mean_40_60 = imports.pd.DataFrame(newdf.query("`popularity` >= 40 and `popularity` < 60")[['mode', 'acousticness',
                                                            'danceability', 'energy', 'instrumentalness', 'liveness', 'speechiness', 'valence', 'mode']])
mean_20_40 = imports.pd.DataFrame(newdf.query("`popularity` >= 20 and `popularity` < 40")[['mode', 'acousticness',
                                                            'danceability', 'energy', 'instrumentalness', 'liveness', 'speechiness', 'valence', 'mode']])
mean_20_low = imports.pd.DataFrame(newdf.query("`popularity` < 20")[['mode', 'acousticness','danceability',
                                                             'energy', 'instrumentalness', 'liveness', 'speechiness', 'valence', 'mode']])

categories = ['mode','acousticness','danceability',
              'energy', 'instrumentalness', 'liveness', 'speechiness', 'valence', 'mode']

fig = imports.go.Figure(
    data=[
        imports.go.Scatterpolar(r=mean_80_up.mean(), theta=categories, name='Popularidade 80+'),
        imports.go.Scatterpolar(r=mean_60_80.mean(), theta=categories, name='Popularidade entre 60 e 80'),
        imports.go.Scatterpolar(r=mean_40_60.mean(), theta=categories, name='Popularidade entre 40 e 60'),
        imports.go.Scatterpolar(r=mean_20_40.mean(), theta=categories, name='Popularidade entre 20 e 40'),
        imports.go.Scatterpolar(r=mean_20_low.mean(), theta=categories, name='Popularidade 20-')
    ],
    layout=imports.go.Layout(
        polar={'radialaxis': {'visible': True}},
        showlegend=True
    )
)