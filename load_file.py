import tkinter as tk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo


# create the root window
class LoadFileDialog:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Select an image")
        self.root.resizable(False, False)
        self.root.geometry("400x200")
        self.root.withdraw()
        self.selected_file = None

    def get_selected_file(self):
        return self.selected_file

    def select_file(self):
        filetypes = (("image files", "*.jpeg *.png *.jpg"), ("All files", "*.*"))

        filename = fd.askopenfilename(
            title="Open a file", initialdir="/", filetypes=filetypes
        )

        # showinfo(title="Selected File", message=filename)
        print(filename)
        if filename:
            self.selected_file = filename
            self.root.destroy()
            showinfo("Success", f"Successfully loaded file\n{filename}")

    def create_screen(self):
        # open button
        self.root.deiconify()
        open_button = tk.Button(
            self.root,
            text="Load a scanned test image (.png, .jpg)",
            height=100,
            width=200,
            command=self.select_file,
        )

        open_button.pack(expand=True)

        # run the application
        self.root.mainloop()
