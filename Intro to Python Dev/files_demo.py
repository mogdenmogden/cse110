with open("courses.txt") as courses_file:
    for line in courses_file:
        #line = "WDD 130, 98%"
        part = line.split(",")
        # cleans white space at beginning or end of lines, like carriage returns
        #part = ["WDD 130","98%"]
        # print(part[0])
        # print()
        # print(part[1])
        # print(line)

        course_name = part[0]
        course_grade = float(part[1])

        bonus_grade = course_grade + 0.03

        print(f'{course_name} - Grade: {course_grade}, after bonus is {bonus_grade} ')

        # part = part.strip()
        # print(part)
