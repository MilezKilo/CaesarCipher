# Шифр Цезаря — древний алгоритм шифрования, использовавшийся Юлием Цезарем.
# Буквы в нем шифруются путем сдвига их на определенное количество позиций в алфавите.
# Дистанция сдвига называется ключом. Например, если ключ равен 3, то A превращается в D, B — в E, C — в F и т. д.
# Для расшифровки сообщения необходимо выполнить сдвиг зашифрованных символов в противоположном направлении.
# Данная программа позволяет шифровать и расшифровывать сообщения в соответствии с приведенным алгоритмом.
# Узнать больше о шифре Цезаря можно в статье «Википедии»: https://ru.wikipedia.org/wiki/Шифр_Цезаря.
# Вашей задачей является написание 2х программ – программу-шифратор и программу-дешифратор.

# Шифрование сообщения:

# Программа в действии
# Результат выполнения caesarcipher.py выглядит следующим образом:
# Caesar Cipher, by Al Sweigart al@inventwithpython.com
# Do you want to (e)ncrypt or (d)ecrypt?
# >>e
# Please enter the key (0 to 25) to use.
# >> 4
# Enter the message to encrypt.
# >> Meet me by the rose bushes tonight.
# QIIX QI FC XLI VSWI FYWLIW XSRMKLX.
# Full encrypted text copied to clipboard.
# Do you want to (e)ncrypt or (d)ecrypt?
# >>d
# Please enter the key (0 to 26) to use.
# >>4
# Enter the message to decrypt.
# >> QIIX QI FC XLI VSWI FYWLIW XSRMKLX.
# MEET ME BY THE ROSE BUSHES TONIGHT.
# Full decrypted text copied to clipboard.

# Описание работы
# Подобно большинству программ шифрования, шифр Цезаря преобразует буквы в числа,
# производит над ними определенные математические операции и преобразует их обратно в буквы текста.
# В контексте шифрования мы будем называть элементы текста символами.
# Символы могут быть буквами, цифрами и знаками препинания, каждому из которых соответствует уникальное целочисленное значение.
# В случае программы для шифра Цезаря все символы представляют собой буквы,
# а целочисленные значения — их позиции в строке SYMBOLS: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.


# Взлом шифра Цезаря
# Эта программа способна взламывать сообщения, зашифрованные с помощью шифра Цезаря из проекта 6, даже если ключ неизвестен.
# Существует всего 26 возможных ключей для шифра Цезаря, так что компьютер
# может легко перебрать все возможные расшифровки и отобразить пользователю результаты.
# В криптографии подобная методика называется атакой методом подбора (brute-force attack).
# Если вам интересно узнать больше о шифрах и их взломе, то можете прочитать мою книгу Cracking Codes with Python1
# Программа в действии
# Результат выполнения caesarhacker.py выглядит следующим образом:
# Enter the encrypted Caesar cipher message to hack.
# QIIX QI FC XLI VSWI FYWLIW XSRMKLX.
# Key #0: QIIX QI FC XLI VSWI FYWLIW XSRMKLX.
# Key #1: PHHW PH EB WKH URVH EXVKHV WRQLJKW.
# Key #2: OGGV OG DA VJG TQUG DWUJGU VQPKIJV.
# Key #3: NFFU NF CZ UIF SPTF CVTIFT UPOJHIU.
# Key #4: MEET ME BY THE ROSE BUSHES TONIGHT.
# Key #5: LDDS LD AX SGD QNRD ATRGDR SNMHFGS.
# Key #6: KCCR KC ZW RFC PMQC ZSQFCQ RMLGEFR.
# --сокращено--

maxSizeOfKey = 26


def getTypeOfProgram():  # Метод ввода типа программы.
    while True:
        print('Do you wish to (e)ncrypt or (d)ecrypt or (b)rute force a message?')
        mode = input().lower()
        if mode in 'encrypt e decrypt d brute b'.split():
            return mode
        else:
            print('Enter either "encrypt" or "e" or "decrypt" or "d" or "brute" or "b".')


def getKeyLenght():  # Метод вывода в консоль вопроса о длине ключа шифрования/дешифрования.
    while True:
        print('Enter the key number (1-%s)' % maxSizeOfKey)
        key = int(input())
        if 1 <= key <= maxSizeOfKey:
            return key


def getMessage():  # Метод вывода в консоль вопроса о тексте для шифрования/дешифрования.
    print('Enter your message:')
    return input()


typeOfProgram = getTypeOfProgram()  # Ввод типа программы.
keyLenght = 0  # Создание ключа шифрования
if typeOfProgram != 'b':
    keyLenght = getKeyLenght()  # Ввод длины ключа шифрования/дешифрования.
if typeOfProgram == 'd':
    keyLenght = -keyLenght
inputMessage = getMessage()  # Ввод текста для шифрования/дешифрования.


def caesarCipher(message):
    endMessageInFunc = ''
    for i in list(message.upper()):
        if i.isalpha():
            endMessageInFunc += chr((ord(i) + keyLenght - 64) % 26 + 64)
        else:
            endMessageInFunc += i

    return endMessageInFunc


endMessage = caesarCipher(inputMessage)  # Итогового сообщения.


if typeOfProgram != 'b':
    print(endMessage)
    if typeOfProgram == 'e':
        print('Full encrypted text copied to clipboard.')
    elif typeOfProgram == 'd':
        print('Full decrypted text copied to clipboard.')
else:
    for keyLenght in range(1, maxSizeOfKey + 1):
        print(keyLenght, caesarCipher(inputMessage))
