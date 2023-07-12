from pytube import YouTube

def download_audio(url, output_path):
    try:
        yt = YouTube(url)

        # Select the audio stream with the highest bitrate
        audio_stream = yt.streams.filter(only_audio=True).order_by('abr').last()

        # Download the audio file
        audio_stream.download(output_path=output_path)

        print("Audio download complete!")

    except Exception as e:
        print("An error occurred: ", str(e))

def download_audio_list(url_list, output_path):
    for url in url_list:
        try:
            yt = YouTube(url)
            audio_stream = yt.streams.filter(only_audio=True).order_by('abr').last()
            audio_stream.download(output_path=output_path)
            print("Audio download complete!")

        except Exception as e:
            print("An error occurred:", str(e))

def main():
    # Prompt the user for the YouTube video URL
    url = input("Enter the YouTube video URL: ")

    # Prompt the user for the output directory
    output_path = input("Enter the output directory path: ")

    download_audio(url, output_path)

if __name__ == '__main__':
    main()