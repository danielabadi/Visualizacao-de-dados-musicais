import imports_datasets as datasets
import pandas as pd
import plotly.express as px
import numpy as np

country_count = datasets.df_countries.groupby(by='country_mb').count().reset_index()
country_count = country_count.drop(columns=['artist_id', 'followers', 'artist_type', 'main_genre', 'genres'])
country_count.rename(columns = {'image_url':'count', 'country_mb':'Country', 'popularity':'number_artists'}, inplace = True)
country_count['count'] = np.log2(country_count['count']) 

fig = px.choropleth_mapbox(country_count, geojson=datasets.data, color="count",
                           locations="Country", featureidkey="properties.ADMIN",
                           center={"lat": 37.0902, "lon": -95.7129},
                           mapbox_style="carto-positron", zoom=1,
                           opacity=0.8, color_continuous_scale=px.colors.diverging.Portland,
                           labels={'count':'Taxa log2', 'number_artists':'Número de artistas/bandas', 'Country':'País'},hover_data= ['number_artists'])
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})