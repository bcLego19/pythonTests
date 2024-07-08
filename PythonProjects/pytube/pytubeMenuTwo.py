# Last update 5/11/2024 by Conner Batson
#
# Experiment to test YouTube video download functionality (comments added 11/17/2023)
from pytube.cli import on_progress
from pytube import YouTube, Search
from pytube.exceptions import PytubeError
import os, sys

# Default directory global
DEFAULT_DOWNLOAD_DIR = os.getcwd()

def get_user_input(prompt, valid_options=None):
    """
    This function prompts the user for input and validates it against
    optional valid_options list. It returns the chosen option.
    """
    while True:
        user_input = input(prompt).lower()
        if valid_options and user_input not in valid_options:
            print("Invalid input. Please enter one of:", ", ".join(valid_options))
        else:
            return user_input

def download_stream(stream, filepath=None):
    """
    This function downloads the provided stream to the specified filepath
    or the default download directory (from config.py). It utilizes the
    built-in on_progress callback for a progress bar and raises a
    DownloadError for any exceptions encountered during download.
    """
    try:
        # Access default download directory from config.py
        download_dir = os.path.join(os.getcwd(), DEFAULT_DOWNLOAD_DIR)
        filepath = filepath if filepath else download_dir

        # Download logic using stream.download(filepath)
        stream.download(filepath)
        print("Download completed successfully.")
    except Exception as e:
        raise DownloadError(f"An error occurred during download: {e}") from e
  
class DownloadError(Exception):
    """
    Custom exception class to handle download-related errors.
    """
    pass

# Function to handle YouTube search and video selection process
def search_and_choose(directory_name=None):
    """
    Prompts the user for a search query, performs a YouTube search, displays results,
    allows browsing additional pages, and lets the user choose a video to download.

    This function handles potential exceptions during the search process.
    """
    query = get_user_input("Enter your search query: ")

    try:
        perform_search_with_pagination(query, directory_name)
        return
    except PytubeError as e:
        print(f"An error occurred during the search: {e}")
    except Exception as e:  # Catch unexpected exceptions
        print(f"An unexpected error occurred: {e}")

    print("Search failed. Please try again.")  # General message after exceptions

def perform_search_with_pagination(query, directory_name=None):
    # Perform YouTube search and store results
    search_obj = Search(query)
    search_results = search_obj.results

    # Handle case with no search results
    if not search_results:
        print("No search results found.")
        return
    else:

        # Display search results with titles and watch URLs
        print("Search Results:")
        for i, result in enumerate(search_results, start=1):
            print(f"{i}. {result.title} - {result.watch_url}")

        # Allow viewing additional results (pagination)
        view_more = get_user_input("Do you want to view more results? (y/n): ").lower()
        while view_more in ["y"]:
            if view_more == 'y':
                next_page_results = search_obj.get_next_results()
                for i, result in enumerate(next_page_results[len(search_results):], start=len(search_results) + 1):
                    print(f"{i}. {result.title} - {result.watch_url}")
                search_results.extend(next_page_results)  # Update search_results with new page
                view_more = get_user_input("Do you want to view more results? (y/n): ").lower()
            else:
                break
        
        # Call get_user_choice to handle video and download option selection
        video_info = get_user_choice(search_results)
        if video_info:  # Check if user exited due to invalid input (get_user_choice returns None)
            download_video(video_info["url"], video_info["download_audio"], directory_name)
    
    return

def get_user_choice(search_results):
    """
    Prompts the user to choose a video and download option from search results.

    Args:
        search_results: A list of YouTube video objects from a pytube Search object.

    Returns:
        A dictionary containing the chosen video URL, title, and download option (v or a), 
        or None if the user enters an invalid option.
    """

    while True:
        choice = int(get_user_input("Enter the number of the video you want to download (0 to exit): "))
        if 0 < choice <= len(search_results):
            chosen_video = search_results[choice - 1]

            download_option = get_user_input("Do you want to download Video (v) or Audio (a) only? ").lower()
            if download_option in ['v', 'a']:
                return {
                    "url": chosen_video.watch_url,
                    "title": chosen_video.title,
                    "download_audio": download_option == "a",
                }
            else:
                print("Invalid choice. Please enter 'v' or 'a'.")
        elif choice <= 0:
            print("You chose to exit.\n")
            return None  # Indicate user exited due to invalid input
        else:
            print("Invalid choice. Exiting.\n")
            return None  # Indicate user exited due to invalid input

def download_video(video_url, download_audio=False, directory_name=None):
    """
    This function downloads a YouTube video (entire video or audio only) based on the URL
    and user selection. It prompts the user for a file path, displays download status messages,
    and utilizes the built-in on_progress callback for a progress bar.
    """
    try:
        # Create a YouTube object with the on_progress_callback set
        yt = YouTube(video_url, on_progress_callback=on_progress)

        if download_audio:
            # Select the first audio stream (presumably highest quality)
            audio_stream = yt.streams.filter(only_audio=True).first()
        else:
            # Get the highest resolution video stream
            video_stream = yt.streams.get_highest_resolution()

        # If no path given, prompt user for file path or use current directory if none provided; otherwise, use provided path to directory
        if (directory_name == None):
            filepath = get_user_input("Enter the file path to save the {} (press Enter for current directory): ".format("audio" if download_audio else "video"))
            filepath = filepath if filepath else None
        else:
            filepath = directory_name

        # Print download start message with chosen filename or indicating current directory
        print(f"Starting download of {'audio' if download_audio else 'video'} [{yt.title}] to {filepath or 'the current directory'}")

        # Download the audio/video stream using the download method
        if download_audio:
            download_stream(audio_stream, filepath)
        else:
            download_stream(video_stream, filepath)

        print("Download completed successfully.")
    except Exception as e:
        print(f"An error has occurred: {e}")

def main_menu():
    """
    This is the main driver function for the menu. Based on the given information from the user,
    it will download one or multiple files from youtube.
    """
    directory_name = None

    if len(sys.argv) > 1:
        if os.path.isdir(sys.argv[1]):
            directory_name = sys.argv[1]
        else:
            print(str(sys.argv[1]) + " is not a valid directory location.")

    print("Welcome to pytube menu!")
    options = get_user_input("Do you want to download one or multiple files? (enter \"one\" or \"many\"): ")
    
    while ( options not in ["one", "many", "exit"] ):
        options = get_user_input("Do you want to download one or multiple files? (enter \"one\" or \"many\"): ")
    
    print("options: " + options)

    if (options == "one"):
        print("you chose to get one video")
        search_and_choose(directory_name)
    elif (options == "many"):
        print("you chose to get multiple videos")

    print("\nGoodbye!")

    return

# Execute the search and choose function if script is run directly
if __name__ == "__main__":
    main_menu()
