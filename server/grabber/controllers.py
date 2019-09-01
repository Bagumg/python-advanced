from bs4 import BeautifulSoup
import requests
import os

def grab_images(request):
    req = requests.get(request.get('data'))
    soup = BeautifulSoup(req.text, 'html.parser')
    find_picture = soup.find_all(class_='fileThumb')
    if 'img' not in os.listdir('.'):
        os.mkdir('img')
    os.chdir('img')
    for i in find_picture:
        with open(i.get('href')[20:], 'wb') as img:
            picture = requests.get('http://' + i.get('href')[2:])
            img.write(picture.content)
            print('Картинка ' + i.get('href')[20:] + ' сохранена')
    print('Готово!')