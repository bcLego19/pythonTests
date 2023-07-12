# Author: Conner Batson
# Title: pytubeSongByArtist
# Description: experimental code to fetch audio files of music videos by artist name.
# Status: Partially complete. Using loops with pytube download does not always work.
# Date created: 7/12/2023
# Last revision: 7/12/2023 3:00 PM

from pytube import Search
from pytube import YouTube

def get_artist_songs(artist_name):
    query_string = f"{artist_name} songs"
    return Search(query_string)

def filter_official_songs(search_results, artist_name):
    official_songs = []
    filter_string = f"{artist_name} -"
    for result in search_results.results:
        if (
            filter_string in result.title.lower()
            and "album" not in result.title.lower()
            and result.length <= 600
            or "official" in result.title.lower()
        ):
            official_songs.append(result)
    return official_songs

def print_official_songs(official_list):
    for item in official_list:
        print(f"{item.title}\n{item.watch_url}\n")

def download_audio(url, output_path):
    try:
        yt = YouTube(url)
        audio_stream = yt.streams.filter(only_audio=True).order_by('abr').last()
        audio_stream.download(output_path=output_path)
        print("Audio download complete!")

    except Exception as e:
        print("An error occurred:", str(e))

def download_audio_list(url_list, output_path):
    for url in url_list:
        download_audio(url, output_path)

def get_urls(official_list):
    return [item.watch_url for item in official_list]

def main():
    artist_name = input("Enter the artist name: ")
    output_path = input("Enter the output directory path: ")

    song_link_list = get_artist_songs(artist_name)
    official_list = filter_official_songs(song_link_list, artist_name)
    
    print("----------")
    print_official_songs(official_list)
    
    url_list = get_urls(official_list)
    download_audio_list(url_list, output_path)

if __name__ == '__main__':
    main()
