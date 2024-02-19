import tkinter as tk
from tkinter import ttk
from keypad import Keypad

class Calculator_UI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("400x600")
        

        self.display_var = tk.StringVar()
        self.display_entry = ttk.Entry(self, textvariable=self.display_var, font=('Helvetica', 20), justify='right')
        self.display_entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')

        self.history_text = tk.Text(self, height=10, font=('Helvetica', 12))
        self.history_text.grid(row=1, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')

        self.keypad = Keypad(self, keynames=['7', '8', '9', '/', '4', '5', '6', '*', '1', '2', '3', '-', '0', '.', '=', '+', 'DEL', 'CLR','^','(',')','mod'],columns=4)
        
        self.keypad.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')
        self.keypad.bind("<Button-1>", self.on_keypad_click)
        
    def on_keypad_click(self, event):
        key = event.widget.cget("text")
        if key == "=":
            expression = self.display_var.get()
            try:
                if '^' in expression:
                    expression =expression.replace('^','**')
                if 'mod' in expression:
                    expression =expression.replace('mod','%')
                result = eval(expression)
                if '**' in expression:
                    expression =expression.replace('**','^')
                if '%' in expression:
                    expression =expression.replace('%','mod')
                self.history_text.insert(tk.END, f"{expression} = {result}\n")
                self.display_var.set(result)
            except Exception as e:
                self.display_var.set("Error")
                self.display_entry.config(fg="red")
                self.after(1000, self.reset_display_color)
        elif key == "DEL":
            self.display_var.set(self.display_var.get()[:-1])
        elif key == "CLR":
            self.display_var.set("")
        else:
            self.display_var.set(self.display_var.get() + key)

    def reset_display_color(self):
        self.display_entry.config(fg="black")
    def run(self):
        self.mainloop()
   
    