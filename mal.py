import requests
n = 0
URL = "https://malsignature.com/?/view?username=k0rr&style=normal"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36",
    "Connection": "keep-alive"
}

session = requests.Session()
adapter = requests.adapters.HTTPAdapter(pool_connections=100, pool_maxsize=100)
session.mount("https://", adapter)
session.mount("http://", adapter)

while True:
    n = n + 1
    response = session.get(URL, headers=headers, timeout=10)
    print(response.status_code, n)
