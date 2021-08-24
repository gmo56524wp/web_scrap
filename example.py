from bs4 import BeautifulSoup

with open('web_scrap.html', 'r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, 'lxml')
    tags = soup.find_all('div', class_ = 'card')
    for tag in tags:
        course_name = tag.h5.text
        course_price = tag.a.text.split(" ")[-1]
        print(course_name+' cost '+course_price)
