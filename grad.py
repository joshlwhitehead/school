
wage = 25

yearCurrent = 20000
semCurrent = wage*15*4*4
gradLongMonths = 44
semLate = wage*40*4*4
lateGradSal = wage*40*4*12
estGradSal = 70000

def current_lateGrad():
    return yearCurrent + 2*semCurrent + 2.5*estGradSal

def lateGrad():
    return 3*lateGradSal + 2*semLate + .5*estGradSal

print('full vs part: ',lateGrad()-current_lateGrad())
print('yearly wage: ',wage*40*4*12)
