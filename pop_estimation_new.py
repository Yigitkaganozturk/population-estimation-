# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 21:19:42 2022

@author: yiitk
"""

'''
the list a includes human population number on earth from 1950 to 2015. the data imported from the link below
https://tr.wikipedia.org/wiki/Ge%C3%A7mi%C5%9F_n%C3%BCfuslar%C4%B1na_g%C3%B6re_%C3%BClkeler_listesi_(Birle%C5%9Fmi%C5%9F_Milletler)
this program takes two number of population at different times and makes an estimation about the future number of population
'''
a='2,517,478   2,749,365	3,007,751	3,309,934	3,667,801	4,045,192	4,421,695	4,833,180	5,289,294	5,713,824	6,104,538	6,496,776	6,906,374	7,325,929'
b=''
c=[]
d=[]
e=[]
for i in a:
    if i != ',' and i !=  '\t' and i!= ' ' and i!='':
        b+=str(i)
    elif i==',':
        pass
    else:
        if b!='':
            b=int(b)
            c.append(b)
            b=''
        else:
            pass
for i in range(0,65,5):
    d.append(i)
for i in range(len(d)):
    f=[]
    f=[d[i],c[i]]
    e.append(f)
#start= the first number of population on earth 
#second_number(ikinci_deger)= the second number of population on earth
#(adım)time_difference=enter the time difference between the start year and the second_number
#estimation(yıl)= enter how many year after the second_number value of population you want the programme to estimate the number of population at that time
def pop_estimation(start,second_number,time_difference,estimation):
    estimated_number=start*((second_number/start)**(estimation/time_difference))
    return estimated_number
for i in range(len(e)-2):
    start=e[i][1]
    second_number=e[i+1][1]
    time_difference=e[i+1][0]-e[i][0]
    estimation=5
    g=pop_estimation(start,second_number,time_difference,estimation)
    h=abs(100*(g-e[i+2][1])/e[i+2][1])
    print(f'{g} is estimated number of population in {e[i+2][0]+1950}, {e[i+2][1]} is the real number in {e[i+2][0]+1950}, {h} is miscalculation percentage')
    print('-------------')