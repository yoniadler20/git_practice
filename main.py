import matplotlib.pyplot as plt

bar1 = ['A']
value1 = [20]
value2 = [10]
value3 = [5]

# Create the first set of bars
plt.bar(bar1, value1, label='blabla1')

# Create the second set of bars, stacked on top of the first
plt.bar(bar1, value2, bottom=value1, label='blabla2')

# Create the third set of bars, stacked on top of the previous two
# We need to add values1 and values2 to get the correct bottom position.
bottom_value3 = [value1[i] + value2[i] for i in range(len(value1))]
plt.bar(bar1, value3, bottom=bottom_value3, label='blabla3')

plt.xlabel('bar')
plt.ylabel('amount')
plt.title('יוני אדלר')
plt.legend()  # Add a legend to identify the sets
plt.show()