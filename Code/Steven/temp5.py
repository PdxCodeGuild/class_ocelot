import numpy as np
import matplotlib.pyplot as plt

N = 5
crime1_means = (20, 35, 30, 35, 27)
crime1_std = (2, 3, 4, 1, 2)

ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, crime1_means, width, color='r', yerr=crime1_std)

crime2_means = (25, 32, 34, 20, 25)
crime2_std = (3, 5, 2, 3, 3)
rects2 = ax.bar(ind + width, crime2_means, width, color='y', yerr=crime2_std)

crime3_means = (25, 32, 34, 20, 25)
crime3_std = (3, 5, 2, 3, 3)
rects3 = ax.bar(ind + width, crime2_means, width, color='g', yerr=crime3_std)


# add some text for labels, title and axes ticks
ax.set_ylabel('Crimes')
ax.set_title('Top 3 Crimes per Hour')
ax.set_xticks(ind + width / 3)
# ax.set_xticklabels(('G1', 'G2', 'G3', 'G4', 'G5'))
ax.set_xticklabels((1, 2, 3, 4, 5, 6, 7))

ax.legend((rects1[0], rects2[0]), ('Most Common', '2nd most Common'))


def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%d' % int(height),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)

plt.show()