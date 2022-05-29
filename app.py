#!/usr/bin/env Python3

# TODO: change 'audio only' downloads from mp4 to mp3

from pytube import YouTube, Playlist
from os.path import expanduser
from moviepy.editor import *

save_location = expanduser("~\Videos\Youtube Downloader")

def download_video(url, quality):
    video = YouTube(url)
    print(f"Video Information:\nTitle: {video.title}\nViews: {(video.views)/1000}K")

    match quality:
        case 'b':
             video.streams.get_highest_resolution().download(save_location)
        case 'w':
             video.streams.get_lowest_resolution().download(save_location)
        case 'a':
             save_location = expanduser("~\Music\Youtube Downloader")
             video.streams.get_audio_only().download(save_location)

    print(f"[+] Downloaded {video.title}")


def download_playlist(url, quality):
    playlist = Playlist(url) 
    print(f"[+] Title: {playlist.title}")
    print(playlist.video_urls)
    save_location = expanduser(f"~\Videos\Youtube Downloader\{playlist.title}")
    match quality:
        case 'b':
             for i in playlist.video_urls:
                YouTube(i).streams.get_highest_resolution().download(save_location)
                print(f"[+] Downloaded {YouTube(i).title}")
        case 'w':
            for i in playlist.video_urls:
                YouTube(i).streams.get_lowest_resolution().download(save_location)
                print(f"[+] Downloaded {YouTube(i).title}")
        case 'a':
            try:
                save_location = expanduser(f"~\Music\Youtube Downloader\{playlist.title}")
                for i in playlist.video_urls:
                    YouTube(i).streams.get_audio_only().download(save_location)
                    print(f"[+] Downloaded {YouTube(i).title}")
            except:
                folder_name = input("Enter folder name (no special characters): ")
                save_location = expanduser(f"~\Music\Youtube Downloader\{folder_name}")
                for i in playlist.video_urls:
                    YouTube(i).streams.get_audio_only().download(save_location)
                    print(f"[+] Downloaded {YouTube(i).title}")

    print("Playlist has been downloaded")
        


def main():
    url = input('Enter URL: ')
    quality = input("Video Quatlity: (b)est | (w)orst | (a)udio only | (e)xit: ")
    if 'e' in quality:
        quit()
    if 'playlist' in url:
        download_playlist(url, quality)
    elif 'watch' in url:
        download_video(url, quality)
    else:
        print("[-] An Error Occured. Please check the url provided.\n\n")
    
    print(f"Download Complete\nLocation: {save_location}")



if __name__ == '__main__':
    main()
