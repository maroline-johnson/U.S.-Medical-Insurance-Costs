import csv

# Get patients info from insurance.csv
patients = []
with open('insurance.csv') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for row in csv_reader:
        patients.append(row)


# Function to get count of rows that match value in csv column
def get_count(csv_column, count_value):
    count = 0
    for patient in patients:
        if patient[csv_column] == count_value:
            count += 1
    return count


# Function to get sum of values in csv column
def get_total(sum_value, type):
    total = 0
    for patient in patients:
        total += type(patient[sum_value])
    return total


def get_total_if(csv_if_column, operator, value, sum_value, type):
    total = 0
    for patient in patients:
        if operator == 'equal to':
            if patient[csv_if_column] == value:
                total += type(patient[sum_value])
        elif operator == 'less than or equal to':
            if patient[csv_if_column] <= value:
                total += type(patient[sum_value])
        elif operator == 'greater than or equal to':
            if patient[csv_if_column] >= value:
                total += type(patient[sum_value])
        elif operator == 'not equal to':
            if patient[csv_if_column] != value:
                total += type(patient[sum_value])
    return round(total, 2)


# Get counts
count_females = get_count('sex', 'female')
count_males = get_count('sex', 'male')
count_patients = count_females + count_males
count_smokers = get_count('smoker', 'yes')
count_non_smokers = get_count('smoker', 'no')

# Get totals
total_age = get_total('age', int)
total_cost = get_total('charges', float)
total_cost_smokers = get_total_if('smoker', 'equal to', 'yes', 'charges', float)
total_cost_non_smokers = get_total_if('smoker', 'equal to', 'no', 'charges', float)
total_bmi_females = get_total_if('sex', 'equal to', 'female', 'bmi', float)
total_bmi_males = get_total_if('sex', 'equal to', 'male', 'bmi', float)
total_cost_females = get_total_if('sex', 'equal to', 'female', 'charges', float)
total_cost_males = get_total_if('sex', 'equal to', 'male', 'charges', float)


# Calculate average age of patients
average_age = round(total_age / count_patients)
# print("Average age of patients in this dataset: " + str(average_age))

# Analyze where a majority of patients are from
count = 0
count_patients_per_region = {}
for patient in patients:
    region = patient['region']
    if region not in count_patients_per_region:
        count_patients_per_region[region] = count
    for region in count_patients_per_region:
        count_patients_per_region[region] += 1
max_count_patients_per_region = max(count_patients_per_region)  # southwest has the max
# print("Region with the highest number of patients in this dataset: " + str(max_count_patients_per_region.title()))

# Analyze average insurance cost for smokers vs. non-smokers and how it affects average cost overall
average_cost = round(total_cost / count_patients)
average_cost_smokers = round(total_cost_smokers / count_smokers)
average_cost_nonsmokers = round(total_cost_non_smokers / count_non_smokers)
# Get factor of average insurance cost for smoker to non-smoker
factor = round(average_cost_smokers / average_cost_nonsmokers)
# print("Average insurance cost: $" + str(average_cost))
# print("Average insurance cost for smokers: $" + str(average_cost_smokers))
# print("Average insurance cost for non-smokers: $" + str(average_cost_nonsmokers))
# print("Smokers' average insurance cost is about " + str(factor) +
# "x more than average insurance cost for non-smokers.")

# Analyze average age of patients with at least one child
total_age_patients_with_child = 0
num_patients_with_child = 0
for patient in patients:
    if patient['children'] > '0':
        total_age_patients_with_child += int(patient['age'])
        num_patients_with_child += 1
average_age_patients_with_child = round(total_age_patients_with_child / num_patients_with_child)
# print("Average age of patients with one or more children:", average_age_patients_with_child)

# Analyze average BMI per sex
average_bmi_females = round(total_bmi_females / count_females)
average_bmi_males = round(total_bmi_males / count_males)
# print("Average BMI for females:", average_bmi_females)
# print("Average BMI for males:", average_bmi_males)

# Analyze insurance cost per sex
average_cost_females = round(total_cost_females / count_females)
average_cost_males = round(total_cost_males / count_males)
print("Average cost for females:", average_cost_females)
print("Average cost for males:", average_cost_males)
