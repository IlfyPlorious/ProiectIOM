from tkinter import *
import numpy as np
import os
from PIL import ImageTk, Image
from tkinter import filedialog

def reload_images(path):
    files = os.listdir(path)
    for i in files:
        if i[-4:] != ".jpg":
            files.remove(i)

    files_path = list()
    for i in files:
        files_path.append(os.path.join(path, i))

    np.save('myfiles.npy', np.array(files_path))
    # my_files = np.load('myfiles.npy')

def choose_path():
    path = filedialog.askdirectory(title='Choose Directory')
    reload_images(path)

def open_img():
    global img
    global img1
    global canvas1
    x = openfilename()

    img = Image.open(x)

    img1 = img.resize((125, 125))
    img1 = ImageTk.PhotoImage(img1)

    canvas1.create_image(125, 125, image=img1)
    canvas1.grid(row=2, column=0)


root = Tk()

root.title("Image Viewer")
root.geometry("500x300+300+125")
root.resizable(width=True, height=True)

mesaj = StringVar()
w1 = Label(root, text='Enter Tag:')
w1.grid(row=1, column=2, columnspan=2)

tagbox = Entry(root, textvariable=mesaj)
tagbox.grid(row=1, column=5, columnspan=3)

btnpath = Button(root, text="Choose Path", command=choose_path)
btnpath.grid(row=1, column=0, columnspan=2)

refresh = Button(root, text="Refresh", command=choose_path)
refresh.grid(row=2, column=0, columnspan=2)

search = Button(root, text="Search Tag", command=open_img)
search.grid(row=1, column=9, columnspan=2)

canvas1 = Canvas(root, width=250, height=250)
canvas2 = Canvas(root, width=250, height=250)
canvas3 = Canvas(root, width=250, height=250)
canvas4 = Canvas(root, width=250, height=250)

root.mainloop()
