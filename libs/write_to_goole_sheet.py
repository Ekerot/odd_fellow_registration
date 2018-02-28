import datetime
import pygsheets
import pygame
from .return_index import return_index
import requests

#todo make shets into list
google_sheets = pygsheets.authorize(outh_file="auth.json")
sheet = google_sheets.open('Närvarolista Odd fellow')
sheet2 = google_sheets.open('Matanmälan')
worksheet = sheet.sheet1
worksheet2 = sheet2.sheet1


def getresult(membernumber, name, lodge):

    index = return_index()

    first_column = 'A' + str(index)
    second_column = 'B' + str(index)
    third_column = 'C' + str(index)
    fourth_column = 'D' + str(index)
    fifth_column = 'E' + str(index)

    timestamp = datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p")
    data = worksheet2.get_col(4, 'matrix', include_empty=False)

    if str(membernumber) in data:
        food = 'Ja'
        print(data)
    else:
        food = ''
        print(data)

    worksheet.update_cell(str(second_column), str(name))
    worksheet.update_cell(str(first_column), timestamp)
    worksheet.update_cell(str(third_column), str(membernumber))
    worksheet.update_cell(str(fourth_column), lodge)
    worksheet.update_cell(str(fifth_column), str(food))

    pygame.mixer.init()
    pygame.mixer.music.load("/home/ekerot/PycharmProjects/odd_fellow_registration/audio/welcome.mp3")
    pygame.mixer.music.play()

    requests.post("http://localhost:8080/", data={'name': name, 'membernumber': membernumber})

    pass
