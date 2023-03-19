import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageFilter, ImageEnhance
import tkinter.messagebox as messagebox


class ImageEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Perbaikan Citra")
        self.root.geometry("1000x500")

        self.frame = tk.LabelFrame(self.root, text="Menu", width=200, height=300, bd=2, relief='solid')
        self.frame.place(x=100, y=10)
        self.canvas = tk.Canvas(self.root, width=550, height=500,highlightthickness=2, highlightbackground='black', bd=2)
        self.canvas.place(x=310, y=10)

        self.button_1 = tk.Button(self.frame, text="Method1", command=self.method_1)
        self.button_1.place(relx=0.5, rely=0.2, anchor='center')

        self.button_2 = tk.Button(self.frame, text="Method2", command=self.method_2)
        self.button_2.place(relx=0.5, rely=0.3, anchor='center')

        self.button_3 = tk.Button(self.root, text="F55121087_Asriani",command=self.show_description, bd=2, relief="solid")
        self.button_3.place(x=100, y=310)
        self.button_3.config(highlightbackground="blue",highlightcolor="red", highlightthickness=1)

        self.select_button = tk.Button(
            self.frame, text="Select to File", command=self.select_file)
        self.select_button.place(relx=0.5, rely=0.4, anchor='center')

    def show_description(self):
        messagebox.showinfo(
            "Description", "UJIAN - Pengolahan Citra - F55121087_Asriani")

    def select_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.original_image = Image.open(file_path)
            self.edited_image_1 = self.original_image.copy()
            self.edited_image_2 = self.original_image.copy()
            self.show_image()

    def show_image(self):
        if self.original_image:
            self.canvas.delete("all")
            image_width, image_height = self.original_image.size
            canvas_width, canvas_height = self.canvas.winfo_width(), self.canvas.winfo_height()
            scale = min(canvas_width/image_width, canvas_height/image_height)
            image_width, image_height = int(
                scale*image_width), int(scale*image_height)
            self.original_image.thumbnail((image_width, image_height))
            self.image_1 = ImageTk.PhotoImage(self.original_image)
            self.image_2 = ImageTk.PhotoImage(self.original_image)
            self.canvas.create_image(
                (canvas_width-image_width)//2, (canvas_height-image_height)//2, image=self.image_1, anchor=tk.NW)

    def method_1(self):
        if self.original_image:
            self.edited_image_1 = self.original_image.copy()
            self.edited_image_1 = self.edited_image_1.filter(ImageFilter.BLUR)
            self.edited_image_1 = ImageEnhance.Color(
                self.edited_image_1).enhance(1.5)
            self.edited_image_1 = ImageEnhance.Contrast(
                self.edited_image_1).enhance(1.2)
            self.show_image_method_1()

    def show_image_method_1(self):
        if self.edited_image_1:
            image_width, image_height = self.edited_image_1.size
            canvas_width, canvas_height = self.canvas.winfo_width(), self.canvas.winfo_height()
            if image_width > canvas_width or image_height > canvas_height:
                scale = min(canvas_width/image_width,
                            canvas_height/image_height)
                image_width, image_height = int(
                    scale*image_width), int(scale*image_height)
            self.edited_image_1.thumbnail((image_width, image_height))
            self.image_1 = ImageTk.PhotoImage(self.edited_image_1)
            self.canvas.create_image(0, 0, image=self.image_1, anchor=tk.NW)

        if self.edited_image_2:
            image_width, image_height = self.edited_image_2.size
            if image_width > canvas_width or image_height > canvas_height:
                scale = min(canvas_width/image_width,
                            canvas_height/image_height)
                image_width, image_height = int(
                    scale*image_width), int(scale*image_height)
            self.edited_image_2.thumbnail((image_width, image_height))
            self.image_2 = ImageTk.PhotoImage(self.edited_image_2)
            self.canvas.create_image(
                image_width, 0, image=self.image_2, anchor=tk.NW)

    def method_2(self):
        if self.original_image:
            self.edited_image_2 = self.original_image.copy()
            self.edited_image_2 = ImageEnhance.Brightness(
                self.edited_image_2).enhance(0.5)
            self.edited_image_2 = ImageEnhance.Sharpness(
                self.edited_image_2).enhance(2.0)
            self.edited_image_2 = ImageEnhance.Contrast(
                self.edited_image_2).enhance(1.5)
            self.show_image_method_2()

    def show_image_method_2(self):
        if self.edited_image_2:
            image_width, image_height = self.edited_image_2.size
            canvas_width, canvas_height = self.canvas.winfo_width(), self.canvas.winfo_height()
        if image_width > canvas_width or image_height > canvas_height:
            scale = min(canvas_width/image_width, canvas_height/image_height)
            image_width, image_height = int(
                scale*image_width), int(scale*image_height)
        self.edited_image_2.thumbnail((image_width, image_height))
        self.image_2 = ImageTk.PhotoImage(self.edited_image_2)
        self.canvas.create_image(0, 0, image=self.image_2, anchor=tk.NW)

        if self.edited_image_1:
            image_width, image_height = self.edited_image_1.size
            if image_width > canvas_width or image_height > canvas_height:
                scale = min(canvas_width/image_width,
                            canvas_height/image_height)
                image_width, image_height = int(
                    scale*image_width), int(scale*image_height)
            self.edited_image_1.thumbnail((image_width, image_height))
            self.image_1 = ImageTk.PhotoImage(self.edited_image_1)
            self.canvas.create_image(
                image_width, 0, image=self.image_1, anchor=tk.NW)


if __name__ == "__main__":
    root = tk.Tk()
    app = ImageEditor(root)
    root.mainloop()
