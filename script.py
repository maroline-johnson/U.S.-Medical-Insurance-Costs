import csv

# Get patients info from insurance.csv
patients = []
with open('insurance.csv') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for row in csv_reader:
        patients.append(row)


# Function to get count of rows that match value in csv column
def get_count(csv_column, csv_column_value):
    count = 0
    for patient in patients:
        if patient[csv_column] == csv_column_value:
            count += 1
    return count


# Function to get sum of values in csv column
def get_total(csv_column, type):
    total = 0
    for patient in patients:
        total += type(patient[csv_column])
    return total


# Get counts
count_females = get_count('sex', 'female')
count_males = get_count('sex', 'male')
count_patients = count_females + count_males
count_smokers = get_count('smoker', 'yes')
count_non_smokers = get_count('smoker', 'no')

# Get totals
total_age = get_total('age', int)
total_cost = get_total('charges', float)

# Calculate average age of patients
average_age = round(total_age/len(patients))
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
# Get average cost overall
average_cost = round(total_cost/count_patients)
# Get average cost for smokers
total_cost_smokers = 0
for patient in patients:
    if patient['smoker'] == "yes":
        total_cost_smokers += float(patient['charges'])
average_cost_smokers = round(total_cost_smokers/count_smokers)
# Get average cost for non-smokers
total_cost_nonsmokers = 0
for patient in patients:
    if patient['smoker'] == "no":
        total_cost_nonsmokers += float(patient['charges'])
average_cost_nonsmokers = round(total_cost_nonsmokers/count_non_smokers)
# Get factor of average insurance cost for smoker to non-smoker
factor = round(average_cost_smokers/average_cost_nonsmokers)
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
average_age_patients_with_child = round(total_age_patients_with_child/num_patients_with_child)
# print("Average age of patients with one or more children:", average_age_patients_with_child)

# Analyze average BMI per sex
total_bmi_females = 0
total_bmi_males = 0
for patient in patients:
    if patient['sex'] == 'female':
        total_bmi_females += float(patient['bmi'])
    elif patient['sex'] == 'male':
        total_bmi_males += float(patient['bmi'])
average_bmi_females = round(total_bmi_females/count_females)
average_bmi_males = round(total_bmi_males/count_males)
print("Average BMI for females:", average_bmi_females)
print("Average BMI for males:", average_bmi_males)
