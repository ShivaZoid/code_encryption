import os

from cryptography.fernet import Fernet


def generate_key():
    """
    Генерирует ключ шифрования и сохраняет его в файл.
    """
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)


def load_key():
    """
    Загружает ключ шифрования из файла.
    """
    if os.path.exists('key.key'):
        with open('key.key', 'rb') as key_file:
            key = key_file.read()
        return key
    else:
        print('Ключ шифрования не найден. Перезапустите программу.')
        exit()


def encrypt_file(key, input_file, output_file):
    """
    Шифрует содержимое файла с использованием ключа
    и сохраняет результат в новом файле.
    """
    try:
        with open(input_file, 'rb') as f:
            plaintext = f.read()
    except FileNotFoundError:
        print(f'Файл "{input_file}" не найден.')
        return
    except PermissionError:
        print(f'Произошла ошибка при чтении файла.'
              f'Отказано в доступе к файлу "{input_file}"')
        return

    fernet = Fernet(key)
    ciphertext = fernet.encrypt(plaintext)

    try:
        with open(output_file, 'wb') as f:
            f.write(ciphertext)
    except PermissionError:
        print(f'Произошла ошибка при записи зашифрованного файла.'
              f'Отказано в доступе к файлу "{output_file}"')
        return


def decrypt_file(key, input_file, output_file):
    """
    Расшифровывает содержимое файла с использованием ключа
    и сохраняет результат в новом файле.
    """
    try:
        with open(input_file, 'rb') as f:
            ciphertext = f.read()
    except FileNotFoundError:
        print(f'Файл "{input_file}" не найден.')
        return
    except PermissionError:
        print(f'Произошла ошибка при чтении файла.'
              f'Отказано в доступе к файлу "{input_file}"')
        return

    fernet = Fernet(key)

    try:
        plaintext = fernet.decrypt(ciphertext)
    except Fernet.InvalidToken:
        print('Неверный ключ шифрования. Файл не может быть расшифрован.')
        return

    try:
        with open(output_file, 'wb') as f:
            f.write(plaintext)
    except PermissionError:
        print('Произошла ошибка при записи расшифрованного файла.'
              f'Отказано в доступе к файлу "{output_file}"')
        return


def main():
    try:
        if not os.path.exists('key.key'):
            generate_key()

        while True:
            mode = input('Хотите зашифровать (e) или дешифровать (d) файл? '
                         '(q) для выхода.')
            if mode not in ['e', 'd', 'q']:
                raise ValueError('Некорректный режим работы. '
                                 'Введите (e) или (d).')
            if mode == 'q':
                print('Выход из программы...')
                break

            filename = input('Введите имя файла: ')
            if filename == 'q':
                print('Выход из программы...')
                break
            if not os.path.exists(filename):
                raise FileNotFoundError(f'Файл "{filename}" не найден.')

            key = load_key()

            output_file = input('Введите имя выходного файла: ')
            if output_file == 'q':
                print('Выход из программы...')
                break
            if os.path.exists(output_file):
                overwrite = input(f'Файл "{output_file}" уже существует.'
                                'Перезаписать? (y/n)')
                if overwrite.lower() != 'y':
                    print('Операция отменена пользователем.')
                    return

            if mode == 'e':
                encrypt_file(key, filename, output_file)
                print('Файл успешно зашифрован!')
            elif mode == 'd':
                decrypt_file(key, filename, output_file)
                print('Файл успешно расшифрован!')
    except FileNotFoundError as error:
        print(f"Произошла ошибка: {error}")
    except ValueError as error:
        print(f"Произошла ошибка: {error}")
    except Exception as error:
        print(f"Произошла непредвиденная ошибка: {error}")


if __name__ == '__main__':
    main()
