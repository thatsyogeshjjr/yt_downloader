#!/usr/bin/env Python3

from pytube import YouTube, Playlist
from os.path import expanduser
import os

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
             out_file = video.streams.get_audio_only().download(save_location)
             if out_file:
                base, ext = os.path.splitext(out_file)
                print("hello")
                new_file = base + ".mp3"
                os.rename(out_file, new_file)

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
            save_location = expanduser(f"~\Music\Youtube Downloader")
            try:
                save_location = expanduser(f"~\Music\Youtube Downloader\{playlist.title}")
                for i in playlist.video_urls:
                    out_file = YouTube(i).streams.get_audio_only().download(save_location)
                    print(f"[+] Downloaded {YouTube(i).title}")

                    if out_file:
                        base, ext = os.path.splitext(out_file)
                        new_file = base + ".mp3"
                        os.rename(out_file, new_file)
            except:
                folder_name = input("Enter folder name (no special characters): ")
                save_location = expanduser(f"~\Music\Youtube Downloader\{folder_name}")
                for i in playlist.video_urls:
                    out_file = YouTube(i).streams.get_audio_only().download(save_location)
                    print(f"[+] Downloaded {YouTube(i).title}")

                    if out_file:
                        base, ext = os.path.splitext(out_file)
                        new_file = base + ".mp3"
                        os.rename(out_file, new_file)
        


def main():
    try:
        url = input('Enter URL: ')
    except:
        print("[-] An error occured with the url provided")
    if url == '':
        print("[-] No link provided.\n[-] Exiting Application")
        quit()
        
    quality = input("Video Quatlity: (b)est | (w)orst | (a)udio only | (e)xit: ")
    if 'e' in quality:
        print("[+] Exiting Application.")
        quit()
    if 'playlist' in url:
        download_playlist(url, quality)
    elif 'watch' in url:
        download_video(url, quality)
    else:
        print("[-] An Error Occured. Please check the url provided.\n")
        quit()
    
    print(f"Download Complete\nLocation: {save_location}")


def premain():
    print("          __          __                    __                __         ")
    print("   __  __/ /_    ____/ /___ _      ______  / /___  ____ _____/ /__  _____")
    print("  / / / / __/   / __  / __ \ | /| / / __ \/ / __ \/ __ `/ __  / _ \/ ___/")
    print(" / /_/ / /_    / /_/ / /_/ / |/ |/ / / / / / /_/ / /_/ / /_/ /  __/ /    ")
    print(" \__, /\__/____\__,_/\____/|__/|__/_/ /_/_/\____/\__,_/\__,_/\___/_/     ")
    print("/____/   /_____/                                                         \n\n")
    print("\t\tDownload youtube playlists, audios, videos.\n")



if __name__ == '__main__':
    premain()
    main()