# Практическое занятие №2.

## Задание: 
2) На выбранном ЯП реализовать простейший калькулятор выражений в обратной польской записи с целыми числами.
Загружаете отчет в PDF, назвав в формате «Группа_Фамилия_Имя_ПР-номер» (Например, ИКБО-40-23_Иванов_Иван_ПР1).


```
def evaluate_postfix(expression):
    stack = []  # Стек для хранения операндов и выражений

    # Проходим по каждому токену в выражении
    for token in expression.split():
        if token.lstrip('-').isdigit():  # Проверяем, является ли токен числом (включая отрицательные)
            stack.append(token)  # Добавляем число в стек
        else:  # Если токен - оператор
            b = stack.pop()  # Берем верхний элемент (второй операнд)
            a = stack.pop()  # Берем следующий элемент (первый операнд)

            # Формируем новое выражение с использованием скобок
            new_expr = f"({a} {token} {b})"
            stack.append(new_expr)  # Добавляем выражение в стек

    # Получаем итоговое арифметическое выражение
    final_expression = stack.pop()
    return final_expression

def calculate_expression(expression):
    return eval(expression)  # Вычисляем выражение с помощью eval

# Пример использования
if __name__ == "__main__":
    expression = input("Введите выражение в ОПЗ (например, '3 4 + 2 *'): ")
    try:
        # Преобразование в арифметическое выражение
        arithmetic_expression = evaluate_postfix(expression)
        # Вычисление результата
        result = calculate_expression(arithmetic_expression)
        
        print("Арифметическое выражение:", arithmetic_expression)
        print("Результат:", result)
    except Exception as e:
        print("Ошибка:", e)

```
