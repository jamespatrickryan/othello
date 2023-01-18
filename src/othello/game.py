import tkinter
import tkinter.messagebox

from constants import *
from main import *


class Othello(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.title('Othello')
        self.resizable(False, False)

        container = tkinter.Frame(self)
        container.pack(fill='both', side='top', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.pages = {}
        for section in (Index,):
            page = section(self, container)
            self.pages[section] = page
            page.grid(row=0, column=0, sticky='nsew')

        self.navigate(Index)

    def navigate(self, section):
        page = self.pages[section]
        page.tkraise()


class Index(tkinter.Frame):
    def __init__(self, root, container):
        tkinter.Frame.__init__(self, container)
        self.pack()

        self.root = root
        self.turn = BLACK
        self.color = {
            BLACK: PLAYER,
            WHITE: COMPUTER
        }

        self.surface()

        self.callback()

        self.initialize()

    def surface(self):
        self.canvas = tkinter.Canvas(
            self,
            background=GREEN,
            highlightthickness=0,
            height=DIMENSION + 1,
            width=DIMENSION + 1
        )
        self.canvas.pack(padx=10, pady=10)

    def callback(self):
        self.canvas.bind('<ButtonPress>', self.click)

    def initialize(self):
        self.board = [FRINGE] * 100

        for index in cells():
            self.board[index] = VACANT

        self.area = DIMENSION // BOARD

        for y in range(BOARD):
            for x in range(BOARD):
                top = x * self.area
                left = y * self.area
                bottom = (x + 1) * self.area
                right = (y + 1) * self.area

                self.canvas.create_rectangle(
                    top,
                    left,
                    bottom,
                    right,
                    tag=f'square_{x}{y}'
                )

        i = BOARD // 2 - 1
        j = BOARD // 2

        self.draw_a_disc(i, j, BLACK)
        self.draw_a_disc(j, i, BLACK)

        self.draw_a_disc(j, j, WHITE)
        self.draw_a_disc(i, i, WHITE)

        self.reveal(list(self.hints))

    def reveal(self, hints):
        for y in range(BOARD):
            for x in range(BOARD):
                color = YELLOW if (x, y) in hints else GREEN
                self.canvas.itemconfig(f'square_{x}{y}', fill=color)

    def draw_a_disc(self, x, y, turn):
        i = (x + 0.5) * self.area
        j = (y + 0.5) * self.area

        top = i - (self.area * 0.75) // 2
        left = j - (self.area * 0.75) // 2
        bottom = i + (self.area * 0.75) // 2
        right = j + (self.area * 0.75) // 2

        self.canvas.create_oval(
            top,
            left,
            bottom,
            right,
            fill=self.color[turn],
            tag=f'disk_{x}{y}'
        )

        coordinates = int(f'{y}{x}') + 11
        self.board[coordinates] = turn

    def click(self, event):
        x = event.x // self.area
        y = event.y // self.area

        coordinates = int(f'{y}{x}') + 11

        if verify(coordinates, self.turn, self.board):
            clone = list(self.board)
            progress(coordinates, self.turn, self.board)

            self.put(x, y, self.turn, clone)

    def put(self, x, y, turn, clone):
        self.draw_a_disc(x, y, turn)

        coordinates = int(f'{y}{x}') + 11

        for direction in DIRECTIONS:
            point = batch(coordinates, turn, clone, direction)

            if point is not None:
                square = coordinates + direction

                while square != point:
                    y, x = map(int, str(square))

                    self.canvas.itemconfig(
                        f'disk_{x - 1}{y - 1}',
                        fill=self.color[turn]
                    )

                    square += direction

        previous = self.turn
        self.turn = then(self.board, previous)

        if previous == self.turn:
            title = 'Notice'
            message = 'Player' if self.turn == BLACK else 'Computer'
            tkinter.messagebox.showinfo(title, message)
        elif self.turn is None:
            self.assessment()

        self.reveal(list(self.hints))

        if self.turn == WHITE:
            self.root.after(1000, self.computer)

    def computer(self):
        clone = list(self.board)
        coordinates = fetch(search(4, score), self.turn, self.board)
        progress(coordinates, self.turn, self.board)

        y, x = map(int, str(coordinates))
        self.put(x - 1, y - 1, self.turn, clone)

    def assessment(self):
        player, computer = 0, 0

        for square in cells():
            piece = self.board[square]

            if piece == BLACK:
                player += 1
            elif piece == WHITE:
                computer += 1

        title = 'Assessment'
        message = f'Player: {player} Computer: {computer}'
        tkinter.messagebox.showinfo(title, message)

    @property
    def hints(self):
        for move in legal_moves(self.turn, self.board):
            y, x = map(int, str(move))
            yield x - 1, y - 1


if __name__ == '__main__':
    othello = Othello()
    othello.mainloop()
