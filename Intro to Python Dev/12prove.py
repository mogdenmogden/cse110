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
            # get past the header row
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
    f'MINIMUM life expectancy in the dataset: {min_le_row[0]} {min_le_row[2]}; {min_le_row} ')
print()
print(
    f'MAXIMUM life expectancy in the dataset: {max_le_row[0]} {max_le_row[2]}; {max_le_row} ')
print()
print('+'*60)

# Discover what countries list data in which year
country_col = []
redundant_country_list = []

with open("life-expectancy.csv") as life_exp_dataset:
    for item in life_exp_dataset:
        clean_row = item.strip().split(",")
        try:  # get past the header row
            yr = int(clean_row[2].strip())
        except:
            pass

        entity = clean_row[0].strip()

        if entity == 'Entity':
            pass
        elif entity not in country_col:
            country_col.append(entity)
        else:
            pass

        redundant_country_list.append(entity)
# if len(country_col) > 0:
#     print('country list made\n')

for i in country_col:
    times_present = 0
    times_present = redundant_country_list.count(i)

    print(f'"{i}" has {times_present} years of mortality data.')

print()
print('+'*60)

# Allow the user to look at data for a single year
print()
print('You can investigate data for a certain year. ')
print(f'Years range from {min_yr} to and including {max_yr}. \n')
inv_yr = int(input('What year will you examine? '))
while int(inv_yr) not in years:
    inv_yr = int(input('The data skips that year. Please choose another. '))

# Reset tne variables
min_le = 999.00
min_le_row = ""
max_le = 0.0
max_le_row = ""

with open("life-expectancy.csv") as life_exp_dataset:
    countries = []
    for item in life_exp_dataset:
        clean_row = item.strip().split(",")
        if clean_row[2].strip() == 'Year':
            pass
        else:
            if inv_yr == int(clean_row[2].strip()):
                if clean_row[0] not in countries:
                    countries.append(clean_row[0])
# countries.pop(0)
if len(countries) == 1:
    print(
        f'\nThere is {len(countries)} country with data in {inv_yr}.\nIt is: ')
    print(countries)
else:
    print(
        f'\nThere are {len(countries)} countries with data in {inv_yr}.\nThey are: ')
    print(countries)

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
    f'\nThe MINIMUM life expectancy for {inv_yr} was from {min_le_row[0]}: {float(min_le_row[3]):.2f} years ')

print(
    f'\nThe MAXIMUM life expectancy for {inv_yr} was from {max_le_row[0]}: {float(max_le_row[3]):.2f} years ')
print(
    f'\nThe AVERAGE life expectancy in {inv_yr} is {statistics.mean(le_values):.2f} years ')

print()
print('+'*60)

# # identify the country / year with the largest drop YOY
# c1 = ""  # country
# y0 = 0  # current year
# y_1 = 0  # previous year
# le0 = 0.0  # current year life expectancy
# le_1 = 0.0    # previous year life expectancy
# max_drop = 999
# yr_max_drop = 0
# max_inc = -1
# yr_max_inc = 0
# grand_inc_country = ''
# grand_drop_country = ''
# grand_inc_yr = 0
# grand_drop_yr = 0
# grand_inc_amt = -1
# grand_drop_amt = 999

# prep a clean dataset
dataset1 = []   # make a clean dataset w/o a header row

with open("life-expectancy.csv") as life_exp_dataset:
    # make a clean dataset w/o a header row
    for row in life_exp_dataset:
        clean_row = row.strip().split(",")
        if clean_row[2].strip() == 'Year':
            pass  # jump the header row
        else:
            dataset1.append(clean_row)


# min max min avg life expectancy for a chosen Country or ALL
repeater = False
print('\nHow about exploring data for a certain country?')
print('Type "All"  for all countries, or the name of the country you want from the given list.')
need_list = input('Do you need a list of countries? (Y/N) ').capitalize()
if need_list == 'Y':
    print(country_col)
choice = input('Type your selection ("All" or your choice): ')
while repeater == False:
    if choice == 'All':
        repeater = True
    elif choice not in country_col:
        print(country_col)
        print(f'"{choice}" is not in the dataset.  Choose from the above list.')
        print()
        choice = input('Type your selection ("All" or exact spelling above): ')
    else:
        repeater = True
print(f'You chose {choice}. \n\n')

if choice == 'All':
    for country in country_col:
        cc = country
        country_list = []
        tot_lifeexp = 0
        datarow_country = []
        datarow_years = []
        datarow_lifeexp = []

        for datarow in dataset1:
            c1 = datarow[0].strip()

            if cc == c1:
                datarow_country.append(int(datarow[2]))
                datarow_country.append(float(datarow[3]))
                country_list.append(datarow_country)

                datarow_years.append(int(datarow[2]))
                datarow_lifeexp.append(float(datarow[3]))

                tot_lifeexp += tot_lifeexp
            else:
                pass

        print(f'The {cc} max life expectancy is {max(datarow_lifeexp):.2f}, min {min(datarow_lifeexp):.2f}, average {statistics.mean(datarow_lifeexp):.2f}, in {len(datarow_lifeexp)} datapoints. ')
else:

    cc = choice
    country_list = []
    tot_lifeexp = 0
    datarow_country = []
    datarow_years = []
    datarow_lifeexp = []

    for datarow in dataset1:
        c1 = datarow[0].strip()

        if cc == c1:
            datarow_country.append(int(datarow[2]))
            datarow_country.append(float(datarow[3]))
            country_list.append(datarow_country)

            datarow_years.append(int(datarow[2]))
            datarow_lifeexp.append(float(datarow[3]))

            tot_lifeexp += tot_lifeexp
        else:
            pass

    print(f'The {cc} max life expectancy is {max(datarow_lifeexp):.2f}, min {min(datarow_lifeexp):.2f}, average {statistics.mean(datarow_lifeexp):.2f}, in {len(datarow_lifeexp)} datapoints. ')
print()

# # find the maximum life expectancy drop  and max life expectancy increase for each country
# print(f'this is the beginning of clean_row for {c1}')
# for i in country_col:
#     print(f'this is the beginning of i in country_col {i}')
#     y_1 = 0  # country: reset previous year
#     le_1 = 0  # country: reset previous year life expectancy
#     c0 = i
#     for j in dataset1:
#         c1 = j[0]  # country
#         print(f'starting i {c0}, j {c1}')
#         if c0 == c1:
#             if y_1 == 0:  # skip the comparison of the first year and set it as the previous year
#                 y_1 = int(j[2])
#                 le_1 = float(j[3])
#                 pass
#             else:
#                 y0 = int(j[2])
#                 le0 = float(j[3])
#                 change = le0 - le_1
#                 if change < max_drop:  # biggest drop
#                     max_drop = change
#                     yr_max_drop = y0
#                 elif change > max_inc:  # biggest gain
#                     max_inc = change
#                     yr_max_inc = y0
#                 else:
#                     pass

#                 if change < grand_drop_amt:
#                     grand_drop_amt = change
#                     grand_drop_yr = y0
#                     grand_drop_country = c1
#                 elif change > grand_inc_amt:
#                     grand_inc_amt = change
#                     grand_inc_yr = y0
#                     grand_inc_country = c1
#                 else:
#                     pass
#             # set variables to prepare for next loop evaluation
#             y_1 = y0
#             le_1 = le0
#         else:  # move on if the country isn't the same as c1
#             pass

#     print(f'{max_inc} {yr_max_inc} {c1}')
#     print(f'{max_drop} {yr_max_drop} {c1}')
#     if max_inc != -1 and max_drop != 999:
#         print(
#             f'The biggest gain in life expectancy for "{i}" is {max_inc:.2f} in {yr_max_inc}. ')
#         print(
#             f'The biggest drop in life expectancy for "{i}" is {max_drop:.2f} in {yr_max_drop}. ')
#     elif max_inc == -1 and max_drop == 999:
#         print(
#             f'"{i}" doesn\'t have enough data to calculate change in life expectancy over time. ')
#     elif max_drop == 999:
#         print(f'{i} only shows increases in life expectancy in this dataset. The greatest increase is {max_inc:.2f} in {yr_max_inc}. ')
#     elif max_inc == -1:
#         print(f'{i} only shows decreases in life expectancy in this dataset. The greatest drop is {max_drop:.2f} in {yr_max_drop}. ')
#     else:
#         print(f'\nWhat happened in {i}? \n')
# print()
# print(f'The largest overall GAIN in life expectancy in the dataset')
# print(
#     f'is for "{grand_inc_country}" with a change of  {grand_inc_amt:.2f} in {grand_inc_yr}. ')
# print()
# print(f'The largest overall DROP in life expectancy in the dataset')
# print(
#     f'is for "{grand_drop_country}" with a change of  {grand_drop_amt:.2f} in {grand_drop_yr}. ')


print('+'*60)
print()
