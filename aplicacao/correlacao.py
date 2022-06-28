import imports_datasets as imports

x_1 = ['valence', 'danceability', 'tempo', 'energy']
fig_1 = imports.px.scatter_matrix(imports.df_mix2, # esse mix foi definido na parte das datas de lançamento
    dimensions=x_1,
    color="popularity")
fig_1.update_traces(marker=dict(size=3))

x_2 = ['instrumentalness', 'loudness', 'acousticness', 'speechiness']     
fig_2 = imports.px.scatter_matrix(imports.df_mix2, # esse mix foi definido na parte das datas de lançamento
    dimensions=x_2,
    color="popularity")

fig_2.update_traces(marker=dict(size=3))