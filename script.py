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
print(average_age)  # Prints 39
