import matplotlib.pyplot as plt
 
#draw a simple line chart showing sport categories and number of medals
sports= ["Biathlon", "Bobsleigh", "Curling", "Ice Hockey", "Skating", "Skiing"]
medals= [3, 22, 50, 351, 159, 40]

#plot the chart with data above
plt.plot(sports, medals, color = (0/255, 100/255, 100/255), linewidth=3.0, marker='o') # RGB color 

#label on the left hand side
plt.ylabel("number of medals")

#label on the bottom of the chart
plt.xlabel("Categories of Sports")

#add a title to the chart
plt.title("Number of medals in each sports category", pad="20")

for i, val in enumerate(medals):
    plt.text(i, val + 4, val, color='b', fontweight='bold')

 #run the show method (this lives inside the pylot package)
 # this will generate a graph in a new window 
plt.show()