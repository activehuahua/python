import math

import pandas as pd

field_names = ['场地1', '场地2', '场地3', '场地4']
round_names =[]
player_names_A = ['A1', 'A2', 'A3', 'A4','A5', 'A6', 'A7']
player_names_B = ['B1', 'B2', 'B3', 'B4',  'B5', 'B6', 'B7']
matchups = []
totalCount=0

'''获取轮次数'''
def getRoundCount():
    count_group_A=len(player_names_A)
    count_group_B=len(player_names_B)
    totalCount=count_group_A*count_group_B
    roundCount=math.ceil(totalCount/len(field_names))
    return  roundCount

'''获取轮数名称'''
def getCoundNames(roundCount):
    round_names=[]
    for index in range(roundCount):
        round_names.append('第'+str(index+1)+'轮')
    return round_names

'''获取所有对局数'''
def getAllMatchups(player_names_A,player_names_B,field_names):
    matchups = []
    for index_a in range(len(player_names_A)):
        result = player_names_A[index_a:] + player_names_A[0:index_a]
        for index_b in range(len(player_names_B)):
            matchups.append(result[index_b]+":"+player_names_B[index_b])
    print(len(matchups))
    return matchups

'''输出到excel中'''
def export2Excel(matchups,field_names,round_names):
    df = pd.DataFrame(columns=field_names, index=round_names)
    index=0
    for round_index, round_name in enumerate(round_names):
        for field_index, field_name in enumerate(field_names):
            df.at[round_name, field_name] = matchups[index]
            print("[index=%d],%s"%(index,matchups[index]))
            index=index+1
            if index>=totalCount :
                matchups.append('')

    df.to_excel('秩序表.xlsx')

if __name__ == '__main__':
    roundCount=getRoundCount()
    print(roundCount)
    matchups=getAllMatchups(player_names_A,player_names_B,field_names)
    # print(matchups[0])
    round_names=getCoundNames(roundCount)
    export2Excel(matchups,field_names,round_names)