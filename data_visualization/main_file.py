import matplotlib.pyplot as plt

# 进行简单的图形绘制
squares = [1, 4, 9, 16, 25]
plt.plot(squares)
# plt.show()

# 绘制更复杂一些的图像
plt.title("Square numbers", fontsize = 24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Square of value", fontsize = 14)
plt.tick_params(axis = 'both', labelsize = 14)
# plt.show()

# 校正图像
input_values = [1, 2, 3, 4, 5]
plt.plot(input_values, squares, linewidth = 5)

plt.title("Square numbers", fontsize = 24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Square of value", fontsize = 14)
plt.tick_params(axis = 'both', labelsize = 14)

# plt.show()
# 此时我们见到，先后绘制的曲线都绘制在了相同画布上
plt.close()

# 绘制散点图
plt.scatter(2, 4)
# plt.show()

plt.scatter(2, 4, s = 200)
# plt.show()

plt.close()
x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]
plt.scatter(x_values, y_values, s = 50)
# plt.show()
plt.close()

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, s = 30)
plt.axis([0, 1100, 0, 1100000])
# plt.show()
plt.close()
# 我们看到这些散点都连到了一起

# 进一步可以进行颜色映射，根据不同的值，生成不同颜色的点
x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values, c = y_values, edgecolors='none', s = 30)
# plt.show()
plt.close()

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values, c = y_values, cmap = plt.cm.Blues, edgecolors='none', s = 30)
plt.show()
plt.close()


