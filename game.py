
class Game:
    def __init__(self, board, answer, size, lev, step, colors):
        self.size = size
        self.lev = lev
        self.board = board
        self.answer = answer
        self.step = step
        self.colors = colors

    def set_step(self, new_step):
        self.step = new_step

    def get_lev(self):
        return self.lev

    def set_lev(self, new_lev):
        self.lev = new_lev

    def get_step(self):
        return self.step

    def set_both(self, new_board, new_answer):
        self.board = new_board
        self.answer = new_answer
