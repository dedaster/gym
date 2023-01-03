# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 20:54:50 2022

@author: dedaster
"""

import pandas as pd
from colorama import init, Fore, Back, Style

pd.options.mode.chained_assignment = None  # отключение предупреждений

while True:
    try:
        init()    
        ex = pd.read_csv('/Git/gym/gym.csv')
        group = input('Введите группу мышц (спина, перед, низ): ')
        
        print()
        
        # выводим подходящие упражнение на сегодня
        press_r = ex[ex['Muscules'].isin(['кор'])].sample(n=1)
        ex_r = ex[ex['Muscules'].isin([group])].sample(n=3)
    
        result = pd.concat([press_r, ex_r], ignore_index=True)
    
        print()
        print(result)
        print()
        
        # считаем количество повторений в каждом подходе
        for i in range (4):
            xm = 0
            print()
            print(Fore.BLACK + Back.WHITE + 'Упражнение: '+(result.Name.iloc[i]) + Style.RESET_ALL)
            print()
            for j in range (3):
                print('Подход', j+1, sep=' ', end=' ', )
                x = int(input('повторов: '))
                xm += x
                ex_res = int((xm/3)+1)
            print()
            
            # заносим изменения в нашу базу упражнений
            result.iloc[[i], [3]] = ex_res
            r_name = result.Name.iloc[i]
            in_ex = ex[ex['Name'].isin([r_name])].index
            ex.Times.iloc[in_ex] = ex_res
    
        #записываем изменения в файл с базой упражнений
        ex.to_csv('/Git/gym/gym.csv', index = False)
        
        print()
        print()
        print(Fore.GREEN + 'ОТЛИЧНО ПОРАБОТАЛИ!' + Style.RESET_ALL)
        print()
        print()
        print()
        print("Если хотите продолжить")
        
    except ValueError:
        print(Fore.RED + 'Только низ, перед или спина!' + Style.RESET_ALL)
        print()



