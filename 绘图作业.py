import matplotlib.pyplot as plt#导入matplotlib.pyplot模块，这是用于绘图的库
import numpy as np# 导入numpy模块，这是用于进行数值计算的库
#准备数据
x = np.linspace(0, 10, 100)# 生成一个0到10之间的100个数的数组，用于x轴
y_line = np.sin(x) # 计算x的正弦值，用于后续的折线图
y_bar = np.random.randint(1, 10, size=5) # 生成一个1到10之间的5个随机整数数组，用于条形图的高
x_bar = np.arange(1, 6) # 生成一个1到5的整数数组，用于条形图的x轴位置
y_scatter = np.random.rand(50)# 生成一个包含50个0到1之间随机小数的数组，用于散点图的y坐标
x_scatter = np.random.rand(50) #生成一个包含50个0到1之间随机小数的数组，用于散点图的x坐标

# 创建一个2x2的子图布局
fig, axs = plt.subplots(2, 2) # 创建一个图形对象fig和一个2x2的子图数组axs

# 第一个子图：折线图
axs[0, 0].plot(x, y_line, color='pink', label='sin(x)')# 在子图(0,0)上绘制橙色的正弦折线图
axs[0, 0].set_title('Line Chart')# 设置子图(0,0)的标题为"Line Chart"
axs[0, 0].set_xlabel('X-axis')  # 设置子图(0,0)的x轴标签为"X-axis"
axs[0, 0].set_ylabel('Y-axis')  # 设置子图(0,0)的y轴标签为"Y-axis"
axs[0, 0].legend()  # 在子图(0,0)上显示图例

# 第二个子图：条形图
axs[0, 1].bar(x_bar, y_bar, color='green', label='Random Bars')  # 在子图(0,1)上绘制绿色的条形图
axs[0, 1].set_title('Bar Chart')  # 设置子图(0,1)的标题为"Bar Chart"
axs[0, 1].set_xlabel('Categories')  # 设置子图(0,1)的x轴标签为"Categories"
axs[0, 1].set_ylabel('Values')  # 设置子图(0,1)的y轴标签为"Values"
axs[0, 1].legend()  # 在子图(0,1)上显示图例

# 第三个子图：散点图
axs[1, 0].scatter(x_scatter, y_scatter, color='lightblue', label='Random Points')  # 在子图(1,0)上绘制红色的散点图
axs[1, 0].set_title('Scatter Plot')  # 设置子图(1,0)的标题为"Scatter Plot"
axs[1, 0].set_xlabel('X-axis')  # 设置子图(1,0)的x轴标签为"X-axis"
axs[1, 0].set_ylabel('Y-axis')  # 设置子图(1,0)的y轴标签为"Y-axis"
axs[1, 0].legend()  # 在子图(1,0)上显示图例

# 第四个子图：直方图
axs[1, 1].hist(y_scatter, bins=8, color='orange', label='Histogram')  # 在子图(1,1)上绘制紫色的直方图，分为8个bin
axs[1, 1].set_title('Histogram')  # 设置子图(1,1)的标题为"Histogram"
axs[1, 1].set_xlabel('Value')  # 设置子图(1,1)的x轴标签为"Value"
axs[1, 1].set_ylabel('Frequency')  # 设置子图(1,1)的y轴标签为"Frequency"
axs[1, 1].legend()  # 在子图(1,1)上显示图例

# 调整子图间距
plt.tight_layout()  # 自动调整子图参数，使之填充整个图像区域

# 显示图形
plt.show()  # 显示整个图形界面