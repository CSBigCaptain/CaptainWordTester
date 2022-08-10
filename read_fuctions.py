#读取文件所需要的函数
import json
import change_fuctions , choose_fuctions

def readSettingsFile(settings_str):
    try:
        file = open('./Datas/SettingsFile.json','r',encoding = 'utf-8')
        str = file.read()
        settings = json.loads(str)
        file.close()
    except:
        settings = { "ReadingFormat" : "\t","WrongListNotify" : 1 }
    return settings[settings_str]

def readJsonFile():
    '''读取JSON文件'''
    try:
        askedFile = open('./JsonDatas/MainFile.json','rt',encoding = 'utf-8')
    except:
        print('We can"t find the "./JsonDatas/MainFile.txt" file! Please make sure the file is here and try again!')
        return 'EXIT'
    waitString = askedFile.read()
    askedFile.close()
    dataDict = json.loads(waitString)
    return dataDict

def scanCycle(startDict):
    while True:
        judgeList = scanDict(startDict)
        if judgeList[1] == 0:
            print('The value attribute of the dictionary mixes dictionaries and strings.\n',\
                  'So we keep the dictionary, the string will not be recognized.')
        if judgeList[1] == 'str':
            #将字典转化为列表!
            fianlList = change_fuctions.dictToList(judgeList[0])
            return fianlList
        thenDict = choose_fuctions.askDict(judgeList[0])
        if thenDict == 'EXIT':
            return 'EXIT'
        startDict = thenDict.copy()

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

def readTxtFile(FORMAT , WRONGLISTNOTIFY):
    try:
        askedFile = open('./TxtDatas/MainFile.txt','rt',encoding='utf-8')
    except:
        print('We can"t find the "./TxtDatas/MainFile.txt" file! Please make sure the file is here and try again!')
        return 'EXIT'       
    waitString = askedFile.read()
    askedFile.close()
    waitList = waitString.split("\n")
    finalList = []
    for little in waitList:
        finalList.append(little.split(FORMAT))
    i = 0
    wrongList = []
    for little in finalList:            #通过检查列表中的元素数量的方式，寻找不合格的数据
        if len(little) != 2:
           wrongList.append([i,little])
        i += 1
    wrongList = wrongList[ : :-1]       #为什么要把列表倒序，是需要耐心领会的
    for little in wrongList:            #删除不符合格式的数据
        finalList.pop(little[0])
    wrongList = wrongList[ : :-1]       #再倒序回来是为了打印的时候更符合常人的阅读习惯
    if len(wrongList) > 0 and WRONGLISTNOTIFY == 1:
        print('These datas have problems when reading the file. In order to avoid bugs, we have ignored it.')
        for little in wrongList:
            print('The line:',little[0]+1,little[1],sep=' ')
    return finalList
