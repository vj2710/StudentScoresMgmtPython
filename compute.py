class computeOptions:

    listTypeOfFile = ['a1', 'a2', 'pr', 't1', 't2']

    def marksTypePrompt(self):
        typeOfFile = input('''\nPlease select the type of file:
    A1, A2, PR, T1, T2 \n''')
        return typeOfFile.lower()

    def printOption1(self, complete_data, max_marks_list, marksType):

        print(marksType.upper() + ' grades (' +max_marks_list[marksType] + ')')

        for x in range(len(complete_data["student_id"])):
            print("{:<7}".format(complete_data["student_id"][x]), "{:<14}".format(complete_data["last_name"][x] + ', ' + complete_data["first_name"][x]), "{:<7}".format(complete_data[marksType][x]))

    def printOption2(self, complete_data, max_marks_list, marksType):

        total = 0

        for val in complete_data[marksType]:
            if val != '':
                total = total + int(val)

        average = round(total/len(complete_data[marksType]),2)

        print(marksType+' average:',average,'/', max_marks_list[marksType])

    def print_option3(self, complete_data):
        print("{:<7}".format("ID"), "{:<7}".format("LN"), "{:<7}".format("FN"), "{:<7}".format("A1"), "{:<7}".format("A2")
              , "{:<7}".format("PR"), "{:<7}".format("T1"), "{:<7}".format("T2"), "{:<7}".format("GR"), "{:<7}".format("FL"))

        for x in range(len(complete_data["student_id"])):
            print("{:<7}".format(complete_data["student_id"][x]), "{:<7}".format(complete_data["last_name"][x]), "{:<7}".format(complete_data["first_name"][x]),
            "{:<7}".format(complete_data["a1"][x]), "{:<7}".format(complete_data["a2"][x]), "{:<7}".format(complete_data["project"][x]),
            "{:<7}".format(complete_data["test1"][x]), "{:<7}".format(complete_data["test2"][x]), "{:<7}".format(complete_data["total"][x]),
            "{:<7}".format(complete_data["grades"][x]))

    def printOption4(self, complete_data, sort_order):
        data_list = complete_data.values()
        updated_data_list = list(map(list, zip(*data_list)))
        if sort_order == "lt":
            updated_data_list.sort(key=lambda x:x[2], reverse=True)
        elif sort_order == "gr":
            updated_data_list.sort(key=lambda x: x[8], reverse=True)

        print("{:<7}".format("ID"), "{:<7}".format("LN"), "{:<7}".format("FN"), "{:<7}".format("A1"),
              "{:<7}".format("A2")
              , "{:<7}".format("PR"), "{:<7}".format("T1"), "{:<7}".format("T2"), "{:<7}".format("GR"),
              "{:<7}".format("FL"))

        for x in range(len(updated_data_list)):
            print("{:<7}".format(updated_data_list[x][0]), "{:<7}".format(updated_data_list[x][1]),
                  "{:<7}".format(updated_data_list[x][2]),
                  "{:<7}".format(updated_data_list[x][3]), "{:<7}".format(updated_data_list[x][4]),
                  "{:<7}".format(updated_data_list[x][5]),
                  "{:<7}".format(updated_data_list[x][6]), "{:<7}".format(updated_data_list[x][7]),
                  "{:<7}".format(updated_data_list[x][8]),
                  "{:<7}".format(updated_data_list[x][9]))

    def optionMenu(self, complete_data, max_marks_list, myInput):
        if myInput == "3":
            self.print_option3(complete_data)
        elif myInput == "4":
            while True:
                sortOrderInput = input('''\nPlease select sort order:
LT(Last Name) or GR(Numeric Grades) \n''')
                if sortOrderInput.lower() == "lt" or sortOrderInput.lower() == "gr":
                    self.printOption4(complete_data, sortOrderInput.lower())
                    break
                else:
                    print("Invalid Choice... Please try Again\n")

        else:
            while True:

                typeOfFile = self.marksTypePrompt()

                if typeOfFile in self.listTypeOfFile:
                    if(typeOfFile == 'pr'):
                        typeOfFile='project'
                    elif(typeOfFile == 't1'):
                        typeOfFile='test1'
                    elif (typeOfFile == 't2'):
                        typeOfFile = 'test2'

                    if myInput == "1":
                        self.printOption1(complete_data, max_marks_list, typeOfFile)
                        break
                    elif myInput == "2":
                        self.printOption2(complete_data, max_marks_list, typeOfFile)
                        break
                else:
                    print("Invalid Choice... Please try Again\n")








