import csv
import statistics
min_le = 999.00
min_le_row = ""
max_le = 0.0
max_le_row = ""
min_yr = 9999
max_yr = 0
years = []
le_values = []

print()
print('+'*60)


with open("life-expectancy.csv") as life_exp_dataset:
    for item in life_exp_dataset:
        clean_row = item.strip().split(",")
        try:
            yr = int(clean_row[2].strip())

        except:
            pass

        l_e = clean_row[3].strip()

        if l_e == 'Life expectancy (years)':
            # print('header')
            pass
        else:

            # print(f'{l_e}')
            if float(l_e) < min_le:
                min_le_row = clean_row
                min_le = float(l_e)
            if float(l_e) > max_le:
                max_le_row = clean_row
                max_le = float(l_e)

            yr = int(clean_row[2].strip())
            years.append(yr)

            if yr < min_yr:
                min_yr = yr
            if yr > max_yr:
                max_yr = yr


print(
    f'Minimum life expectancy in the dataset: {min_le_row[0]} {min_le_row[2]}; {min_le_row} ')
print()
print(
    f'Maximum life expectancy in the dataset: {max_le_row[0]} {max_le_row[2]}; {max_le_row} ')

# Reset tne variables
min_le = 999.00
min_le_row = ""
max_le = 0.0
max_le_row = ""


print()
print('You can investigate data for a certain year. ')
print(f'Years range from {min_yr} to and including {max_yr}. \n')
inv_yr = int(input('What year will you examine? '))
while int(inv_yr) not in years:
    inv_yr = int(input('The data skips that year. Please choose another. '))


with open("life-expectancy.csv") as life_exp_dataset:
    for item in life_exp_dataset:
        clean_row = item.strip().split(",")
        l_e = clean_row[3].strip()
        if l_e == 'Life expectancy (years)':
            pass
        else:
            try:
                yr = int(clean_row[2].strip())
                if yr != inv_yr:
                    pass
                else:
                    le_values.append(float(l_e))
                    if float(l_e) < min_le:
                        min_le_row = clean_row
                        min_le = float(l_e)
                    if float(l_e) > max_le:
                        max_le_row = clean_row
                        max_le = float(l_e)
            except:
                pass

print(
    f'\nThe Minimum life expectancy for {inv_yr} is in {min_le_row[0]}: {float(min_le_row[3]):.2f} years ')

print(
    f'\nThe Maximum life expectancy for {inv_yr} is in {max_le_row[0]}: {float(max_le_row[3]):.2f} years ')
print(
    f'\nThe average life expectancy in {inv_yr} is {statistics.mean(le_values):.2f} years ')


print('+'*60)
print()
