from twilio.rest import Client
from ClassReminder import Subject
import datetime
import pickle
# loading the saved Data function
def loadData():
    fileName = "PickleObjects.dat"
    openFile = open(fileName,'rb')
    subjectList = pickle.load(openFile)
    openFile.close()
    return subjectList
# checking which classes the user has today and appending them to a list to be able to identify them in sendtext
def classesToday(list_of_subjects):
    classesTodayList = []
    # checking all subjects from the loadData functions and appending them to classesTodayList if they match the day today using datetime library
    for i in range(len(list_of_subjects)):
        if (datetime.datetime.today().weekday() == list_of_subjects[i].showDay()):
            classesTodayList.append(list_of_subjects[i])
    return classesTodayList
# The function that sends the Texts
def sendText(classes_today):
    # Your Account SID from twilio.com/console
    account_sid = "AC##############################"
    # Your Auth Token from twilio.com/console
    auth_token  = "################################"

    client = Client(account_sid, auth_token)
    # Enter your phone number in the 'to' and enter the twilio number in the 'from_', Leave the body as is.
    for index in  range(len(classes_today)):
        message = client.messages.create(
        to="+###########",
        from_="+###########",
        body=(classes_today[index].structuredMessage()))
def main():
    all_subjects = loadData()
    all_classes_today = classesToday(all_subjects)
    if (len(all_classes_today) > 0):
        sendText(all_classes_today)
main()
