# Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и проверить тип и содержание
# соответствующих переменных. Затем с помощью онлайн-конвертера преобразовать строковые представление в формат Unicode
# и также проверить тип и содержимое переменных.


a = 'разработка'
b = 'сокет'
c = 'декоратор'
print(a)
print(type(a))
print(b)
print(type(b))
print(c)
print(type(c))
a = '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430'
b = '\u0441\u043e\u043a\u0435\u0442'
c = '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'
print(a)
print(type(a))
print(b)
print(type(b))
print(c)
print(type(c))


# Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность кодов
# (не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.


a = b'class'
b = b'function'
c = b'method'
print(type(a))
print(len(a))
print(type(b))
print(len(b))
print(type(c))
print(len(c))


# Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.


a = b'attribute'
# b = b'класс' # SyntaxError: bytes can only contain ASCII literal characters.
# c = b'функция' # SyntaxError: bytes can only contain ASCII literal characters.
d = b'type'


# Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в байтовое
# и выполнить обратное преобразование (используя методы encode и decode).


a = 'разработка'
a = a.encode('utf-8')
a = a.decode('utf-8')
b = 'администрирование'
b = b.encode('utf-8')
b = b.decode('utf-8')
c = 'protocol'
c = c.encode('utf-8')
c = c.decode('utf-8')
d = 'standard'
d = d.encode('utf-8')
d = d.decode('utf-8')


# Выполнить пинг веб-ресурсов yandex.ru, youtube.com
# и преобразовать результаты из байтовового в строковый тип на кириллице.


import subprocess

yandex = ['ping', 'yandex.ru']
youtube = ['ping', 'youtube.com']

yandex_response = subprocess.Popen(yandex, stdout=subprocess.PIPE)
youtube_response = subprocess.Popen(youtube, stdout=subprocess.PIPE)

for i in yandex_response.stdout:
    i = i.decode('cp866').encode('utf-8')
    print(i.decode('utf-8'))

for i in youtube_response.stdout:
    i = i.decode('cp866').encode('utf-8')
    print(i.decode('utf-8'))


# Создать текстовый файл test_file.txt, заполнить его тремя строками:
# «сетевое программирование», «сокет», «декоратор». Проверить кодировку файла по умолчанию.
# Принудительно открыть файл в формате Unicode и вывести его содержимое.


with open('test_file.txt', 'w') as test_file:
    test_file.write('сетевое программирование\n')
    test_file.write('сокет\n')
    test_file.write('декоратор\n')

print(test_file) # encoding='cp1251'


with open('test_file.txt', 'r', encoding='utf-8') as test_file:
    content = test_file.read()
    print(content)
