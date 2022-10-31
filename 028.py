def thirteenth_salary(percent, salary_list):
    avg = sum(salary_list) // len(salary_list)
    return avg * percent // 100


salary_list = [100_000, 100_000, 101_000, 99_000, 101_000, 99_000, 101_000, 99_000, 99_000, 101_000,
               100_000, 100_000]
premium = thirteenth_salary(50, salary_list)  # premium = 50000
print(premium)
