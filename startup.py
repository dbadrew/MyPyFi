import matplotlib.pyplot as plt
import numpy as np

msg = 'hello workd'
print(msg)
msg.capitalize()
msg.split()

x = np.linspace(0, 20, 100)
plt.plot(x, np.sin(x))
plt.show()

