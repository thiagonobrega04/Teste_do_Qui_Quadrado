import pandas as pd
from scipy import stats
from scipy.stats import chisquare
from random import randint

# Are the kids in Space Academy choosing candy colors at random, or do they have a favorite? The provided code performs a Chi-Square Test to compare the observed color choices with what we would expect if the choices were completely random. Click Run to see what the Chi-Square statistic and the P-value reveal!

# Observed and expected candy color preferences
observed_preferences = [35, 40, 25, 10]
expected_preferences = [27.5, 27.5, 27.5, 27.5]

# Perform the Chi-Square Test
chi2_stat, p_value = stats.chisquare(observed_preferences, f_exp=expected_preferences)
print("Chi2 Stat:", chi2_stat, "P-value:", p_value)

if p_value < 0.05:
    print('The observed preferences are significantly different from the expected preferences. We reject the null hypothesis.')
else:
    print('The observed preferences are not significantly different from the expected preferences. We fail to reject the null hypothesis.')

# Stellar Navigator, let's hypothesize that preferences for candy colors are unequal — some are more favored than others. Modify the expected_frequencies in the provided starter code to reflect this new hypothesis. Ensure the sum remains at 100. Analyze the impact on the Chi-Square Statistic and P-value. Onward to discovery!

# Frequencies of each candy color preference
observed_frequencies = [40, 25, 20, 15]
expected_frequencies = [35, 25, 25, 15]  # Original expected frequencies

# Perform the Chi-Square Test
chi_stat, p_value = chisquare(observed_frequencies, expected_frequencies)
print(f"Chi-Square Statistic:\n {chi_stat:.2f}")
print(f"P-value:\n {p_value:.4f}")

if p_value < 0.05:
    print('The observed preferences are significantly different from the expected preferences. We reject the null hypothesis.')
else:
    print('The observed preferences are not significantly different from the expected preferences. We fail to reject the null hypothesis.')

# Great progress, Stellar Navigator! Now, calculate the expected frequencies for your Chi-Square test. Remember, as we expect the chances of pulling each candy type to be equal, expected frequencies should also be equal, and their sum should equal the sum of the observed frequencies.

# Add missing parts to the code, and see if your observed data significantly differs from what was expected!

# Observed candy color preferences
observed = [randint(10, 50) for i in range(100)]

# Calculate the expected frequency
expected = [sum(observed) / len(observed)] * len(observed)

# Perform the Chi-Square Test
stat, p = chisquare(observed, expected)

# Print the test statistic and p-value
print(f"Chi-Square Stat:\n{stat:.2f}, P-value: {p:.4f}")

# Incredible progress, Stellar Navigator! Now, let's unleash the full potential of your newfound Chi-Square Test knowledge. Dive in and complete the code to check for candy color preferences using real-life data.

# Let's imagine we counted candy colors preferred by a group of children
observed_preferences = [40, 30, 20, 10, 25]
expected_uniform_preference = [25, 25, 25, 25, 25]

# TODO: Complete the code to perform the Chi-Square Test and print the results
# May your calculations be as accurate as a laser beam!

Chi_Square, p = chisquare(observed_preferences, expected_uniform_preference)
print(f"Chi-Square Test:\n{Chi_Square:.2f}, {p:.4f}")