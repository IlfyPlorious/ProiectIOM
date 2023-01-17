import tkinter
from tkinter import *
from tkinter import filedialog, messagebox
from tkinter import ttk

import windows.details_window
from inout.io_operations import *
import PIL.Image
import PIL.ImageTk


class MainWindow(tkinter.Tk):
    def __init__(self):
        super().__init__()

        self.title("Image Viewer By Tags")
        self.geometry("1280x560")
        self.resizable(width=True, height=True)

        self.my_images = []
        self.current_page = 0
        self.rs = []
        self.path = None
        self.previous_path = None

        self.rs = []
        self.current_page = 0
        self.query = StringVar()
        self.keep = IntVar()
        self.tagshistoryvariable = StringVar()

        self.btnpath = ttk.Button(self, text="Choose Path of Photos folder", command=self.choose_path)
        self.btnpath.grid(row=1, column=0)

        self.searchhint = ttk.Label(self, text='Enter Tag of Photos you want to see:')
        self.searchhint.grid(row=1, column=1)

        self.searchbox = ttk.Entry(self, textvariable=self.query, width=40)
        self.searchbox.grid(row=1, column=2)

        self.search = ttk.Button(self, text="Search Tag", command=self.search_img)
        self.search.grid(row=1, column=4)

        self.nextpg = ttk.Button(self, text="Next Photo", command=self.next_page)
        self.nextpg.grid(row=4, column=3)

        self.prev = ttk.Button(self, text="Previous Photo", command=self.previous_page)
        self.prev.grid(row=4, column=0)

        self.refresh = ttk.Button(self, text="Refresh image list", command=self.refresh_images(self.path))
        self.refresh.grid(row=5, column=1)

        self.tagshistorylabel = ttk.Label(self, text="List of last searched Tags:")
        self.tagshistorylabel.grid(row=5, column=2)

        self.tagshistorylist = ttk.Label(self, textvariable=self.tagshistoryvariable)
        self.tagshistorylist.grid(row=5, column=3)

        self.keepsearch = ttk.Checkbutton(self, text="Do you want to keep previous search results? ",
                                          variable=self.keep)
        self.keepsearch.grid(row=1, column=3)

        self.canvas1 = Canvas(self, width=250, height=250)
        self.btn1 = Button(self, text="Select Photo", command=lambda: self.preview(0))
        self.canvas2 = Canvas(self, width=250, height=250)
        self.btn2 = Button(self, text="Select Photo", command=lambda: self.preview(1))
        self.canvas3 = Canvas(self, width=250, height=250)
        self.btn3 = Button(self, text="Select Photo", command=lambda: self.preview(2))
        self.canvas4 = Canvas(self, width=250, height=250)
        self.btn4 = Button(self, text="Select Photo", command=lambda: self.preview(3))

        self.img1 = None
        self.img2 = None
        self.img3 = None
        self.img4 = None

    def choose_path(self):
        self.path = filedialog.askdirectory(title='Choose Directory')
        if self.path == '':
            self.path = self.previous_path
        if os.path.exists(os.path.join(self.path, 'images_database.csv').replace("\\", "/")) and self.path != '':
            self.refresh_images(self.path)
            self.my_images = read_images_csv(file=os.path.join(self.path, 'images_database.csv').replace("\\", "/"))
            self.load_images(0)
            self.previous_path = self.path

        else:
            init_images_csv(file=os.path.join(self.path, 'images_database.csv').replace("\\", "/"))
            self.refresh_images(self.path)
            self.my_images = read_images_csv(file=os.path.join(self.path, 'images_database.csv').replace("\\", "/"))
            self.load_images(0)
            self.previous_path = self.path

    def load_images(self, page):
        self.current_page = page
        if self.rs != [] and self.query.get() != '':
            self.my_images = self.rs
        elif self.rs == [] and self.query.get() != '':
            messagebox.showerror('Search Error', 'Error: No search result found! \n Search query has been reset.')
            self.query.set('')
            self.my_images = read_images_csv(file=os.path.join(self.path, 'images_database.csv').replace("\\", "/"))
        elif (self.rs != [] and self.query.get() == '') or (self.rs == [] and self.query.get() == ''):
            # messagebox.showinfo("Load/Reload", "All images have been loaded/reloaded")
            self.my_images = read_images_csv(file=os.path.join(self.path, 'images_database.csv').replace("\\", "/"))
            self.rs = []
        else:
            self.my_images = read_images_csv(file=os.path.join(self.path, 'images_database.csv').replace("\\", "/"))

        if len(self.my_images) > self.current_page + 3:
            img1 = PIL.Image.open(str(self.my_images[self.current_page].path))
            img1 = img1.resize((125, 125))
            self.canvas1.grid(row=2, column=0)
            self.btn1.grid(row=3, column=0)
            self.img1 = PIL.ImageTk.PhotoImage(img1)
            self.canvas1.create_image(125, 125, image=self.img1)

            img2 = PIL.Image.open(str(self.my_images[self.current_page + 1].path))
            img2 = img2.resize((125, 125))
            self.img2 = PIL.ImageTk.PhotoImage(img2)
            self.canvas2.create_image(125, 125, image=self.img2)
            self.canvas2.grid(row=2, column=1)
            self.btn2.grid(row=3, column=1)

            img3 = PIL.Image.open(str(self.my_images[self.current_page + 2].path))
            img3 = img3.resize((125, 125))
            self.img3 = PIL.ImageTk.PhotoImage(img3)
            self.canvas3.create_image(125, 125, image=self.img3)
            self.canvas3.grid(row=2, column=2)
            self.btn3.grid(row=3, column=2)

            img4 = PIL.Image.open(str(self.my_images[self.current_page + 3].path))
            img4 = img4.resize((125, 125))
            self.img4 = PIL.ImageTk.PhotoImage(img4)
            self.canvas4.create_image(125, 125, image=self.img4)
            self.canvas4.grid(row=2, column=3)
            self.btn4.grid(row=3, column=3)
        elif len(self.my_images) > self.current_page + 2:
            img1 = PIL.Image.open(str(self.my_images[self.current_page].path))
            img1 = img1.resize((125, 125))
            self.img1 = PIL.ImageTk.PhotoImage(img1)
            self.canvas1.create_image(125, 125, image=self.img1)
            self.canvas1.grid(row=2, column=0)
            self.btn1.grid(row=3, column=0)

            img2 = PIL.Image.open(str(self.my_images[self.current_page + 1].path))
            img2 = img2.resize((125, 125))
            self.img2 = PIL.ImageTk.PhotoImage(img2)
            self.canvas2.create_image(125, 125, image=self.img2)
            self.canvas2.grid(row=2, column=1)
            self.btn2.grid(row=3, column=1)

            img3 = PIL.Image.open(str(self.my_images[self.current_page + 2].path))
            img3 = img3.resize((125, 125))
            self.img3 = PIL.ImageTk.PhotoImage(img3)
            self.canvas3.create_image(125, 125, image=self.img3)
            self.canvas3.grid(row=2, column=2)
            self.btn3.grid(row=3, column=2)

            self.canvas4.grid_remove()
            self.btn4.grid_remove()
        elif len(self.my_images) > self.current_page + 1:
            img1 = PIL.Image.open(str(self.my_images[self.current_page].path))
            img1 = img1.resize((125, 125))
            self.img1 = PIL.ImageTk.PhotoImage(img1)
            self.canvas1.create_image(125, 125, image=self.img1)
            self.canvas1.grid(row=2, column=0)
            self.btn1.grid(row=3, column=0)

            img2 = PIL.Image.open(str(self.my_images[self.current_page + 1].path))
            img2 = img2.resize((125, 125))
            self.img2 = PIL.ImageTk.PhotoImage(img2)
            self.canvas2.create_image(125, 125, image=self.img2)
            self.canvas2.grid(row=2, column=1)
            self.btn2.grid(row=3, column=1)

            self.canvas3.grid_remove()
            self.btn3.grid_remove()
            self.canvas4.grid_remove()
            self.btn4.grid_remove()
        elif len(self.my_images) > self.current_page:
            img1 = PIL.Image.open(str(self.my_images[self.current_page].path))
            img1 = img1.resize((125, 125))
            self.img1 = PIL.ImageTk.PhotoImage(img1)
            self.canvas1.create_image(125, 125, image=self.img1)
            self.canvas1.grid(row=2, column=0)
            self.btn1.grid(row=3, column=0)

            self.canvas2.grid_remove()
            self.btn2.grid_remove()
            self.canvas3.grid_remove()
            self.btn3.grid_remove()
            self.canvas4.grid_remove()
            self.btn4.grid_remove()
        else:
            self.current_page = page - 1

    def next_page(self):
        nextpage = self.current_page + 1
        if len(self.my_images) >= nextpage:
            self.load_images(nextpage)

    def previous_page(self):
        prevpage = self.current_page - 1
        if prevpage >= 0:
            self.load_images(prevpage)

    def preview(self, button):
        details_window = windows.details_window.DetailsWindow(self, self.my_images[self.current_page + button],
                                                              self.path)
        details_window.grab_set()

    def refresh_images(self,
                       path):  # in case we find a way to refresh the list of photos in case the user adds/deletes one
        if path is not None:
            files = os.listdir(path)  # Detect in some way if changes appeared to current path
            self.my_images = read_images_csv(file=os.path.join(path, 'images_database.csv').replace("\\", "/"))
            for i in files:
                if i[-4:] != ".jpg":
                    files.remove(i)

            my_images_paths = {}
            for image in self.my_images:
                my_images_paths[image.path] = image.image_id

            file_paths = []

            for file in files:
                image_path = os.path.join(path, file).replace("\\", "/")

                if image_path not in my_images_paths.keys():
                    img = Image(image_id=uuid.uuid4(), path=image_path, name=image_path.split("/")[-1])
                    write_image_csv(file=os.path.join(path, 'images_database.csv').replace("\\", "/"), image=img)

                file_paths.append(image_path)

            for image_path_key in my_images_paths.keys():
                if image_path_key not in file_paths:
                    delete_image_by_id(file=os.path.join(path, 'images_database.csv').replace("\\", "/"),
                                       image_id=my_images_paths[image_path_key])

    def search_img(self):
        if (self.keep.get() == 0) or (self.keep.get() == 1 and self.rs == []):
            self.tagshistoryvariable.set(self.query.get())
            newrs = []
            for i in self.my_images:
                for j in i.tags:
                    if j == self.query.get():
                        newrs.append(i)
            self.rs = newrs

        elif self.keep.get() == 1 and self.rs != []:
            self.tagshistoryvariable.set(self.tagshistoryvariable.get() + ', ' + self.query.get())
            newrs = []
            for i in self.rs:
                for j in i.tags:
                    if j == self.query.get():
                        newrs.append(i)
            self.rs = newrs
        self.load_images(0)

# Big question: Este necesara si o bifa pentru a face reuniunea tagurilor cautate? Bifa actuala va face intersectia
# Asta se traduce practic in afisarea tuturor pozelor care au oricare din tagurile x, y, z cautate
