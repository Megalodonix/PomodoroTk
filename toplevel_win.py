import threading
import pydub
from pydub.playback import play
import tkinter as tk 


def soundEffect():
    sfx = pydub.AudioSegment.from_wav('./resources/sfx/sound.wav')
    play(sfx)


class TimeUp():
    def __init__(self, root, text):
        self.timeupwin = tk.Toplevel(root)
        self.timeupwin.geometry("300x155")
        self.time_up_label = tk.Label(self.timeupwin,
                                      text=(f"{str(text)}"),
                                      font=("", 10),
                                      justify="left",
                                      anchor='w').pack(pady=60, 
                                                       fill="both",
                                                       padx=30)
        threading.Thread(target=soundEffect).start()   
