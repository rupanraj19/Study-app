from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk

def to_do_list():
    print("To Do List")

window = Tk() # instantiate window

# window canvas
window.geometry("600x600") # canvas size
window.title("Focus rah") # canvas title

# icon and bg
icon = PhotoImage(file="images/logo.png") # icon path tkinter
image = Image.open("images/logo.png") # image using pil
resize_img = image.resize((64,64)) # resize img
img = ImageTk.PhotoImage(resize_img) # got to convert into TkImage
window.iconphoto(True, icon) # display icon
window.config(background="black")


# label
label = Label(window, text="Study app", font=("poppins", 20, 'bold'), fg="white", bg="black",relief=RAISED, pady=10, image =img, compound = 'left')
# label.place(x= 250, y = 20)
label.pack() # pack to display it in center

#add tabs in window
tab_control = ttk.Notebook(window) # widget that manages a collection of window/displays

tab1 = Frame(tab_control) #tab1
tab2 = Frame(tab_control) #tab2

tab_control.add(tab1, text='To Do List')
tab_control.add(tab2, text='Remainder')
tab_control.pack(expand=1, fill='both')

ttk.Button(tab1, text="To Do List", command=to_do_list).pack()


window.mainloop() # place window on computer screen, listen for events
