import threading


counter = 0


def job1(index):
    print(f"JOB{index} STARTED")
    global counter
    for i in range(1000000):
        counter += 1
    print("JOB1 FINISHED")


def main():
    threads = []

    for i in range(10):
        thread = threading.Thread(target=job1, args=(i,))
        threads.append(thread)

        thread.start()

    print(counter)

    for thread in threads:
        thread.join()

    print(counter)


if __name__ == '__main__':
    main()
