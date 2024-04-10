import pandas as pd
from scipy import stats
from scipy.stats import chisquare
from random import randint

# Introduction to Chi-Square Test
# Greetings, friends! Today, we're diving into a fascinating statistical test called the Chi-Square Test. It's a handy tool for assessing whether there are significant differences between observed and expected frequencies in one or more categories. This tool is often applied in health sciences, business, and market research.

# Ready to unravel the secrets of the Chi-Square Test? Let's get started!

# What is the Chi-Square Test?
# Think of the Chi-Square Test as an investigator, determining if what we observe matches what we expect. Suppose you have a bag of different colored marbles, and you predict how many of each color you will pull out. The Chi-square test is the tool that can help determine if your observations match your expectations.

# The Chi-Square Test assumes two things:

# 1. Randomness: The data was randomly sampled.
# 2. Adequacy: Each cell in the table contains at least five items, ensuring the test's validity.
# Today, we'll learn about the Chi-Square Test in Python!

# Understanding Chi-Square Test
# The Chi-Square Test calculates a test statistic, denoted χ**2, which under the null hypothesis (our observed data matches the expected data) follows a chi-square distribution. This test statistic measures the divergence of the observed data from the expected one. The larger the Chi-Square Test statistic, the less likely the observed and expected data will match by chance.

# A Bag of Marbles
# We've documented the color of each marble drawn from a bag of marbles. Given a predicted distribution of marble colors, we want to know whether our observations match the predictions. Let's explore this situation in Python using the Chi-Square Test!

# Observations
data = pd.DataFrame({
    'Color': ['Red', 'Blue', 'Green', 'Yellow', 'Purple'],
    'Observed': [30, 20, 15, 10, 25],
    'Expected': [20, 20, 20, 20, 20]
})

# Here's our observed and expected color distribution for the marbles drawn.

# Organizing Data
# We prepare the observed and expected frequencies for our Chi-Square Test as follows:

# Prepare observed and expected frequencies
observed_frequencies = data['Observed']
expected_frequencies = data['Expected']

# We select these from their respective columns, 'Observed' and 'Expected'.

# Performing Chi-Square Test
# Let's now perform the Chi-Square Test to ascertain if our observations differ significantly from our expectations:

# Perform Chi-Square Test
chi_square_stat, p_value = stats.chisquare(observed_frequencies,
                                           expected_frequencies)

# Print the chi-square statistic and P-value
print(f"Chi-Square Statistic:\n{chi_square_stat:.1f}")  # 12.5
print(f"P-value:\n{p_value:.3f}")  # 0.014

# The chisquare function from the Scipy stats module provides us with a chi-square statistic and a P-value. The P-value helps us interpret the test results.

# Interpretation
# Let's interpret our Chi-Square Test results. The chi-square statistic is 12.5, indicating a discrepancy between our observations and expectations.

# The P-value of 0.05 is just at the typical threshold used to determine whether a result is significant. A P-value less than or equal to 0.05 usually indicates that our observed data significantly differs from our expected data. Here, our P-value is 0.014, suggesting that our observed marble distribution is statistically different from what we expected.

# So, considering our results, we might conclude that the observed marble distribution in our bag isn't exactly as we expected! Isn't it interesting what we can discover with these statistical tools?

# Calculating Expected Frequencies
# Great, you've progressed well so far! Now, let's learn to calculate expected frequencies, useful when we don't have pre-defined expectations.

# Imagine having a bag with 100 types of differently colored marbles. Let's say for instance, you randomly pull out marbles from this large bag sum(observed) times, and recorded the color of each marble drawn. The obtained color frequencies are stored in a list called observed.

# Observed marble colors
observed = [randint(10, 50) for i in range(100)]

# In this list, each item represents the number of times a particular color was drawn.

# If each marble color had an equal chance of being selected, the expected frequency for each color should be the same. We calculate it as the total number of draws divided by the number of different marble colors.

# We form a list, expected, where each item is this computed expected frequency. Here's how:

# Calculate the expected frequency
expected = [sum(observed) / len(observed)] * len(observed)

# Perform the Chi-Square Test
stat, p = chisquare(observed, expected)

# Print the test statistic and p-value
print(f"Chi-Square Stat:\n{stat:.2f}, P-value: {p:.4f}")

# Now, you can compare these observed and expected frequencies using the Chi-Square Test, exactly like we did with the previous marble example.

