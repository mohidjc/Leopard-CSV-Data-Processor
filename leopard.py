"""
@author: Mohid Javed Chaudhry

"""

import csv


class Leopard:

    def __init__(self, filepath: str) -> None:
        self.filepath = filepath
        header_list = []
        data_list = []
        self.Hl = header_list
        self.Dl = data_list
        self.file_value = 0

        header_found = False
        try:
            # Opens the file only for reading
            with open(self.filepath, "r") as fileObject:
                reader = csv.reader(fileObject)
                for row in reader:
                    # Allows to set first row in csv file as header list
                    if header_found is False:
                        self.Hl = row
                        header_found = True
                    else:
                        # The other rows in file get appended to data list
                        self.Dl.append(row)
        except FileNotFoundError:
            print("file not found")
            self.file_value = 1

        if len(self.Hl) == 0 and self.file_value == 0:
            print("empty file")

    def get_header(self) -> list:
        if len(self.Hl) == 0:
            return None
        else:
            # Returns list with only the headers for each csv file
            return self.Hl

    def get_data(self) -> list:
        if len(self.Hl) == 0:
            return None
        else:
            # Returns a 2 dimentional list with data for each csv file
            return self.Dl

    def stats(self) -> dict:
        if self.get_header() is not None and self.get_data() is not None:
            main_dict = {}
            for i in range(0, len(self.Dl[1])):
                # Checks for indexes with numeric elements
                if self.Dl[1][i].isnumeric():
                    inside_dict = {}
                    count = 0
                    mean = 0
                    counter_1 = 0
                    counter_2 = 0
                    # Conversion to int for calculations
                    minimum = int(self.Dl[1][i])
                    maximum = int(self.Dl[1][i])
                    total = 0
                    for j in range(0, len(self.Dl)):
                        if self.Dl[j][i] == "":
                            # Ignores the values where null data
                            counter_1 = 1
                        elif self.Dl[j][i] == "NA":
                            counter_1 = 2
                        elif self.Dl[j][i] == "-":
                            counter_2 = counter_1 - counter_2
                        else:
                            Current_Num = int(self.Dl[j][i])
                            count += 1
                            total = total+Current_Num
                            if Current_Num <= minimum:
                                minimum = Current_Num
                            if Current_Num >= maximum:
                                maximum = Current_Num
                    mean = total/count
                    mean = round(mean, 2)
                    count1 = str(count)
                    mean1 = str(mean)
                    minimum1 = str(minimum)
                    maximum1 = str(maximum)
                    # The dictionary is assigned the calculated variables
                    inside_dict["count"] = count1
                    inside_dict["mean"] = mean1
                    inside_dict["min"] = minimum1
                    inside_dict["max"] = maximum1
                    # The dictionary is then added inside another dictionary
                    main_dict[self.Hl[i]] = inside_dict
            return main_dict
        else:
            return None

    def html_stats(self, stats: dict, filepath: str) -> None:
        if self.stats() is not None:

            with open(filepath, "w") as html:
                html.write("<html>\n")
                html.write("<head>\n")
                html.write("<meta charset=\"UTF-8\">\n")
                html.write("<style>\n")
                html.write("table, th, td {\n")
                html.write("border: 1px solid black;\n")
                html.write("border-collapse: collapse;\n")
                html.write("}\n")
                html.write("</style>\n")
                html.write("</head>\n")
                html.write("<body>\n")
                html.write("<table>\n")

                # For the first row it should include headers
                html.write("<tr>\n")
                html.write("<th> calculations</th>\n")
                for i in stats:
                    html.write("<th>"+i+"</th>\n")
                html.write("</tr>\n")

                # The other rows hold calculations such as mean
                # The respective columns should hold the data itself
                html.write("<tr>\n")
                html.write("<td> count</td>\n")
                for i in stats:
                    html.write("<td>"+stats[i]["count"]+"</td>\n")
                html.write("</tr>\n")

                html.write("<tr>\n")
                html.write("<td> mean</td>\n")
                for i in stats:
                    html.write("<td>"+stats[i]["mean"]+"</td>\n")
                html.write("</tr>\n")

                html.write("<tr>\n")
                html.write("<td> min</td>\n")
                for i in stats:
                    html.write("<td>"+stats[i]["min"]+"</td>\n")
                html.write("</tr>\n")

                html.write("<tr>\n")
                html.write("<td> max</td>\n")
                for i in stats:
                    html.write("<td>"+stats[i]["max"]+"</td>\n")
                html.write("</tr>\n")

                html.write("</table>\n")
                html.write("</body>\n")
                html.write("</html>\n")

    def count_instances(self, ChosenHeader: str, ChosenValue: str, ChosenHeader2: str, ChosenValue2: str) -> int:
        """
        To use this method the user has to pass 4 arguments, all
        of which have to be string data type regardless of them being
        numeric. The arguments should be passed in order, for example
        to find count for instances where Age=20 and Gender=Male the user
        will have to pass Age,20,Gender,Male. The method will return the
        count for all instances where both the statements Age=20 and
        Gender=Male is true. However the user should make sure that the
        spellings for each argument is correct or that the argument passed
        actually exists because otherwise the method will give a print
        statement showing why the error has occured and will also
        return 0 as the count for the instances. If the file doesnt exist
        it should return None.
        """
        if self.get_header() is not None and self.get_data() is not None:
            indexVar = -1
            for i in range(0, len(self.Hl)):
                if self.Hl[i] == ChosenHeader:
                    # Index is saved for header that matches the argument
                    indexVar = i
            if indexVar == -1:
                print("Wrong Header Name for the first one")
                return 0

            indexList = []
            check_value = -1
            for j in range(0, len(self.Dl)):
                # Finds all instances where the argument is matched
                if self.Dl[j][indexVar] == ChosenValue:
                    check_value = j
                    # List holds all the indexes for the instaces
                    indexList.append(j)
            if check_value == -1:
                print("This value doesnt exist for the given first header")
                return 0

            indexVar2 = -1
            for z in range(0, len(self.Hl)):
                if self.Hl[z] == ChosenHeader2:
                    indexVar2 = z
            if indexVar2 == -1:
                print("Wrong Header Name for the second one")
                return 0

            check_value1 = -1
            countInstances = 0
            for lo in range(0, len(self.Dl)):
                if self.Dl[lo][indexVar2] == ChosenValue2:
                    check_value1 = lo
                    # Iterates through the list and finds all the instances
                    # that match other instances and the count is incremented
                    for index in indexList:
                        if lo == index:
                            countInstances += 1
            if check_value1 == -1:
                print("This value doesnt exist for the given second header")
                return 0

            return countInstances
        else:
            return None


if __name__ == "__main__":
    # DO NOT COMMENT ALL WHEN SUBMIT YOUR FILE, cannot have an if statement
    # with nothing afterwards.

    # test diabetes_data.csv
    test = Leopard("diabetes_data.csv")
    print(test.get_header())
    print(test.get_data())
    stats = test.stats()
    print(stats)
    test.html_stats(stats, "diabetes.html")
    print(test.count_instances("Age", "60", "Gender", "Male"))
    # Should return 10

    # test fide2021.csv
    test2 = Leopard("fide2021.csv")
    print(test2.get_header())
    print(test2.get_data())
    stats2 = test2.stats()
    print(stats2)
    test2.html_stats(stats2, "fide2021.html")
    print(test2.count_instances("Country", "RUS", "B-Year", "1990"))
    # Should return 3

    # test student.csv
    test3 = Leopard("student.csv")
    print(test3.get_header())
    print(test3.get_data())
    stats3 = test3.stats()
    print(stats3)
    test3.html_stats(stats3, "student.html")
    print(test3.count_instances("famsize", "GT3", "guardian", "mother"))
    # Should return 192
