
import matplotlib.pyplot as plt
import numpy as np
data = np.random.rand(10 , 12)
sns.heatmap(data, cmap='viridis')
plt.show()