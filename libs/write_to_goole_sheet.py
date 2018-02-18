import datetime
import pygsheets

google_sheets = pygsheets.authorize(outh_file="auth.json")
sheet = google_sheets.open('Närvarolista Odd fellow')
workingsheet = sheet.sheet1


def getresult(membernumber, name, index):

    first = 'A' + str(index)
    second = 'B' + str(index)
    third = 'C' + str(index)
    fird = 'D' + str(index)

    print(name)
    timestamp = datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p")

    workingsheet.update_cell(str(second), str(name))
    workingsheet.update_cell(str(first), timestamp)
    workingsheet.update_cell(str(third), str(membernumber))
    workingsheet.update_cell(str(fird), 'Your orden name')
    pass

