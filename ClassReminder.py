import datetime
import pickle
# Defining the subject class
class Subject:
    # The subject class with have 4 attributes to identify the the subject to be sent
    def __init__(self,Class,time,day,location):
        self.Class = Class
        self.time = time
        self.day = day
        self.location = location
    # Setters for the attribute
    def changeClass(self, Class):
        self.Class = Class
    def changeTime(self, time):
        self.time = time
    def changeDay(self, day):
        self.day = day
    def changeLocation(self, location):
        self.location = location
    # Getters for the attributes
    def showClass(self):
        return self.Class
    def showTime(self):
        return self.time
    def showDay(self):
        return self.day
    def showLocation(self):
        return self.location
# This makes sure that when this python script is inherited, it doesn't run this part
if __name__ == "__main__":
    # saveData function saves the subjects using pickle in a .dat file
    def saveData(subjects):
        fileName = "PickleObjects.dat"
        openFile = open(fileName, 'wb')
        pickle.dump(subjects, openFile)
        openFile.close()
    # Classes gets the number of classes as input from the user, there is also error handling incase of bad input
    def Classes():
        flag = True
        while flag:
            try:
                numberOfClasses = int(input("How many classes are you taking?"))
                if not(numberOfClasses > 10 or numberOfClasses <= 0):
                    flag = False
            except ValueError:
                print("Please enter a number between 0 and 10 inclusive!")
        return numberOfClasses
    # subjectList function that get's the needed info to be included in the text for each class
    def subjectList(numberOfClasses):
        subjectList = []
        for i in range(numberOfClasses):
            Class = input("Name of Class")
            time =  input("Class time (This is what will be sent to you in the text)")
            flag = True
            while flag:
                try:
                    day = int(input("Day of the week in this formet(Monday = 0 --- Sunday = 7)"))
                    if (day>= 0 and day<=8):
                        flag = False
                except ValueError:
                    print("Enter a number between 0 and 7 inclusive")
            location = input("The location of your class, this can be anything")
            subjectList.append(Subject(Class,time,day,location))
        return subjectList
    # Main function that runs everything
    def main():
            allClasses = Classes()
            allSubjects = subjectList(allClasses)
            saveData(allSubjects)
    main()



