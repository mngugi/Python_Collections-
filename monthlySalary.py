# Define yearly salaries for different careers
career_nursing = 52128
career_marketing = 43464
career_history = 35952

# Calculate monthly salaries
monthly_salary_nursing = career_nursing / 12
monthly_salary_marketing = career_marketing / 12
monthly_salary_history = career_history / 12

# Print the table headers
print(f"{'Career':<20}{'Yearly Salary':<20}{'Monthly Salary':<20}")

# Print the career, yearly salary, and monthly salary for each career
print(f"{'Nursing':<20}${career_nursing:<20.2f}${monthly_salary_nursing:<20.2f}")
print(f"{'Marketing':<20}${career_marketing:<20.2f}${monthly_salary_marketing:<20.2f}")
print(f"{'History':<20}${career_history:<20.2f}${monthly_salary_history:<20.2f}")
