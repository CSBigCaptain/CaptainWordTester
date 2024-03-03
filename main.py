from colorama import Fore, init

import core_fuctions
import modules

init()  # colorama模块初始化
finalList = modules.addTestList()
while True:
    print(finalList + '+++')
    finalList = modules.addTestList(0, finalList)
    while True:
        choose = modules.testModeChoose()
        if choose == 1:
            core_fuctions.askOriginalWords(finalList)
        elif choose == 2:
            core_fuctions.askTranslatedWords(finalList)
        elif choose == 3:
            core_fuctions.practiceMode(finalList)
        elif choose == 'BREAK':
            break
        elif choose == 'EXIT':
            exit(0)
