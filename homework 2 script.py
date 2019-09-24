
def distForm():
    #stores values of point
    x1 = float(input("Enter the x: "))
    y1 = float(input("Enter the y: "))
    z1 = float(input("Enter the z: "))
    #value of centroid, change as needed
    cx = 1.966
    cy = 9.866
    cz = 17.366
    #parts of distance formula
    dp1 = pow((cx - x1), 2)
    dp2 = pow((cy - y1), 2)
    dp3 = pow((cz - z1), 2)
    #returns distance formula results
    return dp1+dp2+dp3
def calAvg():
    num = int(input(" how many points are there"))
    Sum = 0
    for x in range(num):
        Sum += float(input("enter distance: "))  
    return Sum/num

#print(calAvg())
#for x in range(6):
print(distForm())
 
