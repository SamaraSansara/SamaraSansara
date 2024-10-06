# Практическое занятие №2. Менеджеры пакетов

П.Н. Советов, РТУ МИРЭА

Разобраться, что представляет собой менеджер пакетов, как устроен пакет, как читать версии стандарта semver. Привести примеры программ, в которых имеется встроенный пакетный менеджер.

## Задача 1

Вывести служебную информацию о пакете matplotlib (Python). Разобрать основные элементы содержимого файла со служебной информацией из пакета. Как получить пакет без менеджера пакетов, прямо из репозитория?


```
pip install matplotlib
pip show matplotlib
```

![практика1 1](https://github.com/user-attachments/assets/d746fb6b-420a-48ee-af6c-f3026b0f2490)
![практика1 2](https://github.com/user-attachments/assets/9986a590-54b8-4092-a112-94b6a889d05b)
![практика1 3](https://github.com/user-attachments/assets/8ec611d7-a09a-4fad-ab0e-fb91d8af32a7)
![практика1 4](https://github.com/user-attachments/assets/c4110a33-d868-4bd0-b719-8aa8663601fd)


## Задача 2

Вывести служебную информацию о пакете express (JavaScript). Разобрать основные элементы содержимого файла со служебной информацией из пакета. Как получить пакет без менеджера пакетов, прямо из репозитория?

```
git clone https://github.com/expressjs/express.git
cd express
cat package.json
```
![изображение](https://github.com/user-attachments/assets/17f15b5f-96fe-4c67-ab23-a69cd0e92043)

## Задача 3

Сформировать graphviz-код и получить изображения зависимостей matplotlib и express.

 ```bash
  dot -Tpng express_dependencies.dot -o express_dependencies.png
  dot -Tpng matplotlib_dependencies.dot -o matplotlib_dependencies.png
```

  ![image](https://github.com/user-attachments/assets/ea544ab2-652f-410e-93d3-134acf82f304)
  ![image](https://github.com/user-attachments/assets/4143d6b5-76fb-4683-877f-6c8f738dfe2f)
  ![express_dependencies](https://github.com/user-attachments/assets/01837661-91c1-4ace-af58-6602f6140ae9)
  ![matplotlib_dependencies](https://github.com/user-attachments/assets/a8c99236-818a-4be8-9c90-772eb0007a50)

## Задача 4

**Следующие задачи можно решать с помощью инструментов на выбор:**

* Решатель задачи удовлетворения ограничениям (MiniZinc).
* SAT-решатель (MiniSAT).
* SMT-решатель (Z3).

Изучить основы программирования в ограничениях. Установить MiniZinc, разобраться с основами его синтаксиса и работы в IDE.

Решить на MiniZinc задачу о счастливых билетах. Добавить ограничение на то, что все цифры билета должны быть различными (подсказка: используйте all_different). Найти минимальное решение для суммы 3 цифр.

  
```minizinc
  include "alldifferent.mzn";  % Подключаем библиотеку для alldifferent

  % Определяем массив для хранения 6 цифр билета
  array[1..6] of var 0..9: digits;
  
  % Ограничение: все цифры должны быть различными
  constraint alldifferent(digits);
  
  % Ограничение: сумма первых трёх цифр должна равняться сумме последних трёх
  constraint sum(digits[1..3]) = sum(digits[4..6]);
  
  % Целевая функция: минимизируем сумму первых трёх цифр
  solve minimize sum(digits[1..3]);
  
  % Выводим результат
  output [
      "Digits: ", show(digits), 
      "\nSum of first 3 digits: ", show(sum(digits[1..3])), 
      "\nSum of last 3 digits: ", show(sum(digits[4..6]))
  ];
```

  ![Снимок экрана 2024-09-22 214850](https://github.com/user-attachments/assets/5b4ab1ef-1238-47aa-8c17-3f6a9ae03118)
  ![Снимок экрана 2024-09-22 214931](https://github.com/user-attachments/assets/9923e75c-83c8-4736-bb04-6b51e5803d12)


## Задача 5

Решить на MiniZinc задачу о зависимостях пакетов для рисунка, приведенного ниже.

![](images/pubgrub.png)

```minizinc
  % Определяем пакеты
  enum PACKAGES = {
      root, 
      menu_1_0_0, menu_1_1_0, menu_1_2_0, menu_1_3_0, menu_1_4_0, menu_1_5_0, 
      dropdown_2_0_0, dropdown_2_1_0, dropdown_2_2_0, dropdown_2_3_0, dropdown_1_8_0,
      icons_1_0_0, icons_2_0_0
  };
  
  % Переменные, указывающие, установлен ли пакет (1) или нет (0)
  array[PACKAGES] of var 0..1: installed;
  
  % Обязательно устанавливаем root
  constraint
      installed[root] == 1;
  
  % Ограничения зависимостей
  constraint
      (installed[root] == 1) -> (installed[menu_1_0_0] == 1 /\ installed[menu_1_5_0] == 1 /\ installed[icons_1_0_0] == 1) /\
      (installed[menu_1_5_0] == 1) -> (installed[dropdown_2_3_0] == 1 /\ installed[dropdown_2_0_0] == 1) /\
      (installed[menu_1_4_0] == 1) -> (installed[dropdown_2_3_0] == 1 /\ installed[dropdown_2_0_0] == 1) /\
      (installed[menu_1_3_0] == 1) -> (installed[dropdown_2_3_0] == 1 /\ installed[dropdown_2_0_0] == 1) /\
      (installed[menu_1_2_0] == 1) -> (installed[dropdown_2_3_0] == 1 /\ installed[dropdown_2_0_0] == 1) /\
      (installed[menu_1_1_0] == 1) -> (installed[dropdown_2_3_0] == 1 /\ installed[dropdown_2_0_0] == 1) /\
      (installed[menu_1_0_0] == 1) -> (installed[dropdown_1_8_0] == 1) /\
      (installed[dropdown_2_0_0] == 1) -> (installed[icons_2_0_0] == 1) /\
      (installed[dropdown_2_1_0] == 1) -> (installed[icons_2_0_0] == 1) /\
      (installed[dropdown_2_2_0] == 1) -> (installed[icons_2_0_0] == 1) /\
      (installed[dropdown_2_3_0] == 1) -> (installed[icons_2_0_0] == 1);
  
  % Целевая функция: минимизируем количество установленных пакетов
  solve minimize sum(installed);
  
  % Выводим результат
  output [
      "Installed packages: ", show(installed)
  ];
```

  ![Снимок экрана 2024-09-22 221309](https://github.com/user-attachments/assets/9aedc894-8d3e-4e55-a5dd-9e2b513afd13)


## Задача 6

Решить на MiniZinc задачу о зависимостях пакетов для следующих данных:

```
root 1.0.0 зависит от foo ^1.0.0 и target ^2.0.0.
foo 1.1.0 зависит от left ^1.0.0 и right ^1.0.0.
foo 1.0.0 не имеет зависимостей.
left 1.0.0 зависит от shared >=1.0.0.
right 1.0.0 зависит от shared <2.0.0.
shared 2.0.0 не имеет зависимостей.
shared 1.0.0 зависит от target ^1.0.0.
target 2.0.0 и 1.0.0 не имеют зависимостей.
```
```minizinc
  % Определяем пакеты
  enum PACKAGES = {
      root, 
      foo_1_0_0, foo_1_1_0, 
      left_1_0_0, right_1_0_0, 
      shared_1_0_0, shared_2_0_0, 
      target_1_0_0, target_2_0_0
  };
  
  % Переменные, указывающие, установлен ли пакет (1) или нет (0)
  array[PACKAGES] of var 0..1: installed;
  
  % Ограничения зависимостей
  constraint
      (installed[root] == 1) -> (installed[foo_1_1_0] == 1 /\ installed[target_2_0_0] == 1) /\
      (installed[foo_1_1_0] == 1) -> (installed[left_1_0_0] == 1 /\ installed[right_1_0_0] == 1) /\
      (installed[left_1_0_0] == 1) -> (installed[shared_1_0_0] == 1) /\
      (installed[right_1_0_0] == 1) -> (installed[shared_2_0_0] == 1) /\ (installed[shared_1_0_0] == 0) /\
      (installed[shared_1_0_0] == 1) -> (installed[target_1_0_0] == 1);
  
  % Обязательно устанавливаем root
  constraint
      installed[root] == 1;
  
  % Целевая функция: минимизируем количество установленных пакетов
  solve minimize sum(installed);
  
  % Выводим результат
  output [
      "Installed packages: ", show(installed)
  ];
```

  ![Снимок экрана 2024-09-22 221858](https://github.com/user-attachments/assets/e22cd150-dd76-454d-bef1-0dd03da6193f)
  ![Снимок экрана 2024-09-22 221920](https://github.com/user-attachments/assets/5f198866-265a-40ee-a211-7b5dff42324c)


## Задача 7

Представить задачу о зависимостях пакетов в общей форме. Здесь необходимо действовать аналогично реальному менеджеру пакетов. То есть получить описание пакета, а также его зависимости в виде структуры данных. Например, в виде словаря. В предыдущих задачах зависимости были явно заданы в системе ограничений. Теперь же систему ограничений надо построить автоматически, по метаданным.

```python
  # Пример структуры данных с зависимостями и версиями
  packages = {
      "root": {"dependencies": ["foo", "target"], "version": None},
      "foo": {"dependencies": ["left", "right"], "version": None},
      "left": {"dependencies": ["shared>=1.0.0"], "version": None},
      "right": {"dependencies": ["shared<2.0.0"], "version": None},
      "shared": {"dependencies": [], "version": None},
      "target": {"dependencies": [], "version": None},
  }
  
  def generate_minizinc_code(packages):
      package_names = ', '.join(packages.keys())
      # Генерация массива установленных пакетов
      minizinc_code = f"enum PACKAGES = {{{package_names}}};\n"
      minizinc_code += "array[PACKAGES] of var 0..1: installed;\n\n"
      # Добавляем условие для root
      minizinc_code += "constraint installed[root] == 1;\n"
      # Генерация ограничений
      for package, details in packages.items():
          dependencies = details["dependencies"]
          if dependencies:
              dep_constraints = []
              for dep in dependencies:
                  if '>' in dep or '<' in dep or '=' in dep:
                      dep_name = dep.split('>=')[0].split('<')[0].split('=')[0]
                      dep_constraints.append(f"installed[{dep_name}] == 1")
                  else:
                      dep_constraints.append(f"installed[{dep}] == 1")
              constraint = "constraint installed[{}] == 1 -> ({});\n".format(
                  package, ' /\\ '.join(dep_constraints)
              )
              minizinc_code += constraint
      minizinc_code += "\nsolve minimize sum(installed);\n"
      minizinc_code += 'output ["Installed packages: ", show(installed)];\n'
      return minizinc_code
  
  
  # Генерация и вывод MiniZinc кода
  minizinc_code = generate_minizinc_code(packages)
  print(minizinc_code)
```

  ВЫВОД:
  
  ```minizinc
  enum PACKAGES = {root, foo, left, right, shared, target};
  array[PACKAGES] of var 0..1: installed;
  
  constraint installed[root] == 1;
  constraint installed[root] == 1 -> (installed[foo] == 1 /\ installed[target] == 1);
  constraint installed[foo] == 1 -> (installed[left] == 1 /\ installed[right] == 1);
  constraint installed[left] == 1 -> (installed[shared] == 1);
  constraint installed[right] == 1 -> (installed[shared] == 1);
  
  solve minimize sum(installed);
  output ["Installed packages: ", show(installed)];
```

  ВЫВОД MiniZinc:
  Installed packages: [1, 1, 1, 1, 1, 1]
