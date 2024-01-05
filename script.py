import csv

# Get patients info from insurance.csv
patients = []
with open('insurance.csv') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for row in csv_reader:
        patients.append(row)


def calculate_average_age(total_num, csv_column):
    for patient in patients:
        total_num += int(patient[csv_column])
    average = round(total_num / len(patients))
    return average


# Calculate average age of patients
total_age = 0
average_age = calculate_average_age(total_age, 'age')
print("Average age of patients in this dataset: " + str(average_age))

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
# print("Region with highest number of patients in this dataset: " + str(max_count_patients_per_region.title()))

# Analyze average insurance cost for smokers vs. non-smokers and how it affects average cost overall
# Get average cost overall
total_cost = 0
num_patients = 0
for patient in patients:
    total_cost += float(patient['charges'])
    num_patients += 1
average_cost = round(total_cost / num_patients)
# Get average cost for smokers
total_cost_smokers = 0
num_smokers = 0
for patient in patients:
    if patient['smoker'] == "yes":
        total_cost_smokers += float(patient['charges'])
        num_smokers += 1
average_cost_smokers = round(total_cost_smokers / num_smokers)
# Get average cost for non-smokers
total_cost_nonsmokers = 0
num_nonsmokers = 0
for patient in patients:
    if patient['smoker'] == "no":
        total_cost_nonsmokers += float(patient['charges'])
        num_nonsmokers += 1
average_cost_nonsmokers = round(total_cost_nonsmokers / num_nonsmokers)
# Get factor of average insurance cost for smoker to non-smoker
factor = round(average_cost_smokers / average_cost_nonsmokers)
# print("Average insurance cost: $" + str(average_cost))
# print("Average insurance cost for smokers: $" + str(average_cost_smokers))
# print("Average insurance cost for non-smokers: $" + str(average_cost_nonsmokers))
# print("Smokers' average insurance cost is about " + str(factor) +
# "x more than average insurance cost for non-smokers.")
