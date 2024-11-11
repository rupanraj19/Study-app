from tkinter import * # gui
from PIL import Image, ImageTk #pillow
from tkinter import ttk
from tkinter import filedialog # for file
from tkinter import messagebox
from notifypy import Notify  # for notification
from plyer import notification
import time # for time
import pygame # for audio
import os

song_path = None
tasks = []
def add_task():
    gettask = addtask.get() # get from the add task entry box
    if gettask:
        tasks.append(gettask)
        update_task()
        addtask.delete(0, END) # clear the entry box after adding task
    else:
        popupmsg("Please enter a task")
    print(tasks)

def update_task():
    listbox.delete(0, END)
    listbox2.delete(0, END)
    for task in tasks: # using enumerate to add number infront of the task
        listbox.insert(END, task)
        listbox2.insert(END, task)


def delete_task():
    selecttask = listbox.curselection() #cursor selection

    if selecttask:
        tasks.pop(selecttask[0])
        update_task()
    else:
        popupmsg("Please select task to delete")

def complete_task():
    selecttask = listbox.curselection()
    if selecttask:
        tasks.pop(selecttask[0])
        completemsg = f"{listbox.get(selecttask[0])} was completed"
        tasks.append(completemsg)
        update_task()
    else:
        popupmsg("Please select task to complete")

def popupmsg(msg):
    popup = Tk()
    popup.eval("tk::PlaceWindow . center")
    popup.title("oii")
    label = Label(popup, text=msg, font=('poppins'))
    label.pack(fill="x", pady=10)
    B1 = Button(popup, text='ok', command=popup.destroy, background="red")
    B1.pack()
    popup.mainloop()


def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")


def get_details():
    selecttask = listbox2.curselection()
    if selecttask:
        get_title = listbox2.get(selecttask[0])
        print(get_title)
    get_msg = msg.get()
    get_time = mins.get()

    if get_title !="" or get_msg != "" or get_time != "":
        int_time = int(get_time)
        min_to_sec = int_time * 60
        time.sleep(min_to_sec)

        notification.notify(title=get_title,
                            message=get_msg,
                            app_name="Focus rah",
                            app_icon=None,
                            timeout=5)

def set_time():
    try:
        temp = int(hour.get()) * 3600 + int(minute.get()) * 60 + int(second.get())
    except:
        print("Enter correct time")

    while temp > -1:
        mins,secs = divmod(temp,60) # divmod(firstvalue = temp//60, secondvalue - temp%60)

        # convert input in mins or secs to hours

        hours = 0
        if mins > 60:
            hours, mins = divmod(mins, 60)

        hour.set("{0:2d}".format(hours))
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))

        window.update()
        time.sleep(1)

        # message box when temp value = 0

        if (temp == 0):
            messagebox.showinfo("Time Countdown", "Time over take 5 min break")

        temp -= 1



pygame.mixer.init()

def upload_song():
    global song_path
    song_path = filedialog.askopenfilename(
        title="select a song",
        filetypes=[("mp3 files", "*.mp3"), ("wav files", "*.wav")]
    )

    if song_path:
        file_name = os.path.basename(song_path)
        # file_name = song_path.split("/")[-1]
        songLabel.config(text="Song: " + file_name)





def play_song():
    if song_path:
        pygame.mixer.music.load(song_path)
        pygame.mixer.music.play(loops=0)
    else:
        pygame.mixer.music.load("song/lofirain.mp3")
        pygame.mixer.music.play(loops=0)

def stop_song():
    pygame.mixer.music.stop()




window = Tk() # instantiate window

# window canvas
window.geometry("600x600") # canvas size
window.title("Focus rah") # canvas title
window.configure(background="black")
center_window(window)

# Create an instance of ttk style
s = ttk.Style()
s.theme_use('default')
s.configure('TNotebook', background="black")
s.map("TNotebook.Tab", background=[('selected', 'red')])

# icon and bg

#logo
icon = PhotoImage(file="images/logo.png") # icon path tkinter
window.iconphoto(True, icon) # display icon
window.config(background="black")

# icon
image = Image.open("images/logo.png") # image using pil
resize_img = image.resize((64,64)) # resize img
img = ImageTk.PhotoImage(resize_img) # got to convert into TkImage

# label
label = Label(window, text="Study app", font=("poppins", 20, 'bold'), fg="white", bg="black",relief=RAISED, pady=10, image =img, compound = 'left')
# label.place(x= 250, y = 20)
label.pack() # pack to display it in center


#add tabs in window
tab_control = ttk.Notebook(window) # widget that manages a collection of window/displays

tab1 = Frame(tab_control, bg='black') #tab1
tab2 = Frame(tab_control, bg='black') #tab2
tab3 = Frame(tab_control, bg='black') #tab3

tab_control.add(tab1, text='To Do List')
tab_control.add(tab2, text='Remainder' )
tab_control.add(tab3, text='pomodore')
tab_control.pack(expand=1, fill='both')

# either use grid or pack or place. dont mix them in same tab
#tab1 stuff
addtask = Entry(tab1, width=50) # entry box
addtask.grid(row=0, column=0, padx = 10)

addtaskbtn = Button(tab1,
                    text="Add Task",
                    command=add_task,
                    font=("poppins", 10, 'bold'),
                    bg="green",
                    activebackground="red",
                    ).grid(row=0, column=1, padx = 10 )

# list box to display the tasks

listbox = Listbox(tab1, width=50)
listbox.grid(row=3, column=0, columnspan=2, pady=20)

# delete task

detelebtn = Button(tab1,
                   text="Delete Task",
                   font=("poppins", 10, 'bold'),
                   command= delete_task,
                   bg="red",
                   activebackground="yellow",
                   ).grid(row= 10, column=0)

# complete task

completebtn = Button(tab1,
                   text="complete Task",
                   font=("poppins", 10, 'bold'),
                   command= complete_task,
                   bg="yellow",
                   activebackground="white",
                   ).grid(row= 10, column=2)

#--------------------------------------------------------------------------------#

# tab2 notification
choosetask = Label(tab2, text="Choose a task", font=("poppins", 10, 'bold'))
choosetask.place(x = 50, y = 10)

# list box to display the tasks
listbox2 = Listbox(tab2, width=50)
listbox2.place(x = 100, y = 30) # Use grid for the listbox

# set remainder

# msg label and entry box
msgLabel = Label(tab2, text="Enter message", font=("poppins", 10, 'bold'))
msgLabel.place(x = 50, y = 220)
msg = Entry(tab2, width=50, font=("poppins", 10, 'bold'))
msg.place(x = 50, y = 240)

# time label and entry box
timeLabel = Label(tab2, text="Enter time in minutes", font=("poppins", 10, 'bold'))
timeLabel.place(x = 50, y = 280)
mins= Entry(tab2, width=10, font=("poppins", 10, 'bold'))
mins.place(x = 50, y = 300)

# set button
setbtn = Button(tab2,
                text="Set Remainder",
                font=("poppins", 10, 'bold'),
                command= get_details,
                bg="green",
                activebackground="red",
                ).place(x = 50, y = 350)

#-------------------------------------------------------------

#tab 3

# music stuff
musicLabel = Label(tab3,
                   text="Sound",
                   font=("poppins", 20, 'bold'),
                   )
musicLabel.place(x = 250, y = 230)

musicbtn = Button(tab3,
                  text="play",
                  font=("poppins", 10, 'bold'),
                  command= play_song,
                  bg="green",
                  activebackground="lightgreen",
                  )
musicbtn.place(x = 250, y = 280)


stopbtn = Button(tab3,
                  text="stop",
                  font=("poppins", 10, 'bold'),
                  command= stop_song,
                  bg="red",
                  activebackground="yellow",
                  )
stopbtn.place(x = 300, y = 280)

uploadBtn = Button(tab3,
                   text="upload a song",
                   command= upload_song,
                   font=("poppins", 9, 'bold'),
                   bg="pink")
uploadBtn.place(x = 250, y = 330)

songLabel = Label(tab3,
                  text="Song: Lofi " ,
                  font=("poppins", 10, 'bold'),
                )
songLabel.place(x = 250, y = 380)

# variables for time
hour = StringVar()
minute = StringVar()
second = StringVar()

# default values for time

hour.set("00")
minute.set("25")
second.set("00")

# entry for time

hourEntry = Entry(tab3, textvariable=hour, width=3, font=("poppins", 10, 'bold'))
hourEntry.place(x = 230, y = 120)

minutesEntry = Entry(tab3, textvariable=minute, width=3, font=("poppins", 10, 'bold'))
minutesEntry.place(x = 280, y = 120)

secondsEntry = Entry(tab3, textvariable=second, width=3, font=("poppins", 10, 'bold'))
secondsEntry.place(x = 330, y = 120)

#  label for time
timerLabel = Label(tab3, text="Timer", font=("poppins", 20, 'bold'))
timerLabel.place(x =250, y = 50)

hourLabel = Label(tab3, text="Hour", font=("poppins", 10, 'bold'))
hourLabel.place(x = 230, y = 100)

minutesLabel = Label(tab3, text="Mins", font=("poppins", 10, 'bold'))
minutesLabel.place(x = 280, y = 100)

secondsLabel = Label(tab3, text="Secs", font=("poppins", 10, 'bold'))
secondsLabel.place(x = 330, y = 100)

# btn for time

setTimeBtn = Button(tab3, text="Set Time", width=10, font=("poppins", 10, 'bold'), command= set_time, bg="cyan")
setTimeBtn.place(x = 245, y = 150)



window.resizable(0,0)
window.mainloop() # place window on computer screen, listen for events

