import csv

# Get patients info from insurance.csv
patients = []
with open('insurance.csv') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for row in csv_reader:
        patients.append(row)


# Function to get count of rows that match value in csv column
def get_count(csv_column, count_value):
    counter = 0
    for patient in patients:
        if patient[csv_column] == count_value:
            counter += 1
    return counter


# Function to get sum of values in csv column
def get_total(sum_value, datatype):
    total = 0
    for patient in patients:
        total += datatype(patient[sum_value])
    return total


def get_total_if(csv_if_column, operator, value, sum_value, datatype):
    total = 0
    for patient in patients:
        if operator == 'equal to':
            if patient[csv_if_column] == value:
                total += datatype(patient[sum_value])
        elif operator == 'less than or equal to':
            if patient[csv_if_column] <= value:
                total += datatype(patient[sum_value])
        elif operator == 'greater than or equal to':
            if patient[csv_if_column] >= value:
                total += datatype(patient[sum_value])
        elif operator == 'not equal to':
            if patient[csv_if_column] != value:
                total += datatype(patient[sum_value])
    return round(total, 2)


# Get common counts
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
total_bmi_parents = get_total_if('children', 'greater than or equal to', '1', 'bmi', float)
total_bmi_non_parents = get_total_if('children', 'equal to', '0', 'bmi', float)
total_cost_females = get_total_if('sex', 'equal to', 'female', 'charges', float)
total_cost_males = get_total_if('sex', 'equal to', 'male', 'charges', float)

# Calculate average age of patients
average_age = round(total_age / count_patients)
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
print("Region with the highest number of patients in this dataset: " + str(max_count_patients_per_region.title()))

# Analyze average insurance cost for smokers vs. non-smokers and how it affects average cost overall
average_cost = round(total_cost / count_patients)
average_cost_smokers = round(total_cost_smokers / count_smokers)
average_cost_nonsmokers = round(total_cost_non_smokers / count_non_smokers)
# Get factor of average insurance cost for smoker to non-smoker
factor = round(average_cost_smokers / average_cost_nonsmokers)
print("Average insurance cost: $" + str(average_cost))
print("Average insurance cost for smokers: $" + str(average_cost_smokers))
print("Average insurance cost for non-smokers: $" + str(average_cost_nonsmokers))
print("Smokers' average insurance cost is about " + str(factor) +
      "x more than average insurance cost for non-smokers.")

# Analyze average age of patients with at least one child
total_age_patients_with_child = 0
num_patients_with_child = 0
for patient in patients:
    if patient['children'] > '0':
        total_age_patients_with_child += int(patient['age'])
        num_patients_with_child += 1
average_age_patients_with_child = round(total_age_patients_with_child / num_patients_with_child)
print("Average age of patients with one or more children:", average_age_patients_with_child)

# Analyze average BMI per sex
average_bmi_females = round(total_bmi_females / count_females)
average_bmi_males = round(total_bmi_males / count_males)
print("Average BMI for females:", average_bmi_females)
print("Average BMI for males:", average_bmi_males)

# Analyze insurance cost per sex
average_cost_females = round(total_cost_females / count_females)
average_cost_males = round(total_cost_males / count_males)
print("Average cost for females: $" + str(average_cost_females))
print("Average cost for males: $" + str(average_cost_males))

# Analyze what percent of each sex group are smokers/non-smokers
count_female_smokers = 0
count_male_smokers = 0
for patient in patients:
    if patient['sex'] == 'female' and patient['smoker'] == 'yes':
        count_female_smokers += 1
    elif patient['sex'] == 'male' and patient['smoker'] == 'yes':
        count_male_smokers += 1
percent_female_smokers = round((count_female_smokers / count_females * 100))
percent_male_smokers = round((count_male_smokers / count_males * 100))
print("Percent of females that smoke: " + str(percent_female_smokers) + "%")
print("Percent of males that smoke: " + str(percent_male_smokers) + "%")

# Analyze average charge for each region
total_cost_northeast = 0
count_northeast = 0
total_cost_southeast = 0
count_southeast = 0
total_cost_northwest = 0
count_northwest = 0
total_cost_southwest = 0
count_southwest = 0
for patient in patients:
    if patient['region'] == 'northeast':
        total_cost_northeast += float(patient['charges'])
        count_northeast += 1
    elif patient['region'] == 'southeast':
        total_cost_southeast += float(patient['charges'])
        count_southeast += 1
    elif patient['region'] == 'northwest':
        total_cost_northwest += float(patient['charges'])
        count_northwest += 1
    elif patient['region'] == 'southwest':
        total_cost_southwest += float(patient['charges'])
        count_southwest += 1
average_cost_northeast = round(total_cost_northeast / count_northeast)
average_cost_southeast = round(total_cost_southeast / count_southeast)
average_cost_northwest = round(total_cost_northwest / count_northwest)
average_cost_southwest = round(total_cost_southwest / count_southwest)
print("Average cost for patients in the Northeast: $" + str(average_cost_northeast))
print("Average cost for patients in the Southeast: $" + str(average_cost_southeast))
print("Average cost for patients in the Northwest: $" + str(average_cost_northwest))
print("Average cost for patients in the Southwest: $" + str(average_cost_southwest))

# Analyze number of children for each region
total_kids_northeast = 0
total_kids_southeast = 0
total_kids_northwest = 0
total_kids_southwest = 0
for patient in patients:
    if patient['region'] == 'northeast' and patient['children'] != 0:
        total_kids_northeast += int(patient['children'])
    elif patient['region'] == 'southeast' and patient['children'] != 0:
        total_kids_southeast += int(patient['children'])
    elif patient['region'] == 'northwest' and patient['children'] != 0:
        total_kids_northwest += int(patient['children'])
    elif patient['region'] == 'southwest' and patient['children'] != 0:
        total_kids_southwest += int(patient['children'])
average_kids_northeast = round(total_kids_northeast / count_northeast, 2)
average_kids_southeast = round(total_kids_southeast / count_southeast, 2)
average_kids_northwest = round(total_kids_northwest / count_northwest, 2)
average_kids_southwest = round(total_kids_southwest / count_southwest, 2)
print("Average number of children for patients in the Northeast: " + str(average_kids_northeast))
print("Average number of children for patients in the Southeast: " + str(average_kids_southeast))
print("Average number of children for patients in the Northwest: " + str(average_kids_northwest))
print("Average number of children for patients in the Southwest: " + str(average_kids_southwest))

# Analyze likelihood of smoking for patients more than one child
count_parents = 0
count_parent_smokers = 0
for patient in patients:
    if patient['children'] > '0':
        count_parents += 1
    if patient['children'] > '0' and patient['smoker'] != 'yes':
        count_parent_smokers += 1
parent_smoker_probability = round(count_parent_smokers / count_parents * 100)
print("Probability that a parent is a smoker: %" + str(parent_smoker_probability))

# Analyze averages of BMI for parents
average_bmi_parents = round(total_bmi_parents / count_parents, 1)
average_bmi_non_parents = round(total_bmi_non_parents / (count_patients - count_parents), 1)
print("Average BMI of parents:", average_bmi_parents)
print("Average BMI of non-parents:", average_bmi_non_parents)
