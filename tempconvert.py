import time

global c, f, k
c = 32
f = 1.8
k = 273.15


def convCToF():
    # convert formula for C to F: (deg * 1.8) + 32
    print('Please input the degree(s) you would like to convert:'); degCToF = float(input('')); time.sleep(1)
    ans = float((degCToF * f) + c)
    ansFin = round(ans, 0)
    print(f'The degree is: {ansFin}'); time.sleep(35)

def convCToK():
    # convert formula for C to K: deg + 273.15  
    print('Please input the degree(s) you would like to convert:'); degCToK = float(input('')); time.sleep(1)
    ans = float(degCToK + k)
    ansFin = round(ans, 2)
    print(f'The degree is: {ansFin}'); time.sleep(35)

def convFToC():
    # convert formula for F to C: (deg - 32) / 1.8
    print('Please input the degree(s) you would like to convert:'); degFToC = float(input('')); time.sleep(1)
    ans = float((degFToC - c) / f)
    ansFin = round(ans, 2)
    print(f'The degree is: {ansFin}'); time.sleep(35)

def convFToK():
    # convert formula for F to K: (deg - 32) * 5/9 + 273.15
    print('Please input the degree(s) you would like to convert:'); degFToK = float(input('')); time.sleep(1)
    ans = float((degFToK - c) * 5/9 + k)
    ansFin = round(ans, 2)
    print(f'The degree is: {ansFin}'); time.sleep(35)

def convKToF():
    # convert formula for K to F: (deg - 273.15) * 9/5 + 32
    print('Please input the degree(s) you would like to convert:'); degKToF = float(input('')); time.sleep(1)
    ans = float((degKToF - k) * 9/5 + c)
    ansFin = round(ans, 2)
    print(f'The degree is: {ansFin}'); time.sleep(35)

def convKToC():
    # convert formula for K to C: deg - 273.15
    print('Please input the degree(s) you would like to convert:'); degKToC = float(input('')); time.sleep(1)
    ans = float(degKToC - k)
    ansFin = round(ans, 2)
    print(f'The degree is: {ansFin}'); time.sleep(35)


def welcome():
    print('Welcome! What are we converting today?'); time.sleep(1)
    ask = input('')
    if ask.lower() in ['kelvin', 'k']:
        ask = 'k'; time.sleep(1)
        pass
    elif ask.lower() in ['fahrenheit', 'f']:
        ask = 'f'; time.sleep(1)
        pass
    elif ask.lower() in ['celsius', 'c']:
        ask = 'c'; time.sleep(1)
        pass
    else:
        print('Invalid input. Please enter Kelvin, Fahrenheit, or Celsius.'); time.sleep(1); welcome()
        return
    if ask in ['k', 'kelvin']:
        ask2 = input('Do you want to convert K to F, or K to C?\n'); time.sleep(1)
        if ask2.lower() == 'kf':
            convKToF()
        elif ask2.lower() == 'kc':
            convKToC()
        else:
            print('Invalid input. Please enter KF or KC.'); time.sleep(1)
            return
    elif ask in ['f', 'fahrenheit']:
        ask2 = input('Do you want to convert F to C, or F to K?\n'); time.sleep(1)
        if ask2.lower() == 'fc':
            convFToC()
        elif ask2.lower() == 'fk':
            convFToK()
        else:
            print('Invalid input. Please enter FC or FK.'); time.sleep(1)
            return
    elif ask in ['c', 'celcius']:
        ask2 = input('Do you want to convert C to F, or C to K?\n'); time.sleep(1)
        if ask2.lower() == 'cf':
            convCToF()
        elif ask2.lower() == 'ck':
            convCToK()
        else:
            print('Invalid input. Please enter CF or CK.'); time.sleep(1)
            return
    else:
        print('Invalid input. Please enter K, F, or C.'); time.sleep(1); welcome()
        return
    
welcome()