from tkinter import *
from tkinter import filedialog, messagebox
from inout.io_operations import *
import PIL.Image
import PIL.ImageTk

my_images = []
current_page = 0
rs = []
path = None
previous_path = None


def choose_path():
    global my_images
    global path
    global previous_path
    path = filedialog.askdirectory(title='Choose Directory')
    if path == '':
        path = previous_path
    if os.path.exists(os.path.join(path, 'images_database.csv').replace("\\", "/")) and path != '':
        refresh_images(path)
        my_images = read_images_csv(file=os.path.join(path, 'images_database.csv').replace("\\", "/"))
        load_images(0)
        previous_path = path

    else:
        init_images_csv(file=os.path.join(path, 'images_database.csv').replace("\\", "/"))
        refresh_images(path)
        my_images = read_images_csv(file=os.path.join(path, 'images_database.csv').replace("\\", "/"))
        load_images(0)
        previous_path = path


def load_images(page):
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
    global rs

    current_page = page
    if rs != [] and query.get() != '':
        my_images = rs
    elif rs == [] and query.get() != '':
        messagebox.showerror('Search Error', 'Error: No search result found! \n Search query has been reset.')
        query.set('')
        my_images = read_images_csv(file=os.path.join(path, 'images_database.csv').replace("\\", "/"))
    elif (rs != [] and query.get() == '') or (rs == [] and query.get() == ''):
        # messagebox.showinfo("Load/Reload", "All images have been loaded/reloaded")
        my_images = read_images_csv(file=os.path.join(path, 'images_database.csv').replace("\\", "/"))
        rs = []
    else:
        my_images = read_images_csv(file=os.path.join(path, 'images_database.csv').replace("\\", "/"))

    if len(my_images) > current_page + 3:
        img1 = PIL.Image.open(str(my_images[current_page].path))
        img1 = img1.resize((125, 125))
        img1 = PIL.ImageTk.PhotoImage(img1)
        canvas1.create_image(125, 125, image=img1)
        canvas1.grid(row=2, column=0)
        btn1.grid(row=3, column=0)

        img2 = PIL.Image.open(str(my_images[current_page + 1].path))
        img2 = img2.resize((125, 125))
        img2 = PIL.ImageTk.PhotoImage(img2)
        canvas2.create_image(125, 125, image=img2)
        canvas2.grid(row=2, column=1)
        btn2.grid(row=3, column=1)

        img3 = PIL.Image.open(str(my_images[current_page + 2].path))
        img3 = img3.resize((125, 125))
        img3 = PIL.ImageTk.PhotoImage(img3)
        canvas3.create_image(125, 125, image=img3)
        canvas3.grid(row=2, column=2)
        btn3.grid(row=3, column=2)

        img4 = PIL.Image.open(str(my_images[current_page + 3].path))
        img4 = img4.resize((125, 125))
        img4 = PIL.ImageTk.PhotoImage(img4)
        canvas4.create_image(125, 125, image=img4)
        canvas4.grid(row=2, column=3)
        btn4.grid(row=3, column=3)
    elif len(my_images) > current_page + 2:
        img1 = PIL.Image.open(str(my_images[current_page].path))
        img1 = img1.resize((125, 125))
        img1 = PIL.ImageTk.PhotoImage(img1)
        canvas1.create_image(125, 125, image=img1)
        canvas1.grid(row=2, column=0)
        btn1.grid(row=3, column=0)

        img2 = PIL.Image.open(str(my_images[current_page + 1].path))
        img2 = img2.resize((125, 125))
        img2 = PIL.ImageTk.PhotoImage(img2)
        canvas2.create_image(125, 125, image=img2)
        canvas2.grid(row=2, column=1)
        btn2.grid(row=3, column=1)

        img3 = PIL.Image.open(str(my_images[current_page + 2].path))
        img3 = img3.resize((125, 125))
        img3 = PIL.ImageTk.PhotoImage(img3)
        canvas3.create_image(125, 125, image=img3)
        canvas3.grid(row=2, column=2)
        btn3.grid(row=3, column=2)

        canvas4.grid_remove()
        btn4.grid_remove()
    elif len(my_images) > current_page + 1:
        img1 = PIL.Image.open(str(my_images[current_page].path))
        img1 = img1.resize((125, 125))
        img1 = PIL.ImageTk.PhotoImage(img1)
        canvas1.create_image(125, 125, image=img1)
        canvas1.grid(row=2, column=0)
        btn1.grid(row=3, column=0)

        img2 = PIL.Image.open(str(my_images[current_page + 1].path))
        img2 = img2.resize((125, 125))
        img2 = PIL.ImageTk.PhotoImage(img2)
        canvas2.create_image(125, 125, image=img2)
        canvas2.grid(row=2, column=1)
        btn2.grid(row=3, column=1)

        canvas3.grid_remove()
        btn3.grid_remove()
        canvas4.grid_remove()
        btn4.grid_remove()
    elif len(my_images) > current_page:
        img1 = PIL.Image.open(str(my_images[current_page].path))
        img1 = img1.resize((125, 125))
        img1 = PIL.ImageTk.PhotoImage(img1)
        canvas1.create_image(125, 125, image=img1)
        canvas1.grid(row=2, column=0)
        btn1.grid(row=3, column=0)

        canvas2.grid_remove()
        btn2.grid_remove()
        canvas3.grid_remove()
        btn3.grid_remove()
        canvas4.grid_remove()
        btn4.grid_remove()
    else:
        current_page = page - 1


def next_page():
    global current_page
    nextpage = current_page + 1
    if len(my_images) >= nextpage:
        load_images(nextpage)


def previous_page():
    global current_page
    prevpage = current_page - 1
    if prevpage >= 0:
        load_images(prevpage)


def preview():
    # TODO: Link to Andreea's window for viewing image info and adding/deleting tags
    return


def search_img():
    global rs
    if (keep.get() == 0) or (keep.get() == 1 and rs == []):
        tagshistoryvariable.set(query.get())
        newrs = []
        for i in my_images:
            for j in i.tags:
                if j == query.get():
                    newrs.append(i)
        rs = newrs

    elif keep.get() == 1 and rs != []:
        tagshistoryvariable.set(tagshistoryvariable.get() + ', ' + query.get())
        newrs = []
        for i in rs:
            for j in i.tags:
                if j == query.get():
                    newrs.append(i)
        rs = newrs
    load_images(0)


root = Tk()

root.title("Image Viewer By Tags")
root.geometry("1180x560")
root.resizable(width=True, height=True)

query = StringVar()
keep = IntVar()
tagshistoryvariable = StringVar()

btnpath = Button(root, text="Choose Path of Photos folder", command=choose_path)
btnpath.grid(row=1, column=0)

searchhint = Label(root, text='Enter Tag of Photos you want to see:')
searchhint.grid(row=1, column=1)

searchbox = Entry(root, textvariable=query, width=40)
searchbox.grid(row=1, column=2)

search = Button(root, text="Search Tag", command=search_img)
search.grid(row=1, column=4)

nextpg = Button(root, text="Next Photo", command=next_page)
nextpg.grid(row=4, column=3)

prev = Button(root, text="Previous Photo", command=previous_page)
prev.grid(row=4, column=0)

refresh = Button(root, text="Refresh image list", command=refresh_images(path))
refresh.grid(row=5, column=1)

tagshistorylabel = Label(root, text="List of last searched Tags:")
tagshistorylabel.grid(row=5, column=2)

tagshistorylist = Label(root, textvariable=tagshistoryvariable)
tagshistorylist.grid(row=5, column=3)

keepsearch = Checkbutton(root, text="Do you want to keep previous search results? ", variable=keep)
keepsearch.grid(row=1, column=3)

canvas1 = Canvas(root, width=250, height=250)
btn1 = Button(root, text="Select Photo", command=preview())
canvas2 = Canvas(root, width=250, height=250)
btn2 = Button(root, text="Select Photo", command=preview())
canvas3 = Canvas(root, width=250, height=250)
btn3 = Button(root, text="Select Photo", command=preview())
canvas4 = Canvas(root, width=250, height=250)
btn4 = Button(root, text="Select Photo", command=preview())


def open_window():
    root.mainloop()
    # Big question: Este necesara si o bifa pentru a face reuniunea tagurilor cautate? Bifa actuala va face intersectia
    # Asta se traduce practic in afisarea tuturor pozelor care au oricare din tagurile x, y, z cautate
