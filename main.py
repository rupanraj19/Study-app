from tkinter import * # gui
from PIL import Image, ImageTk #pillow
from tkinter import ttk
from notifypy import Notify
from plyer import notification
import time

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



window = Tk() # instantiate window

# window canvas
window.geometry("600x600") # canvas size
window.title("Focus rah") # canvas title
center_window(window)

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

tab1 = Frame(tab_control) #tab1
tab2 = Frame(tab_control) #tab2
tab3 = Frame(tab_control) #tab3

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


window.resizable(0,0)
window.mainloop() # place window on computer screen, listen for events

