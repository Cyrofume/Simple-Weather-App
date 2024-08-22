##modules

import sys #handles system variables
import PyQt5.Qt
import PyQt5.QtWidgets
import requests #make request to API's
import PyQt5
# from PyQt5.QtWidgets import QApplication, QWidget ,QLabel, QlineEdit, QPushButton, QVBoxLayout #Front-end

##functions
print("weather API")

window = None

#Inital window creator using QMainWindow from PyQt
#Call itself to run
#PyQt5.QtWidgets.QWidget vs PyQt5.QtWidgets.QMainWindow
class WeatherWindow(PyQt5.QtWidgets.QWidget):
    # print(window)
    def __init__(self):
        super().__init__()
        # self.setWindowTitle("754WeatherApp")
        self.current_city_label = PyQt5.QtWidgets.QLabel("Enter city name", self)
        self.current_city_input = PyQt5.QtWidgets.QLineEdit(self)
        #these two will overlap, need a widget manger
        self.confirm_city_button = PyQt5.QtWidgets.QPushButton("Confirm Weather", self)
        self.temperature_label = PyQt5.QtWidgets.QLabel("70*F", self)
        self.emoji_label = PyQt5.QtWidgets.QLabel("*", self)
        self.description_label = PyQt5.QtWidgets.QLabel("Sunny", self)
        self.setUI()
        # self.setGeometry(0, 0, 1000, 1000)
    #user interface/frontend
    def setUI(self):
        self.setWindowTitle("Weather App")

        #window manger vertical
        vertBox = PyQt5.QtWidgets.QVBoxLayout()
        #add the following self.current_city_input, self.confirm_city_button, self.temperature_label, 
        # self.emoji_label, self.description_label
        vertBox.addWidget(self.current_city_label)
        vertBox.addWidget(self.current_city_input)
        vertBox.addWidget(self.confirm_city_button)
        vertBox.addWidget(self.temperature_label)
        vertBox.addWidget(self.emoji_label)
        vertBox.addWidget(self.description_label)

        #set the layout
        self.setLayout(vertBox)

        #align the layout by adding id
        self.current_city_label.setObjectName("currentCityLabel")
        self.current_city_input.setObjectName("currentCityInput")
        self.confirm_city_button.setObjectName("confirmCityButton")
        self.temperature_label.setObjectName("temperatureLabel")
        self.emoji_label.setObjectName("emojiLabel")
        self.description_label.setObjectName("descriptionLabel")
        #set css stylesheet

        #note any mistake will revert back to default
        self.setStyleSheet("""
            QLabel, QPushButton{
                    font-family: calibri;
                }
            QLabel#currentCityLabel{
                           font-size:49px;
                           font-style:bold;
                           font-weight: bold;
                }
                           

            """)

        #note id uses # and classes uses .

    
    # pass

##Main
def main():
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    window = WeatherWindow()
    #window object created and is hidden
    window.show()
    sys.exit(app.exec_()) #exec non _ older code base
    #window object is showen and will exit after closing
    # pass

#running main will require proc boilerplate
if __name__ == "__main__":
    print("start")
    main()

