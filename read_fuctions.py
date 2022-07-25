#读取文件所需要的函数
import sys , json
import change_fuctions , choose_fuctions

def readJsonFile():
    '''读取JSON文件'''
    try:
        askedFile = open('./JsonDatas/MainFile.json','rt',encoding='utf-8')
    except:
        print('We can"t find the "./JsonDatas/MainFile.txt" file! Please make sure the file is here and try again!')
        return 'EXIT'
    waitString = askedFile.read()
    askedFile.close()
    dataDict =json.loads(waitString)
    return dataDict

def scanCycle(startDict):
    while True:
        judgeList = scanDict(startDict)
        if judgeList[1] == 0:
            print('The value attribute of the dictionary mixes dictionaries and strings.\n \
                So we keep the dictionary, the string will not be recognized.')
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

def readTxtFile():
    try:
        askedFile = open('./TxtDatas/MainFile.txt','rt',encoding='utf-8')
    except:
        print('We can"t find the "./TxtDatas/MainFile.txt" file! Please make sure the file is here and try again!')
        return 'EXIT'       
    waitString = askedFile.read()
    askedFile.close()
    try:
        finalString = waitString.replace(' ',',')
        waitList = finalString.split("\n")
        finalList = []
        for littleList in waitList:
            finalList.append(littleList.split(','))
    except:
        print('ERROR!')
        print('There is a question whose reason is that the "Mainfile.txt" have some format problems.')
        print("Please check your file's format!")
        return 'EXIT'
    return finalList
