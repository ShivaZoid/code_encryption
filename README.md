# Данный код представляет собой простое консольное приложение для шифрования и расшифровки файлов с помощью алгоритма симметричного шифрования AES с использованием библиотеки [cryptography](https://pypi.org/project/cryptography/).

## Основные функции:

### Генерация ключа

~~~
Функция generate_key() генерирует ключ шифрования и сохраняет его в файл key.key.
~~~

### Загрузка ключа

~~~
Функция load_key() загружает ключ шифрования из файла key.key. 
~~~

### Шифрование файла

~~~
Функция encrypt_file() шифрует содержимое файла, используя ключ key, 
и сохраняет результат в новом файле output_file. 
~~~

### Расшифровка файла
~~~
Функция decrypt_file() расшифровывает содержимое файла, используя ключ key, 
и сохраняет результат в новом файле output_file. 
~~~

### Использование
~~~
Функция main() позволяет пользователю выбрать режим работы программы: 
шифрование или расшифровка файла. 
---------------------------------------------------------------------------------
Пользователь может ввести "e" для шифрования файла или "d" для расшифровки файла. 
---------------------------------------------------------------------------------
Если пользователь вводит "q", программа завершается. 
---------------------------------------------------------------------------------
Пользователь также должен ввести имя файла для шифрования или расшифровки, 
а также имя файла для сохранения результата. 
---------------------------------------------------------------------------------
Если файл с таким именем уже существует, программа спросит, 
хочет ли пользователь перезаписать файл.
~~~

### Для запуска приложения, проделайте следующие шаги:

1) Склонируйте репозиторий.

2) Перейдите в папку с кодом и создайте виртуальное окружение:
~~~
python -m venv venv
~~~

3) Активируйте виртуальное окружение:
~~~
source venv/Scripts/activate
~~~

4) Установите зависимости:
~~~
python -m pip install -r requirements.txt
~~~

5) Запуск программы:
~~~
python main.py
~~~
