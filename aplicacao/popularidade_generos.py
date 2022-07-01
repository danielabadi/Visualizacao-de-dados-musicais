import aplicacao.imports_datasets as imports

df_split = imports.df_metadata_artists.copy()
df_split = df_split[df_split['genres'] != '[]']
df_split['genres'] = df_split['genres'].apply(imports.literal_eval)
df_split = df_split.explode('genres')

newdf = imports.df_popularity_artist_pop.set_index('artist_id').join(df_split[['artist_id', 'genres']].set_index('artist_id'))

all_pop_mean = newdf.groupby('year').mean().reset_index()
genre_pop_mean = newdf.groupby(['year', 'genres']).mean().reset_index()
years = all_pop_mean['year']

music_genres = sorted(list(genre_pop_mean['genres'].unique()))

def compare_genres(genres_choosen):
	global all_pop_mean
	fig = imports.go.Figure()
	fig.add_trace(imports.go.Scatter(x=years, y=all_pop_mean['year_end_score'],name="Pontuação Média", line_width=2))

	for i in range(len(genres_choosen)):
		genre = genre_pop_mean[genre_pop_mean['genres'] == genres_choosen[i]]
		fig.add_trace(
	        imports.go.Scatter(
	            x = years,
	            y = genre['year_end_score'],
	            name = 'Gênero: ' + genres_choosen[i],
	        )
	    ),

	return fig
