import numpy as np

def f(x):
    clipped_x = np.clip(x, -500, 500)  # 对输入进行截断
    return 1 / (np.exp(-clipped_x) + 1)

values = [-1000, -100, -10, -1, -0.1, -0.01, 0, 0.01, 0.1, 1, 10, 100, 1000]
for x in values:
    print(f(x))