#!/user/bin/env python3
# -*- coding:utf-8 -*-
"""
@author: Tian Qunhui(Alien)
@contact: tqunhui@163.com
@time: 2019/7/10 9:17
@file: comparefile.py
@Software:PyCharm
"""
from pandas import read_excel
import tkinter as tk
from tkinter import filedialog


class CompareFile:
    def __init__(self, root):
        self.file_a = tk.StringVar()
        self.file_b = tk.StringVar()
        self.compare_columns = 18
        self.message = tk.StringVar()
        self.var = tk.StringVar()

        frame = tk.Frame(root)
        frame.pack()

        s = tk.Scale(root, label='Select the number of Comparing columns(default=18)', from_=10, to=25, orient=tk.HORIZONTAL,
                     length=400, showvalue=0, tickinterval=1, command=self.set_c)
        s.place(x=50, y=15, anchor='nw')

        l1 = tk.Label(root, textvariable=self.file_a, bg='SkyBlue',font=('Arial', 12), width=30)
        l1.place(x=50, y=80, anchor='nw')

        l2 = tk.Label(root, textvariable=self.file_b, bg='SkyBlue', font=('Arial', 12), width=30)
        l2.place(x=50, y=130, anchor='nw')

        open_file = tk.Button(root, text='Open A', fg='Purple', command=self.open_fileA, width=15)
        open_file.place(x=350, y=78, anchor='nw')

        open_file = tk.Button(root, text='Open B', fg='Purple', command=self.open_fileB, width=15)
        open_file.place(x=350, y=128, anchor='nw')

        open_file = tk.Button(root, text='Start Compare Two file', fg='Purple', command=self.read_compare_file, width=20, height=2)
        open_file.place(x=175, y=180, anchor='nw')

        l2 = tk.Label(root, textvariable=self.message,fg='Purple', bg='SkyBlue', font=('Arial', 12), width=45, height=8)
        l2.place(x=50, y=280, anchor='nw')

    def set_c(self, v):
        print(v)
        self.compare_columns = int(v)


    def open_fileA(self):
        file_a = filedialog.askopenfilename()
        self.file_a.set(file_a)


    def open_fileB(self):
        file_b = filedialog.askopenfilename()
        self.file_b.set(file_b)


    def read_compare_file(self):
        compare_columns = [i for i in range(self.compare_columns)]
        data_a = read_excel(self.file_a.get(), usecols=compare_columns)
        headers = data_a.columns.values
        data_a =data_a.values
        data_b = read_excel(self.file_b.get(), usecols=compare_columns).values
        c = (data_a == data_b)

        message = ''
        for i in range(c.shape[0]):
            for j in range(c.shape[1]):
                if c[i][j] == True:
                    pass
                else:
                    wrong = 'row:'+str(i+2)+'  column:'+ headers[j] + '   is wrong\n(a)'\
                            + str(data_a[i][j]) + ' != (b)' + str(data_b[i][j]) + '\n'
                    message += wrong
        if message == '':
            message = 'All is ok!Nothing wrong!'
        self.message.set(message)


if __name__ == "__main__":
    compare_columns = [i for i in range(18)]
    root = tk.Tk()
    root.title('Compare two file')
    root.geometry('500x500')
    app = CompareFile(root)
    root.mainloop()