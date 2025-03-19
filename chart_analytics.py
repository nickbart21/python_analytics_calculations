import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame
import numpy as np

df = pd.read_csv(r'mtcars.csv')

#----------- Part 1 ------------

fig1 = plt.figure(1)
plt.hist(df.mpg, bins=5, density = 0, color = 'r', edgecolor = 'b')
plt.xlabel('MPG')
plt.ylabel('Number of Cars')
plt.title('MPG Histogram')

#----------- Part 2 ------------

fig2 = plt.figure()
plt.scatter(df.mpg, df.hp, s = 5, c = 'b')
plt.ylabel('HP')
plt.xlabel('MPG')
plt.title('MPG vs. HP')

#----------- Part 3 ------------

dfscattermatrix = DataFrame(np.random.randn(100, 5), columns=['disp', 'hp', 'drat', 'wt', 'qsect'])
plt.style.use('classic')
pd.plotting.scatter_matrix(dfscattermatrix, s = 60, diagonal = 'kde')

#----------- Part 4 ------------

dfboxplots = DataFrame(np.random.randn(100, 5), columns=['disp', 'hp', 'drat', 'wt', 'qsect'])
dfboxplots_sub = dfboxplots.iloc[:, 0:5]
dfboxplots_sub.plot.box(color = 'red', sym = 'r+')
dfboxplots_sub.boxplot()


#----------- Part 5 ------------

plt.figure()
plt.scatter(df.mpg, df.hp, s = 5, c = 'b')
plt.ylabel('HP')
plt.xlabel('MPG')
plt.title('MPG vs. HP')

plt.figure()
plt.scatter(df.mpg, df.cyl, s = 5, c = 'b')
plt.ylabel('Cyl')
plt.xlabel('MPG')
plt.title('MPG vs. Cyl')

plt.figure()
plt.scatter(df.mpg, df.disp, s = 5, c = 'b')
plt.ylabel('Disp')
plt.xlabel('MPG')
plt.title('MPG vs. Disp')

plt.figure()
plt.scatter(df.mpg, df.wt, s = 5, c = 'b')
plt.ylabel('Wt')
plt.xlabel('MPG')
plt.title('MPG vs. Wt')

plt.figure()
plt.scatter(df.mpg, df.qsec, s = 5, c = 'b')
plt.ylabel('Qsec')
plt.xlabel('MPG')
plt.title('MPG vs. Qsec')

plt.figure()
plt.scatter(df.mpg, df.gear, s = 5, c = 'b')
plt.ylabel('Gear')
plt.xlabel('MPG')
plt.title('MPG vs. Gear')

plt.figure()
plt.scatter(df.mpg, df.carb, s = 5, c = 'b')
plt.ylabel('Carb')
plt.xlabel('MPG')
plt.title('MPG vs. Carb')

plt.show()

print("Looking at the plots, the wt appears to have the most impact on mpg.")