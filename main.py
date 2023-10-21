import choose_fuctions , read_fuctions , core_fuctions , modules
import sys

finalList = []
while True:
    finalList = modules.addOrRefresh(finalList)
    print(finalList)
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