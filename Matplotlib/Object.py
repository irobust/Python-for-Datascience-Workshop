import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot()
ax.set_title("Demo Matplotlib")
# fig.set_subtitle("with Object Oriented")

data = np.linspace(1,100,20)

ax.plot(data)
fig.show()

