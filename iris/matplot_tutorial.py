import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#https://matplotlib.org/3.1.1/tutorials/introductory/pyplot.html

#Just plots y and then x-axis data:
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
# plt.show()
plt.close()

#3rd argyment in plot specificed colour and line type
# plt.axis specifies xmin, xmax, ymin, ymax
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
plt.axis([0, 6, 0, 20])
plt.show()
plt.close()


# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()
plt.close()


#data is a keyword argument in matplotlib. Can generate graphs from variables using strings. Can see keyword "data" in blue below
data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

plt.scatter('a', 'b', c='c', s='d', data=data)
plt.xlabel('entry a')
plt.ylabel('entry b')
plt.show()
plt.close()

#example showing how to pass categorical variables. The plt.subplot must be an integer
names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]

plt.figure(figsize=(9, 3))

plt.subplot(131)
plt.bar(names, values)
plt.subplot(132)
plt.barh(names, values)
plt.show()
plt.close()

plt.clf()

#can set lots of line attributes: https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D
#below example is how to set attribues to 4 graphs (x1, y1 etc)
# lines = plt.plot(x1, y1, x2, y2)
# # use keyword args
# plt.setp(lines, color='r', linewidth=2.0)
# # or MATLAB style string value pairs
# plt.setp(lines, 'color', 'r', 'linewidth', 2.0)


# Matplotlib automatically remembers current axes. So the two graphs below will have the same X and Y axis values
#n.b. the number inside plt.subplot(abc) a=number of rows, b=number of columns, c=index position. This refers to where the graph is, not relating to the data in the graph
# plt.figure denotes the figure. Can have as many sub plots in a figure as you want. Each time you call plt.figure, it starts a new figure for subplots
def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure(1)
plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')
plt.show()

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.title("my title", color="red", fontsize=13)
plt.xlabel("this is my x label")
plt.ylabel("this is my y")
plt.grid(True) #adds gridlines
plt.show()
plt.close()


# example of annotations. 1) the text to show, 2) the location to point to, 3) the location of the text, 4) arrow composition
plt.figure(3)
ax = plt.subplot(111)

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
line, = plt.plot(t, s, lw=2)

plt.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
             arrowprops=dict(facecolor='black', shrink=0.05),
             )

plt.ylim(-2, 2)
plt.show()