import numpy as np
import matplotlib.pyplot as plt

# 定义原函数及其导数
def f(x):
    return x**3 - 3*x**2 + 2*x

def f_prime(x):
    return 3*x**2 - 6*x + 2

def f_double_prime(x):
    return 6*x - 6

def f_triple_prime(x):
    return np.full_like(x, 6)  # 创建一个与 x 具有相同维度的常数数组

# 定义x的范围
x = np.linspace(-1, 3, 400)

# 计算函数值及其导数值
y = f(x)
y1 = f_prime(x)
y2 = f_double_prime(x)
y3 = f_triple_prime(x)

# 绘制图形
plt.figure(figsize=(10, 8))

plt.subplot(4, 1, 1)
plt.plot(x, y, label='f(x) = x^3 - 3x^2 + 2x')
plt.title('Function and its Derivatives')
plt.legend()

plt.subplot(4, 1, 2)
plt.plot(x, y1, label="f'(x) = 3x^2 - 6x + 2", color='orange')
plt.legend()

plt.subplot(4, 1, 3)
plt.plot(x, y2, label="f''(x) = 6x - 6", color='green')
plt.legend()

plt.subplot(4, 1, 4)
plt.plot(x, y3, label="f'''(x) = 6", color='red')
plt.legend()

plt.tight_layout()
plt.show()