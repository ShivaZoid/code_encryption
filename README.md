# Данный код представляет собой простое консольное приложение для шифрования и расшифровки файлов с помощью алгоритма симметричного шифрования AES с использованием библиотеки [cryptography](https://pypi.org/project/cryptography/).

## Основные функции:

### Генерация ключа

~~~
Функция generate_key() генерирует ключ шифрования и сохраняет его в файл key.key.
~~~

### Загрузка ключа

~~~
Функция load_key() загружает ключ шифрования из файла key.key. 
Если файл не найден, пользователю будет выведено сообщение о том, что ключ шифрования не найден, и программа будет завершена.
~~~

### Шифрование файла

~~~
Функция encrypt_file() шифрует содержимое файла, используя ключ key, и сохраняет результат в новом файле output_file. 
Если файл input_file не найден или отсутствует доступ к файлу, пользователю будет выведено сообщение об ошибке.
~~~

### Расшифровка файла
~~~
Функция decrypt_file() расшифровывает содержимое файла, используя ключ key, и сохраняет результат в новом файле output_file. 
Если файл input_file не найден или отсутствует доступ к файлу, пользователю будет выведено сообщение об ошибке. 
Если ключ шифрования неверный, пользователю будет выведено сообщение о том, что файл не может быть расшифрован.
~~~

### Использование
~~~
Функция main() позволяет пользователю выбрать режим работы программы: шифрование или расшифровка файла. 
Пользователь может ввести "e" для шифрования файла или "d" для расшифровки файла. 
Если пользователь вводит "q", программа завершается. 
Пользователь также должен ввести имя файла для шифрования или расшифровки, а также имя файла для сохранения результата. 
Если файл с таким именем уже существует, программа спросит, хочет ли пользователь перезаписать файл.
~~~
