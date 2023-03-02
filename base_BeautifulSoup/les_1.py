from bs4 import BeautifulSoup
import re

with open("blank/index.html", encoding="utf-8") as file:
    src = file.read()


soup = BeautifulSoup(src, "lxml")

title = soup.title


# print(title.string)

# page_h_1=soup.find('h1')

# page_all_h_1 = soup.find_all('h1')

# print(page_all_h_1)

# for i in page_all_h_1:
#     print(i.string)

# user_name=soup.find("div",class_="user__name").find("span").text
# print(user_name)

# user_name = soup.find("div", {"class": "user__name", "id":"fff"}).find("span").text
# print(user_name)


# all_span= soup.find(class_= 'user__info').find_all("span")
# print(all_span[0].text)


# спарсить ссылки 1
# parc_link=soup.find(class_='social__networks').find('ul').find_all('a')
# print(parc_link)

# спарсить ссылки 2
# parc_all_link=soup.find_all('a')
# for i in parc_all_link:
#     item_url=i.get('href')
#     print(f'{i.text}: {item_url}')

# post_div=soup.find(class_="post__text").find_parent()
# print(post_div)

# post_div = soup.find(class_="post__text").find_parent('div', 'user__post')
# print(post_div)

# post_div = soup.find(class_="post__text").find_parent(class_='user__post')
# print(post_div)


# .next_element .previous_element
# следующий элемент и предыдущий
# next_elem=soup.find(class_='post__title').next_element.next_element
# print(next_elem.text)

# next_elem = soup.find(class_='post__title').find_next()
# print(next_elem.text)

# next_elem = soup.find(class_='post__title').previous_element
# print(next_elem.text)

# .find_next_sibling()  .find_previous_sibling()
# крч выводит то, что находится под блоком
# next_sib = soup.find(class_='post__title').find_next_sibling()
# print(next_sib)

# links=soup.find(class_='some__links').find_all('a')
# # for item in links:
# #     print(item.get('data-attr'))
# # мы также можем вызывать аттрибуты не через get, а через
# for item in links:
#     print(item['data-attr'])


# find_a_by_text=soup.find("a",text='Одеяние') # не справляется с частью текста
# print(find_a_by_text)

# find_a_by_text = soup.find("a", text='Магазин')
# print(find_a_by_text)

# всё ок если через регулярки

# find_a_by_text = soup.find_all("a", text=re.compile('Оде'))
# print(find_a_by_text)


# find_a_by_text = soup.find_all("a", text=re.compile('([Оо]де)'))
# print(find_a_by_text)
# for i in find_a_by_text:
#     print(i.text)
