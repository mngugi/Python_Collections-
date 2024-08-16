import math
from scipy.stats import norm, ttest_ind

# Given data
right_footed = {
    "total": 17,
    "success": 11,
    "misses": 4,
    "near_misses": 2
}

left_footed = {
    "total": 17,
    "success": 10,
    "misses": 5,
    "near_misses": 2
}

# Success Rates
right_success_rate = right_footed["success"] / right_footed["total"]
left_success_rate = left_footed["success"] / left_footed["total"]

# Mean success rate
mean_success_rate = (right_success_rate + left_success_rate) / 2

# Variance and Standard Deviation
variance = ((right_success_rate - mean_success_rate) ** 2 + (left_success_rate - mean_success_rate) ** 2) / 2
std_dev = math.sqrt(variance)

# Z-scores
right_z = (right_success_rate - mean_success_rate) / std_dev
left_z = (left_success_rate - mean_success_rate) / std_dev

# Precision and Recall for F1 Score Calculation
# Here we calculate for "Success" as positive class
right_precision = right_footed["success"] / (right_footed["success"] + right_footed["misses"] + right_footed["near_misses"])
right_recall = right_footed["success"] / right_footed["total"]
right_f1 = 2 * (right_precision * right_recall) / (right_precision + right_recall)

left_precision = left_footed["success"] / (left_footed["success"] + left_footed["misses"] + left_footed["near_misses"])
left_recall = left_footed["success"] / left_footed["total"]
left_f1 = 2 * (left_precision * left_recall) / (left_precision + left_recall)

# Two-sample t-test (to derive P-value)
t_stat, p_value = ttest_ind([right_success_rate] * right_footed["total"], [left_success_rate] * left_footed["total"], equal_var=False)

# Results
right_z, left_z, right_f1, left_f1, p_value
