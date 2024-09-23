# Практическое занятие №1. Введение, основы работы в командной строке

П.Н. Советов, РТУ МИРЭА

Научиться выполнять простые действия с файлами и каталогами в Linux из командной строки. Сравнить работу в командной строке Windows и Linux.

## Задача 1

Вывести отсортированный в алфавитном порядке список имен пользователей в файле passwd (вам понадобится grep).

<img width="663" alt="Screenshot 2024-09-23 at 09 30 26" src="https://github.com/user-attachments/assets/ff99f846-f075-435c-bd65-a2d0db7fc73a">


## Задача 2

Вывести данные /etc/protocols в отформатированном и отсортированном порядке для 5 наибольших портов, как показано в примере ниже:

```
[root@localhost etc]# cat /etc/protocols ...
142 rohc
141 wesp
140 shim6
139 hip
138 manet
```

<img width="1034" alt="Screenshot 2024-09-23 at 09 33 25" src="https://github.com/user-attachments/assets/02ad2631-ba96-4d2d-9418-108a43d88d57">


## Задача 3

Написать программу banner средствами bash для вывода текстов, как в следующем примере (размер баннера должен меняться!):

```
[root@localhost ~]# ./banner "Hello from RTU MIREA!"
+-----------------------+
| Hello from RTU MIREA! |
+-----------------------+
```
<img width="598" alt="Screenshot 2024-09-23 at 09 36 36" src="https://github.com/user-attachments/assets/1b91e2af-b176-4305-bf9f-a7def6a6129e">

<img width="612" alt="Screenshot 2024-09-23 at 09 37 16" src="https://github.com/user-attachments/assets/fddacf6b-d48b-48bd-bf02-0907f0e38b2e">

Перед отправкой решения проверьте его в ShellCheck на предупреждения.

## Задача 4

Написать программу для вывода всех идентификаторов (по правилам C/C++ или Java) в файле (без повторений).

Пример для hello.c:

```
h hello include int main n printf return stdio void world
```

<img width="763" alt="Screenshot 2024-09-23 at 09 38 03" src="https://github.com/user-attachments/assets/7e7d144f-4117-4986-ac41-c7c0fd819b09">

<img width="903" alt="Screenshot 2024-09-23 at 09 38 28" src="https://github.com/user-attachments/assets/a6905e8e-eeb2-4f65-843d-d225e04f2c4c">

<img width="599" alt="Screenshot 2024-09-23 at 09 38 49" src="https://github.com/user-attachments/assets/a0f0ab86-32be-4c51-88be-6ea7a5ad58f2">


## Задача 5

Написать программу для регистрации пользовательской команды (правильные права доступа и копирование в /usr/local/bin).

Например, пусть программа называется reg:

```
./reg banner
```

В результате для banner задаются правильные права доступа и сам banner копируется в /usr/local/bin.

<img width="508" alt="Screenshot 2024-09-23 at 09 39 31" src="https://github.com/user-attachments/assets/432ea7a8-863a-4088-97e0-1a4755db471f">

<img width="513" alt="Screenshot 2024-09-23 at 09 40 07" src="https://github.com/user-attachments/assets/7d9ec380-be37-47a1-9d1e-8d8f26f25754">

<img width="531" alt="Screenshot 2024-09-23 at 09 40 29" src="https://github.com/user-attachments/assets/93088c36-ebef-463b-9dad-9ee5b7786194">

<img width="693" alt="Screenshot 2024-09-23 at 09 41 12" src="https://github.com/user-attachments/assets/cd5607bb-2d7e-4a9a-ab90-acc71f688c70">


## Задача 6

Написать программу для проверки наличия комментария в первой строке файлов с расширением c, js и py.

<img width="733" alt="Screenshot 2024-09-23 at 09 41 36" src="https://github.com/user-attachments/assets/0e77fa5d-ffee-4a16-acb6-87b50ae47af2">

<img width="260" alt="Screenshot 2024-09-23 at 09 41 57" src="https://github.com/user-attachments/assets/3ef53816-dc2b-46c8-9761-dcb91b8fe77f">

<img width="384" alt="Screenshot 2024-09-23 at 09 42 21" src="https://github.com/user-attachments/assets/bf08fcb1-bc63-469b-a7e1-309914a7cce0">


<img width="691" alt="Screenshot 2024-09-23 at 09 42 39" src="https://github.com/user-attachments/assets/3c175af1-af33-43f5-a3db-a05e20ef4703">

<img width="753" alt="Screenshot 2024-09-23 at 09 43 18" src="https://github.com/user-attachments/assets/183c79e9-f871-4016-aec3-f0c35c8776f4">

<img width="758" alt="Screenshot 2024-09-23 at 09 43 45" src="https://github.com/user-attachments/assets/7c649f45-2fbe-4062-85c9-643f1f1e696b">

<img width="675" alt="Screenshot 2024-09-23 at 09 44 14" src="https://github.com/user-attachments/assets/ee134ceb-ca5b-4a8c-9dc4-1943cb3c060d">

<img width="528" alt="Screenshot 2024-09-23 at 09 44 44" src="https://github.com/user-attachments/assets/65348373-98d7-4cb6-b40f-335f71a8d876">

<img width="402" alt="Screenshot 2024-09-23 at 09 45 19" src="https://github.com/user-attachments/assets/18ade100-c18c-4e06-a3df-263258fb7d0c">



## Задача 7

Написать программу для нахождения файлов-дубликатов (имеющих 1 или более копий содержимого) по заданному пути (и подкаталогам).

<img width="506" alt="Screenshot 2024-09-23 at 09 46 43" src="https://github.com/user-attachments/assets/f1b605d7-dc04-405d-9b3a-57a224393453">

<img width="435" alt="Screenshot 2024-09-23 at 09 49 24" src="https://github.com/user-attachments/assets/252e974a-364f-482a-8f19-43521daa5a20">

<img width="486" alt="Screenshot 2024-09-23 at 09 49 34" src="https://github.com/user-attachments/assets/ff696e89-87ee-4791-8c33-80179b1fa2c8">

<img width="513" alt="Screenshot 2024-09-23 at 09 47 11" src="https://github.com/user-attachments/assets/5862e474-fec9-45ff-8b68-b15611a420ed">

<img width="536" alt="Screenshot 2024-09-23 at 09 47 33" src="https://github.com/user-attachments/assets/0ca3be26-6f5f-49d5-845d-d8322d36817a">

<img width="599" alt="Screenshot 2024-09-23 at 09 47 56" src="https://github.com/user-attachments/assets/7ad9cd2a-3e76-4609-9b6c-d32f288217ab">


## Задача 8

Написать программу, которая находит все файлы в данном каталоге с расширением, указанным в качестве аргумента и архивирует все эти файлы в архив tar.

<img width="678" alt="Screenshot 2024-09-23 at 09 50 38" src="https://github.com/user-attachments/assets/43b8a03b-001b-49fb-8462-37bda8e57969">

<img width="652" alt="Screenshot 2024-09-23 at 09 51 13" src="https://github.com/user-attachments/assets/fa4b4ce4-ce7d-48e2-922e-487950d85f0f">

<img width="497" alt="Screenshot 2024-09-23 at 09 51 47" src="https://github.com/user-attachments/assets/af6eb9d4-f8bf-4a70-85e3-e089fd1348b3">

<img width="645" alt="Screenshot 2024-09-23 at 09 52 27" src="https://github.com/user-attachments/assets/e406b24b-aed7-4354-b7b4-6a0819162c70">

<img width="665" alt="Screenshot 2024-09-23 at 09 52 54" src="https://github.com/user-attachments/assets/6b607c0d-a612-4354-a335-6d97806bcacd">


## Задача 9

Написать программу, которая заменяет в файле последовательности из 4 пробелов на символ табуляции. Входной и выходной файлы задаются аргументами.

<img width="538" alt="Screenshot 2024-09-23 at 09 54 10" src="https://github.com/user-attachments/assets/df34be81-7e94-4b12-a21d-627f525a24b2">

<img width="407" alt="Screenshot 2024-09-23 at 09 54 32" src="https://github.com/user-attachments/assets/87d7a9d1-3812-4e9c-b471-9a4989b9c047">

<img width="407" alt="Screenshot 2024-09-23 at 09 55 05" src="https://github.com/user-attachments/assets/939379c6-a6e6-4f67-bf57-fd22f9d04d2f">

<img width="558" alt="Screenshot 2024-09-23 at 09 55 28" src="https://github.com/user-attachments/assets/442bd605-b339-4009-853e-23ce53bfb830">


## Задача 10

Написать программу, которая выводит названия всех пустых текстовых файлов в указанной директории. Директория передается в программу параметром. 

<img width="820" alt="Screenshot 2024-09-23 at 09 56 00" src="https://github.com/user-attachments/assets/fcce7361-05b5-479d-9bdf-77ce6f58dfe6">

<img width="562" alt="Screenshot 2024-09-23 at 09 56 28" src="https://github.com/user-attachments/assets/b1b30605-5f54-4c56-97a8-f3c0b6f14098">


## Полезные ссылки

Линукс в браузере: https://bellard.org/jslinux/

ShellCheck: https://www.shellcheck.net/

Разработка CLI-приложений

Общие сведения

https://ru.wikipedia.org/wiki/Интерфейс_командной_строки
https://nullprogram.com/blog/2020/08/01/
https://habr.com/ru/post/150950/

Стандарты

https://www.gnu.org/prep/standards/standards.html#Command_002dLine-Interfaces
https://www.gnu.org/software/libc/manual/html_node/Argument-Syntax.html
https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap12.html

Реализация разбора опций

Питон

https://docs.python.org/3/library/argparse.html#module-argparse
https://click.palletsprojects.com/en/7.x/
