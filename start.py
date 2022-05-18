import os
import sys
import subprocess
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import tkinter.ttk as ttk 
from tkinter import colorchooser


def path0(relative_path):
    base_path = getattr(
        sys,
        '_MEIPASS',
        os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


class Shutdown:

    def __init__(self, root):
        # main-frame
        ico = path0("ico.png")
        root.iconphoto(True, tk.PhotoImage(file=ico))
        root.title("Shutdown v105")
        root.geometry("300x80+600+300")
        root.resizable(FALSE, FALSE)
        self.setting = path0("setting.txt")
        self.i = 0
        self.chcolor()

    def chcolor(self):
        ossr = open(self.setting).readline()
        if ossr == 'blue':
            self.colorb = '#0F9EAD'
            self.colorf = 'black'
        elif ossr == 'white':
            self.colorb = 'white'
            self.colorf = 'black'
        elif ossr == 'black':
            self.colorb = 'black'
            self.colorf = 'white'
        elif ossr == '':
            self.colorb = '#0F9EAD'
            self.colorf = 'black'

        # x/y
        self.min = StringVar()
        self.sec = StringVar()

        root.configure(bg=self.colorb)

        # input-line
        entry = ttk.Entry(width=5, textvariable=self.min)
        entry.grid(column=1, row=0)
        # enter
        entry.bind("<Return>", self.down)
 
        # line
        l = ttk.Label(text="Через сколько минут выключить?", background=self.colorb, padding=5, foreground=self.colorf)
        l.grid(column=0, row=0)
        ttk.Label(text="", background=self.colorb).grid(column=0, row=1)
 
        # button
        ttk.Button(text="Запланировать!", command=self.down).grid(column=0, row=2)
        ttk.Button(text="Отмена!", command=self.cancel).grid(column=1, row=2)
        settings_button = tk.Button(text="⚙", command=self.plus)
        settings_button.grid(column=2, row=0,  sticky=tk.W)
        settings_button.configure(bg=self.colorb, fg=self.colorf)

        # radiobutton
        color = StringVar()
        a = tk.Radiobutton(text='Blue', variable=color, value='a', command=self.blue)
        b = tk.Radiobutton(text='White', variable=color, value='b', command=self.white)
        c = tk.Radiobutton(text='Black', variable=color, value='c', command=self.black)
        d = tk.Radiobutton(text='Own', variable=color, value='own', command=self.own)
        
        a.grid(column=6, row=0)
        a.configure(bg=self.colorb, fg=self.colorf)
        b.grid(column=7, row=0)
        b.configure(bg=self.colorb, fg=self.colorf)
        c.grid(column=8, row=0)
        c.configure(bg=self.colorb, fg=self.colorf)
        d.grid(column=9, row=0)
        d.configure(bg=self.colorb, fg=self.colorf)

    # definitions
    def blue(self):
        open(self.setting, 'w').write('blue')
        self.colorb = '#0F9EAD'
        self.colorf = 'black'
        self.chcolor()

    def white(self):
        open(self.setting, 'w').write('white')
        self.colorb = 'white'
        self.colorf = 'black'
        self.chcolor()

    def black(self):
        open(self.setting, 'w').write('black')
        self.colorb = 'black'
        self.colorf = 'white'
        self.chcolor()

    def own(self):
        moot = Tk()
        moot.geometry("+400+300")
        ttk.Button(moot, text='Background', command=self.picker).grid(column=0, row=0)
        ttk.Button(moot, text='Font', command=self.picker).grid(column=1, row=0)
        self.chcolor()
    
    def picker(self):
        (rgb, hx) = colorchooser.askcolor()

    def cancel(self):
        subprocess.call('shutdown -a', shell=True)
        messagebox.showinfo(message='Отмена успешна')

    def down(self, a=None):
        try:
            min = int(self.min.get())
            if min == 0:
                min = 'abc'
            sec = int(min * 60)
            subprocess.call(f'shutdown -s -t {sec}', shell=True)
            messagebox.showinfo(message=f'Ваш пк будет выключен через {min} min')
        except ValueError:
            pass
    
    def plus(self):
        if self.i == 0:
            root.geometry("500x80")
            self.i = 1
        else:
            root.geometry("300x80")
            self.i = 0


root = Tk()
Shutdown(root)
root.mainloop()
