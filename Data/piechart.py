# number of the medals women received: 239
# number of the medals men received:386

from matplotlib import pyplot as plt
fig = plt.figure(figsize = (12,12))
ax = fig.add_subplot(111)
ax.axis('equal')
values = [239, 386]
labels = ["Women", "Men"]
colors = ["red", "blue"]
explode = (0, 0.03)
ax.set_title('Percentage of Medals Received by Gender', pad="20", fontsize = 24)
ax.pie(values, labels = labels,autopct='%3.0f%%', colors=colors, explode= explode, textprops={'fontsize': 24})
plt.show()