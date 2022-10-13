from bs4 import BeautifulSoup
import requests
from object import Link


# Headers for requests module
Headers = {
    'Content-Type': 'text/html',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
}


def initial_crawler(url):
    # Initial crawler. It's purpose is to gather raw urls for further analysis
    try:
        page = requests.get(url, headers=Headers)
        soup = BeautifulSoup(page.text, 'html.parser')
        tags = soup.find_all('a')
        queue = set()  # Set with urls to be crawled

        for tag in tags:
            # Loop that iterates through gathered tags, finds all with urls
            # extract those starting with '/',
            # add them to queue set and returns the sorted set
            if 'href' in tag.attrs:
                if tag['href'].startswith('/'):
                    queue.add(f"{url}{tag['href']}")
    except:
        pass

    return sorted(queue)


def crawler(urls):
    # Crawler that gather data from provided url, such as title,
    # number of internal and external links and references
    queue = initial_crawler(urls)

    for url in queue:
        # Loop that iterates through list of urls, gather data
        # and add it to csv file
        try:
            link = Link(url)
            page = requests.get(url, headers=Headers, allow_redirects=False)
            soup = BeautifulSoup(page.text, 'html.parser')
            tags = soup.find_all('a')
            title = soup.find('title')
            try:
                # Trying to set title of currently crawled url
                link.set_title(title.text)
            except:
                continue
            for tag in tags:
                # Loop that search for <a> tag containing html reference,
                # counts references and number of internal and external links
                if 'href' in tag.attrs:
                    link.count_reference()
                    if tag['href'].startswith('/'):
                        link.count_internal_links()
                    elif tag['href'].startswith('http'):
                        link.count_external_links()
            link.add_to_csv()
        except:
            continue
