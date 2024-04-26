import pytesseract
import urllib
from PIL import ImageGrab, Image
import os
import re
import tkinter as tk
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt, QPoint
import sys
from bs4 import BeautifulSoup #web html getter
import subprocess
import requests


pytesseract.pytesseract.tesseract_cmd = r'E:\Program Files\Python Shit\tesseract.exe' #path to tesseract since it doesnt work directly

#COORDS VAR
coord_entry = None
x1, y1, x2, y2 = 1481,640,1708,819

def screengrab():
    global x1, y1, x2, y2
    #capture the screenshot
    screenshot_image = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    #save the screenshot
    screenshot_image.save('screenshot.png')

#opens screenshot
def open_screen(): 
    os.startfile('screenshot.png')


class Overlay_QSS(QWidget):
    def __init__(self):
        super().__init__()
        
        #make the window transparent and remove frame
        self.setWindowOpacity(0.5)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        
        # Set mouse tracking to receive mouse move events
        self.setMouseTracking(True)
        
        # Initialize coordinates of the selection rectangle
        self.start_pos = None
        self.end_pos = None
        
    def paintEvent(self, event):
        #set up the painter
        painter = QPainter(self)
        painter.setPen(QColor(255, 0, 0, 255))
        painter.setBrush(QColor(255, 0, 0, 50))
        if self.start_pos and self.end_pos:
            painter.setOpacity(1.0)
            painter.drawRect(self.start_pos.x(), self.start_pos.y(), self.end_pos.x() - self.start_pos.x(), self.end_pos.y() - self.start_pos.y())
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            # Set the starting position of the selection rectangle
            self.start_pos = event.pos()
        elif event.button() == Qt.RightButton:
            self.close()
    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            # Update the ending position of the selection rectangle
            self.end_pos = event.pos()
            self.update()
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            global x1, y1, x2, y2
            # Get the coordinates of the selected rectangle and print them
            top_left_x = min(self.start_pos.x(), self.end_pos.x())
            top_left_y = min(self.start_pos.y(), self.end_pos.y())
            bottom_right_x = max(self.start_pos.x(), self.end_pos.x())
            bottom_right_y = max(self.start_pos.y(), self.end_pos.y())
            x1 = top_left_x
            y1 = top_left_y
            x2 = bottom_right_x
            y2 = bottom_right_y
            print(f"QSScoords Top left coordinate: ({top_left_x}, {top_left_y})")
            print(f"QSScoords Bottom right coordinate: ({bottom_right_x}, {bottom_right_y})")
            # Close the overlay window
            self.close()

def quick_select():
    app = QApplication(sys.argv)  
    # createoverlaywindow
    overlay = Overlay_QSS()
    overlay.showFullScreen() 
    # Start the event loop
    app.exec_()
    screengrab()

#uses screenshot and converts to text
def img2text():
    screenshot_image = Image.open("screenshot.png")
    # Convert the screenshot to grayscale and recognize the text using Tesseract OCR
    screenshot_image = screenshot_image.convert('L')
    text = pytesseract.image_to_string(screenshot_image)
    text = re.sub(r'[^\w\s\?]+', '', text) # remove special characters except spaces and question marks
    text = re.sub(r'\n', ' ', text) # replace line breaks with spaces
    text = text.strip() # remove leading and trailing spaces
    text = text.replace('_', ' ') # replace underscores with spaces
    return text

#searching valorant
def search_val():
    text = img2text()
    query = urllib.parse.quote(text + " valorant") # add "valorant" to the end of the search query
    url = f"https://www.google.com/search?q={query}"
    os.system(f'start {url}')

#searching valorant lore
def search_vallore():
    text = img2text()
    query = urllib.parse.quote(text + " valorant lore") # add "valorant" to the end of the search query
    url = f"https://www.google.com/search?q={query}"
    os.system(f'start {url}')

#highlight searching
def searchv2():
    text = img2text()
    search_query = urllib.parse.quote(text + " valorant")
    url = f"https://www.google.com/search?q={search_query}"
    first = webgetter(url)
    search_query = urllib.parse.quote(text + " valorant lore")
    url = f"https://www.google.com/search?q={search_query}"
    second = webgetter(url)
    return first,second



def webgetter(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    response = requests.get(url, headers=headers)

    html_content = response.content

    # Create a BeautifulSoup object from the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # find the first <b> tag
    bold_tag = soup.find('b')

    # get the preceding and succeeding <div> tags
    preceding_p_tag = bold_tag.find_previous('div')
    succeeding_p_tag = bold_tag.find_next('div')

    # get the text of the <b> tag and its preceding and succeeding <div> tags
    text = "⏩⏩" + bold_tag.text.strip() + '⏪⏪\n'
    text += preceding_p_tag.text.strip() + '\n'
    text += succeeding_p_tag.text.strip() + '\n'

    # remove any text after a fullstop
    text = re.sub('\..*', '.', text)

    return text

    

