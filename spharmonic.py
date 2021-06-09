#Showing the orbital of the hydrogen atom in 3D
#Where talking in the account of the wavefunction of the electrons/electron in the hydrogen atom.

# It will help us visualize the shapes of the orbital of the hydrogen atom.

import numpy as np
import matplotlib.pyplot as plt
import pyshtools.legendre as pysh


def factorial(a):
  if a == 0:
    return 1
  elif a ==1:
    return 1
  else:
    return a * factorial(a-1)

def sphHarmonic(l, m, thetha):
  if l ==0:
    p_lm = pysh.legendre_lm(l,m, np.cos(thetha))
    ylm = np.sqrt((((2*l)+1)/(4*np.pi))*((factorial(l-abs(m)))/(factorial(l+abs(m)))))*p_lm
    p = abs((ylm) **2)
  elif (m >=0 and l!=0):
    p_lm = pysh.legendre_lm(l,m, np.cos(thetha))
    ylm = np.sqrt((((2*l)+1)/(4*np.pi))*((factorial(l-abs(m)))/(factorial(l+abs(m)))))*p_lm
    p = abs((ylm) **2)
  elif (m <0 and l!=0):
    p_lm = pysh.legendre_lm(l,m, np.cos(thetha))
    ylm = (((-1)**m)*((factorial(l-abs(m)))/(factorial(l+abs(m)))))*np.sqrt((((2*l)+1)/(4*np.pi))*((factorial(l-abs(m)))/(factorial(l+abs(m)))))*(p_lm)
    p = abs((ylm) ** 2)
  return p

thetha = np.linspace(0, 2 * np.pi, 300)
phi = np.linspace(0, 2*np.pi, 300)
THETA, PHI = np.meshgrid(thetha, phi)
l = int(input("Please Key in orbital quantum number l : " ))
m = int(input("Please Key in magnetic quantum number m : " ))
probability = sphHarmonic(l, m, THETA)
fig = plt.figure()
X = probability * np.sin(THETA) * np.cos(PHI)
Y = probability * np.sin(THETA) * np.sin(PHI)
Z = probability * np.cos(THETA)
ax = fig.add_subplot(1, 1, 1, projection='3d')
plot = ax.plot_surface(X, Y, Z, rstride = 1, cstride = 1, cmap = plt.get_cmap('jet'), linewidth = 0, antialiased = False, alpha = 0.5)
plt.show()


