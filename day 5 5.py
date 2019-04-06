import matplotlib.pyplot as plt
import numpy as np
plt.figure(figsize=(10,5))
gaussian_numbers = np.random.randn(1000)
plt.hist(gaussian_numbers,30, color = 'navy', alpha = 0.5)
plt.title('Gaussian Histgram')
plt.xlabel('value')
plt.ylabel('frequency')
plt.show()