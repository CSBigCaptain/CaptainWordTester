import fuctions
import sys

while True:
    choose = fuctions.jsonOrTxt()
    if choose == 1:
        startDict = fuctions.readJsonFile()
        finalDict = fuctions.scanCycle(startDict)
        if finalDict == 'EXIT':
            continue
    elif choose == 2:
        finalList = fuctions.readTxtFile()
    elif choose == 3:
        sys.exit(0)

    while True:
        choose = fuctions.testModeChoose()
        if choose == 1:
            fuctions.modeA(finalList)
        elif choose == 2:
            fuctions.modeB(finalList)
        elif choose == 3:
            break

