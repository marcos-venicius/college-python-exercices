import os
from time import sleep
from multiprocessing import Process


def job():
    print('...loading')
    sleep(10)
    os.system("open $HOME")


while (res := input("open[y/N]: ")).lower() != "y":
    pass

process = Process(target=job)

process.start()
