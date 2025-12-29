# num1= int(input("enter a  num: "))
# num2= int(input("enter b num: "))

try:
    num1= int(input("enter a  num: "))
    num2= int(input("enter b num: "))
    result=num1/num2
    print(result)
except ZeroDivisionError:
    print("demoniter is zero")
except ValueError:
    print("input only digit")#input time int hoy ne biju nakhe  tyare
except IndexError:
    print("")