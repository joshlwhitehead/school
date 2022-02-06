
wage = 19
yearCurrent = 25000
semCurrent = wage*15*4*4
gradLongMonths = 44
semLate = wage*40*4*4
lateGradSal = wage*40*4*12
estGradSal = 60000

def current_2026():
    return yearCurrent + 2*semCurrent + 1.5*estGradSal

def lateGrad():
    return 2*lateGradSal + 2*semLate + 1.5*estGradSal

print(current_2026()-lateGrad())
# print(lateGradSal)