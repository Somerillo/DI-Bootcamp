import requests
import time


def get_load_time(url):
    """
    returns the amount of time it takes a webpage to load\n
    (how long it takes for a complete response to a request).
    """
    try:
        start = time.time()  # sets time of start
        response = requests.get(url)  # sends request
        end = time.time()  # sets time of end
        load_time = end - start

        if response.status_code == 200: # if success
            return f"For {url} the load time is {load_time:.3f} seconds."
        else: # if sh!t happens
            return f"Error loading {url}: status code {response.status_code}"
    except requests.RequestException as e: # the code must flow on
        return f"error loading {url}: {e}"


webpages = ["https://www.google.com", "https://www.google.co.il", "https://www.google.com.ar",
            "https://www.ynet.co.il", "https://www.imdb.com", "https://etc.com/"]

for web in webpages: # times change from page to page and in between requests
    result = get_load_time(web)
    print(get_load_time(web))

# to do list: repeat the for loop k-times and take averae time for each page