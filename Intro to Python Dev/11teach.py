print()
print('='*50)
with open("hr_system.txt") as hr_data:
    for datum in hr_data:
        data_row = datum.strip().split(" ")

        # print(data_row)
        # print(f'data_row[0]')
        # print(f'Name: {data_row[0]}; Title: {data_row[2]} ')

        name = data_row[0]
        id_number = data_row[1]
        job_title = data_row[2]
        salary = float(data_row[3])
        paycheck = salary/24
        if job_title == 'Engineer':
            paycheck = 1000 + salary/24

        #print(f'{name} (ID: {id_number}), {job_title} - ${salary:.2f}')
        print(
            f'{name} (ID: {id_number}), {job_title} - ${paycheck:.2f}/paycheck (biweekly)')
print('='*50)
print()
