import matplotlib.pyplot as plt
import numpy as np
import random
import math

print ("BODY RECOMPOSITION - macro split DIET PLAN \n")
x_array = [2380, 2600, 2840]
'''
with open('../sampled_data/input.txt', 'r') as f:
    for line in f:
        x_array.append(line.strip())

print(len(x_array))
'''
count = 0
for x in x_array:
    
    count = count +1 
    c = 0.4 * x
    p = 0.3 * x
    f = 0.3 * x
    print ("\n count ", count, " calorie intake", x)
    print("Start point \n carbs",c,"\n protein", p, '\n fat', f )
    print("\n gm Intake \n carbs",c/4,"\n protein", p/4, '\n fat', f/9 )
    
    c1 = 0.5 * x
    p1 = 0.3 * x
    f1 = 0.2 * x
    print("CArbohydrate refeed day \n carbs",c1,"\n protein", p1, '\n fat', f1 )
    print("\n gm Intake \n carbs",c1/4,"\n protein", p1/4, '\n fat', f1/9 )
# carb refeed day - do it on day of MIIT/HIIT training or leg or abs day