import datetime
from datetime import *
from tkinter import *

import tkinter as tk

class Application(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		self.pack()
		self.create_widgets() # invokes these commands immediately which is why timer will run 
		                      # immediately if given the self.start
		

	def create_widgets(self):
		# Step 1: Create a 'Time Start' button
		self.start_timer = tk.Button(self)
		self.start_timer["text"] = "Start Timer"
		self.start_timer["command"] = self.start
		self.start_timer.pack(side="top")



		self.quit = tk.Button(self, text="Quit", fg="red",
							  command=self.master.destroy)
		self.quit.pack(side="bottom")

	def start(self):
		# Step 2: Print the start time
		start_time = datetime.now()
		print("The Start Time is: " + str(start_time))
		end_time = start_time + timedelta(seconds=5)
		print("You can take a break at " + str(end_time))
		print("Get to work!")
		self.time_iter = self.break_time(end_time)
		

	def break_time(self, end_time):
		while datetime.now() < end_time:
			if end_time == datetime.now():
				print("Time to take a break!")
				break
			print(datetime.now().strftime("%H:%M:%S"))



	# def short_break(self):
	# 	# Create a function that prints "Take a short break"
	# 	# to the window when the time has reached 25 minutes
	# 	# Step a: Start the timer
	# 	# Step b: Compare the initial time with the latter time (25 minutes later)
	# 	# Step c: Print "Take a break! to the screen"
	# 	# Step d: Start a 3 minute timer 
	# 	# Step e: Print "Alright, get back to work!"
	# 	if datetime.now() == self.begin.start_time + timedelta(seconds=5):
	# 		print("Take a 3 minute break!")





root = tk.Tk()
app = Application(master=root)
app.mainloop()