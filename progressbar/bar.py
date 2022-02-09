import sys

class Progressbar:
    def __init__(self):
        pass

    def _clear_line(self):
        print("\r\033[0K", end = "\r")

    def _progress_print(self, current, end):
        if current == 0:
            current += 1

        self._clear_line()
        message = "["

        for i in range(end):
            if i < current:
                message += "-"
            else:
                message += " "
        message += "]"
        message += f"({current}/{end})"

        print(message, end = "")
        sys.stdout.flush()


    def update(self, current_count, max_count):
        current = int((current_count / max_count) * 100)
        self._progress_print(current = current, end = 100)



