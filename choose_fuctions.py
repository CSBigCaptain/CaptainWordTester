#choose_fuctions文件，用来存储交互式界面所需要的函数
import json
import change_fuctions

def jsonOrTxt():
    while True :
        print('----------------------------------------------',\
              'Choose your reading mode:',\
              'Press "a" : Json mode.(The programe will read the Json data file)',\
              'Press "b" : Txt mode. (The programe will read the txt data file)',\
              'Press "q" : Quit the programe.'
              'If you done ,you should press "ENTER" .(Yeah,you should do it in the programe every time)',\
               sep = '\n')
        judge = input('Yours : ')
        if judge == 'a':                                    #Json Files
            return 1
        elif judge == 'b':                                  #Txt Files
            return 2
        elif judge == 'q':
            return 3
        else:
            print("WARNING!It isn't allowed,as it wasn't defined! \nYou should input again!")
            continue

def askDict(Dict):
    '''
    scanCycle函数的必要部分
    '''
    print('Choose a Dict which you want to choose:')
    print('Press "q" to return the mode choose page.')
    i = 1
    List = change_fuctions.dictToList(Dict)
    for little in List:
        print('%d : %s.' % (i , little[0]))
        i += 1
    while True:                     #判定输入的字符是否合法
        choose = input('Input its ID then press "ENTER":')
        #这个地方使用try的原因：如果输入为非数字（比如按Q键是退出），就会报错。
        try:
            choose = int(choose)
            if choose > 0 and choose <= len(List):
                break
            else:
                print('ERROR! Please input the true answer!')
                continue
        except:
            if choose == 'q':
                return 'EXIT'
            else:
                print('ERROR!Your input is not defined!')
    return List[choose - 1][1]

def testModeChoose():
    while True:
        print('----------------------------------------------------------',\
              'Let us choose your mode :',\
              'Press "a": The programe will ask you its meaning and you must answer its word.',\
              'Press "b": You must answer its meaning by its word.',\
              'Press "q": Break.',\
              'Press "ENTER" to make your answer sure.',sep = '\n')
        answer = input('Your answer:')
        if answer == 'a':
            return 1
        elif answer == 'b':
            return 2
        elif answer == 'q':
            return 3
        else:
            print("WARNING!It isn't allowed,as it wasn't defined! \nYou should input again!")
            continue
