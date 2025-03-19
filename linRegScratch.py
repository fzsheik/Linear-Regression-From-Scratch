import sys
sys.path.append('path/to/venv/lib/python3.13/site-packages')

import pandas as pd
import matplotlib.pyplot as mp

data = pd.read_csv('dataset.csv') #just intaking the mock data set

print(data)
mp.scatter(data.study_hours, data.test_score)
mp.show()

def gradient_descent(current_m, current_b, points, learning_rate): 
#gradient descent is the alogorithm of basically taking each point seperatly and coming up with a m and b, 
#the learning rate basically tells how much we adjust, smaller means more slow and steady, larger means more big chnages, more risky
#but over time we should develop a pretty good line of best fit from adjusting the m and b over time

    m_grad = 0
    b_grad = 0

    n =  len(points)

    for i in range(n):
        x = points.iloc[i].study_hours
        y = points.iloc[i].test_score

        m_grad += -(2/n) * x * (y - (current_m * x + current_b))
        b_grad += -(2/n) * (y - (current_m * x + current_b))

    m = current_m - m_grad * learning_rate
    b = current_b - b_grad * learning_rate

    return m, b

m = 0 
b = 0 
epoch = 100 #number of points we going through
learningRate = 0.01

for i in range(epoch):
    m, b = gradient_descent(m, b, data, learningRate)

print(m, b)

mp.scatter(data.study_hours, data.test_score, color="black")
mp.plot(list(range(0, 15)), [m * x + b for x in range(0, 15)])
mp.show()



