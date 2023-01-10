from tkinter import *
# from tkinter.ttk import *
from pprint import pprint

letters = ['', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', '']
buttons = []
double_massive = []
x_label = 10
y_label = 5
x_button = 30
y_button = 20
# pieces = [
#     '♖'
# ]


root = Tk()


def repaint_all_buttons():
    for y, button_list in enumerate(double_massive):
        for x, button in enumerate(button_list):
            even_column = x % 2 == 0
            even_row = y % 2 == 0
            odd_column = x % 2 != 0
            odd_row = y % 2 != 0
            if button in button_list and (even_row and even_column) or (odd_row and odd_column):
                button.config(bg='white')
            else:
                button.config(bg='black')


def paint_vertical():
    repaint_all_buttons()
    letter = entry.get()[0].capitalize()
    even_column_number = (letters.index(letter) - 1) % 2 == 0
    odd_column_number = (letters.index(letter) - 1) % 2 != 0
    for y, button_list in enumerate(double_massive):
        for x, button in enumerate(button_list):
            even_row = y % 2 == 0
            odd_row = y % 2 != 0
            vertical_line = letters.index(letter) - 1 == x
            cell_light = even_row and even_column_number or odd_row and odd_column_number
            if cell_light and vertical_line:
                button.config(bg='light green')
            elif not cell_light and vertical_line:
                button.config(bg='green')


def paint_horizontal():
    repaint_all_buttons()
    row_number = int(entry.get()[1])
    for y, button_list in enumerate(double_massive):
        for x, button in enumerate(button_list):
            even_column = x % 2 == 0
            odd_column = x % 2 != 0
            even_row_number = (8 - row_number) % 2 == 0
            odd_row_number = (8 - row_number) % 2 != 0
            horizontal_line = 8 - row_number == y
            cell_light = even_column and even_row_number or odd_row_number and odd_column
            if cell_light and horizontal_line:
                button.config(bg='light green')
            elif not cell_light and horizontal_line:
                button.config(bg='green')


def paint_cell():
    repaint_all_buttons()
    letter = entry.get()[0].capitalize()
    row_number = int(entry.get()[1])
    for y, button_list in enumerate(double_massive):
        for x, button in enumerate(button_list):
            vertical_line = 8 - row_number == y
            horizontal_line = letters.index(letter) - 1 == x
            if horizontal_line and vertical_line:
                button.config(bg='blue')


def paint_rook():
    repaint_all_buttons()
    letter = entry.get()[0].capitalize()
    row_number = int(entry.get()[1])
    for y, button_list in enumerate(double_massive):
        for x, button in enumerate(button_list):
            even_row = y % 2 == 0
            odd_row = y % 2 != 0
            even_column = x % 2 == 0
            odd_column = x % 2 != 0
            vertical_line = 8 - row_number == y
            horizont_line = letters.index(letter) - 1 == x
            vertical_cross_horizontal = vertical_line and horizont_line
            cell_light = (even_row and even_column or odd_row and odd_column)
            if vertical_cross_horizontal:
                button.config(bg='blue')
            elif cell_light and (vertical_line or horizont_line):
                button.config(bg='light green')
            elif not cell_light and (vertical_line or horizont_line):
                button.config(bg='green')


def left_right_paint_diagonal():
    repaint_all_buttons()
    row_number = int(entry.get()[1])
    letter = entry.get()[0].capitalize()
    for y, button_list in enumerate(double_massive):
        for x, button in enumerate(button_list):
            even_row = y % 2 == 0
            odd_row = y % 2 != 0
            even_column = x % 2 == 0
            odd_column = x % 2 != 0
            diagonal_from_left_to_right = x + 8 - row_number == y + letters.index(letter) - 1
            cell_light = (even_row and even_column or odd_row and odd_column)
            if cell_light and diagonal_from_left_to_right:
                button.config(bg='light green')
            elif not cell_light and diagonal_from_left_to_right:
                button.config(bg='green')


def right_left_paint_diagonal():
    repaint_all_buttons()
    row_number = int(entry.get()[1])
    letter = entry.get()[0].capitalize()
    for y, button_list in enumerate(double_massive):
        for x, button in enumerate(button_list):
            even_row = y % 2 == 0
            odd_row = y % 2 != 0
            even_column = x % 2 == 0
            odd_column = x % 2 != 0
            cell_light = even_row and even_column or odd_row and odd_column
            diagonal_from_right_to_left = 7 - y == x - 1 + row_number - (letters.index(letter) - 1)
            if diagonal_from_right_to_left and cell_light:
                button.config(bg='light green')
            elif diagonal_from_right_to_left and not cell_light:
                button.config(bg='green')


def paint_bishop():
    repaint_all_buttons()
    row_number = int(entry.get()[1])
    letter = entry.get()[0].capitalize()
    for y, button_list in enumerate(double_massive):
        for x, button in enumerate(button_list):
            even_row = y % 2 == 0
            odd_row = y % 2 != 0
            even_column = x % 2 == 0
            odd_column = x % 2 != 0
            diagonal_from_left_to_right = x + 8 - row_number == y + letters.index(letter) - 1
            diagonal_from_right_to_left = 7 - y == x - 1 + row_number - (letters.index(letter) - 1)
            cell_light = even_row and even_column or odd_row and odd_column
            if diagonal_from_right_to_left and diagonal_from_left_to_right:
                button.config(bg='blue')
            elif cell_light and (diagonal_from_left_to_right or diagonal_from_right_to_left):
                button.config(bg='light green')
            elif not cell_light and (diagonal_from_left_to_right or diagonal_from_right_to_left):
                button.config(bg='green')


def paint_queen():
    repaint_all_buttons()
    row_number = int(entry.get()[1])
    letter = entry.get()[0].capitalize()
    for y, button_list in enumerate(double_massive):
        for x, button in enumerate(button_list):
            even_row = y % 2 == 0
            odd_row = y % 2 != 0
            even_column = x % 2 == 0
            odd_column = x % 2 != 0
            vertical_line = letters.index(letter) - 1 == x
            horizontal_line = 8 - row_number == y
            diagonal_from_left_to_right = x + 8 - row_number == y + letters.index(letter) - 1
            diagonal_from_right_to_left = 7 - y == x - 1 + row_number - (letters.index(letter) - 1)
            cell_light = even_row and even_column or odd_row and odd_column
            if vertical_line and horizontal_line:
                button.config(bg='blue')
            elif cell_light and (vertical_line or horizontal_line or diagonal_from_right_to_left or
                                 diagonal_from_left_to_right):
                button.config(bg='light green')
            elif vertical_line or horizontal_line or diagonal_from_right_to_left or diagonal_from_left_to_right:
                button.config(bg='green')


def paint_5_vertical():
    repaint_all_buttons()
    letter = entry.get()[0].capitalize()
    for y, button_list in enumerate(double_massive):
        for x, button in enumerate(button_list):
            even_row = y % 2 == 0
            odd_row = y % 2 != 0
            even_column = x % 2 == 0
            odd_column = x % 2 != 0
            vertical_five_lines = x - 2 <= letters.index(letter) - 1 <= x + 2
            cell_light = even_row and even_column or odd_row and odd_column
            if cell_light and vertical_five_lines:
                button.config(bg='light green')
            elif not cell_light and vertical_five_lines:
                button.config(bg='green')


def paint_5_horizontal():
    repaint_all_buttons()
    row_number = int(entry.get()[1])
    for y, button_list in enumerate(double_massive):
        for x, button in enumerate(button_list):
            even_row = y % 2 == 0
            odd_row = y % 2 != 0
            even_column = x % 2 == 0
            odd_column = x % 2 != 0
            horizontal_five_lines = y - 2 <= 8 - row_number <= y + 2
            cell_light = even_row and even_column or odd_row and odd_column
            if cell_light and horizontal_five_lines:
                button.config(bg='light green')
            elif not cell_light and horizontal_five_lines:
                button.config(bg='green')


def paint_king():
    repaint_all_buttons()
    row_number = int(entry.get()[1])
    letter = entry.get()[0].capitalize()
    for y, button_list in enumerate(double_massive):
        for x, button in enumerate(button_list):
            even_row = y % 2 == 0
            odd_row = y % 2 != 0
            even_column = x % 2 == 0
            odd_column = x % 2 != 0
            vertical_cross_horizontal = 8 - row_number == y and letters.index(letter) - 1 == x
            horizontal_three_lines = y - 1 <= 8 - row_number <= y + 1
            vertical_three_lines = x - 1 <= letters.index(letter) - 1 <= x + 1
            cell_light = even_row and even_column or odd_row and odd_column
            if vertical_cross_horizontal:
                button.config(bg='blue')
            elif cell_light and vertical_three_lines and horizontal_three_lines:
                button.config(bg='light green')
            elif not cell_light and vertical_three_lines and horizontal_three_lines:
                button.config(bg='green')


def paint_knight():
    repaint_all_buttons()
    row_number = int(entry.get()[1])
    letter = entry.get()[0].capitalize()
    for y, button_list in enumerate(double_massive):
        for x, button in enumerate(button_list):
            even_row = y % 2 == 0
            odd_row = y % 2 != 0
            even_column = x % 2 == 0
            odd_column = x % 2 != 0
            vertical_cross_horizontal = 8 - row_number == y and letters.index(letter) - 1 == x
            cell_light = even_row and even_column or odd_row and odd_column
            top_knight = 8 - row_number == y + 2 and (letters.index(letter) - x == 2 or letters.index(letter) == x)
            bottom_knight = 8 - row_number == y - 2 and (letters.index(letter) - x == 2 or letters.index(letter) == x)
            left_knight = (y + row_number == 7 or y + row_number == 9) and letters.index(letter) - 3 == x
            right_knight = (y + row_number == 7 or y + row_number == 9) and letters.index(letter) + 1 == x
            if vertical_cross_horizontal:
                button.config(bg='blue')
            elif cell_light and (top_knight or bottom_knight or left_knight or right_knight):
                button.config(bg='light green')
            elif not cell_light and (top_knight or bottom_knight or left_knight or right_knight):
                button.config(bg='green')


for y in range(10):
    buttons = []
    for x, letter in enumerate(letters):
        if y == 0 or y == 9:
            Label(text=letter).grid(row=y, column=x, ipadx=x_label, ipady=y_label)
        elif 1 <= y <= 8 and (x == 0 or x == 9):
            Label(text=9 - y).grid(row=y, column=x, ipadx=x_label, ipady=y_label)
        elif 1 <= y <= 8 and 1 <= x <= 8 and (y % 2 != 0 and x % 2 != 0) or (y % 2 == 0 and x % 2 == 0):
            button_white = Button(bg='white')
            button_white.grid(row=y, column=x, ipadx=x_button, ipady=y_button)
            buttons.append(button_white)
        elif 1 <= y <= 8 and 1 <= x <= 8 and (y % 2 == 0 and x % 2 != 0) or (y % 2 != 0 and x % 2 == 0):
            button_black = Button(bg='black')
            button_black.grid(row=y, column=x, ipadx=x_button, ipady=y_button)
            buttons.append(button_black)
    if buttons:
        double_massive.append(buttons)


label_frame = LabelFrame(text='Figures')
label_frame.grid(row=0, column=10, rowspan=10, sticky=NSEW)
entry = Entry(label_frame)
entry.pack()

Button(label_frame, text='Repaint', command=repaint_all_buttons).pack(fill=BOTH, expand=1)
Button(label_frame, text='Vertical', command=paint_vertical).pack(fill=BOTH, expand=1)
Button(label_frame, text='Horizont', command=paint_horizontal).pack(fill=BOTH, expand=1)
Button(label_frame, text='Cell', command=paint_cell).pack(fill=BOTH, expand=1)
Button(label_frame, text='Rook', command=paint_rook).pack(fill=BOTH, expand=1)
Button(label_frame, text='LeftRight Diagonal', command=left_right_paint_diagonal).pack(fill=BOTH, expand=1)
Button(label_frame, text='RightLeft Diagonal', command=right_left_paint_diagonal).pack(fill=BOTH, expand=1)
Button(label_frame, text='Bishop', command=paint_bishop).pack(fill=BOTH, expand=1)
Button(label_frame, text='Queen', command=paint_queen).pack(fill=BOTH, expand=1)
Button(label_frame, text='5 Vertical', command=paint_5_vertical).pack(fill=BOTH, expand=1)
Button(label_frame, text='5 Horizons', command=paint_5_horizontal).pack(fill=BOTH, expand=1)
Button(label_frame, text='King', command=paint_king).pack(fill=BOTH, expand=1)
Button(label_frame, text='Knight', command=paint_knight).pack(fill=BOTH, expand=1)

root.mainloop()