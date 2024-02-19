import tkinter as tk
from tkinter import ttk
import math

class Keypad(tk.Frame):

    def __init__(self, parent, keynames=[], columns=1, **kwargs):
        
        super().__init__(parent,**kwargs)
        self.keynames = keynames
        self.init_components(columns)
        self.parent = parent
    def init_components(self, columns) -> None:
        """Create a keypad of keys using the keynames list.
        The first keyname is at the top left of the keypad and
        fills the available columns left-to-right, adding as many
        rows as needed.
        :param columns: number of columns to use
        """
        
        for i,key in enumerate(self.keynames):
            keypad = ttk.Button(self,text=key)
            keypad.grid(row=i // columns, column=i % columns, sticky="nsew")
        

       
        pass

    def bind(self,  sequence=None, func=None, add=None):
        """Bind an event handler to an event sequence."""
        
        for child in self.winfo_children():
            child.bind(sequence, func, add)

    
    def __setitem__(self, key, value) -> None:
        """Overrides __setitem__ to allow configuration of all buttons
        using dictionary syntax.

   
        """
        for child in self.winfo_children():
            child[key] = value
       

    def __getitem__(self, key):
        """Overrides __getitem__ to allow reading of configuration values
        from buttons.
        
        """
        return self[key]
        

    def configure(self, cnf=None, **kwargs):
        """Apply configuration settings to all buttons.

        To configure properties of the frame that contains the buttons,
        use `keypad.frame.configure()`.
        """
        for child in self.winfo_children():
            child.configure(cnf, **kwargs)

   

if __name__ == '__main__':
    keys = list('789456123 0.')  # = ['7','8','9',...]

    root = tk.Tk()
    root.title("Keypad Demo")
    keypad = Keypad(root, keynames=keys, columns=3)
    keypad.pack(expand=True, fill=tk.BOTH)
    root.mainloop()
