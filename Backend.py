import tkinter as tk

def timer(root, hours, minutes, seconds, finished_bool, func, widget_var):
	print(hours + minutes + seconds)
	if hours + minutes + seconds > 0:
		finished_bool = False

		#Backend
		if hours == 0 and minutes == 0 and seconds > 0:
		    seconds-=1
		elif hours == 0 and minutes > 0 and seconds == 0:
		    seconds = 59
		    minutes-=1
		elif hours == 0  and minutes > 0 and seconds > 0:
		    seconds-=1
		elif hours > 0 and minutes == 0 and seconds == 0:
		    hours-=1
		    minutes = 59
		    seconds = 59
		elif hours > 0 and minutes > 0 and seconds == 0:
		    minutes-=1
		    seconds = 59
		elif hours > 0 and minutes > 0 and seconds > 0:
		    seconds-=1
		elif hours > 0 and minutes == 0  and seconds > 0:
		    seconds-=1
		else:
		    pass

		#Making the timer look more like a timer only when the digits are 1. Eg, 1:2:9 to 01:02:09
		if (hours >= 0 and hours < 10):
		    hours = "0" + str(hours)
		if (minutes >= 0 and minutes < 10):
		    minutes = "0" + str(minutes)
		if (seconds >= 0 and seconds < 10):
		    seconds = "0" + str(seconds)

		#Displaying the timer
		widget_var.set(f"{hours}: {minutes}: {seconds}")
		root.after(1000, timer(root, int(hours), int(minutes), int(seconds), finished_bool, func, widget_var))
	else:
	    finished_bool = True
	    print("done")
	    func()