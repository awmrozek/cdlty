import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

class SimpleNotepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Notepad")
        self.root.geometry("800x600")

        self.text_area = tk.Text(self.root, wrap='word')
        self.text_area.pack(expand=1, fill='both')
        self.text_area.bind('<<Modified>>', self.on_text_modified)

        self.menu_bar = tk.Menu(self.root)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.exit_application)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        self.root.config(menu=self.menu_bar)

        self.current_file = None
        self.text_modified = False

    def on_text_modified(self, event=None):
        self.text_modified = True
        self.text_area.edit_modified(False)

    def check_for_unsaved_changes(self):
        if self.text_modified:
            response = messagebox.askyesnocancel("Unsaved Changes",
                                                 "You have unsaved changes. Do you want to save them?")
            if response:
                self.save_file()
            return response is not None
        return True

    def new_file(self):
        if self.check_for_unsaved_changes():
            self.text_area.delete(1.0, tk.END)
            self.current_file = None
            self.text_modified = False

    def open_file(self):
        if self.check_for_unsaved_changes():
            file_path = filedialog.askopenfilename(defaultextension=".txt",
                                                   filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
            if file_path:
                with open(file_path, "r") as file:
                    self.text_area.delete(1.0, tk.END)
                    self.text_area.insert(tk.END, file.read())
                self.current_file = file_path
                self.text_modified = False

    def save_file(self):
        if self.current_file:
            file_path = self.current_file
        else:
            file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                     filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text_area.get(1.0, tk.END))
            self.current_file = file_path
            self.text_modified = False

    def exit_application(self):
        if self.check_for_unsaved_changes():
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleNotepad(root)
    root.mainloop()
