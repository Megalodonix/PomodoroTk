import tkinter as tk
import helpmenu
import toplevel_win 
from tkinter import messagebox, ttk
from ttkthemes import ThemedTk


def handle_focus_in(_):
    task_box.delete(0, tk.END)
    task_box.config()


def add(*args):
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

    if(usrinpt == 0):
        toplevel_win.TimeUp(win, "Focus time is over!\nYou may take a break now!")
        removeTopTask()
        focus_minute.set("25")
        focus_second.set("00")
        return
        
    usrinpt -= 1
    mins, secs = divmod(usrinpt,60)
    focus_minute.set("{0:2d}".format(mins))
    focus_second.set("{0:2d}".format(secs))
    win.after(1000, focusTimer)
    win.update()


def restTimer():
    try:
        usrinpt = int(rest_minute.get())*60 + int(rest_second.get())
    except Exception:
        messagebox.showwarning(title="Error!", message="Invalid input.")

    if(usrinpt == 0):
        toplevel_win.TimeUp(win, "Break time is over!\nYou may do another task.")
        removeTopTask()
        rest_minute.set("05")
        rest_second.set("00")
        return
        
    usrinpt -= 1
    mins, secs = divmod(usrinpt,60)
    rest_minute.set("{0:2d}".format(mins))
    rest_second.set("{0:2d}".format(secs))
    win.after(1000, restTimer)
    win.update()


win = ThemedTk(theme="yaru")

icon = tk.PhotoImage(file="./resources/icon/pomodorotk.png")
win.iconphoto(True, icon)
win.title("PomodoroTk")
# win.geometry("600x300") ------ EXPERIMENTAL! NOT NEEDED

notebook = ttk.Notebook(win)
focus_tab = ttk.Frame(notebook)
rest_tab = ttk.Frame(notebook)
notebook.add(focus_tab, text="Focus")
notebook.add(rest_tab, text="Rest")
notebook.pack(expand=True, fill="both")

win.resizable(False, False)

focus_minute = tk.StringVar()
focus_second = tk.StringVar()

rest_minute = tk.StringVar()
rest_second = tk.StringVar()

focus_minute.set("25")
focus_second.set("00")

rest_minute.set("05")
rest_second.set("00")

center_frame = ttk.Frame(focus_tab)
task_frame = ttk.Frame(focus_tab)
center_frame.pack()
task_frame.pack()

focus_min_box = ttk.Entry(
    center_frame,
    width=9,
    font=("", 16),
    textvariable=focus_minute
    )

focus_sec_box = ttk.Entry(
    center_frame,
    width=9,
    font=("", 16),
    textvariable=focus_second
    )

task_box = ttk.Entry(
    task_frame,
    width=26,
    font=("", 12),
        )

focus_min_box.pack(side=tk.LEFT)
focus_sec_box.pack(side=tk.LEFT)
task_box.pack()

task_box.insert(0, "Insert tasks here...")
task_box.bind("<FocusIn>", handle_focus_in)
task_box.bind("<Return>", add)

task_listbox = tk.Listbox(
        focus_tab,
        font=("", 12),
        width=27,
        selectmode=tk.SINGLE
        )
task_listbox.pack() 
task_listbox.config(height=task_listbox.size())

task_button_frame = ttk.Frame(task_frame)
task_button_frame.pack()

add_button = ttk.Button(task_button_frame, 
                       text="Add task",
                       width=14,
                       command=add)

delete_button = ttk.Button(task_button_frame,
                          text="Remove task",
                          width=14,
                          command=delete)

add_button.pack(side=tk.LEFT)
delete_button.pack(side=tk.LEFT)

start_focus_button = ttk.Button(focus_tab, 
                        text="Start focus",
                        width=31,
                        command=focusTimer)
start_focus_button.pack()

rest_frame = ttk.Frame(rest_tab)
rest_frame.pack()

rest_min_box = ttk.Entry(
    rest_frame,
    width=9,
    font=("monosopace", 16),
    textvariable=rest_minute
    )
rest_sec_box = ttk.Entry(
    rest_frame,
    width=9,
    font=("", 16),
    textvariable=rest_second
    )
rest_label = ttk.Label(rest_frame, text="Rest timer",
                      font=("", 16),
                      )
rest_label.pack(pady=4)
rest_min_box.pack(side=tk.LEFT)
rest_sec_box.pack(side=tk.LEFT)

start_rest_button = ttk.Button(rest_tab,
                              text="Start rest",
                              width=31,
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

helpMenu.add_command(label="What is Pomodoro?", command=whatIsPomodoro)
helpMenu.add_separator()
helpMenu.add_command(label="About", command=About)

#topper = tk.Toplevel(win)
#tk.Label(topper, text="test", font=("", 60)).pack()

win.mainloop()
