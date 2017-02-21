text = '<a class="nav" href="/teachers">講師紹介</a></li>'
href_number = text.find("href=")
start_number = text.find('"', href_number + 1)
end_number = text.find('"', start_number + 1)

url = text[start_number + 1:end_number]
print(url)
