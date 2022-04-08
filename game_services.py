from PIL import ImageDraw
from game import Game
import sys
from PyQt5.QtGui import QPixmap, QImage
from PIL.ImageQt import ImageQt
from PIL import Image
from seting import Setting


class Game_Service:

    @staticmethod
    def read_level(path):
        matrix = []
        with open(path, "r") as f:
            cur_arr = []
            for line in f:
                if not (line == "\n"):
                    cur_arr.append([int(x) for x in line.split(',')])
                else:
                    matrix.append(cur_arr)
                    cur_arr = []
        return matrix

    @staticmethod
    def print_matrix(matrix):
        for i in matrix:
            print(i)

    @staticmethod
    def get_coords(nas, n):
        row = 0
        column = 0
        for i in nas:
            try:
                column = i.index(n)
            except ValueError:
                column = -1
            if column != -1:
                break
            row += 1
        return row, column

    @staticmethod
    def cr_new_matrix(t_ar1r):
        matrix = [row[:] for row in t_ar1r]
        return matrix

    def move(self, str1, arr):
        flag = False
        row, col = self.get_coords(arr, 4)
        if str1 == "up":
            try:
                if arr[row - 2][col] == 0 and arr[row - 1][col] > 1:
                    arr[row][col] = 0
                    arr[row - 2][col] = arr[row - 1][col]
                    arr[row - 1][col] = 4
                    flag = True
                if arr[row - 1][col] == 0:
                    arr[row][col] = 0
                    arr[row - 1][col] = 4
                    flag = True
            except IndexError:
                flag = False
        if str1 == "down":
            try:
                if arr[row + 2][col] == 0 and arr[row + 1][col] > 1:
                    arr[row][col] = 0
                    arr[row + 2][col] = arr[row + 1][col]
                    arr[row + 1][col] = 4
                    flag = True
                if arr[row + 1][col] == 0:
                    arr[row][col] = 0
                    arr[row + 1][col] = 4
                    flag = True
            except IndexError:
                flag = False
        if str1 == "left":
            try:
                if arr[row][col - 2] == 0 and arr[row][col - 1] > 1:
                    arr[row][col] = 0
                    arr[row][col - 2] = arr[row][col - 1]
                    arr[row][col - 1] = 4
                    flag = True
                if arr[row][col - 1] == 0:
                    arr[row][col] = 0
                    arr[row][col - 1] = 4
                    flag = True
            except IndexError:
                flag = False
        if str1 == "right":
            try:
                if arr[row][col + 2] == 0 and arr[row][col + 1] > 1:
                    arr[row][col] = 0
                    arr[row][col + 2] = arr[row][col + 1]
                    arr[row][col + 1] = 4
                    flag = True
                if arr[row][col + 1] == 0:
                    arr[row][col] = 0
                    arr[row][col + 1] = 4
                    flag = True
            except IndexError:
                flag = False
        return flag

    @staticmethod
    def make_pict(size, matrix, colors):
        new_image = Image.new("RGB", (len(matrix[0]) * size, len(matrix) * size), "#ffffff")
        y = size * len(matrix)
        x = size * len(matrix[0])
        draw = ImageDraw.Draw(new_image)
        for i in range(0, y, size):
            for j in range(0, x, size):
                fill = colors[matrix[int(i / size)][int(j / size)]]
                draw.rectangle((j, i, j + size - 1, i + size - 1), fill=fill)
        return new_image

    def create_game(self):
        lev = 1
        matrix = self.read_level(f"level{lev}")
        return Game(matrix[0], matrix[1], 30, lev, 0, colors={
            1: "#262526",
            0: "#e6eaeb",
            2: "#4799ad",
            3: "#941e33",
            4: "#262c4a",
            5: "#284533",
            6: "#c01fb1",
            7: "#262c4a",
            8: "#262c4a",
            9: "#262c4a",
        })

    def cr_new_without(self, t_ar1r):
        matrix = [row[:] for row in t_ar1r]
        row, col = self.get_coords(matrix, 4)
        matrix[row][col] = 0
        return matrix

    def update(self, game: Game):
        flag = False
        if self.cr_new_without(game.board) == game.answer:
            game.set_lev(game.get_lev() + 1)
            self.win(game.lev)
            matrix = self.read_level(f"level{game.lev}")
            game.set_both(matrix[0], matrix[1])
            game.step = 0
            flag = True
        return flag

    def win(self, n):
        if n > 2:
            print("ПОБЕДА!!!")
            sys.exit(0)


class Window_service:
    def __init__(self, window):
        self.window = window
        self.gs = Game_Service()
        self.set_s = Setting_Service(window)
        self.game = self.gs.create_game()

    def set_data(self):
        q_img = ImageQt(self.gs.make_pict(self.game.size, self.game.board, self.game.colors).convert("RGBA"))
        self.window.num_account.setText(str(self.game.step))
        self.window.num_level.setText(str(self.game.lev))
        self.window.label.setPixmap(QPixmap(QImage(q_img)))
        self.window.central_widget.update()

    def move_up(self):
        if self.gs.move("up", self.game.board):
            self.game.set_step(self.game.get_step() + 1)
        self.set_data()
        if self.gs.update(self.game):
            self.set_data()

    def move_down(self):
        if self.gs.move("down", self.game.board):
            self.game.set_step(self.game.get_step() + 1)
        self.set_data()
        if self.gs.update(self.game):
            self.set_data()

    def move_left(self):
        if self.gs.move("left", self.game.board):
            self.game.set_step(self.game.get_step() + 1)
        self.set_data()
        if self.gs.update(self.game):
            self.set_data()

    def move_right(self):
        if self.gs.move("right", self.game.board):
            self.game.set_step(self.game.get_step() + 1)
        self.set_data()
        if self.gs.update(self.game):
            self.set_data()

    def restart(self):
        matrix = self.gs.read_level(f"level{self.game.lev}")
        self.game.set_both(matrix[0], matrix[1])
        self.game.set_step(0)
        self.set_data()


class Setting_Service:
    def __init__(self, main_wind):
        self.window = main_wind
        self.w = Setting()
        self.func()

    @staticmethod
    def dr_rectangle(num_1, num_2, num_3):
        new_image = Image.new("RGB", (21, 21), "#ffffff")
        draw = ImageDraw.Draw(new_image)
        draw.rectangle((0, 0, 20, 20), (num_1, num_2, num_3))
        return new_image

    def set_data1(self):
        n_1, n_2, n_3 = self.w.s_1.value(), self.w.s_2.value(), self.w.s_3.value()
        q_img = ImageQt(self.dr_rectangle(n_1, n_2, n_3).convert("RGBA"))
        self.w.color_box.setPixmap(QPixmap(QImage(q_img)))

    def set_data2(self):
        n_1, n_2, n_3 = self.w.b_1.value(), self.w.b_2.value(), self.w.b_3.value()
        q_img = ImageQt(self.dr_rectangle(n_1, n_2, n_3).convert("RGBA"))
        self.w.color_back_la.setPixmap(QPixmap(QImage(q_img)))

    def func(self):
        self.w.s_1.sliderMoved.connect(self.set_data1)
        self.w.s_2.sliderMoved.connect(self.set_data1)
        self.w.s_3.sliderMoved.connect(self.set_data1)
        self.w.b_1.sliderMoved.connect(self.set_data2)
        self.w.b_2.sliderMoved.connect(self.set_data2)
        self.w.b_3.sliderMoved.connect(self.set_data2)
        self.w.apply_beck.clicked.connect(self.back_fun)
        self.w.apply_color.clicked.connect(self.cub_fun)
        self.w.apply_wind.clicked.connect(self.wind_fun)

    def back_fun(self):
        num_1 = self.w.b_1.value()
        num_2 = self.w.b_2.value()
        num_3 = self.w.b_3.value()
        self.window.setStyleSheet(f"background-color:#{self.rgb_to_hex((num_1, num_2, num_3))};")

    def cub_fun(self):
        num_1 = self.w.s_1.value()
        num_2 = self.w.s_2.value()
        num_3 = self.w.s_3.value()
        num = self.w.comboBox.currentText()
        self.window.ws.game.colors.pop(int(num))
        self.window.ws.game.colors[int(num)] = '#' + self.rgb_to_hex((num_1, num_2, num_3))
        self.window.ws.set_data()

    def wind_fun(self):
        width = int(self.w.lineEdit.text())
        self.window.ws.game.size = width

        self.window.ws.set_data()

    @staticmethod
    def rgb_to_hex(rgb):
        return '%02x%02x%02x' % rgb

    def show_new_window(self):
        self.set_data1()
        self.set_data2()
        self.w.show()
