wage = 25

yearCurrent = 20000
semCurrent = wage*15*4*4
gradLongMonths = 44
semLate = wage*40*4*4
lateGradYear = wage*40*4*12
estGradSal = 70000

def current_lateGrad(timeAfter,fullYearBefore,semesterCount):
    return fullYearBefore*yearCurrent + semesterCount*semCurrent + timeAfter*estGradSal

def lateGrad(timeAfter,fullYearBefore,semesterCount):
    return fullYearBefore*lateGradYear + semesterCount*semLate + timeAfter*estGradSal

print('\nyou will have',lateGrad(.5,3,2)-current_lateGrad(2.5,1,2),'more dollars \n')
# print('yearly wage: ',wage*40*4*12)
