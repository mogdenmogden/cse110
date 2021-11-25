#courses_file = open("courses.txt")

with open("courses.txt") as courses_file:
    for row in courses_file:
        print(row)
how_many = len(courses_file)
