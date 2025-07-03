import matplotlib.pyplot as plt

data1 = [x*2  for x in range(1,11)]
data2 = [x**2 for x in range(1,11)]
data3 = [30,40,30]
data3_label = ['Product A', 'Product B', 'Product C']

sales = {
    'Product A': 30,
    'Product B': 40,
    'Product C': 30
}

# fig = plt.figure()

# ax1 = fig.add_subplot(2,2,1)
# ax2 = fig.add_subplot(2,2,2)
# ax3 = fig.add_subplot(2,2,3)
# ax4 = fig.add_subplot(2,2,4)

fig, (ax1, ax2) = plt.subplots(1,2, sharey=True)

ax1.plot(data1)
ax2.plot(data2)
# ax3.pie(x=data3, labels=data3_label)
# ax3.pie(x=sales.values(), 
#         labels=sales.keys(),
#         explode=[0.1, 0.1, 0.1],
#         autopct="%1.1f%%")
# ax4.barh(y= sales.keys(), width=sales.values())

plt.show()