 
import pandas as pd
import numpy as np

#df = pd.DataFrame(list(Vaksinasi.objects.all().values()))

df = pd.read_csv('home_vaksinasi.csv',sep=',')
print(df.columns)

df1 = df.groupby(['year']).sum()

print()

import matplotlib.pyplot as plt
 
  
def estimate_coef(x, y):
    # number of observations/points
    n = np.size(x)
 
    # mean of x and y vector
    m_x = np.mean(x)
    m_y = np.mean(y)
 
    # calculating cross-deviation and deviation about x
    SS_xy = np.sum(y*x) - n*m_y*m_x
    SS_xx = np.sum(x*x) - n*m_x*m_x
 
    # calculating regression coefficients
    b_1 = SS_xy / SS_xx
    b_0 = m_y - b_1*m_x
 
    return (b_0, b_1)
 
  
def plot_regression_line(x, y, b):
    # plotting the actual points as scatter plot
    plt.scatter(x, y, color = "m",
               marker = "o", s = 30)
 
    # predicted response vector
    y_pred = b[0] + b[1]*x
 
    # plotting the regression line
    plt.plot(x, y_pred, color = "g")
 
    # putting labels
    plt.xlabel('x')
    plt.ylabel('y')
 
    # function to show plot
    plt.show()
 
def main():
    # observations / data

    x = df1.index.values
    y = df1.vac_able.values

    # estimating coefficients
    b = estimate_coef(x, y)
    print("Estimated coefficients:\nb_0 = {}  \
          \nb_1 = {}".format(b[0], b[1]))
 
    # plotting regression line
    plot_regression_line(x, y, b)

    # predict data for 2021
    x_new = 2021
    y_pred = b[0] + b[1]*x_new
    
    print("2021",y_pred)
    
    x = np.append(x, x_new)
    y = np.append(y, y_pred)
    print(x)
    plot_regression_line(x, y, b)

    
  
if __name__ == "__main__":
    main()
 
