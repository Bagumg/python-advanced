from bs4 import BeautifulSoup
import requests
import os
import zipfile
import shutil

def grab_images(request):
    req = requests.get(request.get('data'))
    soup = BeautifulSoup(req.text, 'html.parser')
    find_picture = soup.find_all(class_='fileThumb')
    thread_name = soup.find(class_='postMessage')
    if thread_name.text not in os.listdir('.'):
        os.mkdir(thread_name.text)
    os.chdir(thread_name.text)
    for i in find_picture:
        with open(i.get('href')[20:], 'wb') as img:
            picture = requests.get('http://' + i.get('href')[2:])
            img.write(picture.content)
            print('Картинка ' + i.get('href')[20:] + ' сохранена')
    arch = zipfile.ZipFile(r'..\\img.zip', 'w')
    for root, dirs, files in os.walk('.'):
        for file in files:
            arch.write(file)
    arch.close()
    print('Архив создан')
    print('Удаляем папку')
    os.chdir('..')
    shutil.rmtree(thread_name.text, ignore_errors=True)
    if not os.path.exists('img'):
        print('Папка удалена!')
    print('Жду комманды')
