import imports_datasets as imports

df_mix = imports.df_songfeatures_acoustic_features.set_index('song_id').join(imports.df_metadata_songs.set_index('song_id'), how='inner')
df_mix2 = df_mix.join(imports.df_metadata_tracks.set_index('song_id'), how='inner')
df_mix2['release_date'] = imports.pd.to_datetime(df_mix2['release_date'])
df_mix2['year'] = df_mix2['release_date'].dt.year
df_mix2['month'] = df_mix2['release_date'].dt.month
df_mix2['day'] = df_mix2['release_date'].dt.day
df_mix2['decade'] = df_mix2['year'] - df_mix2['year'] % 10

x = df_mix2.groupby(['month', 'day']).size()
x = x.reset_index(level=0)
x = x.reset_index(level=0)
x.rename( columns={0 :'quantidade'}, inplace=True )

lista = []
for i in range(1, 13):
  dias = x[x['month'] == i]
  mes = []
  for dia in range(1, 32):
    if len(dias[dias['day'] == dia]) == 0:
      mes.append(0)
    else:
      mes.append(dias[dias['day'] == dia]['quantidade'].iloc[0])
  lista.append(mes)

  lista[0][0] = 0
fig = imports.px.imshow(lista,x=list(range(1, 32)), y=['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 
                                               'Agosto','Setembro', 'Outubro', 'Novembro','Dezembro'], 
                labels=dict(color='Número de<br>músicas'), )