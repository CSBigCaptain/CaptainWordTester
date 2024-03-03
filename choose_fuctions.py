#choose_fuctions文件，用来存储选择功能的功能所需要的函数
from colorama import Fore, init

import change_fuctions

init()  # colorama模块初始化

def askDict(Dict):
    '''
    scanCycle函数的必要部分
    '''
    print('Choose a Grope which you want to choose:')
    print('Press "q" to return the mode choose page.')
    i = 1
    List = change_fuctions.dictToList(Dict)
    for little in List:
        print(f'{i}: {little[0]}')
        i += 1

    print('---- Input its ID then press "ENTER":', end='')
    while True:
        choose = input('')
        if choose.isdigit():
            choose = int(choose)
            if choose > 0 and choose <= len(List):
                break
            else:
                print(Fore.RED + 'Warning: Please input true ID!' + Fore.RESET)
                continue
        else:
            if choose == 'q':
                return 'EXIT'
            else:
                print(Fore.RED + "Warning: Your answer isn't defined!" + Fore.RESET)
    return List[choose - 1][1]


