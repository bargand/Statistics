x = 3

match x:
    case 0:
        print("The X value is 0")
    case 3:
        print(f"The X value is {x}")
    case _:
        print(x)


def num(x):
    match x:
        case 0:
            print(f"The X value is {x}") 
        case 10:
            print(f"The X value is {x}")
        case 20:
            print(f"The X value is not 10 not 20")