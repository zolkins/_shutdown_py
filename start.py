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
        root.title("Shutdown v105")
        root.geometry("300x80+600+300")
        root.resizable(FALSE, FALSE)

        self.setting = path0("setting.txt")
        colorb = '#0F9EAD'
        colorf = 'black'
        self.i = 0
        open('setting.txt', 'r')

        # x/y
        self.min = StringVar()
        self.sec = StringVar()
 
        root.configure(bg=colorb)

        # input-line
        entry = ttk.Entry(width=5, textvariable=self.min)
        entry.grid(column=1, row=0)
 
        # line
        ttk.Label(text="  Через сколько минут выключить?", background=colorb, foreground='black').grid(column=0, row=0)
        ttk.Label(text="", background=colorb).grid(column=0, row=1)
 
        # button
        ttk.Button(text="Запланировать!", command=self.down).grid(column=0, row=2)
        ttk.Button(text="Отмена!", command=self.cancel).grid(column=1, row=2)
        login_button = tk.Button(text="⚙", command=self.plus)
        login_button.grid(column=2, row=0,  sticky=tk.W)
        login_button.configure(bg=colorb, fg=colorf)

        # radiobutton
        color = StringVar()
        a = tk.Radiobutton(text='Blue', variable=color, value='a', command=self.blue)
        b = tk.Radiobutton(text='White', variable=color, value='b', command=self.white)
        c = tk.Radiobutton(text='Black', variable=color, value='c', command=self.black)
        d = tk.Radiobutton(text='Own', variable=color, value='own', command=self.own)
        
        a.grid(column=6, row=0)
        a.configure(bg=colorb, fg=colorf)
        b.grid(column=7, row=0)
        b.configure(bg=colorb, fg=colorf)
        c.grid(column=8, row=0)
        c.configure(bg=colorb, fg=colorf)
        d.grid(column=9, row=0)
        d.configure(bg=colorb, fg=colorf)
        # enter
        root.bind("<Return>", self.down2)

    #DEF-------

    def blue(self):
        open(self.setting, 'w').write('blue')

    def white(self):
        open(self.setting, 'w').write('white')

    def black(self):
        open(self.setting, 'w').write('black')

    def own(self):
        moot = Tk()
        ttk.Button(moot, text='Background', command=self.picker).grid(column=0, row=0)
        ttk.Button(moot, text='Font', command=self.picker).grid(column=1, row=0)
    
    def picker(self):
        (rgb, hx) = colorchooser.askcolor()
        

    def cancel(self):
        subprocess.call('shutdown -a', shell=True)
        messagebox.showinfo(message='Отмена успешна')
 
    def down2(self, event):
        try:
            min = int(self.min.get())
            if min == 0:
                min = 'abc'
            sec = int(min * 60)
            subprocess.call('shutdown -s -t ' + str(sec), shell=True)
            messagebox.showinfo(message='Ваш пк будет выключен через ' + str(min) + ' min')
        except ValueError:
            pass
 
    def down(self):
        try:
            min = int(self.min.get())
            if min == 0:
                min = 'abc' 
            sec = int(min * 60)
            subprocess.call('shutdown -s -t ' + str(sec), shell=True)
            messagebox.showinfo(message='Ваш пк будет выключен через ' + str(min) + ' min')
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
