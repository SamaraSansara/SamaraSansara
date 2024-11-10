# Практическое задание №5. Системы контроля версий

П.Н. Советов, РТУ МИРЭА

Работа с Git.

## Задача 1

На сайте https://onlywei.github.io/explain-git-with-d3 или http://git-school.github.io/visualizing-git/ (цвета могут отличаться, есть команды undo/redo) с помощью команд эмулятора git получить следующее состояние проекта (сливаем master с first, перебазируем second на master): см. картинку ниже. Прислать свою картинку.
<img width="814" alt="Screenshot 2024-11-10 at 18 47 01" src="https://github.com/user-attachments/assets/0ffd999a-453a-4fa3-997e-617b203b3918">


Решение: 

<img width="893" alt="Screenshot 2024-11-10 at 19 04 59" src="https://github.com/user-attachments/assets/47b6f55c-76ce-46e4-ad75-27ac54a55cfb">




## Задача 2

Создать локальный git-репозиторий. Задать свои имя и почту (далее – coder1). Разместить файл prog.py с какими-нибудь данными. Прислать в текстовом виде диалог с git.

Решение: 


<img width="691" alt="Screenshot 2024-11-10 at 19 39 08" src="https://github.com/user-attachments/assets/21052b27-899f-4b2d-90b2-40983153d17b">
.....................................................................
<img width="766" alt="Screenshot 2024-11-10 at 19 40 16" src="https://github.com/user-attachments/assets/381b1cdf-99b8-454b-92df-bcc89c23fb35">
.....................................................................
<img width="771" alt="Screenshot 2024-11-10 at 19 40 27" src="https://github.com/user-attachments/assets/7b5eff38-410a-4c83-9c25-cf1c533bfb14">
.....................................................................
<img width="770" alt="Screenshot 2024-11-10 at 19 40 43" src="https://github.com/user-attachments/assets/f06e665d-2f54-4bf5-890a-d7b930ff3a03">
.....................................................................
<img width="779" alt="Screenshot 2024-11-10 at 19 40 59" src="https://github.com/user-attachments/assets/2b977fbe-cbf8-427d-b38e-4a61233c8b3b">
.....................................................................
<img width="265" alt="Screenshot 2024-11-10 at 19 41 07" src="https://github.com/user-attachments/assets/c5b6571f-dee1-4478-bf29-3c077ec3b3e5">
.....................................................................
<img width="580" alt="Screenshot 2024-11-10 at 19 41 24" src="https://github.com/user-attachments/assets/35e67969-aeff-421b-bdca-ffa8c27e8635">



## Задача 3

Создать рядом с локальным репозиторием bare-репозиторий с именем server. Загрузить туда содержимое локального репозитория. Команда git remote -v должна выдать информацию о server! Синхронизировать coder1 с server.

Клонировать репозиторий server в отдельной папке. Задать для работы с ним произвольные данные пользователя и почты (далее – coder2). Добавить файл readme.md с описанием программы. Обновить сервер.

Coder1 получает актуальные данные с сервера. Добавляет в readme в раздел об авторах свою информацию и обновляет сервер.

Coder2 добавляет в readme в раздел об авторах свою информацию и решает вопрос с конфликтами.

Прислать список набранных команд и содержимое git log.

Пример лога коммитов:

```
*   commit a457d748f0dab75b4c642e964172887de3ef4e3e
|\  Merge: 48ce283 d731ba8
| | Author: Coder 2 <coder2@corp.com>
| | Date:   Sun Oct 11 11:27:09 2020 +0300
| | 
| |     readme fix
| | 
| * commit d731ba84014d603384cc3287a8ea9062dbb92303
| | Author: Coder 1 <coder1@corp.com>
| | Date:   Sun Oct 11 11:22:52 2020 +0300
| | 
| |     coder 1 info
| | 
* | commit 48ce28336e6b3b983cbd6323500af8ec598626f1
|/  Author: Coder 2 <coder2@corp.com>
|   Date:   Sun Oct 11 11:24:00 2020 +0300
|   
|       coder 2 info
| 
* commit ba9dfe9cb24316694808a347e8c36f8383d81bbe
| Author: Coder 2 <coder2@corp.com>
| Date:   Sun Oct 11 11:21:26 2020 +0300
| 
|     docs
| 
* commit 227d84c89e60e09eebbce6c0b94b41004a4541a4
  Author: Coder 1 <coder1@corp.com>
  Date:   Sun Oct 11 11:11:46 2020 +0300
  
      first commit
```

Решение: 

.....................................................................
<img width="663" alt="Screenshot 2024-11-10 at 21 59 22" src="https://github.com/user-attachments/assets/542e903a-05d3-41d3-aa48-23c3af01e804">
.....................................................................
<img width="665" alt="Screenshot 2024-11-10 at 21 59 39" src="https://github.com/user-attachments/assets/be47c4dc-ed85-4783-abbc-a97b3aaabc87">


## Задача 4

Написать программу на Питоне (или другом ЯП), которая выводит список содержимого всех объектов репозитория. Воспользоваться командой "git cat-file -p". Идеальное решение – не использовать иных сторонних команд и библиотек для работы с git.

## Полезные ссылки

Git

Учебник (рус.): https://git-scm.com/book/ru/v2

Шпаргалка (рус.): https://training.github.com/downloads/ru/github-git-cheat-sheet/

Официальная документация: https://git-scm.com/docs

Эксцентричный доклад Л. Торвальдса о Git: https://www.youtube.com/watch?v=4XpnKHJAok8

Дерево Меркла: http://cryptowiki.net/index.php?title=Дерево_Merkle

Git for Windows: https://git-scm.com/download/win

Репозиторий chibicc: https://github.com/rui314/chibicc.git

Игра по git: https://learngitbranching.js.org/?locale=ru_RU

SHA-1

Описание алгоритма: https://ru.wikipedia.org/wiki/SHA-1

Вероятность хеш-коллизии: https://preshing.com/20110504/hash-collision-probabilities/

https://ru.m.wikipedia.org/wiki/Парадокс_дней_рождения

https://security.googleblog.com/2017/02/announcing-first-sha1-collision.html
