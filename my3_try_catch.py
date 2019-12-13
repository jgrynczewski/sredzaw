import math

def circle_area(r):
    #r= float(r)
    if r >=0:
        return math.pi*r**2
    else:
        print ("promień musi być dodatni")

raw_r=input("Podaj primień koła: ")  #if not raw_r.isnumeriprint("Nie podałeś poprawnej wartosci")
try:
    r=float(raw_r)
    if(r < 0 ):
        print("Promień nie może być ujemy")
    else:
        area = circle_area(r)
        print(f'pole koła o promieniu {r} wynosi {round(area,2)}')
except:
    print("Podano niepoprawną wartość")

