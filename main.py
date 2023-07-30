import tkinter as tk
import helpmenu
import toplevel_win 
from tkinter import messagebox 
import time


def add():
    task_listbox.insert(task_listbox.size(), task_box.get())
    print(f"Added new task: {task_box.get()}")


def delete():
    for index in reversed(task_listbox.curselection()):
        print("Removed task")
        task_listbox.delete(index)

def removeTopTask():
    task_listbox.delete(0)
    print("Task done. removing top task.")

# Please ignore "possibly unbound" errors if you use mypy...
def focusTimer():
    try:
        usrinpt = int(focus_minute.get())*60 + int(focus_second.get())
    except Exception:
        messagebox.showwarning(title="Error!", message="Invalid input.")
    finally:
        pass
    while usrinpt > -1:
        mins, secs = divmod(usrinpt,60)
        focus_minute.set("{0:2d}".format(mins))
        focus_second.set("{0:2d}".format(secs))
        win.update()
        time.sleep(1)

        if(usrinpt == 0):
            toplevel_win.TimeUp(win, "Focus time is over!\nYou may take a break now!")
            removeTopTask()
            focus_minute.set("25")
            focus_second.set("00")
            
        usrinpt -= 1

def restTimer():
    try:
        usrinpt = int(rest_minute.get())*60 + int(rest_second.get())
    except Exception:
        messagebox.showwarning(title="Error!", message="Invalid input.")
    finally:
        pass
    while usrinpt > -1:
        mins, secs = divmod(usrinpt,60)
        rest_minute.set("{0:2d}".format(mins))
        rest_second.set("{0:2d}".format(secs))
        win.update()
        time.sleep(1)

        if(usrinpt == 0):
            toplevel_win.TimeUp(win, "Break time is over!\nYou may do another task.")
            removeTopTask()
            rest_minute.set("05")
            rest_second.set("00")
            
        usrinpt -= 1



win = tk.Tk()


icon = tk.PhotoImage(file="./resources/icon/pomodorotk.png")
win.iconphoto(True, icon)
win.title("PomodoroTk")
win.config(bg="#282828")
# win.geometry("600x300") ------ EXPERIMENTAL! NOT NEEDED
win.resizable(False, False)

tk.Label(text="Task focus",
         font=("UbuntuMono", 20), 
         bg="#282828", 
         fg="azure").pack()


focus_minute = tk.StringVar()
focus_second = tk.StringVar()

rest_minute = tk.StringVar()
rest_second = tk.StringVar()

focus_minute.set("25")
focus_second.set("00")

rest_minute.set("05")
rest_second.set("00")

center_frame = tk.Frame(win)
task_frame = tk.Frame(win)
center_frame.pack()
task_frame.pack()

focus_min_box = tk.Entry(
    center_frame,
    width=9,
    font=("monospace", 16),
    bg="#1c2023",
    fg="azure",
    bd=1,
    textvariable=focus_minute
    )

focus_sec_box = tk.Entry(
    center_frame,
    width=9,
    bg="#1c2023",
    fg="azure",
    font=("monospace", 16),
    textvariable=focus_second
    )

task_box = tk.Entry(
    task_frame,
    width=24,
    font=("monospace", 12),
        )
task_box.insert(0, "Insert tasks here...")

focus_min_box.pack(side=tk.LEFT)
focus_sec_box.pack(side=tk.LEFT)
task_box.pack()

task_listbox = tk.Listbox(
        win,
        bg="#282828",
        fg="azure",
        font=("monospace", 12),
        width=24,
        selectmode=tk.SINGLE
        )
task_listbox.pack() 
task_listbox.config(height=task_listbox.size())

task_button_frame = tk.Frame()
task_button_frame.pack()

add_button = tk.Button(task_button_frame, 
                       text="Add task",
                       bd=2,
                       relief=tk.RIDGE,
                       fg="white",
                       bg="#9a9a9a",
                       width=12,
                       command=add)

delete_button = tk.Button(task_button_frame,
                          text="Remove task",
                          fg="white",
                          bg="#9a9a9a",
                          bd=2,
                          relief=tk.RIDGE,
                          width=11,
                          command=delete)

add_button.pack(side=tk.LEFT)
delete_button.pack(side=tk.LEFT)

start_focus_button = tk.Button(win, 
                        text="Start focus",
                        font=("monospace", 15),
                        bd=3,
                        fg="white",
                        bg="#9a9a9a",
                        width=18,
                        command=focusTimer)
start_focus_button.pack()

rest_frame = tk.Frame()
rest_frame.config(bg="#232323")
rest_frame.pack()

rest_min_box = tk.Entry(
    rest_frame,
    width=9,
    font=("monosopace", 16),
    fg="azure",
    bg="#1c2023",
    textvariable=rest_minute
    )
rest_sec_box = tk.Entry(
    rest_frame,
    width=9,
    fg="azure",
    bg="#1c2023",
    font=("monospace", 16),
    textvariable=rest_second
    )
rest_label = tk.Label(rest_frame, text="Rest timer",
                      font=("monospace", 16),
                      bg="#232323",
                      fg="white")
rest_label.pack(pady=4)
rest_min_box.pack(side=tk.LEFT)
rest_sec_box.pack(side=tk.LEFT)

start_rest_button = tk.Button(win,
                              text="Start rest",
                              bd=5,
                              fg="white",
                              bg="#9a9a9a",
                              font=("monospace", 15),
                              width=18,
                              command=restTimer)
start_rest_button.pack()

menubar = tk.Menu(win)
win.configure(menu=menubar)
helpMenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=helpMenu)

def About():   # Please refer to helpmenu.py, HelpMenuCommands.  
    helpmenu.HelpMenuCommands(win, 
                              "./resources/icon/icon_lowres.png",
                              "./resources/text/about.txt",
                              "About PomodoroTk")

def whatIsPomodoro():
    helpmenu.HelpMenuCommands(win,
                              "./resources/icon/icon_lowres.png",
                              "./resources/text/whatispomodoro.txt",
                              "What is Pomodoro?")

def knownIssues():
    helpmenu.HelpMenuCommands(win,
                              "./resources/pics/paz.png",
                              "./resources/text/knownissues.txt",
                              "Known issues...")

helpMenu.add_command(label="What is Pomodoro?", command=whatIsPomodoro)
helpMenu.add_command(label="Known issues", command=knownIssues)
helpMenu.add_separator()
helpMenu.add_command(label="About", command=About)

#topper = tk.Toplevel(win)
#tk.Label(topper, text="test", font=("monospace", 60)).pack()

win.mainloop()
