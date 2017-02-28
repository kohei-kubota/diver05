import requests

def get_link(text):
    href_number = text.find("href=")
    if href_number == -1:
        return None, 0
    start_number = text.find('"', href_number)
    end_number = text.find('"', start_number + 1)
    url = text[start_number + 1:end_number]
    return url, end_number

text = requests.get('https://diveintocode.jp/').text
while True:
    url,end_position = get_link(text)
    if url:
        print(url)
        text = text[end_position:]
    else:
        break
