##modules
import os
from dotenv import load_dotenv #handles .env
import sys #handles system variables
import PyQt5.Qt
import PyQt5.QtWidgets
import requests #make request to API's
import PyQt5
# from PyQt5.QtWidgets import QApplication, QWidget ,QLabel, QlineEdit, QPushButton, QVBoxLayout #Front-end
#qt core
from weatherWindow import WeatherWindow
from PyQt5.QtCore import Qt
##functions
# print("weather API")
# load_dotenv()
# # weather_api_key = os.getenv("WK_API")
# weather_api_key = os.getenv("MY_API_WK")
# print(weather_api_key, "api key comes here")
# api_key = weather_api_key


# window = None

#Inital window creator using QMainWindow from PyQt
#This is a subclass for QMainWindow/Window
#we can improve encapsulation by seperating through different files
#Call itself to run
#PyQt5.QtWidgets.QWidget vs PyQt5.QtWidgets.QMainWindow
# class WeatherWindow(PyQt5.QtWidgets.QWidget):
#     # print(window)
#     def __init__(self):
#         super().__init__()
#         # self.setWindowTitle("754WeatherApp")
#         self.current_city_label = PyQt5.QtWidgets.QLabel("Enter city name", self)
#         self.current_city_input = PyQt5.QtWidgets.QLineEdit(self)
#         #these two will overlap, need a widget manger
#         self.confirm_city_button = PyQt5.QtWidgets.QPushButton("Confirm Weather", self)
#         self.temperature_label = PyQt5.QtWidgets.QLabel("70°F", self)
#         self.emoji_label = PyQt5.QtWidgets.QLabel(self)
#         self.description_label = PyQt5.QtWidgets.QLabel("Sunny", self)
#         self.setUI()
#         # self.setGeometry(0, 0, 1000, 1000)
#     #user interface/frontend
#     def setUI(self):
#         self.setWindowTitle("Weather App")

#         #window manger vertical
#         vertBox = PyQt5.QtWidgets.QVBoxLayout()
#         #add the following self.current_city_input, self.confirm_city_button, self.temperature_label, 
#         # self.emoji_label, self.description_label
#         vertBox.addWidget(self.current_city_label)
#         vertBox.addWidget(self.current_city_input)
#         vertBox.addWidget(self.confirm_city_button)
#         vertBox.addWidget(self.temperature_label)
#         vertBox.addWidget(self.emoji_label)
#         vertBox.addWidget(self.description_label)

#         #set the layout
#         self.setLayout(vertBox)

#         self.current_city_label.setAlignment(Qt.AlignCenter)
#         self.current_city_input.setAlignment(Qt.AlignCenter)
#         # self.confirm_city_button.setAlignment(Qt.AlignCenter) #has no center element
#         self.temperature_label.setAlignment(Qt.AlignCenter)
#         self.emoji_label.setAlignment(Qt.AlignCenter)
#         self.description_label.setAlignment(Qt.AlignCenter)

#         #align the layout by adding id
#         self.current_city_label.setObjectName("currentCityLabel")
#         self.current_city_input.setObjectName("currentCityInput")
#         self.confirm_city_button.setObjectName("confirmCityButton")
#         self.temperature_label.setObjectName("temperatureLabel")
#         self.emoji_label.setObjectName("emojiLabel")
#         self.description_label.setObjectName("descriptionLabel")

        

#         #set css stylesheet

#         #note any mistake will revert back to default
#         self.setStyleSheet("""
#             QLabel, QPushButton{
#                     font-family: calibri;
#                 }
#             QLabel#currentCityLabel{
#                            font-size:49px;
#                            font-style:bold;
#                            font-weight: bold;
#                 }
#             QLineEdit#currentCityInput{
#                            font-size:35px;
#                            font-style:bold;
                   
                           
#                            }
#             QPushButton#confirmCityButton{
#                            font-size:40px;
#                            font-style:bold;
#                            background-color:light gray;
#                            }
                           
#             QLabel#temperatureLabel{
#                            font-size:100px;
                           
#                            }
#             QLabel#emojiLabel{
#                            font-size:200px;
#                            padding:100px;
#                            font-family: Noto Emoji;
                        
#                            }
#             QLabel#descriptionLabel{
#                            font-size:100px;
#                            }

#             """)
            

#         #note id uses # and classes uses .
    
#         self.confirm_city_button.clicked.connect(self.getWeather)
#     def getWeather(self):
#         print("weather get")
#         #retrieve api key
#         key = api_key
#         #the input we want to get the text written when user clicks on confirm city button
#         city = self.current_city_input.text()
#         #using api to get our response given as JSON
#         url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}"
#         response = requests.get(url)
#         #convert to JSON object
#         data = response.json() 
#         print(data)
#         #since its in a dict we can retrieve by getting the key to the value
#         # print(data["cod"])
        
#         if data["cod"] == 200:
#             #passed and will get all data
#             self.handleError(str(data["cod"]))
#             self.handleWeather(data)
#         else:
#             #this json will contain COD(int) and a message(str)
#             self.handleError((data["message"]))
#         # self.handleError(str(data["cod"]))
#         #data pass and error codes can appear such as 404 or 400, etc
        
#         pass
#     ##get the temperature_label
#     #add a new text notifying
#     #if city was found or errors found
#     def handleError(self, errorMessage):
#         self.temperature_label.setText(errorMessage)
#         self.errorCode = errorMessage
#         # pass

#     # self.temperature_label = PyQt5.QtWidgets.QLabel("70°F", self)
#     # self.emoji_label = PyQt5.QtWidgets.QLabel("☀️", self)
#     # self.description_label
#     def handleWeather(self, data):
#         # if self.errorCode == 200:
#         # self.temperature_label.setText(data["weather"]["main"])
        
#         weatherData = data["weather"]
#         mainData = data["main"]
#         currentWeatherDescription = weatherData[0]["main"]
#         currentWeatherImage = weatherData[0]["main"]
#         kelvinNum = (mainData["temp"])
#         fahrenheitNum = ((kelvinNum - 273.15) * 1.8) + 32
#         # fahrenheitNum = (kelvinNum * 9/5) - 459.67
#         #to display we need in string
#         fahrenheitStr = f"{fahrenheitNum:.0f}*F"
        
#         # weatherData[0]
#         # print(weatherData[0]["main"])
#         # self.emoji_label.setText(weatherData[0]["main"])
       
#         # self.description_label.setText(weatherData[0]["main"])
#         self.temperature_label.setText(fahrenheitStr)
#         self.emoji_label.setText(currentWeatherImage)
#         self.description_label.setText(currentWeatherDescription)
#         # if currentWeather == "Clouds":
#         #     self.emoji_label.setText("⛅")
#         # pass

    
#     # pass

# ##Main
def main():
    #passing sys enables command line reading  
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    #add a seperate file for this class
    window = WeatherWindow()
    #window object created and is hidden
    window.show()

    #here we start the event loop
    sys.exit(app.exec_()) #exec non _ older code base
    # app.exec_()
    #window object is showen and will exit after closing
    # pass

#running main will require proc boilerplate
if __name__ == "__main__":
    print("start")
    main()

