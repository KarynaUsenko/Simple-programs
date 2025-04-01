hrs = input("How many hours do you work?\n")
pay = input("How much do you get paid per hour?\n")
try:
    h = float(hrs)
except:
    h = float(input("Error, please enter numeric input:\n"))
try:
    p = float(pay)
except:
    p = float(input("Error, please enter numeric input:\n"))
if h <= 40:
    print('Your salary =', h*p)
else:
    #при понаднормових годинах (норма це 40) ставка кожної наступної години кратна 1.5 звичайної
    print('Your salary =', 40*p+((h-40)*1.5*p))
