import random
import pandas as pd
from time import sleep

def makeAnnonyCode(code):
    return code[:6] + "***"

def makeAnnonyName(name):
    if(len(name)==2):
        return "*"+name[1]
    elif(len(name)==3):
        return name[0]+ "*" +name[2]
    elif(len(name) > 3):
        return name[:2] + "*" + name[3]    

def printInfo(df,random_list):
    for i in range(len(random_list)):
        sleep(0.5)
        grade = str(i + 1)+"번"

        index = random_list[i]
        name = makeAnnonyName(str(df[df.keys()[0]][index]))
        major = str(df[df.keys()[1]][index])
        code = makeAnnonyCode(str(df[df.keys()[2]][index]))
        
        print("{} / {} / {} / {}".format(grade, name, major, code))

def Lots(number):
    random_list = []
    rand_num = random.randint(0, count-1)
    for _ in range(number):
        while rand_num in random_list:
            rand_num = random.randint(0, count-1)
        random_list.append(rand_num)
    random_list.sort()
    return random_list

if __name__ == "__main__":
    print("*****************************************************")
    name = input("Excel Name : ")
    df = pd.read_excel(name + '.xlsx')
    print("*****************************************************")
    count = len(df.values)
    print("총 응답 개수 : " + str(count)+"개")
    print("*****************************************************")
    number = int(input("Lots Number : "))
    print(str(number)+"개를 추첨합니다")
    print("*****************************************************")
    random_list = Lots(number)
    printInfo(df,random_list)
    print("*****************************************************")

