from math import *

def Pindala(a:float,b:float)->float:
    '''Riistküliku pindala leidmine
    :param float a:Riistküliku esemine külg
    :param float b:Riistküliku teine külg
    :rtype:float
    '''
    S=a*b
    return S

def arithmetic(x:float,y:float,z:str):
    '''Saab teha +,-,*,/ ja tagastab arv, kui vaastus on arv ja "Tundmatu tehe", kui ei saa vaastus leida.
    :param float x: Esimine arv
    :param float y: Teine arv
    :param str z: Aritmeetile tehe
    :rtype:var
    '''
    if z=="+":
        vaastus=x+y
    elif z=="-":
        vaastus=x-y
    elif z=="*":
        vaastus=x*y
    elif z=="/":
        if y==0:
            vaastus="Tundmatu tehe"
        else:
            vaastus=x/y
    else:
        vaastus="Неизвестная операция"
    return vaastus

def is_year_leap(year:int)->bool:
    '''
    :param int year:
    :rtype:bool
    '''
    if year%4==0:
        return True
    else:
        return False

def square(a:float)->float:
    '''
    :param float a:
    :rtype:float
    '''
    P=a*4
    S=a*a
    d=round(sqrt(a**2+a**2),2)
    return P, S, d

def season(month:int)->str:
    '''
    :param int month:
    :rtype:str
    '''
    talv=[1,2,12]
    kevad=[3,4,5]
    suvi=[6,7,8]
    sugis=[9,10,11]
    if month in talv:
        season="talv"
    elif month in kevad:
        season="kevad"
    elif month in suvi:
        season="suvi"
    elif month in sugis:
        season="sugis"
    return season

def bank(a:int,years:int)->float:
    '''
    :param int a:
    :param int years:
    :rtype:float
    '''
    for i in range(years):
        x=a*10/100
        a+=x
    return round(a)

def is_prime(arv:int)->bool:
    '''
    :param int arv:
    :rtype:bool
    '''
    if arv in list(range(1000+1)):
        return True
    else:
        return False

def date(day:int,month:int,year:int)->bool:
    '''
    :param int day:
    :param int month:
    :param int year:
    :rtype:bool
    '''
    





