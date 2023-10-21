#choose_fuctions文件，用来存储选择功能的功能所需要的函数
import change_fuctions

def askDict(Dict):
    '''
    scanCycle函数的必要部分
    '''
    print('Choose a Grope which you want to choose:')
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
                print('Please check and input the true answer!')
                continue
        except:
            if choose == 'q':
                return 'EXIT'
            else:
                print("Your answer isn't defined!")
    return List[choose - 1][1]


