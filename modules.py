#规模较大的函数组件
from colorama import Fore, init

import read_fuctions

init()  # colorama模块初始化


# 红色文本用来表示警告


def addTestList(isReset=1, finalList=None):
    """
    添加或者重置单词列表,默认重置
    """
    if not finalList:
        isReset = 1
    if finalList is None:
        finalList = []
    if isReset == 1:
        return read_fuctions.readDatasFiles()
    else:
        print('Do you want to reset the word list?')
        while True:
            isResetInFunction = input()
            if isResetInFunction == 'y':
                return read_fuctions.readDatasFiles()
            elif isResetInFunction == 'n':
                return finalList
            elif isResetInFunction == 'a':
                return finalList + read_fuctions.readDatasFiles()
            else:
                print(Fore.RED + "Warning: Your answer isn't defined!\n"
                                 "Please input again!" + Fore.RESET)
                continue


def testModeChoose():
    while True:
        print('----------------------------------------------------------',
              'Choose your mode :',
              'Press "a": Guess words by translations!',
              'Press "b": Translate words!',
              'Press "c": Practise!',
              'Press "l": Back.',
              'Press "q": Exit.',
              'Press "ENTER" to confirm.', sep='\n')
        answer = input('Your answer:')
        if answer == 'a':
            return 1
        elif answer == 'b':
            return 2
        elif answer == 'c':
            return 3
        elif answer == 'l':
            return 'BREAK'
        elif answer == 'q':
            return 'EXIT'
        else:
            print("Your answer isn't defined!\nPlease input again!")
            continue
