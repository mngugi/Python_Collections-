from pytube import Playlist

youtube_url = input('https://www.youtube.com/watch?v=XhGDh-niEB4')
play_list = Playlist(youtube_url)


for video in play_list.videos:
    video.stream.get_highest_resolution().download()
    
    
