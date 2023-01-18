import numpy as np
import matplotlib.pylab as plt

jezyki=["Python","C","C++","Java","C#","VisualBasic","JavaScript","SQL","Assembly Language","PHP"]
procenty=[17,16,13,12,6,5,3,2.5,1.6,1.4]

plt.bar(jezyki,procenty,color="red")
plt.xlabel('Jezyki programowania')
plt.title('Zainteresowanie jezykami programowania')
plt.ylabel('Zainteresowanie[%]')

plt.show()