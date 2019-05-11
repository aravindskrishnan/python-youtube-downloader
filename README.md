# python-youtube-downloader
A simple and lightweight python based youtube downloader made using pytube 


## install pytube
*pytube* is and lightweight, dependency-free Python library (and command-line utility) for downloading YouTube Videos
we make use of this library in our project, as a beginers guide i will try to keep the steps as detailed as possible and code as simple as possible.
*pytube* can be installed usig pip, for that open up terminal or cmd and copy paste the following commands
```bash
$ pip install pytube
```
NOTE: for pip to work, python should be installed on your computer


## Get started with the code
open up your python IDE and start by importing the libraries
```python
>>> from pytube import YouTube
```
after importing the libraries, we can print some introductory statements like instruction to use or simply a message. For that we use *print()* function, which is a standard function in python.
```python
>>> print("Youtube Downloader")
```
now comes the main part, here we will accept input from the user for the adress of the video to be downloaded and the path to where the video is to be stored, for that we use the function *input()*, which is again a standard function in python.
The adress of the the YouTube video is stored in the object *url*, similarly the path to which the file is to be downloaded is stored in the object *path*. Both *path* and *url* are values which has to be entered by the user.
```python
>>>url=input("Video link goes here : ")
>>>path=input("enter file destination : ")
```
for giving confirmation to user we can print back the entered values by using *print()* function again
```python
>>>print("video link is %s"  % url)
>>>print("downloading to %s" %path)
```
next comes the part where we use the pytube library to download the YouTube video whose link we entered, 
but to have some added functionality, we use the exception handling property of python ( for example, if we enter a broken or invalid URL then it will return *unfinished due to errors* rather than traditional error reports ). For doing so we use the block *try* and *except*(The try block lets you test a block of code for errors. The except block lets you handle the error.)
Here, the line *YouTube(url).streams.first().download(path)* means that it will download the highest quality video file to the path which we specified, ( this line of code is specific to the pytube library, for more information and functionality visit https://github.com/nficano/pytube/blob/master/README.md )
```python
>>>try:
    >>>YouTube(url).streams.first().download(path)
    >>>print("Downloading")
>>>except:
    >>>print("Unfinished due to errors")
```
And with that we are done with the coding. The entire code is given below
```python


from pytube import YouTube

print("Youtube Downloader")

url=input("Video link goes here : ")
path=input("enter file destination : ")


print("video link is %s"  % url)
print("downloading to %s" %path)



try:
    YouTube(url).streams.first().download(path)
    print("Downloading")
except:
    print("Unfinished due to errors")
```

For those who doesnt like to code, there is an executable file as well. You can get the file from here or download the *.py* file and compile for your specific operating system.

