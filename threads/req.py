import threading
import requests
import time

start = time.time()

urls = [
    "https://www.google.com",
    "https://www.apple.com",
    "https://www.instagram.com",
    "https://microsoft.com",
    "https://marcosvenicius.com.br"
]


calls = []


def call(url: str) -> None:
    s = time.time() - start

    _ = requests.get(url)

    e = time.time() - start

    calls.append((url, s, e))


threads = [threading.Thread(target=call, args=(url,)) for url in urls]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

for c in calls:
    print(f'url: "{c[0]}" \t\t\t duration: {c[2] - c[1]:.5f}s')

