#IMPORTS
from tkinter import *
from weather_with_wrapper import Weather

#-------------------------------------------------
#GUI
# root = Tk()
# root.title('Weather')
# root.geometry("600x400")

# root.mainloop()

w = Weather('Tralee,IE')
w.get_current_cloud_status()