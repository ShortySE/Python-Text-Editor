import tkinter
import customtkinter
import os

from Application.Editor import App

class CreateProjectWizard(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")
        self.title("Unefix Project Creation Wizard")
        self.geometry("550x350")
        self.create_widgets()

    def create_widgets(self):
        # The name of the new project
        self.project_name_label = customtkinter.CTkLabel(master=self, text="Name: ")
        self.project_name_label.place(x=5, y=25)
        self.project_name = customtkinter.CTkEntry(master=self, width=300, height=30)
        self.project_name.place(x=105, y=25)

        # The directory in which it has to be created
        self.directory_label = customtkinter.CTkLabel(master=self, text="Directory: ")
        self.directory_label.place(x=0, y=70)
        self.directory = customtkinter.CTkEntry(master=self, width=300, height=30)
        self.directory.place(x=105, y=70)

        # Dummy checkbox. Will be implemented later
        self.enable_python = customtkinter.CTkCheckBox(master=self, text="Enable Python Interpreter Support")
        self.enable_python.place(x=130, y=120)

        # New project creation button
        self.new_project = customtkinter.CTkButton(master=self, text="New Project", command=self.create_project)
        self.new_project.place(x=165, y=160)

        # Open project // Dummy button
        self.open_folder = customtkinter.CTkButton(master=self, text="Open Folder")
        self.open_folder.place(x=165, y=200)

    def create_project(self):
        os.mkdir(f"{self.directory.get()}\{self.project_name.get()}")
        self.app = App()
        self.app.run()

    def run(self):
        self.mainloop()