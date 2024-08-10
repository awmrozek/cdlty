# tabbed view in tkinter. First tab should contain text edit, second tab should contain table view with two columns: key : value.
import tkinter as tk
from tkinter import ttk

class TabbedEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Tabbed Editor")
        self.root.geometry("800x600")

        # Create the Notebook
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Create the first tab with a text editor
        self.text_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.text_tab, text="Text Editor")

        self.text_editor = tk.Text(self.text_tab)
        self.text_editor.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Create the second tab with a table view
        self.table_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.table_tab, text="Table View")

        self.table = ttk.Treeview(self.table_tab, columns=("Key", "Value"), show="headings")
        self.table.heading("Key", text="Key")
        self.table.heading("Value", text="Value")
        self.table.column("Key", stretch=tk.YES)
        self.table.column("Value", stretch=tk.YES)
        self.table.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Add sample data to the table view
        self.table.insert("", "end", values=("Name", "Alice"))
        self.table.insert("", "end", values=("Age", "30"))
        self.table.insert("", "end", values=("Country", "Wonderland"))

if __name__ == "__main__":
    root = tk.Tk()
    app = TabbedEditor(root)
    root.mainloop()

