# Experimental file to test pytube 11/17/2023 (Conner Batson)
from pytube import YouTube
from pytube import Search

def download_program():
    Test1()
    Test2()

def ytPrint(ytObject):
    print(ytObject.title)
    print(ytObject.author)
    print(str(ytObject.length)+"s")
    print(ytObject.thumbnail_url)

def Test1():
    yt = YouTube('http://youtube.com/watch?v=2lAe1cqCOXo')
    print(yt.title)
    print(yt.thumbnail_url)

def Test2():
    s = Search('wliia')
    print(len(s.results))
    for result in s.results:
        print("<========>")
        ytPrint(result)
    s.get_next_results()
    print(len(s.results))
    for result in s.results:
        print("<========>")
        ytPrint(result)

if __name__ == "__main__":
    download_program()