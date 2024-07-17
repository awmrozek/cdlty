import tkinter as tk
from tkinter import ttk

class RegistryEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Registry Editor")
        self.root.geometry("600x400")

        # Creating a Treeview widget
        self.tree = ttk.Treeview(self.root)
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Define columns
        self.tree["columns"] = ("value",)
        self.tree.column("#0", width=200, minwidth=100, stretch=tk.YES)
        self.tree.column("value", width=400, minwidth=200, stretch=tk.YES)

        # Define headings
        self.tree.heading("#0", text="Key")
        self.tree.heading("value", text="Value")

        # Dummy data for demonstration
        self.load_dummy_data()

    def load_dummy_data(self):
        # Insert dummy data for demonstration purposes
        keys = {
            "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion": {
                "ProductName": "Windows 95",
                "BuildLab": "9500",
                "InstallDate": "20220101",
            },
            "HKEY_CURRENT_USER\\Software\\Python": {
                "Version": "3.10.1",
                "Path": "C:\\Python310",
                "Editor": "IDLE",
            }
        }

        self.insert_node("", keys)

    def insert_node(self, parent, node):
        for key, values in node.items():
            item = self.tree.insert(parent, "end", text=key)
            if isinstance(values, dict):
                self.insert_node(item, values)
            else:
                self.tree.set(item, "value", values)

if __name__ == "__main__":
    root = tk.Tk()
    app = RegistryEditor(root)
    root.mainloop()
