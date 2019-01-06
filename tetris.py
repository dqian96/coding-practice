# TODO: WIP

from timeit import timeit

class _Board:
    def __init__(self, l, w):
        self.l, self.w, = l, w
        self.board = [[0 for i in range(w)] for j in range(l)]

    def update():
        # remove lines


class Tetris:
    def __init__(self, l=24, w=10):
        self.board = _Board(l, w)
        self.player_actions = Queue()
        self.end_game = False

    def _get_player_actions(self):
        while True:
            action = input()
            # input checking

            if self.end_game:
                return

            self.player_actions.put(action)


    def start(self, speed):
        t = Thread(target=self._get_player_actions)

        last_tick = timeit()
        while not self.end_game:
            # game loop
            now = timeit()
            if now - last_tick >= speed:

                self.check_game_cond()
                self.board.update()
                self.gen_new_piece()
                self.gravity_falls()
                self.process_player_actions()

                last_tick = now

        t.join()
