import matplotlib.pyplot as plt


# 2 different graphs plotting

# x1 = [2, 4, 5, 6]
# y1 = [2, 3, 6, 7]

# plt.plot(x1, y1, label = 'Line 1')

# x2 = [1, 2, 3, 4]
# y2 = [1, 2, 3, 4]

# plt.plot(x2, y2, label = 'Line 2')

# plt.xlabel('X Axis')

# plt.ylabel('Y Axis')

# plt.title('Demo Graph - Two Lines')

# plt.legend()

# plt.show()


# Custom graph plotting

# x = [2, 4, 5, 6]
# y = [2, 3, 6, 7]

# plt.plot(x, y, color = 'green', linestyle = 'dashed', linewidth = 3, marker = 'o', markerfacecolor = 'blue', markersize = 12)

# plt.ylim(1, 8)
# plt.xlim(1, 8)

# plt.xlabel('X Axis')
# plt.ylabel('Y Axis')

# plt.title('Demo Graph - Customization')

# plt.show()


# Bar chart plotting

left = [1, 2, 3, 4, 5]
right = [10, 11, 23, 36, 4]

tick_label = ['one', 'two' , 'three', 'four', 'five']

plt.bar(left, right, tick_label = tick_label, width = 0.8, color = ['blue', 'orange'])

plt.xlabel('X Axis')
plt.ylabel('Y Axis')

plt.title('Demo Graph - Bar Chart')

plt.show()