from pygame import *

mixer.init()
#use either double back slashes or front slashes to give paths
mixer.music.load("C:/Users/ashug/OneDrive/Documents/python2025/exercises/healthy programmer/water.mp3")

mixer.music.set_volume(0.3)

while True:
    print("welcome to music player")
    print("press 1 to play the music player")
    print("press 2 to pause the music player")
    print("press 3 to resume the music player")
    print("press 4 to stop and quit the music player")

    user_input = int(input())
    if user_input == 1:
        mixer.music.play()
        print("\nmusic is playing")

    elif user_input == 2:
        mixer.music.pause()
        print("\nmusic is paused")
    elif user_input == 3:
        mixer.music.unpause()
        print("\nmusic is resumed")

    else:
        mixer.music.fadeout(1000)
        # mixer.music.stop()
        print("\nmusic is stopped bye bye")
        break