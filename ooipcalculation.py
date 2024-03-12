"""
Created on Fri Nov 27 22:11:36 2020

@author: Toghrul Nasirli
"""
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# The values should be change according the requirements. This part can be also changed in the equations below and deleted.
A = 22
B = 00
C = 20
D = 8
E = 4

porosity_mean = (A+3)/100
porosity_std = 3.5/100
sw_mean = A/100
sw_std = 8/100
thickness_min = B
thickness_likely = B + C
thickness_max = B+C+D+E
area_min = A*(10^6)
area_likely = A*1.2*(10^6)
area_max = A*3.5*(10^6)
fvf_min = 1.08
fvf_max = 1.23
number_of_input = 500
number_of_iter = 10000

#porosity distribution(normal) in fraction
porosity_dist = np.random.normal(porosity_mean, porosity_std,size=(number_of_input) )
p = plt.hist(porosity_dist, bins=100, density = True)
plt.title("Porosity")
px = sns.distplot(porosity_dist)
plt.show()

#water saturation distribution(log normal) in fraction
sw_distribution = np.random.normal(sw_mean, sw_std, size=(number_of_input))
sw = plt.hist(sw_distribution, bins = 100, density = True)
plt.title("Water Saturation")
sx = sns.distplot(sw_distribution)
plt.show()

#thickness distribution(triangular) meters
thickness_dist = np.random.triangular(thickness_min, thickness_likely, thickness_max, size=(number_of_input))
thick = plt.hist(thickness_dist, bins=100, density=True)
plt.title("Thickness Distribution")
tx = sns.distplot(thickness_dist)
plt.show()

#area distribution(triangular) meters-squared
area_dist = np.random.triangular(area_min, area_likely, area_max, size=(number_of_input) )
area = plt.hist(area_dist, bins=100, density = True)
plt.title("Area Distribution")
ax = sns.distplot(area_dist)
plt.show()

#oil formation volume factor distribution(uniform)
fvf_dist = np.random.uniform(fvf_min, fvf_max, size = (number_of_input))
fvf = plt.hist(fvf_dist, bins = 100, density = True)
plt.title("Formation Volume Factor")
fx = sns.distplot(fvf_dist)
plt.show()

def OIP(area, h, water_saturation ,oil_fvf, phi):
    OIP = 6.28981077*(area*h*(1-water_saturation)*phi)/oil_fvf
    return OIP


oil_in_place = []

#Monte-Carlo Iteration
for i in range(number_of_iter):
    area_iter = np.random.choice(area_dist)
    saturation_iter = np.random.choice(sw_distribution)
    thickness_iter = np.random.choice(thickness_dist)
    fvf_iter = np.random.choice(fvf_dist)
    phi_iter = np.random.choice(porosity_dist)
    oil = OIP(area_iter, thickness_iter, saturation_iter, fvf_iter, phi_iter)
    oil_in_place.append(oil)

oil_in_place_array = np.array(oil_in_place)

#Histogram of STOIIP
oip_hist = plt.hist(oil_in_place, bins = 100, density = True)
plt.title("STOIIP")
ox = sns.distplot(oil_in_place)
plt.show()

#Constructing the Cumulative Distribution Function
oil_in_place_sorted = np.sort(oil_in_place_array)
p = 1 - (1.*np.arange(len(oil_in_place_array))/(len(oil_in_place_array)))


#plotting the sorted data
fig = plt.figure()
ax1 = fig.add_subplot(122)
ax1.plot(oil_in_place_sorted, p)
ax1.set_xlabel("Oil In Place")
ax1.set_ylabel("Probability Fraction")
ax1.set_title("Expectation Curve")

