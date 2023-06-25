import sys
from threading import Thread
from time import sleep


def task(wait_time: float, name: str) -> None:
    print(f'S {name}')
    sleep(wait_time)
    print(f'E {name}')


def get_order() -> (int, int, int):
    if len(sys.argv) != 4:
        print('invalid parameters')
        exit(1)

    args: list[int] = []
    valid_args = ['1', '2', '3']

    for i in sys.argv[1:]:
        if i not in valid_args:
            print(f'invalid parameter {i} type')
            exit(1)

        if args.count(int(i)) >= 1:
            print(f'duplicated parameter {i}')
            exit(1)

        args.append(int(i))

    return (args[0], args[1], args[2])


def main():
    threads: list[Thread] = []

    for i in range(3):
        time_wait = 3 - i if i < 2 else 0
        thread = Thread(target=task, args=(time_wait, f'Thread {i + 1}'))
        threads.append(thread)

    order = get_order()

    for i in order:
        threads[i - 1].start()
        threads[i - 1].join()


if __name__ == '__main__':
    main()
