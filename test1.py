
import matplotlib.pyplot as plt 
import numpy as np 

def linear_regression(x,y):
    n=np.size(x)
    m_x,m_y=np.mean(x),np.mean(y)
    ss_xy=np.sum(y*x)-n*m_x*m_y
    ss_xx=np.sum(x*x)-n*m_x*m_x

    b1=ss_xy/ss_xx
    b0=m_y-b1*m_x

    return b0,b1

# x=[]
# y=[]
# a=a[3:-3].split()

    
# for i in range(len(a)):
#     if i%3==0:
#         x.append(float(a[i]))
#     if i%3==1:
#         y.append(float(a[i]))

# x=np.array(x)
# y=np.array(y)

# b0,b1=linear_regression(x,y)

# plt.scatter(x,y,color='m',marker='o',s=30)
# y_pred=b0+b1*x
# plt.plot(x,y_pred,color="g")

# plt.xlabel('x')
# plt.ylabel('y')
# plt.show()

from sklearn.model_selection import train_test_split
from sklearn import datasets, linear_model, metrics 
  
# load the boston dataset 
boston = datasets.load_boston(return_X_y=False) 
  
# defining feature matrix(X) and response vector(y) 
X = boston.data 
y = boston.target 
  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=1)


# create linear regression object 
reg = linear_model.LinearRegression() 
  
# train the model using the training sets 
reg.fit(X_train, y_train) 
  
# regression coefficients 
print('Coefficients: \n', reg.coef_) 
  
# variance score: 1 means perfect prediction 
print('Variance score: {}'.format(reg.score(X_test, y_test))) 
  
# plot for residual error 
  
## setting plot style 
plt.style.use('fivethirtyeight') 
  
## plotting residual errors in training data 
plt.scatter(reg.predict(X_train), reg.predict(X_train) - y_train, 
            color = "green", s = 10, label = 'Train data') 
  
## plotting residual errors in test data 
plt.scatter(reg.predict(X_test), reg.predict(X_test) - y_test, 
            color = "blue", s = 10, label = 'Test data') 
  
## plotting line for zero residual error 
plt.hlines(y = 0, xmin = 0, xmax = 50, linewidth = 2) 
  
## plotting legend 
plt.legend(loc = 'upper right') 
  
## plot title 
plt.title("Residual errors") 
  
## function to show plot 
plt.show() 