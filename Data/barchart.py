# Number of the gold medals:220
# Number of the silver medals:96
# Number of the bronze medals:35

import matplotlib.pyplot as plt

fig = plt.figure(figsize = (6,12))
ax = fig.add_subplot(111)
labels = ['Gold', 'Silver', 'Bronze']
values = [220,96,35]
ax.bar(labels,values)
ax.get_children()[0].set_color('Gold')
ax.get_children()[1].set_color('Silver') 
ax.get_children()[2].set_color((0.804,0.498,0.196))
ax.set_title('Number of medals received in ice hockey', pad='20')
for i, v in enumerate(values):
    ax.text(-0.05 + i, v + i, str(v), color='blue', fontweight='bold', fontsize = 18)
plt.show()



