import pandas as pd
import numpy as np
import json

df_songfeatures_acoustic_features = pd.read_csv('../musicoset_songfeatures/acoustic_features.csv', sep='\t')
df_songfeatures_lyrics = pd.read_csv('../musicoset_songfeatures/lyrics.csv', sep='\t')

df_popularity_song_pop = pd.read_csv('../musicoset_popularity/song_pop.csv', sep='\t')
df_popularity_song_chart = pd.read_csv('../musicoset_popularity/song_chart.csv', sep='\t')
df_popularity_artist_pop = pd.read_csv('../musicoset_popularity/artist_pop.csv', sep='\t')
df_popularity_artist_chart = pd.read_csv('../musicoset_popularity/artist_chart.csv', sep='\t')
df_popularity_album_pop = pd.read_csv('../musicoset_popularity/album_pop.csv', sep='\t')
df_popularity_album_chart = pd.read_csv('../musicoset_popularity/album_chart.csv', sep='\t')

df_metadata_tracks = pd.read_csv('../musicoset_metadata/tracks.csv', sep='\t')
df_metadata_songs = pd.read_csv('../musicoset_metadata/songs.csv', sep='\t')
df_metadata_releases = pd.read_csv('../musicoset_metadata/releases.csv', sep='\t')
df_metadata_artists = pd.read_csv('../musicoset_metadata/artists.csv', sep='\t')
df_metadata_albums = pd.read_csv('../musicoset_metadata/albums.csv', sep='\t')

f = open('../countries.geojson')
data = json.loads(f.read())

df_countries = pd.read_csv('../artist_country.csv')
df_countries = df_countries.set_index('name').join(df_metadata_artists.set_index('name'), how='inner')