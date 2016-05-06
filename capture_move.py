import pyautogui, sys, time


class CaptureMove(object):

    UP_KEY = 'up'
    DOWN_KEY = 'down'
    LEFT_KEY = 'left'
    RIGHT_KEY = 'right'
    __gui = pyautogui
    __moves = []

    def capture_key(self, key):
        self.__moves.append(key)

    def start_moves(self):
        print("Starting moves")
        for move in self.__moves:
            print("Moving to "+move)
            self.__gui.press(move)
            time.sleep(1)

