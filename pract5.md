# Задача 1
Исследование виртуальной стековой машины CPython. Изучите возможности просмотра байткода ВМ CPython.

```Python
import dis

def foo(x):
    while x:
        x -= 1
    return x + 1

print(dis.dis(foo))
```
Опишите по шагам, что делает каждая из следующих команд (приведите эквивалентное выражение на Python):

11 0 LOAD_FAST 0 (x) 2 LOAD_CONST 1 (10) 4 BINARY_MULTIPLY 6 LOAD_CONST 2 (42) 8 BINARY_ADD 10 RETURN_VALUE

1. `0 LOAD_FAST 0 (x)` - Загружает переменной x из локалки. Это эквивалент получения значения переменной в Python.
```Python 
x
```
2. `2 LOAD_CONST 1 (10)` - Загружает константы (10) в стек.
```Python
10
```
3. `4 BINARY_MULTIPLY` - Извлекает два верхних элемента из стека и выполняет операцию умножения, результат помещает обратно в стек.
```Python
x * 10
```
4. `6 LOAD_CONST 2 (42)` - Загружает константу 42 в стек.
```Python
42
```
5. `8 BINARY_ADD` - Извлекает два верхних элемента из стека и выполняет операцию сложения, результат помещает обратно в стек.
```Python
(x * 10) + 42
```
6. `10 RETURN_VALUE` - Возвращает верхнее значение из стека в качестве результата функции и завершает её выполнение.
```Python
return (x * 10) + 42
```
Полный эквивалент на Python:
```Python
def foo(x):
    return (x * 10) + 42
```

# Задача 2

Что делает следующий байткод (опишите шаги его работы)? Это известная функция, назовите ее.
```arduino
  5           0 LOAD_CONST               1 (1)
              2 STORE_FAST               1 (r)

  6     >>    4 LOAD_FAST                0 (n)
              6 LOAD_CONST               1 (1)
              8 COMPARE_OP               4 (>)
             10 POP_JUMP_IF_FALSE       30

  7          12 LOAD_FAST                1 (r)
             14 LOAD_FAST                0 (n)
             16 INPLACE_MULTIPLY
             18 STORE_FAST               1 (r)

  8          20 LOAD_FAST                0 (n)
             22 LOAD_CONST               1 (1)
             24 INPLACE_SUBTRACT
             26 STORE_FAST               0 (n)
             28 JUMP_ABSOLUTE            4

  9     >>   30 LOAD_FAST                1 (r)
             32 RETURN_VALUE
```

1. `0 LOAD_CONST 1 (1)` - Загружает константу (1) в стек.
2. `2 STORE_FAST 1 (r)` - Сохраняет значение 1 в локальной переменной r.
3. `4 LOAD_FAST 0 (n)` - Загружает значение переменной n из локальной области в стек.
4. `6 LOAD_CONST 1 (1)` - Загружает константу (1) в стек.
5. `8 COMPARE_OP 4 (>)` - Сравнивает значение n с 1. Проверяет, больше ли n единицы.
6. `10 POP_JUMP_IF_FALSE 30` - Если результат сравнения False (то есть n не больше 1), выполняется переход на инструкцию с индексом 30 (выход из цикла). Иначе продолжает выполнение следующих команд.
7. `12 LOAD_FAST 1 (r)` - Загружает значение переменной r из локальной области.
8. `14 LOAD_FAST 0 (n)` - Загружает значение переменной n из локальной области.
9. `16 INPLACE_MULTIPLY` - Перемножает r и n и сохраняет результат в r.
10. `18 STORE_FAST 1 (r)` - Обновляет значение переменной r новым результатом умножения.
11. `20 LOAD_FAST 0 (n)` - Загружает значение переменной n.
12. `22 LOAD_CONST 1 (1)` - Загружает константу 1.
13. `24 INPLACE_SUBTRACT` - Вычитает 1 из n и сохраняет результат в n.
14. `26 STORE_FAST 0 (n)` - Обновляет значение переменной n.
15. `28 JUMP_ABSOLUTE 4` - Переход к началу цикла (инструкция с индексом 4), чтобы проверить условие заново.
16. `30 LOAD_FAST 1 (r)` - Загружает значение переменной r.
17. `32 RETURN_VALUE` - Возвращает значение r и завершает выполнение функции.

Этот байткод соответствует реализации функции вычисления факториала с помощью цикла while. 

```Python
def factorial(n):
    r = 1
    while n > 1:
        r *= n
        n -= 1
    return r
```

# Задача 3
Приведите результаты из задач 1 и 2 для виртуальной машины JVM (Java) или .Net (C#).

Эквивалент функции из Задания №1 на языке Java:
```Java
public int foo(int x) {
    return (x * 10) + 42;
}
```
Байт-код JVM:
``` arduino
public int foo(int);
  Code:
     0: iload_1           // Загружает параметр x
     1: bipush 10         // Загружает константу 10
     3: imul              // Умножает x на 10
     4: bipush 42         // Загружает константу 42
     6: iadd              // Складывает результат умножения с 42
     7: ireturn           // Возвращает результат
```

Эквивалент функции из Задания №2 на языке Java:
```Java
public int factorial(int n) {
    int r = 1;
    while (n > 1) {
        r *= n;
        n--;
    }
    return r;
}
```
Байт-код JVM:
``` arduino
public int factorial(int);
  Code:
     0: iconst_1           // Загружает константу 1
     1: istore_2           // Сохраняет ее в переменную r
     2: iload_1            // Загружает n
     3: iconst_1           // Загружает константу 1
     4: if_icmple 21       // Переход к инструкции 21, если n <= 1

     7: iload_2            // Загружает r
     8: iload_1            // Загружает n
     9: imul               // Умножает r на n
    10: istore_2           // Сохраняет результат в r
    11: iload_1            // Загружает n
    12: iconst_1           // Загружает константу 1
    13: isub               // Вычитает 1 из n
    14: istore_1           // Сохраняет результат в n
    15: goto 2             // Переход на инструкцию 2 (начало цикла)

    21: iload_2            // Загружает r
    22: ireturn            // Возвращает r
```


