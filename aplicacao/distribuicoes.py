import aplicacao.imports_datasets as imports

charts = []

cols = ["duration_ms", "acousticness", "danceability", "energy", "instrumentalness", "liveness", "loudness", "speechiness", "valence", "tempo"]
for c in cols:
    if c == "duration_ms":
        fig = imports.px.histogram(imports.df_songfeatures_acoustic_features[c]/(10**3)/60, x=c, width=500, height=250)
        charts.append(fig)
    else:
        fig = imports.px.histogram(imports.df_songfeatures_acoustic_features[c], x=c, width=500, height=250)
        charts.append(fig)