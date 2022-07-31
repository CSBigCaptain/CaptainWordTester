#核心功能函数
from itertools import count
import random , time
from tkinter import E
import change_fuctions

def askOriginalWords(finalList):
    '''
    根据译义写出原义的模式
    '''
    answerList = change_fuctions.keyList(finalList)
    askedList = change_fuctions.valueList(finalList)
    questionMEM = 1
    trueMEM = 0
    falseMEM = 0
    wrongWord = []
    askedLog = open(".\Datas\log.txt", "a+",encoding='utf-8')
    askedLog.write('--------------The Start Line-----------------\nDate and Time：')
    askedLog.write(time.asctime())
    askedLog.write('\nMode : A (translation => literal meaning)\n---------------------------------------------')
    print('=============')
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
            print('=============')
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

def askTranslatedWords(finalList):
    '''
    根据原义写出译义的模式
    '''
    answerList = change_fuctions.keyList(finalList)
    askedList = change_fuctions.valueList(finalList)
    questionMEM = 1     
    trueMEM = 0
    falseMEM = 0
    unknownMEM = 0
    wrongQuestions = []
    unknownQuestions = []
    askedLog = open(".\Datas\log.txt", "a+", encoding='utf-8')
    askedLog.write('--------------The Start Line-----------------\nTime：')
    askedLog.write(time.asctime())
    askedLog.write('\nMode : A (English => Chinese)\n-------------------------------------')
    print('=============')
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
            print('=============')
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
 
def practiceMode(finalList):
    originalList = change_fuctions.keyList(finalList)
    translatedList = change_fuctions.valueList(finalList)
    questionMEM = 1
    print('=============')
    while True:
        if questionMEM > len(originalList):
            break
        print('The word %d : %s  %s' % (questionMEM , originalList[questionMEM-1][1] , translatedList[questionMEM-1][1]))
        print('Please input the word rightly:',end='')
        while True:
            answer = input()
            if answer == originalList[questionMEM - 1][1]:
                questionMEM += 1
                break
            if answer == 'q':
                break
            else:
                print('Wrong! Please input again!')
                continue
        if answer == 'q':
            break
    print('The practice is over.')
    print('=============')    
