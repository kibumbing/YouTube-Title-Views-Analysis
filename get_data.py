from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser

DEVELOPER_KEY='AIzaSyDUenmVjAhswiOQ-62Q_EpxFL84EfyatUk'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
channel_id = 'UCUj6rrhMTR9pipbAWBAMvUQ'
playlists = youtube.playlists().list(channelId=channel_id, part='snippet', maxResults=20).execute()

import pandas as pd

ids = []
titles = []
for i in playlists['items']:
    ids.append(i['id'])
    titles.append(i['snippet']['title'])

df = pd.DataFrame([ids, titles]).T
df.columns = ['PlayLists', 'Titles']
print(df)

#영상 list
cdm = df['PlayLists'][7]
playlist_videos = youtube.playlistItems().list(playlistId=cdm, part='snippet', maxResults=50).execute()
nextPageToken = playlist_videos.get('nextPageToken')

while ('nextPageToken' in playlist_videos):
    nextPage = youtube.playlistItems().list(playlistId=cdm, part='snippet', maxResults=50, pageToken=nextPageToken).execute()
    playlist_videos['items'] = playlist_videos['items'] + nextPage['items']

    if 'nextPageToken' not in nextPage:
        playlist_videos.pop('nextPageToken', None)
    else:
        nextPageToken = nextPage.get('nextPageToken')


video_names = []
video_ids = []
date = []

for v in playlist_videos['items']:
    video_names.append(v['snippet']['title'])
    video_ids.append(v['snippet']['resourceId']['videoId'])
    date.append(v['snippet']['publishedAt'])

vdf = pd.DataFrame([date, video_names, video_ids]).T
vdf.columns = ['Date', 'Title', 'IDS']
print(vdf)

import re

category_id = []
views = []
likes = []
dislikes = []
comments = []
mins = []
seconds = []
title = []
date = []

print(len(vdf))

for u in range(len(vdf)):
    request = youtube.videos().list(part='snippet,contentDetails,statistics', id=vdf['IDS'][u])
    response = request.execute()

    if response['items'] == []:
        ids.append('-')
        category_id.append('-')
        views.append('-')
        likes.append('-')
        dislikes.append('-')
        comments.append('-')
        date.append('-')

    else:
        title.append(response['items'][0]['snippet']['title'])
        category_id.append(response['items'][0]['snippet']['categoryId'])
        views.append(response['items'][0]['statistics']['viewCount'])
        likes.append(response['items'][0]['statistics']['likeCount'])
        #dislikes.append(response['items'][0]['statistics']['dislikeCount'])
        #comments.append(response['items'][0]['statistics']['commentCount'])
        date.append(response['items'][0]['snippet']['publishedAt'])

cdm = pd.DataFrame([title, category_id, views, likes, dislikes, comments, date]).T
cdm.columns=['title', 'category_id', 'views', 'likes', 'dislikes', 'comments', 'date']
print(cdm)
cdm.to_csv('calmdownman_2022.csv')