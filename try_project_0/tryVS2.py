"""Пробуем дурацкую игрушку"""

import numpy as np

number = np.random.randint(1, 101) #генерим число


def random_predict(number:int=1) -> int:
    """Угадываем случайным образом

    Args:
        number (int, optional): Заданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    count = 0 # количество попыток
    
    while True:
        count+=1
        predict_number = np.random.randint(1, 101) # предполагаемое число
        if number == predict_number:
            break # выход из цикла, если угадали
        
    return(count)

def score_game(random_predict) -> int:
    """За какое количество попыток среднем за 1000 подходов угадывает наш подход

    Args:
        random_predict (int ): Функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1) # Фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # Загадали 1000 чисел

    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

if __name__ == '__main__':
    #RUN
    score_game(random_predict)
#print(f'Количество попыток: {random_predict(10)}')