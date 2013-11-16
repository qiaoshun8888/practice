import tkMessageBox
from Tkinter import *
from models import Game, State
from ab import alphabeta_search


class Block():

    def click(self, event=None):
        if self.position in self.app.game.actions(self.app.state):
            self.draw(self.app.state.to_move)
            self.app.state = self.app.game.result(
                self.app.state, self.position)
        else:
            tkMessageBox.showinfo("wrong move", "cannot click here")
        if self.app.game.terminal_test(self.app.state):
            tkMessageBox.showinfo("done", "aaa")

    def vs_robot_click(self, event=None):
        self.click(event)
        if self.app.state.to_move == self.app.game.robot:
            import datetime
            _s = datetime.datetime.now()
            p = alphabeta_search(
                self.app.state, self.app.game, self.position)
            print((datetime.datetime.now() - _s).seconds)
            # print p
            self.app.block[p].click()

    def draw(self, ox):
        if ox == 'o':
            self.canvas.create_oval(10, 10, 90, 90)
        else:
            self.canvas.create_line(10, 10, 90, 90)
            self.canvas.create_line(10, 90, 90, 10)

    def __init__(self, app, position):
        self.app = app
        self.position = position
        self.canvas = Canvas(
            self.app.master, width=100, height=100, bd=-3, bg='#eee')
        self.canvas.pack()
        self.canvas.place(x=position[1] * 100, y=position[0] * 100)
        self.canvas.bind('<1>', self.vs_robot_click)


class Application(Frame):
    block = None
    state = None

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()

        self.master = master
        self.game = Game()
        self.state = State(self.game)
        self.block = {}
        for k in self.state.board.keys():
            self.block[k] = Block(self, k)

        self.master.geometry("%dx%d" %
                             (self.game.width * 100, self.game.height * 100))

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
