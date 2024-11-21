from gevent import monkey; monkey.patch_all()

from time import sleep, time
from concurrent.futures import ThreadPoolExecutor as Executor

def fetch_web_page_old(url):
    from urllib.request import urlopen, HTTPError
    try:
        print(f"Fetching {url}...")
        response = urlopen(url)
        print(f"Fetched {url}.")
    except HTTPError as e:
        return str(e)
    else:
        return str(response.code)


def fetch_web_page(url):
    import requests # pip install requests
    try:
        print(f"Fetching {url}...")
        response = requests.get(url, verify=False)
        print(f"Fetched {url}.")
    except Exception as e:
        return str(e)
    else:
        return str(response.status_code)


urls = [
    "https://www.chandrashekar.info/",
    "https://cisco.com/",
    "https://www.python.org/",
    "https://www.dhrona.net/",
    "https://www.kernel.org/",
    "https://www.debian.org/",
    "https://www.moonranger.net/"
]

if __name__ == '__main__':
    start = time()
    #result = [ fetch_web_page(x) for x in urls ]
    result = list(map(fetch_web_page, urls))
    duration = time() - start
    print(f"duration = {duration}")
    print(f"result = {result}")
    print("-" * 40)

    start = time()
    with Executor(max_workers=10) as workers:
        result = list(workers.map(fetch_web_page, urls))
    duration = time() - start
    print(f"duration = {duration}")
    print(f"result = {result}")
