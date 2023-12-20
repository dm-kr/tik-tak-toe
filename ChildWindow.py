import tkinter as tk

class ChildWindow(tk.Toplevel):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.bind("<Destroy>", self.kill_root)

    def kill_root(self, event):
        if event.widget == self and self.root.winfo_exists():
            self.root.destroy()
