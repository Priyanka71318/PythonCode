x=eval(input("Enter a N0. = "))
match x:
    case 1.1:
        print("one")
    case 3+4j:
        print("Two")
    case [1,2,3]:
        print("Three")
    case True:
        print("Four")
    case _:
        print("Invalid value")       

print("outside match")
