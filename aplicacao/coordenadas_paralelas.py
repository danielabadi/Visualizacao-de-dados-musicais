import aplicacao.imports_datasets as imports

cols = ["instrumentalness", "duration_ms", "speechiness", "liveness", "acousticness", "danceability", "energy", "valence", "tempo", "loudness"]
merged = imports.df_songfeatures_acoustic_features.merge(imports.df_metadata_songs, on="song_id")
fig = imports.px.parallel_coordinates(merged[cols+["popularity"]], color="popularity",
                             color_continuous_scale=imports.px.colors.diverging.Tealrose,
                             color_continuous_midpoint=2, range_color=[0,100])