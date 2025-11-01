import matplotlib.pyplot as plt
import numpy as np

# Generate some sample data
data1 = np.random.randn(1000)  #generates an array of 1000 random floating-point numbers.
#These numbers are sampled from a "standard normal" (or Gaussian) distribution.
data2 = np.random.randn(1000) + 2

# Create a figure and subplots
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# 'bar' histtype
axes[0, 0].hist(data1, bins=30, histtype='bar', color='skyblue', edgecolor='black')
axes[0, 0].set_title('histtype="bar"')

# 'barstacked' histtype with multiple datasets
axes[0, 1].hist([data1, data2], bins=30, histtype='barstacked', color=['lightcoral', 'lightgreen'], edgecolor='black')
axes[0, 1].set_title('histtype="barstacked"')

# 'step' histtype
axes[1, 0].hist(data1, bins=30, histtype='step', color='purple', linewidth=2)
axes[1, 0].set_title('histtype="step"')

# 'stepfilled' histtype
axes[1, 1].hist(data1, bins=30, histtype='stepfilled', color='orange', alpha=0.2, edgecolor='black')
axes[1, 1].set_title('histtype="stepfilled"')

fig.suptitle('Various Histogramm Understanding', fontsize=24)
fig.set_facecolor('lightblue')
fig.savefig('histvarious.png')

plt.tight_layout()
plt.show()