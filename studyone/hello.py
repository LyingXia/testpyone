#!_*_ coding:utf-8_*_
"""
# @Author:xiapf
# create on
# @Time : 2018/2/28 15:22
"""
from tkinter import Frame, Button, Entry, messagebox


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.alertButton = Button(self, text='Hello', command=self.hello)
        self.nameInput = Entry(self)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput.pack()
        self.alertButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Message', 'Hello, %s' % name)


app = Application()
# 设置窗口标题:
app.master.title('Hello World')
# 主消息循环:
app.mainloop()
