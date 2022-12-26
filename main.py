from tkinter import *
from tkinter import filedialog
from inout.io_operations import *
import PIL.Image
import PIL.ImageTk


def choose_path():
    global my_images
    path = filedialog.askdirectory(title='Choose Directory')
    init_images_csv()
    init_tags_csv()
    reload_images(path)
    my_images = read_images_csv(file='images_database.csv')
    load_images(my_images, 0)


def load_images(my_images, page):
    global canvas1
    global img1
    global btn1
    global canvas2
    global img2
    global btn2
    global canvas3
    global img3
    global btn3
    global canvas4
    global img4
    global btn4
    global current_page

    current_page = page

    if len(my_images) > current_page+3:
        img1 = PIL.Image.open(str(my_images[current_page].path))
        img1 = img1.resize((125, 125))
        img1 = PIL.ImageTk.PhotoImage(img1)
        canvas1.create_image(125, 125, image=img1)
        canvas1.grid(row=2, column=0)
        btn1.grid(row=3, column=0)

        img2 = PIL.Image.open(str(my_images[current_page+1].path))
        img2 = img2.resize((125, 125))
        img2 = PIL.ImageTk.PhotoImage(img2)
        canvas2.create_image(125, 125, image=img2)
        canvas2.grid(row=2, column=1)
        btn2.grid(row=3, column=1)

        img3 = PIL.Image.open(str(my_images[current_page+2].path))
        img3 = img3.resize((125, 125))
        img3 = PIL.ImageTk.PhotoImage(img3)
        canvas3.create_image(125, 125, image=img3)
        canvas3.grid(row=2, column=2)
        btn3.grid(row=3, column=2)

        img4 = PIL.Image.open(str(my_images[current_page+3].path))
        img4 = img4.resize((125, 125))
        img4 = PIL.ImageTk.PhotoImage(img4)
        canvas4.create_image(125, 125, image=img4)
        canvas4.grid(row=2, column=3)
        btn4.grid(row=3, column=3)
    else:
        current_page = page-1


def next_page():
    global current_page
    nextpage = current_page + 1
    if len(my_images) >= nextpage:
        load_images(my_images, nextpage)


def previous_page():
    global current_page
    prevpage = current_page - 1
    if prevpage >= 0:
        load_images(my_images, prevpage)


def preview():
    return


def open_img():
    return


root = Tk()

root.title("Image Viewer")
root.geometry("1024x600")
root.resizable(width=True, height=True)

querry = StringVar()

btnpath = Button(root, text="Choose Path", command=choose_path)
btnpath.grid(row=1, column=0)

searchhint = Label(root, text='Enter Tag:')
searchhint.grid(row=1, column=1)

searchbox = Entry(root, textvariable=querry)
searchbox.grid(row=1, column=2)

search = Button(root, text="Search Tag", command=open_img)
search.grid(row=1, column=3)

nextpg = Button(root, text="Next Photos", command=next_page)
nextpg.grid(row=4, column=3)

prev = Button(root, text="Prev Photos", command=previous_page)
prev.grid(row=4, column=0)

refresh = Button(root, text="Refresh", command=choose_path)
refresh.grid(row=5, column=1)

canvas1 = Canvas(root, width=250, height=250)
btn1 = Button(root, text="Select", command=preview())
canvas2 = Canvas(root, width=250, height=250)
btn2 = Button(root, text="Select", command=preview())
canvas3 = Canvas(root, width=250, height=250)
btn3 = Button(root, text="Select", command=preview())
canvas4 = Canvas(root, width=250, height=250)
btn4 = Button(root, text="Select", command=preview())

root.mainloop()
