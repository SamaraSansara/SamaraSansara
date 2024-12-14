import sys
import tarfile
import time
from datetime import datetime

from fs_handler import VirtualFileSystem


class ShellEmulator:
    def __init__(self, username, fs, fs_archive, start_script):
        self.username = username
        self.fs = fs
        self.current_dir = '/'  # Начальная директория в виртуальной файловой системе
        self.virtual_files = {}  # Словарь для хранения "виртуальных" файлов и их содержимого
        self.file_timestamps = {}  # Словарь для хранения "временных меток" виртуальных файлов
        self.fs_path = fs_archive
        self.script_path = start_script
        self.start_time = time.time()

    def prompt(self):
        return f"{self.username}@emulator:{self.current_dir}$ "

    def execute_command(self, command):
        if command == "ls":
            return self.ls()
        elif command.startswith("cd "):
            directory = command.split(" ")[1]
            return self.cd(directory)
        elif command.startswith("uniq "):
            filename = command.split(" ")[1]
            return self.uniq(filename)
        elif command == "tree":
            return self.tree()
        elif command == "uptime":
            return self.uptime()
        elif command == "exit":
            self.exit()
        else:
            return f"Unknown command: {command}"

    def tree(self, path=None, indent=0, prefix=""):
        """
        Рекурсивно выводит структуру директорий и файлов в формате дерева.
        """
        path = self.current_dir if path is None else path
        output = ""
        current_path = path if path.endswith('/') else path + '/'

        # Получаем элементы текущего уровня (директории и файлы)
        items = [f[len(current_path):].split('/')[0] for f in self.fs.list_files() if f.startswith(current_path)]
        items = sorted(set(items))  # Убираем дубли и сортируем

        for index, item in enumerate(items):
            if "._" not in item:
                is_last = (index == len(items) - 1)
                branch = "└─ " if is_last else "├─ "
                output += prefix + branch + item + "\n"

                # Определяем полный путь для текущего элемента
                item_path = current_path + item
                if any(f.startswith(item_path + '/') for f in self.fs.list_files()):
                    # Если это директория, рекурсивно вызываем tree
                    new_prefix = prefix + ("   " if is_last else "│  ")
                    output += self.tree(item_path, indent + 1, new_prefix)
        return output

    def uptime(self):
        # Выводит время работы эмулятора и информацию о системе
        elapsed_time = time.time() - self.start_time
        hours, remainder = divmod(int(elapsed_time), 3600)
        minutes, seconds = divmod(remainder, 60)

        # Добавляем информацию о дате и времени запуска
        start_time = datetime.fromtimestamp(self.start_time).strftime("%Y-%m-%d %H:%M:%S")
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        return (
            f"Uptime: {hours}h {minutes}m {seconds}s\n"
            f"System started: {start_time}\n"
            f"Current time: {current_time}"
        )

    def uniq(self, filename):
        """
        Удаляет дублирующиеся строки в содержимом файла.
        Проверяет как "виртуальные" файлы, так и файлы из файловой системы.
        """
        file_path = (self.current_dir.rstrip('/') + '/' + filename).lstrip('/')

        # Проверяем в виртуальных файлах
        if file_path in self.virtual_files:
            content = self.virtual_files[file_path].splitlines()
        else:
            # Проверяем в файловой системе
            files = self.fs.list_files()
            if file_path in files:
                # Читаем содержимое файла из файловой системы
                content = self.fs.open_file(file_path).splitlines()
            else:
                return f"File not found: {filename}"

        # Убираем дубликаты строк, сохраняя порядок
        unique_lines = list(dict.fromkeys(content))
        return '\n'.join(unique_lines)

    def ls(self):
        # Список файлов в текущей директории виртуальной файловой системы, включая виртуальные файлы.
        files = self.fs.list_files()
        current_path = self.current_dir.lstrip('/') + '/' if self.current_dir != '/' else ''
        filtered_files = [f[len(current_path):] for f in files if f.startswith(current_path)]

        # Добавляем виртуальные файлы, созданные командой touch
        virtual_files_in_dir = [
            f[len(current_path):] for f in self.virtual_files.keys() if f.startswith(current_path)
        ]
        list_ls_current = []
        for file in filtered_files:
            if '/' in file:
                if file[:file.index('/')] not in list_ls_current and "._" not in file[:2]:
                    list_ls_current.append(file[:file.index('/')])
            else:
                if file not in list_ls_current and "._" not in file:
                    list_ls_current.append(file)
        for file in virtual_files_in_dir:
            if '/' in file:
                if file[:file.index('/')] not in list_ls_current:
                    list_ls_current.append(file[:file.index('/')])
            else:
                if file not in list_ls_current:
                    list_ls_current.append(file)

        # return '\n'.join(filtered_files + virtual_files_in_dir)
        return '\n'.join(list_ls_current)

    def cd(self, directory):
        # Переход в другую директорию (эмуляция).
        if directory == '/':
            self.current_dir = '/'
        elif directory == '..':
            # Переход в родительскую директорию
            if self.current_dir != '/':
                self.current_dir = '/'.join(self.current_dir.rstrip('/').split('/')[:-1]) or '/'
        else:
            # Определяем полный путь (абсолютный или относительный)
            if self.current_dir == '/' and len(self.current_dir) == 1:
                possible_path = self.current_dir.rstrip('/') + directory
            elif directory[0] == '/' and len(directory) != 1:
                #  possible_path = self.current_dir.rstrip('/')
                possible_path = directory[1:]
            else:
                possible_path = self.current_dir.rstrip('/') + '/' + directory

            # Проверка, существует ли директория в виртуальной файловой системе
            if any(f.startswith(possible_path + '/') or f == possible_path for f in self.fs.list_files()):
                self.current_dir = possible_path
            else:
                return f"Directory not found: {directory}, path - {possible_path}"
        return ""

    def exit(self):
        sys.exit(0)

    def execute_script(self, gui_output_callback=None):
        """
        Выполняет команды из стартового скрипта.
        Если предоставлен gui_output_callback, направляет вывод в GUI.
        """
        if self.script_path:
            try:
                with open(self.script_path, 'r') as script_file:
                    for line in script_file:
                        line = line.strip()  # Убираем лишние пробелы
                        if line:
                            result = self.execute_command(line)
                            # Если есть callback для вывода в GUI, используем его
                            if gui_output_callback:
                                gui_output_callback(f"{self.prompt()}{line}\n")
                                if result:
                                    gui_output_callback(f"{result}\n")
                            else:
                                print(f"Выполнение: {line}")
                                print(result)
            except FileNotFoundError:
                error_message = f"Ошибка: Файл стартового скрипта '{self.script_path}' не найден.\n"
                if gui_output_callback:
                    gui_output_callback(error_message)
                else:
                    print(error_message)
        else:
            error_message = "Непредоставлен стартовый скрипт.\n"
            if gui_output_callback:
                gui_output_callback(error_message)
            else:
                print(error_message)

