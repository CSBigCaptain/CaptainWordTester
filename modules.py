#
import read_fuctions
def addOrRefresh(startList):
    '''
    添加或者重置单词列表
    '''
    while True:
        if startList == []:
            return read_fuctions.readDatasFiles()
        else:
            choose = input('Do you want to add or reset your words list?("a" or "r")')
        if choose == 'a':
            addedList = read_fuctions.readDatasFiles()
            finalList = startList + addedList
        if choose == 'r':
            startList = []
            continue
        else:
            continue
        return finalList

def testModeChoose():
    while True:
        print('----------------------------------------------------------',\
              'Let us choose your mode :',\
              'Press "a": Guess words by translations!',\
              'Press "b": Translate words!',\
              'Press "c": Practise!',\
              'Press "l": Back.',\
              'Press "q": Exit.',\
              'Press "ENTER" to confirm.',sep = '\n')
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