import choose_fuctions , read_fuctions , core_fuctions
import sys


while True:
    choose = choose_fuctions.jsonOrTxt()
    if choose == 1:
        startDict = read_fuctions.readJsonFile()
        if startDict == 'EXIT':
            continue
        finalDict = read_fuctions.scanCycle(startDict)
        if finalDict == 'EXIT':
            continue
    elif choose == 2:
        finalList = read_fuctions.readTxtFile()
        if finalList == 'EXIT':
            continue
    elif choose == 3:
        sys.exit(0)

    while True:
        choose = choose_fuctions.testModeChoose()
        if choose == 1:
            core_fuctions.askOriginalWords(finalList)
        elif choose == 2:
            core_fuctions.askTranslatedWords(finalList)
        elif choose == 3:
            core_fuctions.practiceMode(finalList)
        elif choose == 'EXIT':
            break

