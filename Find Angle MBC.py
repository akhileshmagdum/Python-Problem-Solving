from math import degrees,atan #importing degree conversion function and atan returns tangent
ab = int(input())
bc = int(input())
m = atan((1.0)*ab/bc) #getting the tangent in radian
print(str(int(round(degrees(m))))+'°') #str to append ° int and round for rounding degrees for coversion