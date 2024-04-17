import time
import winsound        #to play sound on windows interface

def alarm(hour, minute):
    while True:
        now = time.localtime()
        if now.tm_hour == hour and now.tm_min == minute:
            winsound.PlaySound("audio.wav", winsound.SND_ALIAS)   #(file location, snd_alias mean the sound plays only if it exists)
            break

hour = int(input("Enter the hour: "))
minute = int(input("Enter the minute: "))
alarm(hour, minute)