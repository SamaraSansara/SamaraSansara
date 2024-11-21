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
  array[1..6] of var 0..9: digits;
  constraint alldifferent(digits);
  constraint sum(digits[1..3]) = sum(digits[4..6]);
  solve minimize sum(digits[1..3]);
  output [
      "Digits: ", show(digits), 
      "\nSum of first 3 digits: ", show(sum(digits[1..3])), 
      "\nSum of last 3 digits: ", show(sum(digits[4..6]))
  ];
```

<img width="811" alt="Screenshot 2024-10-07 at 10 16 53" src="https://github.com/user-attachments/assets/1285d5a6-e45d-43da-9d39-97352c957f88">

## Задача 5

Решить на MiniZinc задачу о зависимостях пакетов для следующих данных:
<img width="573" alt="Screenshot 2024-10-07 at 10 05 36" src="https://github.com/user-attachments/assets/92db945a-d4c8-4915-b606-0f641568e648">

```
set of int: MenuVersion = {100, 110, 120, 130, 140, 150};
set of int: DropDownVersion = {180, 200, 210, 220, 230};
set of int: IconsVersion = {100, 200};

var MenuVersion: menu;
var DropDownVersion: dropdown;
var IconsVersion: icons;

% Ограничение для зависимости между menu и dropdown
constraint
  if menu >= 110 then
    dropdown >= 200
  else
    dropdown = 180
  endif;

% Ограничение для зависимости между dropdown и icons
constraint
  if dropdown >= 200 then
    icons = 200
  else
    icons = 100
  endif;
 
 output ["Menu Version: ", show(menu),
         "\nDropdown Version: ", show(dropdown),
         "\nIcons Versions: ", show(icons)]
```
<img width="1180" alt="Screenshot 2024-10-07 at 10 02 02" src="https://github.com/user-attachments/assets/62e2ef79-8c7a-4c8e-b362-76f9217862d1">


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

```
int: root = 100;
var 100..300: foo;
var 100..300: target;
var 100..300: left;
var 100..300: right;
var 100..300: shared;

constraint
  root = 100 ->
  (foo >= 100 /\ foo < 200 /\ 
  target >= 200 /\ target < 300);
 
constraint
  foo = 110 -> 
  (left >= 100 /\ left < 200 /\
  right >= 100 /\ right < 200);
 
constraint
  (left = 100 -> shared >= 100) /\
  (right = 100 -> shared < 200);

constraint
  left = 100 ->
  (shared >= 100);
 
constraint
  right = 100 ->
  (shared < 200);
  
constraint
  shared = 100 ->
  (target >= 100 /\ target < 200);

output [
    "Root Version: ", show(root), "\n",
    "Foo Version: ", show(foo), "\n",
    "Left Version: ", show(left), "\n",
    "Right Version: ", show(right), "\n",
    "Shared Version: ", show(shared), "\n",
    "Target Version: ", show(target), "\n"
];
```

<img width="808" alt="Screenshot 2024-10-07 at 10 12 23" src="https://github.com/user-attachments/assets/aa70e0e2-8e6b-4050-bc6b-313668d9f400">
<img width="806" alt="Screenshot 2024-10-07 at 10 12 40" src="https://github.com/user-attachments/assets/57e32c5b-37fd-4a73-b2a6-a4becfc6757f">
<img width="803" alt="Screenshot 2024-10-07 at 10 12 54" src="https://github.com/user-attachments/assets/6a404f5d-f149-410a-a298-7c090689185c">


## Задача 7

Представить задачу о зависимостях пакетов в общей форме. Здесь необходимо действовать аналогично реальному менеджеру пакетов. То есть получить описание пакета, а также его зависимости в виде структуры данных. Например, в виде словаря. В предыдущих задачах зависимости были явно заданы в системе ограничений. Теперь же систему ограничений надо построить автоматически, по метаданным.
```
packages = {
    'root': {
        '1.0.0': {
            'dependencies': {
                'foo': '^1.0.0',
                'target': '^2.0.0'
            }
        }
    },
    'foo': {
        '1.1.0': {
            'dependencies': {
                'left': '^1.0.0',
                'right': '^1.0.0'
            }
        },
        '1.0.0': {
            'dependencies': {}
        }
    },
    'left': {
        '1.0.0': {
            'dependencies': {
                'shared': '>=1.0.0'
            }
        }
    },
    'right': {
        '1.0.0': {
            'dependencies': {
                'shared': '<2.0.0'
            }
        }
    },
    'shared': {
        '2.0.0': {
            'dependencies': {}
        },
        '1.0.0': {
            'dependencies': {
                'target': '^1.0.0'
            }
        }
    },
    'target': {
        '2.0.0': {
            'dependencies': {}
        },
        '1.0.0': {
            'dependencies': {}
        }
    }
}

def find_compatible_version(package_name, version_constraint, resolved):
    def is_compatible(version, min_version='', max_version=''):
        return (not min_version or version >= min_version) and (not max_version or version <= max_version)

    min_version, max_version = '', ''
    if version_constraint.startswith('^'):
        min_version = version_constraint[1:] 
    elif version_constraint.startswith('>='):
        min_version = version_constraint[2:]
    elif version_constraint.startswith('<='):
        max_version = version_constraint[2:]
    elif version_constraint.startswith('<'):
        max_version = version_constraint[1:]

    for version in sorted(packages[package_name].keys()):
        if is_compatible(version, min_version, max_version) and package_name not in resolved:
            if check_package_dependencies(package_name, version, resolved):
                return True
    return False

def check_package_dependencies(package_name, version, resolved):
    if package_name in resolved:
        return True

    for dep_pkg, dep_version in packages[package_name][version]['dependencies'].items():
        if not find_compatible_version(dep_pkg, dep_version, resolved):
            return False  

    resolved[package_name] = version
    return True

resolved_set = {}
root_version = '1.0.0'
if check_package_dependencies('root', root_version, resolved_set):
    print("Совместимые версии пакетов:")
    for pkg, ver in resolved_set.items():
        print(f"Пакет: {pkg}, Версия: {ver}")
else:
    print("Not found")
```
<img width="944" alt="Screenshot 2024-10-07 at 10 29 26" src="https://github.com/user-attachments/assets/c856398d-f1bf-42e8-97c3-de05d26c2243">

