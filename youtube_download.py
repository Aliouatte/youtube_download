# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 19:01:13 2022

@author: younes
younesbelabid@yahoo.com

install pytube
"""

from pytube import YouTube

#url = "https://www.youtube.com/watch?v=8qcSdqc7QYo"
print("START")

BASE = "https://www.youtube.com"
def get_url_user():
    while True:
        url = input("Donnez un url de votre vidéo (Youtube) : ")
        if url[:len(BASE)] == BASE:
            print("url valide")
            return url  
        print("ERREUR : Voud devez rentrer une url valide !")

url = get_url_user()




def on_download_progress(stream, chunk, bytes_remaining):
    bytes_downloaded = stream.filesize - bytes_remaining
    percent_downloaded = bytes_downloaded * 100 / stream.filesize
    
    print(f'progression du telechargement : {int(percent_downloaded)} %')


youtube_video = YouTube(url)

youtube_video.register_on_progress_callback(on_download_progress)


print("Title : " + youtube_video.title)
print("Nb Views : " + str(youtube_video.views))


print("")

def get_video_stream_itag_user(strms):
    print("Choix des résolutions")
    index = 1
    for stream in streams:
        print(f"{index} - {stream.resolution}")
        index += 1
        
    while True:
        res_num = input("Choisir la résolution : ")  
        if res_num == "":
            print("ERREUR : vous devez donner un nombre")
        else:
            try:
                res_num_int = int(res_num)
            except:
                print("ERREUR : vous devez donner un nombre")
            else:
                if not 1 <= res_num_int <= len(streams):
                    print("ERREUR : vous devez donner un nombre entre 1 et", len(streams))
                else:
                    break
                
                
    Itag = streams[res_num_int - 1].itag
    return Itag

streams = youtube_video.streams.filter(progressive= True,file_extension='mp4')
Itag = get_video_stream_itag_user(streams)


stream = youtube_video.streams.get_by_itag(Itag)

print("Downloading :")
stream.download()
print()
print('END')
