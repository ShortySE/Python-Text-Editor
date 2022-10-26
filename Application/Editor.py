import customtkinter
import tkinter
import sys
from tkinter import filedialog

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.window_title = "Editor"
        self.title(self.window_title)
        self.geometry("1080x720")
        self.create_widgets()

    def create_widgets(self):
        # The base menu bar
        self.base_menu = tkinter.Menu(self)

        # File menu
        self.file_menu = tkinter.Menu(self.base_menu, tearoff=0)
        self.base_menu.add_cascade(menu=self.file_menu,
        label="File")
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_to_file)
        self.file_menu.add_command(label="Exit", command=self.exit_app)

        self.config(menu=self.base_menu)

        # The main editing area
        self.editing_area = tkinter.Text(master=self, width=1080,
        height=500)
        self.editing_area.pack()

    def run(self):
        self.mainloop()

    def open_file(self):
        file = filedialog.askopenfilename(filetypes=[("All files", "*.*")])
        #self.window_title = file
        if not file == '':
            source_file = open(file, 'r')
            self.editing_area.delete('1.0', tkinter.END)
            self.editing_area.insert('1.0', source_file.read())

    def save_to_file(self):
        pass

    def exit_app(self):
        sys.exit()
