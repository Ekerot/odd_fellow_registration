import datetime
import pygsheets
import pygame
from .return_index import return_index

google_sheets = pygsheets.authorize(outh_file="auth.json")
sheet = google_sheets.open('Närvarolista Odd fellow')
workingsheet = sheet.sheet1


def getresult(membernumber, name, lodge):

    index = return_index()

    first = 'A' + str(index)
    second = 'B' + str(index)
    third = 'C' + str(index)
    fird = 'D' + str(index)

    timestamp = datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p")

    workingsheet.update_cell(str(second), str(name))
    workingsheet.update_cell(str(first), timestamp)
    workingsheet.update_cell(str(third), str(membernumber))
    workingsheet.update_cell(str(fird), lodge)

    pygame.mixer.init()
    pygame.mixer.music.load("/home/ekerot/PycharmProjects/odd_fellow_registration/audio/welcome.mp3")
    pygame.mixer.music.play()

    return name

