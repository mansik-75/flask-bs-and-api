import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = 'dasopdfjlskfjdss'


@app.route('/')
def main_page():
    context = {
        'news': []
    }
    page = requests.get('https://rg.ru/news.html')
    page_text = page.text
    soup = BeautifulSoup(page_text, 'html.parser')
    news = soup.find_all(class_='ItemOfListStandard_wrapper__bO1Hw ItemOfListStandard_imageRight__c0qb9')
    for news_item in news:
        context['news'].append({})
        current_context = context['news'][-1]
        # print(news_item)
        news_item = BeautifulSoup(str(news_item), 'html.parser')
        # print(news_item.find(class_='LinksOfRubric_item__SwOXg ItemOfListStandard_rubric__XePeA').text)
        current_context['news_name'] = news_item.find(class_='ItemOfListStandard_title__eX0Jw').text
        current_context['news_time'] = news_item.find(class_='ItemOfListStandard_datetime__1tmwG').text
        current_context['news_location'] = news_item.find(class_='LinksOfRubric_item__SwOXg ItemOfListStandard_rubric__XePeA').text
        image = news_item.find(class_='Image_img__m9RSC ItemOfListStandard_image___sWCo')
        current_context['news_img'] = image.get('src') if image else None
        current_context['news_link'] = news_item.find(class_='ItemOfListStandard_title__eX0Jw').get('href')

    return render_template('main.html', **context)


# https://jsonplaceholder.typicode.com/posts/1 - сайт API
# https://rg.ru/news.html - сайт для новостей


if __name__ == '__main__':
    app.run()
