from threading import Thread
from time import time, sleep


def task(wait_time: float, message: str) -> None:
    print(f'Task started: {message}')
    sleep(wait_time)
    print(f'Task finished: {message}')


thread = Thread(target=task, args=(2, 'Executing...'))
thread.start()
start = time()
thread.join()
end = time() - start

print(f'task duration: {end:.5f}s')
