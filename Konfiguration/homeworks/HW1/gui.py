import tkinter as tk
from tkinter import scrolledtext
from shell import ShellEmulator
from fs_handler import VirtualFileSystem

class ShellGUI:
    def __init__(self, shell):
        self.shell = shell
        self.root = tk.Tk()
        self.root.title("Shell Emulator")
        self.root.configure(bg="white")

        # Настройка текстового вывода
        self.text_output = scrolledtext.ScrolledText(
            self.root,
            bg="white",
            fg="black",
            insertbackground="white",
            font=("Consolas", 12),
            wrap=tk.WORD,
        )
        self.text_output.pack(fill=tk.BOTH, expand=True, padx=10, pady=(10, 5))

        # Поле ввода команды
        self.entry_input = tk.Entry(
            self.root,
            bg="white",
            fg="black",
            insertbackground="white",
            font=("Consolas", 12),
        )
        self.entry_input.pack(fill=tk.X, padx=10, pady=(0, 5))
        self.entry_input.bind("<Return>", self.process_command)

        # Удаляем вызов выполнения стартового скрипта
        # Если хотите выполнить его в будущем, оставьте комментарий
        # self.shell.execute_script(self.add_output)

    def process_command(self, event):
        command = self.entry_input.get()
        self.entry_input.delete(0, tk.END)
        self.add_output(f"{self.shell.prompt()}{command}\n")
        output = self.shell.execute_command(command)
        if output:
            self.add_output(f"{output}\n")

    def add_output(self, text):
        """Добавляет текст в поле вывода GUI."""
        self.text_output.insert(tk.END, text)
        self.text_output.see(tk.END)  # Прокрутка вниз

    def clear_output(self):
        self.text_output.delete("1.0", tk.END)

    def start(self):
        self.root.mainloop()
def run_gui(username, fs, fs_archive, start_script):
    shell = ShellEmulator(username, fs, fs_archive, start_script)
    gui = ShellGUI(shell)
    gui.start()




