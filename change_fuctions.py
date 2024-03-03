#change_fuctions文件用来存储转换函数

def dictToList(finalDict):
    """
    将字典转换为列表
    """
    finalList = []
    startList = finalDict.items()
    for object in startList:
        finalList.append(list(object))
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
    """
    keyList函数：将列表的子列表(key , value)转换为（数字：key）的形式
    """
    i = 1
    List = []
    for littleList in list:
        list = [i ,littleList[0]]
        List.append(list)
        i += 1
    return List
