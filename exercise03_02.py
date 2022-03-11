hrs = input("Enter Hours:")
try :
    h = float(hrs)
except :
    print('Error, please enter numeric value')
    quit()
try :
    rate = input("Enter Rate:")
    r = float(rate)
except :
    print('Error, please enter numeric value')
    quit()
#print(h, r)
if h > 40:
    #print("Overtime")
    reg = h * r
    otp = (h-40.0) * (r * 0.5)
    #print(reg, otp)
else :
    print("Regular")
    reg = h * r
    otp = 0
pay = reg + otp
print(pay)