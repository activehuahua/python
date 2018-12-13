import  string
def compute_fare(distance,times):
    distance=float(distance)
    times=process_time(times)
    Dis_Per=0.99
    Time_Per=0.17
    Bonus=0.3
    Bonus_Limit=15
    LDis_Per=0.45
    LDis_limit=15
    def base_fare():
        return distance*Dis_Per+times*Time_Per

    def long_bonus():
        if distance>15:
               return (distance-LDis_limit)*LDis_Per
        else:
               return 0
    def extra_bonus():
        a = Bonus*base_fare()
        if (a>Bonus_Limit):
            return  Bonus_Limit
        else:
            print(a)
            return a

    return base_fare()+long_bonus()+extra_bonus()

def process_time(times):
    try:
        if times.index(':')>0:
            list=times.split(':')
            times= float(list[1])/60+float(list[0])
        elif times.index('.')>0:
            list=times.split('.')
            times= float(list[1])/60+float(list[0])
    except: ValueError
    finally:
        return float(times)

while True:
    distance=input('Please input distance')

    if distance=='exit':
        break
    times=input('Please input times')
    print('The fare is %.2f'%(compute_fare(distance,times)))

