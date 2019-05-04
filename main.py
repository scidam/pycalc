# coding: utf-8
__version__ = "0.1"
__author__ = "Dmitry E. Kislov"
__email__ = "kislov@easydan.com"

import time
import operator
import datetime
import random

CONFIG = {'plus' : ([0, 100], operator.add, '+'),
          'minus' : ([0, 100], operator.add, '-'),
          'multiply': ([1, 10], operator.mul, 'x')
          }

def save_result():
    pass

def plot_result(type='all'):
    with open('data.dat', 'r') as f:
        pass

def run_game(opt='plus'):
    print("\nВам будут предложены задания. Для выхода введите: exit\n")
    if opt == 'all':
        comb_flag = True
    else:
        comb_flag = False
    def make_task():
        nonlocal opt
        done = False
        while not done:
            if comb_flag == True:
                opt = random.choice(CONFIG.keys())
            v1 = random.randint(CONFIG[opt][0][0], CONFIG[opt][0][1])
            v2 = random.randint(CONFIG[opt][0][0], CONFIG[opt][0][1])
            res = CONFIG[opt][1](v1, v2)
            if res >= CONFIG[opt][0][0]:
                done = True
        eq = str(v1) + ' ' + CONFIG[opt][-1] + ' ' + str(v2)
        return eq, res, opt

    storage = []
    while True:
        eq, res, op = make_task()
        print("\n Решите пример: " + eq)
        start = time.time()
        while True:
            value = input("\n Введите ответ: ")
            try:
                if 'exit' in value.lower():
                    print("Программа завершает работу. До свидания!")
                    return
                if int(value) == res:
                    end = time.time()
                    print("\n Правильный ответ. ")
                    print("\n Затраченное время: {} c.".format(end - start))
                    storage.append([datetime.datetime.now(), end - start, op])
                    break
                else:
                    print("\n Неправильный ответ. Повторите попытку")
            except:
                print("\n Неправильный ответ.")
                continue
        with open('output.dat', 'a') as f:
            f.write(','.join(map(str, storage[-1])) + '\n')


def main():
    while True:
        value = input("\nВыберите режим (1 - сложение, 2 - вычитание, "
                      "3 - умножение,  4 - комбинированный): ")
        value = value.strip()
        if value not in ['1','2', '3', '4']:
            continue
        else:
            break
    if value == '1':
        opt = 'plus'
    elif value == '2':
        opt = 'minus'
    elif value == '3':
        opt = 'multiply'
    else:
        opt = 'all'

    run_game(opt=opt)

if __name__ == '__main__':
    main()
