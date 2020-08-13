while True:
    try:
        x = int(input("Enter Number1: "))
        y = int(input("Enter Number2: "))
        z = x // y
        print(z[0])
    except ValueError:
        print('Enter Valid number like: 12 , 13 ,')
    except ZeroDivisionError:
        print('Enter non zero number for divisor part')
    except Exception as e:
        print(e)
        print(type(e))
# try:
#     pass
# except:
#     pass
# finally:
#     pass

'''
Errors:
    Syntaxt Error
    
    RunTime Error
    
    LogicError
'''
