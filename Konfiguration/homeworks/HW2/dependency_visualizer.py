import argparse #Для обработки аргументов командной строки.
import subprocess #Для выполнения внешних команд, таких как git и mermaid-cli
import os
import tempfile
import shutil #Для работы с файловой системой и временными файлами
from datetime import datetime #Для обработки временных данных (на будущее)
import xml.etree.ElementTree as ET #Для разбора XML-файла конфигурации

def get_commit_data(repo_path):
    """
    Извлекает данные о коммитах из git-репозитория.
    Возвращает список словарей с информацией о коммитах.
    """
    log_cmd = [
        "git", "-C", repo_path, "log", "--all",
        "--pretty=format:%H|%P|%an|%ad|%s", "--date=iso"
    ]
    result = subprocess.run(log_cmd, capture_output=True, text=True, check=True)

    commits = []
    for line in result.stdout.splitlines():
        if "|" in line:
            commit_id, parents, author, date, message = (line.split("|") + [""])[:5]
            parents = parents.split() if parents else []
            commits.append({
                "id": commit_id,
                "parents": parents,
                "author": author,
                "date": date,
                "message": message.strip()
            })

    return commits



#Начинается создание Mermaid-графа. 
#Mermaid использует синтаксис для представления связей в стиле "от узла к узлу".
def generate_mermaid_graph(commits):
    """
    Создает Mermaid-описание графа зависимостей для коммитов.
    """
    graph = ["graph TD"]
    for commit in commits:
        sanitized_message = commit["message"].replace('"', "'").replace("<", "&lt;").replace(">", "&gt;")
        node_label = (
            f"Commit: {commit['id']}<br>"
            f"Author: {commit['author']}<br>"
            f"Date: {commit['date']}<br>"
            f"Message: {sanitized_message}"
        )
        #Действие: Каждый коммит представляется узлом графа с информацией:
        #ID коммита.
        #Автор.
        #Дата.
        #Сообщение (очищается от потенциально некорректных символов).
        graph.append(f'{commit["id"]}["{node_label}"]')

        for parent in commit["parents"]:
            graph.append(f"{parent} --> {commit['id']}")
            #Создаются ребра (связи) между родительскими коммитами и текущим.


    return "\n".join(graph)


#Эта функция сохраняет Mermaid-граф в файл PNG.
def save_mermaid_graph(mermaid_code, mermaid_cli, output_path):
    """
    Сохраняет Mermaid-граф в файл PNG.
    """
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mmd") as temp_file:
        temp_file.write(mermaid_code.encode("utf-8"))
        temp_file_path = temp_file.name
    #Mermaid-код временно записывается в .mmd-файл. Этот файл позже используется Mermaid CLI.

    try:
        cmd = [mermaid_cli, "-i", temp_file_path, "-o", output_path]
        print(f"Running command: {' '.join(cmd)}")  # Лог команды перед вызовом
        subprocess.run(cmd, check=True)
        #Команда запускает mermaid-cli, чтобы преобразовать .mmd-файл в PNG.
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при выполнении команды Mermaid CLI: {e}")
        raise  # Повторно бросаем ошибку для сохранения поведения
    finally:
        os.remove(temp_file_path)

def load_config(config_file):
    tree = ET.parse(config_file)
    root = tree.getroot()
    print("Parsed config XML:")
    print(ET.tostring(root, encoding='unicode'))

    return {
        "mermaid_path": root.find("mermaidPath").text.strip(),
        "repo_path": root.find("repoPath").text.strip(),
        "output_path": root.find("outputPath").text.strip(),
    }

def main():
    parser = argparse.ArgumentParser(description="Визуализация графа зависимостей для git-репозитория.")
    parser.add_argument("--config", required=True, help="Путь к XML-файлу конфигурации.")
    args = parser.parse_args()

    # Чтение конфигурации
    config = load_config(args.config)
    mermaid_cli = config["mermaid_path"]
    repo_path = config["repo_path"]
    output_path = config["output_path"]

    if not shutil.which(mermaid_cli):
        raise FileNotFoundError(
            f"Mermaid CLI не найден по указанному пути {mermaid_cli}. "
            "Проверьте, установлен ли Mermaid CLI (npm install -g @mermaid-js/mermaid-cli) и добавлен ли он в PATH."
    )

    # Работа с репозиторием
    if not os.path.exists(os.path.join(repo_path, '.git')):
        raise ValueError(f"Папка {repo_path} существует, но не является git-репозиторием (нет .git).")
    # Построение графа зависимостей
    commits = get_commit_data(repo_path)
    mermaid_code = generate_mermaid_graph(commits)
    print("Mermaid-граф успешно сгенерирован.")

    # Сохранение графа в PNG
    save_mermaid_graph(mermaid_code, mermaid_cli, output_path)
    print(f"Граф зависимостей сохранен в {output_path}.")

if __name__ == "__main__":
    main()
