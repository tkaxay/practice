from ast import While

def addition(a,b):
    return a+b
def  subtraction(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

while True:
    c = input("enter your operation\n1 addition \n2 subtraction \n3 multiply \n4 divide")
    if c in ('1','2','3','4'):
        a = int(input('enter number 1 :'))
        b = int(input('enter number 2 :'))

        if c=='1':
            print(addition(a,b))
        elif c=='2':
            print(subtraction(a,b))
        elif c=='3':
            print(multiply(a,b))
        elif c=='4':
            print(divide(a,b))


        next_calcution = input("yes to continue no to exit ")
        if next_calcution == 'no':
            break

    else:
        print('invalid input !')