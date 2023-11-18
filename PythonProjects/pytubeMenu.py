#Experiment to test ChatGPT's ability to create pytube downloader 11/17/2023 Conner Batson

from pytube import YouTube, Search
import os

def search_and_choose():
    query = input("Enter your search query: ")

    # Perform the YouTube search
    search = Search(query)
    search_results = search.results

    if not search_results:
        print("No search results found.")
        return

    # Display search results
    print("Search Results:")
    for i, result in enumerate(search_results, start=1):
        print(f"{i}. {result.title} - {result.watch_url}")

    # Allow the user to view additional results
    while True:
        view_more = input("Do you want to view more results? (y/n): ").lower()
        if view_more == 'y':
            search = search.get_next_results()
            for i, result in enumerate(search.results[len(search_results):], start=len(search_results) + 1):
                print(f"{i}. {result.title} - {result.watch_url}")
        else:
            break

    # Allow the user to choose a video
    try:
        choice = int(input("Enter the number of the video you want to download (0 to exit): "))
        if 0 < choice <= len(search.results):
            chosen_video = search.results[choice - 1]
            download_option = input("Do you want to download Video (v) or Audio (a) only? ").lower()
            if download_option == 'v':
                download_video(chosen_video.watch_url, download_audio=False)
            elif download_option == 'a':
                download_video(chosen_video.watch_url, download_audio=True)
            else:
                print("Invalid choice. Exiting.")
        else:
            print("Invalid choice. Exiting.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def download_video(video_url, download_audio=False):
    try:
        yt = YouTube(video_url)
        if download_audio:
            # Get the highest quality audio stream
            audio_stream = yt.streams.filter(only_audio=True).first()
            filepath = input("Enter the file path to save the audio (press Enter for current directory): ")
            filepath = filepath if filepath else None

            print(f"Starting download of audio [{yt.title}] to {filepath or 'the current directory'}")
            audio_stream.download(filepath)
            print("Download completed successfully.")
        else:
            # Get the highest resolution video stream
            video_stream = yt.streams.get_highest_resolution()

            filepath = input("Enter the file path to save the video (press Enter for current directory): ")
            filepath = filepath if filepath else None

            print(f"Starting download of video [{yt.title}] to {filepath or 'the current directory'}")
            video_stream.download(filepath)
            print("Download completed successfully.")
    except Exception as e:
        print(f"An error has occurred: {e}")

if __name__ == "__main__":
    search_and_choose()
