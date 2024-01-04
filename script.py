import csv

# Get patients info from insurance.csv
patients = []
with open('insurance.csv') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for row in csv_reader:
        patients.append(row)

# Calculate average age of patients
total_age = 0
for patient in patients:
    total_age += int(patient['age'])
average_age = round(total_age/len(patients))
# print(average_age)  # Prints 39

# Analyze where a majority of patients are from
count = 0
count_patients_per_region = {}
for patient in patients:
    region = patient['region']
    if region not in count_patients_per_region:
        count_patients_per_region[region] = count
    for region in count_patients_per_region:
        count_patients_per_region[region] += 1
max_count_patients_per_region = max(count_patients_per_region) # southwest has the max
# print("The " + str(max_count_patients_per_region.title()) + " region contains the highest number of patients in this dataset.")
