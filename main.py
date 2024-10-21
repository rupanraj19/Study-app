from tkinter import * # gui
from PIL import Image, ImageTk #pillow
from tkinter import ttk

tasks = []
def add_task():
    gettask = addtask.get() # get from the add task entry box
    if gettask:
        tasks.append(gettask)
        update_task()
        addtask.delete(0, END) # clear the entry box after adding task
    else:
        print("Please enter a task")
    print(tasks)

def update_task():
    listbox.delete(0, END)
    for task in enumerate(tasks, start=1): # using enumerate to add number infront of the task
        listbox.insert(END, task)


def delete_task():
    selecttask = listbox.curselection() #cursor selection

    if selecttask:
        tasks.pop(selecttask[0])
        update_task()
    else:
        print("Please select task to delete")

def complete_task():
    selecttask = listbox.curselection()
    if selecttask:
        tasks.pop(selecttask[0])
        completemsg = f"{listbox.get(selecttask[0])} was completed"
        tasks.append(completemsg)
        update_task()
    else:
        print("Please select task to complete")

window = Tk() # instantiate window

# window canvas
window.geometry("600x600") # canvas size
window.title("Focus rah") # canvas title

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
tab_control.add(tab2, text='Remainder')
tab_control.add(tab3, text='pomodore')
tab_control.pack(expand=1, fill='both')

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


window.mainloop() # place window on computer screen, listen for events

