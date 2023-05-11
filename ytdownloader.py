#!/usr/bin/python3

from pytube import YouTube

link = input("Paste the link of the video: ")
location = input("Where would you like the video to be downloaded? ")

yt = YouTube(link)

print("Title: ", yt.title)
print("Channel: ", yt.author)

dl = input("Is this the right video? ").lower

if dl == "yes" or "y":
    print("Great! Starting download now!")
else:
    print("Use a different link and try again.")
    quit

yt.streams.get_highest_resolution().download(location)

print("Video downloaded!")
