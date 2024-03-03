import json
import os
from colorama import Fore, init

import change_fuctions
import choose_fuctions

init()  # colorama模块初始化


def readSettingsFile(settings_str):
    try:
        file = open('./Datas/SettingsFile.json', 'r', encoding='utf-8')
        settingStr = file.read()
        settings = json.loads(settingStr)
        file.close()
    except:
        # 如果没有找到文件，就使用默认设置
        settings = {"ReadingFormat": ["\t", " ", ","], "WrongListNotify": 1}
    return settings[settings_str]


def readJsonFile(fileName):
    """读取JSON文件"""
    jsonDir = './NewDatas/' + fileName
    askedFile = open(jsonDir, 'rt', encoding='utf-8')
    waitString = askedFile.read()
    askedFile.close()
    dataDict = json.loads(waitString)
    finalList = scanCycle(dataDict)
    return finalList


def scanCycle(dic):
    """处理读取JSON文件产生的字典"""
    while True:
        judgeList = scanDict(dic)
        if judgeList[1] == 0:
            print('The value attribute of the dictionary mixes dictionaries and strings.\n',
                  'So we keep the dictionary, the string will not be recognized.')
        if judgeList[1] == 'str':
            # 将字典转化为列表!
            finalList = change_fuctions.dictToList(judgeList[0])
            return finalList
        thenDict = choose_fuctions.askDict(judgeList[0])
        if thenDict == 'EXIT':
            return ''
        dic = thenDict.copy()


def scanDict(dataDict):
    """对字典进行解析，处理掉单独的字典"""
    judge = [1, 1]  # [是否为纯字典（字典中的子字典），是否为纯字符串]
    delete = []
    for key in dataDict:
        # 遍历字典中的每一个元素，判断类型
        if isinstance(dataDict[key], dict):
            judge[1] = 0
        if isinstance(dataDict[key], str):
            judge[0] = 0
            # 后续会删除杂的字符串
            delete.append(key)
    if judge == [0, 0]:
        for few in delete:
            del dataDict[few]
    if judge == [0, 0]:
        return [dataDict, 0]  # 0是二者得兼喽...
    if judge == [0, 1]:  # 注意，这里说的是处理之前的字典
        return [dataDict, 'str']  # 'str'是纯字符串，直接退出循环就可以了
    if judge == [1, 0]:
        return [dataDict, 1]  # 1就是纯字典喽...


def readTxtFile(fileName, FORMAT, WRONGFULNESS):
    dir = './NewDatas/' + fileName
    try:
        askedFile = open(dir, 'rt', encoding='utf-8')
    except:
        print('We can"t find the "./TxtDatas/MainFile.txt" file! Please make sure the file is here and try again!')
        return 'EXIT'
    waitString = askedFile.read()
    askedFile.close()
    waitList = waitString.split("\n")
    finalList = []
    for little in waitList:
        for i in FORMAT:
            finalList.append(little.split(i))
    i = 0
    wrongList = []
    for little in finalList:  # 通过检查列表中的元素数量的方式，寻找不合格的数据
        if len(little) != 2:
            wrongList.append([i, little])
        i += 1
    wrongList = wrongList[::-1]  # 为什么要把列表倒序，是需要耐心领会的
    for little in wrongList:  # 删除不符合格式的数据
        finalList.pop(little[0])
    wrongList = wrongList[::-1]  # 再倒序回来是为了打印的时候更符合常人的阅读习惯
    if len(wrongList) > 0 and WRONGFULNESS == 1:
        print('These datas may have problems. In order to avoid errors, we ignored them.')
        for little in wrongList:
            print('The line:', little[0] + 1, little[1], sep=' ')
    return finalList


def readDatasFiles():
    dirList = os.listdir('./NewDatas')
    fileName = ''
    print('Choose your files from these files.\n'
          'Use "q" to back.')
    print(Fore.GREEN)
    for i in range(1, len(dirList) + 1):
        print(i, dirList[i - 1], sep=': ')
    print(Fore.RESET)
    while True:
        userChosen = input()
        if userChosen.isdigit():
            userChosen = int(userChosen)
            if 0 < userChosen <= len(dirList):
                fileName = dirList[userChosen - 1]
            else:
                print(Fore.RED + 'Warning: Please input true ID!' + Fore.RESET)
                continue
        else:
            if userChosen == 'q':
                return []
            else:
                print(Fore.RED + "Warning: Your answer isn't defined!" + Fore.RESET)
        fileName = fileName.split('.')
        fileType = fileName[-1]
        FORMAT = readSettingsFile('ReadingFormat')
        WRONGFULNESS = readSettingsFile('WrongListNotify')
        fileName = fileName[0] + '.' + fileType     # 恢复原来的文件名
        if fileType == 'json':
            a = readJsonFile(fileName)
            return a
        elif fileType == 'txt':
            return readTxtFile(fileName, FORMAT, WRONGFULNESS)
        else:
            print(Fore.RED + 'Warning: We cannot support this kind of file.' + Fore.RESET)
