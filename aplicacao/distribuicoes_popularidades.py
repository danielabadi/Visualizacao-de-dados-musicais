import aplicacao.imports_datasets as imports

artist_pop_by_year = imports.df_popularity_artist_pop.groupby(['year', 'is_pop']).count().reset_index()
album_pop_by_year =  imports.df_popularity_album_pop.groupby(['year', 'is_pop']).count().reset_index()
song_pop_by_year =  imports.df_popularity_song_pop.groupby(['year', 'is_pop']).count().reset_index()

artist_by_year =  imports.df_popularity_artist_pop.groupby(['year']).count().reset_index()
album_by_year =  imports.df_popularity_album_pop.groupby(['year']).count().reset_index()
song_by_year =  imports.df_popularity_song_pop.groupby(['year']).count().reset_index()

artist_pop_by_year = artist_pop_by_year[artist_pop_by_year['is_pop'] == True]
album_pop_by_year = album_pop_by_year[album_pop_by_year['is_pop'] == True]
song_pop_by_year = song_pop_by_year[song_pop_by_year['is_pop'] == True]

artist_pop_by_year.rename(columns = {'artist_id':'count', 'year_end_score':'percentage'}, inplace = True)
album_pop_by_year.rename(columns = {'album_id':'count', 'year_end_score':'percentage'}, inplace = True)
song_pop_by_year.rename(columns = {'song_id':'count', 'year_end_score':'percentage'}, inplace = True)

artist_by_year.rename(columns = {'year_end_score':'count_total'}, inplace = True)
album_by_year.rename(columns = {'year_end_score':'count_total'}, inplace = True)
song_by_year.rename(columns = {'year_end_score':'count_total'}, inplace = True)

artist_by_year = artist_by_year.drop(columns = ['is_pop'])
album_by_year = album_by_year.drop(columns = ['is_pop'])
song_by_year = song_by_year.drop(columns = ['is_pop'])

artist_pop_by_year = artist_pop_by_year.set_index('year').join(artist_by_year.set_index('year'))
album_pop_by_year = album_pop_by_year.set_index('year').join(album_by_year.set_index('year'))
song_pop_by_year = song_pop_by_year.set_index('year').join(song_by_year.set_index('year'))

charts = []

fig = imports.make_subplots(
    rows=1, cols=1
)

fig.add_trace(
    imports.go.Bar(name='Total de albums', x=album_by_year['year'], y=album_pop_by_year['count_total'], marker_color="#009E7F"),
    row = 1, col = 1
)

fig.add_trace(
    imports.go.Bar(name='Albums populares', x=album_by_year['year'], y=album_pop_by_year['count'], marker_color="#FA4300"),
    row = 1, col = 1
)

fig.update_layout({
    'barmode': 'overlay'})

fig.update_xaxes(title_text="Anos", row=1, col=1)
fig.update_yaxes(title_text="Quantidade", row=1, col=1)

charts.append(fig)

#Chart 2
fig = imports.make_subplots(
    rows=1, cols=1
)

fig.add_trace(
    imports.go.Bar(name='Total de artistas', x=artist_by_year['year'], y=artist_pop_by_year['count_total'], marker_color="#009E7F"),
    row = 1, col = 1
)

fig.add_trace(
    imports.go.Bar(name='Artistas populares', x=artist_by_year['year'], y=artist_pop_by_year['count'], marker_color="#FA4300"),
    row = 1, col = 1
)

fig.update_layout({
    'barmode': 'overlay'})

fig.update_xaxes(title_text="Anos", row=1, col=1)
fig.update_yaxes(title_text="Quantidade", row=1, col=1)

charts.append(fig)

#Chart 3

fig = imports.make_subplots(
    rows=1, cols=1
)

fig.add_trace(
    imports.go.Bar(name='Total de músicas', x=song_by_year['year'], y=song_pop_by_year['count_total'], marker_color="#009E7F"),
    row = 1, col = 1
)

fig.add_trace(
    imports.go.Bar(name='Músicas populares', x=song_by_year['year'], y=song_pop_by_year['count'], marker_color="#FA4300"),
    row = 1, col = 1
)

fig.update_layout({
    'barmode': 'overlay'})

fig.update_xaxes(title_text="Anos", row=1, col=1)
fig.update_yaxes(title_text="Quantidade", row=1, col=1)

charts.append(fig)