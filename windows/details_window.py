import os
import tkinter
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import filedialog, messagebox
from inout import io_operations as io_op


class DetailsWindow(tkinter.Toplevel):
    def __init__(self, parent, img, image_dir_path):
        super().__init__(parent)

        self.title("Picture")
        self.geometry("1200x300+300+100")
        self.resizable(width=True, height=True)

        self.parent = parent

        self.image_data = img
        self.parent_path = image_dir_path
        self.image_dir_path = os.path.join(image_dir_path, 'images_database.csv')

        image_src = Image.open(self.image_data.path)
        image_src = image_src.resize((200, 200))
        self.image = ImageTk.PhotoImage(image_src)

        self.image_label = tk.Label(self, image=self.image)
        self.image_label.place(x=800, y=30)

        self.back_btn = tk.Button(self, text='BACK', command=self.return_to_main_window)
        self.back_btn.grid(row=0, column=0)

        self.title_label = tk.Label(self, text='TITLE')
        self.title_label.grid(row=3, column=0)

        self.path_label = tk.Label(self, text='PATH')
        self.path_label.grid(row=5, column=0)

        self.dim_label = tk.Label(self, text='DIMENSION')
        self.dim_label.grid(row=7, column=0)

        self.tags_label = tk.Label(self, text='TAGS')
        self.tags_label.grid(row=9, column=0)

        self.add_tags_label = tk.Label(self, text='ADD TAGS')
        self.add_tags_label.grid(row=11, column=0)

        self.add_btn = tk.Button(self, text='ADD', height=1, width=6, command=self.add_tag)
        self.add_btn.grid(row=11, column=3)

        self.delete_tags_label = tk.Label(self, text='DELETE TAGS')
        self.delete_tags_label.grid(row=13, column=0)

        self.delete_btn = tk.Button(self, text='DELETE', height=1, width=6, command=self.delete_tag)
        self.delete_btn.grid(row=13, column=3)

        self.title_txt = tk.Text(self, height=1, width=60)
        self.title_txt.insert(tk.END, self.image_data.name)
        self.title_txt.grid(row=3, column=1)

        self.path_txt = tk.Text(self, height=1, width=60)
        self.path_txt.grid(row=5, column=1)
        self.path_txt.insert(tk.END, self.image_data.path)

        self.dimension_txt = tk.Text(self, height=1, width=60)
        self.dimension_txt.insert(tk.END, self.image_data.get_dimension('kb'))
        self.dimension_txt.grid(row=7, column=1)

        self.tags_txt = tk.Text(self, height=1, width=60)
        self.tags_txt.insert(tk.END, self.image_data.get_tags() if self.image_data.get_tags() != '' else 'No tag set')
        self.tags_txt.grid(row=9, column=1)

        self.add_tag_entry = tk.StringVar()
        self.delete_tag_entry = tk.StringVar()

        self.add_txt = tk.Entry(self, width=60, textvariable=self.add_tag_entry)
        self.add_txt.grid(row=11, column=1)

        self.delete_txt = tk.Entry(self, width=60, textvariable=self.delete_tag_entry)
        self.delete_txt.grid(row=13, column=1)

    def add_tag(self):
        if str(self.add_tag_entry.get()) != '':
            io_op.add_tag_to_image(file=self.image_dir_path, image_id=self.image_data.image_id,
                                   tag=str(self.add_tag_entry.get()))
            self.image_data = io_op.read_image_by_id(file=self.image_dir_path, image_id=self.image_data.image_id)
            self.tags_txt.delete('1.0', tk.END)
            self.tags_txt.insert(tk.END,
                                 self.image_data.get_tags() if self.image_data.get_tags() != '' else 'No tag set')
        else:
            messagebox.showerror('Delete Error', 'Error: tag field must have a value')

    def delete_tag(self):
        if str(self.delete_tag_entry.get()) != '':
            io_op.delete_tag_from_image(file=self.image_dir_path, image_id=self.image_data.image_id,
                                        tag=str(self.delete_tag_entry.get()))
            self.image_data = io_op.read_image_by_id(file=self.image_dir_path, image_id=self.image_data.image_id)
            self.tags_txt.delete('1.0', tk.END)
            self.tags_txt.insert(tk.END,
                                 self.image_data.get_tags() if self.image_data.get_tags() != '' else 'No tag set')
        else:
            messagebox.showerror('Delete Error', 'Error: tag field must have a value')

    def return_to_main_window(self):
        self.parent.refresh_images(self.parent_path)
        self.destroy()
