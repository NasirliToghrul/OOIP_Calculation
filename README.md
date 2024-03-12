## OOIP Calculation

This Python script is designed to perform Monte Carlo simulations for estimating the Original Oil in Place (OOIP) in petroleum reservoirs. The OOIP is a crucial parameter used in the oil and gas industry to assess the total volume of oil present in a reservoir.

### Requirements:

- Python 3.x
- NumPy
- Matplotlib
- Seaborn

### Script Overview:

The script utilizes Monte Carlo simulation techniques to estimate the OOIP based on various reservoir parameters such as porosity, water saturation, thickness, area, and oil formation volume factor. Here's a brief overview of how the script works:

1. **Input Parameters:**
   - The script begins by defining input parameters that describe the reservoir characteristics. These parameters include mean and standard deviation values for porosity and water saturation, as well as minimum, likely, and maximum values for reservoir thickness and area.
   - Additionally, a range for the oil formation volume factor (fvf) is specified.

2. **Parameter Distributions:**
   - Normal distributions are generated for porosity and water saturation parameters.
   - Triangular distributions are used for thickness and area parameters.
   - A uniform distribution is employed for the oil formation volume factor.

3. **Monte Carlo Simulation:**
   - The script performs Monte Carlo iterations to estimate the OOIP. It randomly samples values from the distributions of the input parameters and calculates the OOIP using the specified equation.

4. **Visualization:**
   - Histograms and distribution plots are generated to visualize the distributions of porosity, water saturation, thickness, area, oil formation volume factor, and OOIP.
   - A cumulative distribution function (CDF) is constructed to represent the probability distribution of the OOIP estimates.

### Instructions for Usage:

To use the script effectively, follow these steps:

1. **Adjust Input Parameters:**
   - Modify the input parameters (A, B, C, D, E) according to the specific reservoir characteristics and requirements. These parameters define the mean, standard deviation, and range of reservoir properties.

2. **Set Simulation Parameters:**
   - Define the number of iterations (`number_of_iter`) for the Monte Carlo simulation and the number of samples (`number_of_input`) to be drawn from the distributions.

3. **Run the Script:**
   - Execute the script using a Python interpreter. Ensure that the necessary libraries (`numpy`, `matplotlib`, `seaborn`) are installed in your Python environment.

4. **Interpret Results:**
   - Analyze the generated histograms and distribution plots to understand the distributions of reservoir parameters and the estimated OOIP.
   - Use the CDF to assess the probability distribution of OOIP estimates and evaluate the uncertainty associated with the results.

## Credits

This script was developed by Toghrul Nasirli.


