from tkinter import *
import numpy as np
import os
from PIL import ImageTk, Image
from tkinter import filedialog


def reload_images(path):  # in case we find a way to refresh the list of photos in case the user deletes one
    files = os.listdir(path)  # Detect in some way if changes appeared to current path
    for i in files:
        if i[-4:] != ".jpg":
            files.remove(i)

    files_path = list()
    for i in files:
        files_path.append(os.path.join(os.sep, path, i))

    np.save(os.path.join(path, 'myfiles.npy'), np.array(files_path))


def choose_path():
    path = filedialog.askdirectory(title='Choose Directory')
    reload_images(path)
    my_files = np.load(os.path.join(os.sep, path, 'myfiles.npy'))
    load_images(my_files, 0)


def load_images(my_files, page):
    global canvas1
    global btn1
    global canvas2
    global btn2
    global canvas3
    global btn3
    global canvas4
    global btn4

    filepath = my_files[page]
    print(filepath)
    img1 = Image.open(filepath)
    img1 = img1.resize((125, 125))
    img1 = ImageTk.PhotoImage(img1)
    canvas1.create_image(125, 125, image=img1)
    canvas1.grid(row=2, column=0)
    btn1.grid(row=3, column=0)

    filepath = my_files[page+1]
    img2 = Image.open(filepath)
    img2 = img2.resize((125, 125))
    img2 = ImageTk.PhotoImage(img2)
    canvas2.create_image(125, 125, image=img2)
    canvas2.grid(row=2, column=1)
    btn2.grid(row=3, column=1)

    filepath = my_files[page+2]
    img3 = Image.open(filepath)
    img3 = img3.resize((125, 125))
    img3 = ImageTk.PhotoImage(img3)
    canvas3.create_image(125, 125, image=img3)
    canvas3.grid(row=2, column=2)
    btn3.grid(row=3, column=2)

    filepath = my_files[page+3]
    img4 = Image.open(filepath)
    img4 = img4.resize((125, 125))
    img4 = ImageTk.PhotoImage(img4)
    canvas4.create_image(125, 125, image=img4)
    canvas4.grid(row=2, column=3)
    btn4.grid(row=3, column=3)


def preview():
    return


def open_img():
    return


root = Tk()

root.title("Image Viewer")
root.geometry("1024x600")
root.resizable(width=True, height=True)

mesaj = StringVar()

btnpath = Button(root, text="Choose Path", command=choose_path)
btnpath.grid(row=1, column=0)

w1 = Label(root, text='Enter Tag:')
w1.grid(row=1, column=1)

tagbox = Entry(root, textvariable=mesaj)
tagbox.grid(row=1, column=2)

search = Button(root, text="Search Tag", command=open_img)
search.grid(row=1, column=3)

refresh = Button(root, text="Refresh", command=choose_path)
refresh.grid(row=4, column=0)

canvas1 = Canvas(root, width=250, height=250)
btn1 = Button(root, text="Select", command=preview())
canvas2 = Canvas(root, width=250, height=250)
btn2 = Button(root, text="Select", command=preview())
canvas3 = Canvas(root, width=250, height=250)
btn3 = Button(root, text="Select", command=preview())
canvas4 = Canvas(root, width=250, height=250)
btn4 = Button(root, text="Select", command=preview())


root.mainloop()
