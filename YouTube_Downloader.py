

from pytube import YouTube

print("Open Source Youtube Downloader, A7AVIND")

url=input("Video link goes here : ")
print("video link is %s"  % url)
path=input("enter file destination")
print("downloading to %s" %path)



print("Downloading")




try:
    YouTube(url).streams.first().download(path)
except:
    print("Unfinished due to errors")