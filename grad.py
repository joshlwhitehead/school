
wage = 23
yearCurrent = 25000
semCurrent = wage*15*4*4
gradLongMonths = 44
semLate = wage*40*4*4
lateGradSal = wage*40*4*12
estGradSal = 70000

def current_2026():
    return yearCurrent + 2*semCurrent + 2.5*estGradSal

def lateGrad():
    return 3*lateGradSal + 2*semLate + .5*estGradSal

print(lateGrad()-current_2026())
print(wage*40*4*12)
