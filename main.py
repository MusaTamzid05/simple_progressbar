from progressbar.bar import Progressbar
import time

def main():
    progressbar = Progressbar()
    count = 100

    for i in range(count):
        progressbar.update(current_count = i + 1, max_count = count)
        time.sleep(0.5)



if __name__ == "__main__":
    main()
