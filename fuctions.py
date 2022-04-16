import json
import random
import sys
import time

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

def readJsonFile():
    '''读取JSON文件'''
    print('\nWe are preparing......')
    try:
        askedFile = open('./Datas/MainFile.json','rt',encoding='utf-8')
    except:
        print('We meet a serious problem.You should check weather "./Datas/MainFile.json" file is here!')
        sys.exit(1)
    waitString = askedFile.read()
    askedFile.close()
    dataDict =json.loads(waitString)
    return dataDict

def scanDict(dataDict):
    '''对字典进行解析，处理掉单独的字典'''
    judge = [1,1]                       #[是否为纯字典，是否为纯字符串]   
    delete = []             
    for key in dataDict:
        if isinstance(dataDict[key],dict):
            judge[1] = 0
        if isinstance(dataDict[key],str):
            judge[0] = 0
            delete.append(key)
    if judge == [0,0]:
        for few in delete:
            del dataDict[few]
    if judge == [0,0]:
        return [dataDict , 0]           #0是二者得兼喽...
    if judge == [0,1]:                  #注意，这里说的是处理之前的字典
        return [dataDict , 'str']       #'str'是纯字符串，直接退出循环就可以了
    if judge == [1,0]:
        return [dataDict , 1]           #1就是纯字典喽...
    
def askDict(Dict):
    print('Choose a Dict which you want to choose:')
    print('Press "q" to return the mode choose page.')
    i = 1
    List = dictToList(Dict)
    for little in List:
        print('%d : %s.' % (i , little[0]))
        i += 1
    while True:                     #判定输入的字符是否合法
        choose = input('Input its ID then press "ENTER":')
        try:
            choose = int(choose)
            if choose > 0 and choose <= len(List):
                break
            else:
                print('ERROR!Your input is not defined!')
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

def readTxtFile():
    print('\nWe are preparing......')
    try:
        askedFile = open('./Datas/MainFile.txt','rt',encoding='utf-8')
    except:
        print('We meet a serious problem.You should check weather "./Datas/MainFile.txt" file is here!')
        sys.exit(1)
    waitString = askedFile.read()
    askedFile.close()
    finalString = waitString.replace(' ',',')
    waitList = finalString.split("\n")
    finalList = []
    for littleList in waitList:
        finalList.append(littleList.split(','))
    return finalList

def valueList(list):
    """
    valueList函数：将列表的子列表(key , value)转换为（数字：value）的形式
    """
    i = 1
    List = []
    for littleList in list:
        list = [i ,littleList[1]]
        List.append(list)
        i += 1
    return List

def keyList(list):
    '''
    keyList函数：将列表的子列表(key , value)转换为（数字：key）的形式
    '''
    i = 1
    List = []
    for littleList in list:
        list = [i ,littleList[0]]
        List.append(list)
        i += 1
    return List

def modeA(finalList):
    '''
    根据译义写出原义的模式
    '''
    print('preparing......')
    answerList = keyList(finalList)
    askedList = valueList(finalList)
    questionMEM = 1
    trueMEM = 0
    falseMEM = 0
    wrongWord = []
    askedLog = open(".\Datas\log.txt", "a+",encoding='utf-8')
    askedLog.write('--------------The Start Line-----------------\nDate and Time：')
    askedLog.write(time.asctime())
    askedLog.write('\nMode : A (translation => literal meaning)\n------------------------------------------------')
    print('Done！')
    print('-----------------------------------------------------')
    while True:
        int = random.randint(0,len(askedList) - 1)
        print('Question %d : %s ' % (questionMEM , askedList[int][1]))
        answer1 = input('Your answer:')
        if answer1 == answerList[int][1]:
            askedLog.write('\nQuestion %d : %s ' % (questionMEM, askedList[int][1]))
            askedLog.write('\nAnswer : %s  (True)' % answer1)
            askedLog.write('\n-------')
            print('Right！''\n-------')
            trueMEM += 1
            questionMEM += 1
            continue
        elif answer1 == 'q':
            print('*************************')
            print('The test have done.Here is the simple information of the test.',\
                  'And you can see the detailed information of the test in the Log file.')
            print('\tTotleMember : %d\n\tTrueMember : %d \n\tFalseMember : %d ' % (questionMEM - 1,trueMEM , falseMEM))
            askedLog.write('\nSummarize:'\
                           '\nTotleMember : %d\nTrueMember : %d \nFalseMember : %d ' % (questionMEM - 1,trueMEM , falseMEM))
            if (questionMEM - 1) != 0:          #被除数为0会怎么样呢？
                print('\tCorrect rate: %.2f' % (trueMEM/(questionMEM - 1)))
                askedLog.write('\nCorrect rate: %.2f' % (trueMEM/(questionMEM - 1)))
            askedLog.write('\nWrong Words : ')  #错误回答的问题写入到日志中
            for little in wrongWord:
                askedLog.write('\n\t%s %s (Your answer：%s %s )' %
                              (little[0][0] , little[0][1] , little[1][0] , little[1][1]) )
            askedLog.write('\n------The End Line-------\n\n\n\n\n')
            askedLog.close()
            break
        else:
            print('Wrong！You need answer again.We will give the right answer if you are wrong again')
            answer2 = input()
            if answer2 == answerList[int][1]:
                print('Right！''\n-------')
                questionMEM += 1
                trueMEM += 1
                continue
            else:
                askedLog.write('\nQuestion %d : %s ' % (questionMEM, askedList[int][1]))
                askedLog.write('\nAnswer1: %s (False)' % answer1)
                askedLog.write('\nAnswer2: %s (False)' % answer2)
                askedLog.write('\nRight Answer : %s ' % answerList[int][1])
                askedLog.write('\n-------')
                print('What is a pity! The right answer is:')
                print(answerList[int][1])
                print('-------')
                wrongWord.append([finalList[int] , [answer1,answer2]])
                questionMEM += 1
                falseMEM += 1
                continue

def modeB(finalList):
    '''
    根据原义写出译义的模式
    '''
    print('Preparing.....')
    answerList = keyList(finalList)
    askedList = valueList(finalList)
    questionMEM = 1
    trueMEM = 0
    falseMEM = 0
    unknownMEM = 0
    wrongQuestions = []
    unknownQuestions = []
    askedLog = open(".\Datas\log.txt", "a+", encoding='utf-8')
    askedLog.write('--------------The Start Line-----------------\nTime：')
    askedLog.write(time.asctime())
    askedLog.write('\nMode : A (English => Chinese)\n------------------------------------------------')
    print('Done!')
    print('-----------------------------------------------------')
    print('Warning:The mode is subjective question. You should judge right or not by yourself.')
    while True:
        int = random.randint(0,len(askedList) - 1)
        print('Question %d : %s ' % (questionMEM , answerList[int][1]))
        answer1 = input('Your answer：')
        if answer1 == 'q':
            print('*************************')
            print('The test have done.Here is the simple information of the test.',\
                  'And you can see the detailed information of the test in the Log file.')
            print('\tTotleMember : %d\n\tTrueMember : %d \n\tFalseMember : %d \n\tUnknownMember : %d ' \
                    % (questionMEM - 1,trueMEM , falseMEM , unknownMEM))
            askedLog.write( '\nSummarize:' \
                            '\nTotleMember : %d\nTrueMember : %d \nFalseMember : %d \nUnknownMember : %d ' \
                                 % (questionMEM - 1, trueMEM, falseMEM, unknownMEM))
            if (questionMEM - 1) != 0:                  #被除数为0会怎么样呢？
                print('\tCorrect rate: %.2f' % (trueMEM/(questionMEM - 1)))
                askedLog.write('\nCorrect rate: %.2f' % (trueMEM/(questionMEM - 1)))
            askedLog.write('\nWrong Questions : ')      #错误回答的问题写入到日志中
            for little in wrongQuestions:
                askedLog.write('\n\t%s %s (Your Answer：%s )' % (little[0][0],little[0][1],little[1]))
            askedLog.write('\nUnknown Questions:')
            for little in unknownQuestions:             #未能判断对错的问题也应该写入到日志中
                askedLog.write('\n\t%s %s (Your Answer：%s )' % (little[0][0],little[0][1],little[1]))
            askedLog.write('\n------The End Line-------\n\n\n\n\n')
            askedLog.close()
            break
        print('--Your judge was recorded.We will show the standard answer.')
        print('The standard answer is：%s' % askedList[int][1])
        while True:
            answer2 = input('Check your answer(Right（“y”）Wrong（“n”）Skip（“ENTER”）):')
            if answer2 == 'y':
                askedLog.write('\nQuestion %d : %s ' % (questionMEM, answerList[int][1]))
                askedLog.write('\nAnswer : %s  (True)' % answer1)
                askedLog.write('\n-------')
                trueMEM += 1
                questionMEM += 1
                print('-------')
                break
            elif answer2 == 'n':
                askedLog.write('\nQuestion %d : %s ' % (questionMEM, answerList[int][1]))
                askedLog.write('\nYour Answer: %s (False)' % answer1)
                askedLog.write('\nStandard Answer : %s ' % askedList[int][1])
                askedLog.write('\n-------')
                wrongQuestions.append([finalList[int] , answer1])
                falseMEM += 1
                questionMEM += 1
                print('-------')
                break
            elif answer2 == '':
                askedLog.write('\nQuestion %d : %s ' % (questionMEM, answerList[int][1]))
                askedLog.write('\nAnswer : %s  (Unknown)' % answer1)
                askedLog.write('\n-------')
                unknownQuestions.append([finalList[int] , answer1])
                unknownMEM += 1
                questionMEM += 1
                print('-------')
                break
            else:
                print('ERROR! The answer is not defined! You should answer again!')
                continue

def dictToList(finalDict):
    '''
    将字典转换为列表
    '''
    finalList = []
    startList = finalDict.items()
    for object in startList:
        finalList.append(list(object))
    return finalList
  
def scanCycle(startDict):
    while True:
        judgeList = scanDict(startDict)
        if judgeList[1] == 0:
            print('The value attribute of the dictionary mixes dictionaries and strings.\n \
                So we keep the dictionary, the string will not be recognized.')
        if judgeList[1] == 'str':
            #Need change the dict to list!
            fianlList = dictToList(judgeList[0])
            return fianlList
        thenDict = askDict(judgeList[0])
        if thenDict == 'EXIT':
            return 'EXIT'
        startDict = thenDict.copy()

