import requests

def join_lists(crawl_url, obtained_urls):
    url_lists = []
    for i in obtained_urls:
        if not i in crawl_url:
            crawl_url.append(i)
    return crawl_url


def get_link(text):
    href_number = text.find("href=")
    if href_number == -1:
        return None, 0

    start_number = text.find('"', href_number)
    end_number = text.find('"', start_number + 1)
    url = text[start_number + 1:end_number]
    return url, end_number

def get_all_links(x):
    page = requests.get(x)
    text = page.text
    urls = []

    while True:
        url, end_position = get_link(text)
        if url:
            urls.append(url)
            text = text[end_position:]
        else:
            break
    return urls

crawl_urls = ["https://diveintocode-crawling-sample.herokuapp.com/"]
already_crawled_urls = []

while crawl_urls:
    crawl_url = crawl_urls.pop()

    if crawl_url not in already_crawled_urls:
        already_crawled_urls.append(crawl_url)
        obtained_urls = get_all_links(crawl_url)
        # crawl_urls.extend(join_lists(crawl_urls, obtained_urls))
        crawl_urls = join_lists(crawl_urls, obtained_urls)
        # crawl_urls.extend(obtained_urls)
        print(already_crawled_urls)
