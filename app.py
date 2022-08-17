import tkinter as tk
from tkinter import ttk
import sys
from turtle import bgcolor
from process import CpuBar
from widget_update import Configure_widgets


class Application(tk.Tk, Configure_widgets):

    def __init__(self):
        tk.Tk.__init__(self)
        self.resizable(False, False)
        self.attributes('-alpha', 0.9)
        self.bind('<FocusOut>', lambda ev: self.focus_force())

        self.title('CPU-RAM usage bar')

        self.cpu = CpuBar()
        self.run_set_ui()

    def run_set_ui(self):
        self.set_ui()
        self.make_bar_cpu_usage()
        self.configure_cpu_bar()

    def set_ui(self):

        self.bar1 = ttk.LabelFrame(self, text='Control buttons:\n')
        self.bar1.pack(fill=tk.X)

        exit_but = ttk.Button(self.bar1, text='Exit', command=self.app_exit, width=6)
        exit_but.pack(side=tk.TOP)

        move_but = ttk.Button(self.bar1, text='Mode', command=self.configure_win, width=6)
        move_but.pack(side=tk.TOP)

        win_but = ttk.Button(self.bar1, text='Window', command=self.min_win, width=6)
        win_but.pack(side=tk.TOP)

        self.bar = ttk.LabelFrame(self, text='\n\nCPU-RAM information:\n',)
        self.bar.pack(fill=tk.BOTH)

    def make_bar_cpu_usage(self):
        ttk.Label(self.bar, text=f'physical cores: {self.cpu.cpu_count}, logical cores: {self.cpu.cpu_count_logica}\n',
                  anchor=tk.CENTER).pack(fill=tk.X)
        self.list_lable = []
        self.list_pbar = []

        for i in range(self.cpu.cpu_count_logica):
            self.list_lable.append(ttk.Label(self.bar, anchor=tk.CENTER))
            self.list_pbar.append(ttk.Progressbar(self.bar, length=100))

        for i in range(self.cpu.cpu_count_logica):
            self.list_lable[i].pack(fill=tk.X)
            self.list_pbar[i].pack(fill=tk.X)

        self.ram_lab = ttk.Label(self.bar, text='', anchor=tk.CENTER)
        self.ram_lab.pack(fill=tk.X)
        self.ram_bar = ttk.Progressbar(self.bar, length=100)
        self.ram_bar.pack(fill=tk.X)

    def make_minimal_win(self):
        self.bar_one = ttk.Progressbar(self, length=100)
        self.bar_one.pack(side=tk.LEFT)

        self.ram_bar = ttk.Progressbar(self, length=100)
        self.ram_bar.pack(side=tk.LEFT)

        ttk.Button(self, text='Window',command=self.full_win, width=6).pack(side=tk.RIGHT)

        ttk.Button(self, text='Mode', command=self.configure_win, width=6).pack(side=tk.RIGHT)

        ttk.Button(self, text='Exit', command=self.app_exit, width=6).pack(side=tk.RIGHT)

        self.update()
        self.configure_minimal_win()

    def min_win(self):
        self.after_cancel(self.wheel)
        self.clear_win()
        self.update()
        self.make_minimal_win()

    def full_win(self):
        self.after_cancel(self.wheel)
        self.clear_win()
        self.update()
        self.run_set_ui()

    def app_exit(self):
        self.destroy()
        sys.exit()


if __name__ == '__main__':
    root = Application()
    root.mainloop()
