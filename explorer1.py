import os
import tkinter as tk
from tkinter import ttk, filedialog

class FileExplorer:
    def __init__(self, root):
        self.root = root
        self.root.title("Windows 95 File Explorer")
        self.root.geometry("800x600")
        
        self.create_ui()

        # Start at the user's home directory
        self.load_directory(os.path.expanduser("."))

    def create_ui(self):
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Create a treeview for the directory structure
        self.tree = ttk.Treeview(self.main_frame)
        self.tree.pack(side=tk.LEFT, fill=tk.Y)
        
        # Create a scrollbar for the treeview
        self.tree_scrollbar = ttk.Scrollbar(self.main_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.tree_scrollbar.set)
        self.tree_scrollbar.pack(side=tk.LEFT, fill=tk.Y)

        # Create a listbox for the file list
        self.file_listbox = tk.Listbox(self.main_frame)
        self.file_listbox.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Bind double-click event to open directory
        self.tree.bind("<Double-1>", self.on_tree_double_click)

    def load_directory(self, path):
        # Clear the current content
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Add the root directory
        self.insert_directory("", path)
        self.root_directory = path

    def insert_directory(self, parent, path):
        # Add a directory node
        node = self.tree.insert(parent, tk.END, text=os.path.basename(path), open=True)

        # Insert directories and files
        try:
            for item in os.listdir(path):
                item_path = os.path.join(path, item)
                if os.path.isdir(item_path):
                    self.insert_directory(node, item_path)
                else:
                    self.tree.insert(node, tk.END, text=item, open=False)
        except PermissionError:
            pass  # Ignore directories that cannot be accessed

    def on_tree_double_click(self, event):
        item_id = self.tree.focus()
        item_text = self.tree.item(item_id, "text")
        
        # Get the full path of the selected item
        selected_path = self.get_full_path(item_id)

        if os.path.isdir(selected_path):
            # Update the file listbox with the contents of the directory
            self.update_file_listbox(selected_path)
        else:
            self.open_file(selected_path)

    def update_file_listbox(self, path):
        self.file_listbox.delete(0, tk.END)
        try:
            for item in os.listdir(path):
                self.file_listbox.insert(tk.END, item)
        except PermissionError:
            pass  # Ignore directories that cannot be accessed

    def get_full_path(self, item_id):
        # Reconstruct the full path from the item_id
        path = ""
        while item_id:
            item_text = self.tree.item(item_id, "text")
            path = os.path.join(item_text, path)
            item_id = self.tree.parent(item_id)
        
        return os.path.join(self.root_directory, path)

    def open_file(self, path):
        # Open the file using the default application
        os.startfile(path)

if __name__ == "__main__":
    root = tk.Tk()
    app = FileExplorer(root)
    root.mainloop()

