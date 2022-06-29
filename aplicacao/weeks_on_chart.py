import imports_datasets as imports

k = imports.df_popularity_song_chart.groupby("song_id").max().join(imports.df_metadata_songs.set_index("song_id"), how='inner')

weeks_on_chart_peak_position = imports.px.scatter(k,x ='weeks_on_chart', y="peak_position", color='popularity')
weeks_on_chart_peak_position.update_layout(
    yaxis = dict(autorange="reversed"),
    xaxis_title="Número de semanas", 
    yaxis_title = "Posição máxima"
)
weeks_on_chart_peak_position.layout.coloraxis.colorbar.title = "Popularidade"

weeks_on_chart = imports.px.histogram(imports.df_popularity_song_chart.groupby(by='song_id').max('weeks_on_chart'), x='weeks_on_chart')

weeks_on_chart.add_vline(imports.df_popularity_song_chart.groupby(by='song_id').max('weeks_on_chart')['weeks_on_chart'].median(), line_width=3, line_dash="dash", line_color="black", 
              annotation_text="Número de semanas mediano", annotation_font_size=20)

weeks_on_chart.update_layout(
    xaxis_title="Número de semanas", 
    yaxis_title = "Quantidade"
)