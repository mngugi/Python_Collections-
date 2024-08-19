from scipy.stats import ttest_ind

sample1 = [1,2,3,4,5]
sample2 = 2*(sample1)

t_stat, p_value = ttest_ind(sample1, sample2, equal_var=False)

print(t_stat, p_value)


print("-----------------------------------")
# Example with valid data
sample1 = [1, 2, 3, 4, 5]
sample2 = [2, 4, 6, 8, 10]

# Perform t-test
t_stat, p_value = ttest_ind(sample1, sample2, equal_var=False)

print(t_stat, p_value)