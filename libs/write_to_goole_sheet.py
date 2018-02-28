import datetime
import pygsheets
import pygame
from .return_index import return_index
import requests

google_sheets = pygsheets.authorize(outh_file="auth.json")
sheet = google_sheets.open('Närvarolista Odd fellow')
workingsheet = sheet.sheet1


def getresult(membernumber, name, lodge):

    index = return_index()

    firstColumn = 'A' + str(index)
    secondColumn = 'B' + str(index)
    thirdColumn = 'C' + str(index)
    fouthColumn = 'D' + str(index)

    timestamp = datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p")

    workingsheet.update_cell(str(secondColumn), str(name))
    workingsheet.update_cell(str(firstColumn), timestamp)
    workingsheet.update_cell(str(thirdColumn), str(membernumber))
    workingsheet.update_cell(str(fouthColumn), lodge)

    pygame.mixer.init()
    pygame.mixer.music.load("/home/ekerot/PycharmProjects/odd_fellow_registration/audio/welcome.mp3")
    pygame.mixer.music.play()

    requests.post("http://localhost:8080/", data={'name': name, 'membernumber': membernumber})


    pass
