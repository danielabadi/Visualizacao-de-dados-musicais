import imports_datasets as imports


x = imports.df_mix2.groupby(['popularity']).mean() # esse mix foi definido na parte das datas de lançamento
x = x.reset_index(level=0)
a = ['acousticness', 'danceability', 'energy', 'instrumentalness', 'liveness', 'speechiness', 'valence']

fig = imports.px.line(x, x="popularity", y=a, markers=True, labels=dict(x='Popularidade', y='Valor'))

fig.add_vline(x=imports.df_mix2['popularity'].median(), line_width=3, line_dash="dash", line_color="black", 
              annotation_text="Popularidade mediana", annotation_font_size=20)

fig.update_layout(xaxis_title="Popularidade (0 a 100)", 
    yaxis_title = "Valor (0 a 1)")