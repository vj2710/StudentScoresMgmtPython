from compute import computeOptions

completeData = {}
classList = []
studentIdList=[]
max_marks_list = {}
grade_perc_value = {"a1": 7.5, "a2": 7.5, "project" : 25, "test1" : 30, "test2" : 30}


def update_fail_limit():

    while True:
        new_limit_input = input("Please enter the new limit? \n")
        if int(new_limit_input) >= 0 and int(new_limit_input) <= 100:
            final_grades_list = []

            for val in completeData["total"]:
                final_grades_list.append(calculate_grade(val, float(new_limit_input)))

            new_complete_data = completeData.copy()
            new_complete_data["grades"] = final_grades_list
            break
        else:
            print("Invalid input... New limit can be between 0 and 100\n")

    return new_complete_data

def mainMenu():
    while True:
        myInput = input('''\nPlease select one option
1> Display individual component
2> Display component average
3> Display Standard Report
4> Sort by alternate column
5> Change Pass/Fail point
6> Exit \n''')
        mainMenuInput = ["1","2","3","4"]
        if myInput in mainMenuInput:
            myObj = computeOptions()
            myObj.optionMenu(completeData, max_marks_list, myInput)
        elif myInput == "5":
            new_complete_data = update_fail_limit()
            myObj = computeOptions()
            myObj.optionMenu(new_complete_data, max_marks_list, "3")
        elif myInput == "6":
            print("Good Bye")
            break
        else:
            print("Incorrect choice... Please try again")


def fill_grades(file_name):
    temp_list = []
    temp_dict = {}

    file = open(file_name + '.txt', 'r')
    max_marks_list[file_name] = file.readline().strip('\n')

    with open(file_name+'.txt', 'r') as fileObj:
        next(fileObj)
        for line in fileObj:
            tempVar = line.strip('\n').split('|')
            temp_dict[tempVar[0]] = tempVar[1]

    for val in studentIdList:
        if val in temp_dict:
            temp_list.append(temp_dict[val])
        else:
            temp_list.append('')

    return temp_list


def calculate_grade(totalMarks, limit):

    grade_factor = (100 - limit)/7
    if totalMarks <= limit:
        final_grade = 'F'
    elif totalMarks <= (limit + grade_factor):
        final_grade = 'C'
    elif totalMarks <= (limit + 2*grade_factor):
        final_grade = 'B-'
    elif totalMarks <= (limit + 3*grade_factor):
        final_grade = 'B'
    elif totalMarks <= (limit + 4*grade_factor):
        final_grade = 'B+'
    elif totalMarks <= (limit + 5*grade_factor):
        final_grade = 'A-'
    elif totalMarks <= (limit + 6*grade_factor):
        final_grade = 'A'
    else:
        final_grade = 'A+'
    return final_grade

def read_lists():

    firstNameList=[]
    lastNameList=[]

    classFileObj = open('class.txt', 'r')
    temp_list = []
    for line in classFileObj:
        tempVar = line.strip('\n').split('|')
        temp_list.append(tempVar)

    temp_list = sorted(temp_list, key=lambda x: x[0])

    for val in temp_list:
        studentIdList.append(val[0])
        firstNameList.append(val[1])
        lastNameList.append(val[2])

        completeData["student_id"] = studentIdList
        completeData["last_name"] = lastNameList
        completeData["first_name"] = firstNameList

        completeData["a1"] = fill_grades('a1')
        completeData["a2"] = fill_grades('a2')
        completeData["project"] = fill_grades('project')
        completeData["test1"] = fill_grades('test1')
        completeData["test2"] = fill_grades('test2')


    total_marks_list = []
    final_grades_list = []
    for x in range(len(completeData["student_id"])):
        totalMarks = 0
        if completeData["a1"][x]:
            totalMarks = totalMarks + (int(completeData["a1"][x]) / int(max_marks_list["a1"])) * grade_perc_value["a1"]
        if completeData["a2"][x]:
            totalMarks = totalMarks + (int(completeData["a2"][x]) / int(max_marks_list["a2"])) * grade_perc_value["a2"]
        if completeData["project"][x]:
            totalMarks = totalMarks + (int(completeData["project"][x]) / int(max_marks_list["project"])) * grade_perc_value["project"]
        if completeData["test1"][x]:
            totalMarks = totalMarks + (int(completeData["test1"][x]) / int(max_marks_list["test1"])) * grade_perc_value["test1"]
        if completeData["test2"][x]:
            totalMarks = totalMarks + (int(completeData["test2"][x]) / int(max_marks_list["test2"])) * grade_perc_value["test2"]

        total_marks_list.append(round(totalMarks,2))
        final_grades_list.append(calculate_grade(totalMarks, 50))

    completeData["total"] = total_marks_list
    completeData["grades"] = final_grades_list


read_lists()
mainMenu()

