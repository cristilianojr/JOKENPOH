from tkinter import *

class Replay(Frame):
    def __init__(self, master, state, **kwargs):
        super(Replay, self).__init__(master, background='#1a1a1a', **kwargs)
    
        self.state = state

        self.imgtext = PhotoImage(file=r'assets\replayimg.png')
        self.imgbutton = PhotoImage(file=r'assets\replayimgbutton.png')
        self.winimg = PhotoImage(file=r'assets\vv.png')
        self.gameoverimg = PhotoImage(file=r'assets\gameover.png')

        self.textwl = Label(self, background='#1a1a1a')

        if self.state == 'win':
            self.textwl['image'] = self.winimg
        elif self.state == 'lose':
            self.textwl['image'] = self.gameoverimg

        
        
        self.labeltextask = Label(self, image=self.imgtext, background='#1a1a1a')
        self.btnreplay = Button(self, image=self.imgbutton, background='#1a1a1a', bd=0, command=master.new_init)

        self.textwl.place(x=0, y=0)
        self.labeltextask.place(x=0, y=200)
        self.btnreplay.place(x=300, y=370)
    