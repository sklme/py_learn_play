import numpy as np
import matplotlib.pyplot as plt

# 定义三次函数
def cubic_function(x):
    return x**3 - 3*x**2 + 2*x + 1

# 定义泰勒展开式的拟合函数（在x=0处展开）
def taylor_approximation(x):
    # 三次函数在x=0处的泰勒展开式
    # f(x) = f(0) + f'(0)x + f''(0)x^2/2! + f'''(0)x^3/3!
    f0 = cubic_function(0)
    f1 = 2  # f'(0) = 2
    f2 = -6  # f''(0) = -6
    f3 = 6  # f'''(0) = 6
    return f0 + f1*x + f2*x**2/2 + f3*x**3/6

# 生成x值
# x = np.linspace(-2, 3, 400)
x = np.linspace(0, 1000, 400)

# 计算y值
y_cubic = cubic_function(x)
y_taylor = taylor_approximation(x)

# 绘制图像
plt.figure(figsize=(10, 6))
plt.plot(x, y_cubic, label='Cubic Function', color='blue')
plt.plot(x, y_taylor, label='Taylor Approximation at x=0', color='red', linestyle='--')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()
plt.title('Cubic Function and its Taylor Approximation at x=0')
plt.xlabel('x')
plt.ylabel('y')
plt.show()