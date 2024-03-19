"""
Created on Fri Nov 27 22:11:36 2020

@author: Toghrul Nasirli
"""
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Setting up parameters for the distributions
#Input values should be changed according to the requirements

# Mean and standard deviation for porosity
porosity_mean = 2500
porosity_std = 0.035

# Mean and standard deviation for water saturation
sw_mean = 0.22
sw_std = 0.08

# Minimum, likely, and maximum values for thickness
thickness_min = 12
thickness_likely = 32
thickness_max = 44

# Minimum, likely, and maximum values for area
area_min = 22 * (10 ** 6)
area_likely = 22 * 1.2 * (10 ** 6)
area_max = 22 * 3.5 * (10 ** 6)

# Minimum and maximum values for formation volume factor
fvf_min = 1.08
fvf_max = 1.23

# Number of data points for distributions and iterations
number_of_input = 500
number_of_iter = 10000

# Porosity distribution (normal) in fraction
porosity_dist = np.random.normal(porosity_mean, porosity_std, size=(number_of_input))
p = plt.hist(porosity_dist, bins=100, density=True)
plt.title("Porosity")
px = sns.histplot(porosity_dist, kde=True)
plt.show()

# Water saturation distribution (log normal) in fraction
sw_distribution = np.random.normal(sw_mean, sw_std, size=(number_of_input))
sx = sns.histplot(sw_distribution, kde=True)
plt.title("Water Saturation")
sx = sns.histplot(sw_distribution, kde=True)
plt.show()

# Thickness distribution (triangular) in meters
thickness_dist = np.random.triangular(thickness_min, thickness_likely, thickness_max, size=(number_of_input))
thick = plt.hist(thickness_dist, bins=100, density=True)
plt.title("Thickness Distribution")
tx = sns.histplot(thickness_dist, kde=True)
plt.show()

# Area distribution (triangular) in meters-squared
area_dist = np.random.triangular(area_min, area_likely, area_max, size=(number_of_input))
area = plt.hist(area_dist, bins=100, density=True)
plt.title("Area Distribution")
ax = sns.histplot(area_dist, kde=True)
plt.show()

# Oil formation volume factor distribution (uniform)
fvf_dist = np.random.uniform(fvf_min, fvf_max, size=(number_of_input))
fvf = plt.hist(fvf_dist, bins=100, density=True)
plt.title("Formation Volume Factor")
fx = sns.histplot(fvf_dist, kde=True)
plt.show()

# Function to calculate Oil in Place (OIP)
def OIP(area, h, water_saturation, oil_fvf, phi):
    """
    Calculates Oil in Place (OIP) using given parameters.

    Parameters:
    area (float): Area of the reservoir.
    h (float): Thickness of the reservoir.
    water_saturation (float): Water saturation.
    oil_fvf (float): Oil formation volume factor.
    phi (float): Porosity.

    Returns:
    float: Oil in Place (OIP) value.
    """
    OIP = 6.28981077 * (area * h * (1 - water_saturation) * phi) / oil_fvf
    return OIP

oil_in_place = []

# Monte-Carlo Iteration to calculate Oil in Place (OIP)
for i in range(number_of_iter):
    area_iter = np.random.choice(area_dist)
    saturation_iter = np.random.choice(sw_distribution)
    thickness_iter = np.random.choice(thickness_dist)
    fvf_iter = np.random.choice(fvf_dist)
    phi_iter = np.random.choice(porosity_dist)
    oil = OIP(area_iter, thickness_iter, saturation_iter, fvf_iter, phi_iter)
    oil_in_place.append(oil)

oil_in_place_array = np.array(oil_in_place)

# Histogram of STOIIP
oip_hist = plt.hist(oil_in_place, bins=100, density=True)
plt.title("STOIIP")
ox = sns.histplot(oil_in_place, kde=True)
plt.show()

# Constructing the Cumulative Distribution Function (CDF)
oil_in_place_sorted = np.sort(oil_in_place_array)
p = 1 - (1. * np.arange(len(oil_in_place_array)) / (len(oil_in_place_array)))

# Plotting the sorted data
fig = plt.figure()
ax1 = fig.add_subplot(122)
ax1.plot(oil_in_place_sorted, p)
ax1.set_xlabel("Oil In Place")
ax1.set_ylabel("Probability Fraction")
ax1.set_title("Expectation Curve")
plt.show()
