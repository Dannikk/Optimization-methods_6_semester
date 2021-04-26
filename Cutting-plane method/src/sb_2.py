import numpy as np
import matplotlib.pyplot as plt
import math as m


# наша функция
u, v = np.mgrid[-0.5:0.5:20j, -1.5:-0.5:20j]
# u, v = np.mgrid[0:0.5:20j, -2.7:-2.2:20j]
x = u
y = v
z = 4 * u ** 2 + v ** 2 + np.cos(3 * u + 3 * v) - u + 2 * v
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(x, y, z, color='r')

# 10x - 7y = 11
v_, t = np.mgrid[-3.5:0.5:10j, -2:2:20j]
x1 = (11 + 7 * v_) / 10
y1 = v_
z1 = t
# ax.plot_wireframe(x1, y1, z1)

# -5x - 3y = 4
x2 = (-4 - 3 * v_) / 5
y2 = v_
z2 = t
# ax.plot_wireframe(x2, y2, z2)

# -x - 5*sqrt(-y - 0.7) + 2 = 0
y_n, z_n = np.mgrid[-1.2:-0.7:10j, -2:2:20j]
x_n = -5*np.sqrt(-y_n - 0.7) + 2
# ax.plot_wireframe(x_n, y_n, z_n, color='b')

# -z = 3
x3 = u
y3 = v
z3 = np.full(shape=x3.shape, fill_value=-3)
# ax.plot_wireframe(x3, y3, z3, color='y')

# z = 0
# позже

# y = -0.7
x4, z4 = np.mgrid[-2:2:10j, -2:2:20j]
y4 = np.full(shape=x4.shape, fill_value=-0.7)
# ax.plot_wireframe(x4, y4, z4, color='r')

# a_k =  [-2.9287001095920346, -3.4671616480535734, -1]  b_k =  6.2122932003238756
# -2.9287 * x - 3.46716 * y - z = 6.21229
x5, z5 = np.mgrid[-1:1.5:10j, -3:2:20j]
y5 = (-2.9287*x5 - z5 - 6.21229) / 3.46716
ax.plot_wireframe(x5, y5, z5, color='b')

#  a_k =  [2.692891337531031, 1.090979282507726, -1] b_k =  1.3062074224483733
y6, z6 = np.mgrid[-1.7:-0.5:25j, -3:2:20j]
x6 = (1.3062074 + z6 - 1.0909792*y6) / 2.692891
ax.plot_wireframe(x6, y6, z6, color='cyan')


# [ 0.09576339013, -1.116946441] - point
ax.plot(0.09576339013, -1.116946441, -2, marker="o", color='b')
# [0.07692308 -1.46153846 -3.00] - point_1
ax.plot(0.07692308, -1.46153846, -3.00, marker="*", color='r')
#  [ 0.28370512 -1.16613554 -3.        ] - point_2
ax.plot(0.28370, -1.16613554, -3.0, marker="s", color='b')
# [-0.30514262 -0.7        -2.89160883]
ax.plot(-0.30514262, -0.7, -2.89160883, marker="o", color='r')


plt.xlabel("x")
plt.ylabel("y")
# ax.legend("Graphik")
plt.show()
