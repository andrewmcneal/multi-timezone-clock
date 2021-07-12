#!/usr/bin/env python

# Imports Section. These Items need to be installed on the machine for it to work.
import Tkinter as tk
from datetime import datetime
import pytz
import time


root = tk.Tk()                                                # Creates the root canvas to place items on.
root.title('Timezones Clock')                                 # Creates the title in the title bar. If the line is removed the title will be 'tk'
canvas = tk.Canvas(root, width=400, height=200, bg="black")   # Sets the size of the canvas and generates the background color
canvas.grid(columnspan=3, rowspan=5)                          # Generates the grid for object placement

# This section creates the various time zones and loads up the first time variables. I haven't figured out why I am getting bad time info yet so don't use the initially loaded times
est = pytz.timezone('US/Eastern')
cnt = pytz.timezone('US/Central')
mtn = pytz.timezone('US/Mountain')
pac = pytz.timezone('US/Pacific')
utc_time = datetime.now()
utc_time =utc_time.replace(tzinfo=pytz.UTC) #replace method
eastern=utc_time.astimezone(est)        #astimezone method
central=utc_time.astimezone(cnt)        #astimezone method
mountain=utc_time.astimezone(mtn)        #astimezone method
pacific=utc_time.astimezone(pac)        #astimezone method


def timeupdate():    # This is the workhorse function. It has to stay here!
  x = 0
  while x == 0:    # creates the time loop
    utc_time = datetime.utcnow()      # Gets new time
    utc_time =utc_time.replace(tzinfo=pytz.UTC) #replace method
    eastern=utc_time.astimezone(est)        #astimezone method
    central=utc_time.astimezone(cnt)        #astimezone method
    mountain=utc_time.astimezone(mtn)        #astimezone method
    pacific=utc_time.astimezone(pac)        #astimezone method

    utctimefield = tk.Label(root, text=utc_time.strftime("%H:%M"), font="Raleway", fg="white", bg="black")            # Loads and formats the label with the new time for utc
    utctimefield.grid(columnspan=1, column=1, row=0)                                                                  # Places the label on the grid
    easterntimefield = tk.Label(root, text=eastern.strftime("%H:%M"), font="Raleway 12 bold", fg="red", bg="black")   # Loads and formats the label with the new time for Eastern
    easterntimefield.grid(columnspan=1, column=1, row=1)                                                              # Places the label on the grid
    centraltimefield = tk.Label(root, text=central.strftime("%H:%M"), font="Raleway", fg="white", bg="black")         # Loads and formats the label with the new time for Central
    centraltimefield.grid(columnspan=1, column=1, row=2)                                                              # Places the label on the grid
    mountaintimefield = tk.Label(root, text=mountain.strftime("%H:%M"), font="Raleway", fg="white", bg="black")       # Loads and formats the label with the new time for Mountain
    mountaintimefield.grid(columnspan=1, column=1, row=3)                                                             # Places the label on the grid
    pacifictimefield = tk.Label(root, text=pacific.strftime("%H:%M"), font="Raleway", fg="white", bg="black")         # Loads and formats the label with the new time for Pacific
    pacifictimefield.grid(columnspan=1, column=1, row=4)                                                              # Places the label on the grid

    root.update()   # Updates the visual of all labels. DO NOT SKIP THIS!
    time.sleep(1)   # Rests the loop for 1 second.


# This secion Initially builds the labels on the canvas. I am only commenting out the first time zone but the comments will be the same for the others
utcitsfield = tk.Label(root, text="It's", font="Raleway", fg="white", bg="black")   # Loads and formats the label of the first cell of the grid with "It's"
utcitsfield.grid(columnspan=1, column=0, row=0)                                     # Places the label on the grid
utctimefield = tk.Label(root, text=" ", font="Raleway", fg="white", bg="black")     # Loads and formats the label of the second cell of the grid with a space
utctimefield.grid(columnspan=1, column=1, row=0)                                    # Places the label on the grid
utcfield = tk.Label(root, text="UTC/GMT", font="Raleway", fg="white", bg="black")   # Loads and formats the label of the third cell of the grid with the timezone in use
utcfield.grid(columnspan=1, column=2, row=0)                                        # Places the label on the grid

easternitsfield = tk.Label(root, text="It's", font="Raleway 12 bold", fg="red", bg="black")
easternitsfield.grid(columnspan=1, column=0, row=1)
easterntimefield = tk.Label(root, text=" ", font="Raleway 12 bold", fg="red", bg="black")
easterntimefield.grid(columnspan=1, column=1, row=1)
easternfield = tk.Label(root, text="US/Eastern", font="Raleway 12 bold", fg="red", bg="black")
easternfield.grid(columnspan=1, column=2, row=1)

centralitsfield = tk.Label(root, text="It's", font="Raleway", fg="white", bg="black")
centralitsfield.grid(columnspan=1, column=0, row=2)
centraltimefield = tk.Label(root, text=" ", font="Raleway", fg="white", bg="black")
centraltimefield.grid(columnspan=1, column=1, row=2)
centralfield = tk.Label(root, text="US/Central", font="Raleway", fg="white", bg="black")
centralfield.grid(columnspan=1, column=2, row=2)

mountainitsfield = tk.Label(root, text="It's", font="Raleway", fg="white", bg="black")
mountainitsfield.grid(columnspan=1, column=0, row=3)
mountaintimefield = tk.Label(root, text=" ", font="Raleway", fg="white", bg="black")
mountaintimefield.grid(columnspan=1, column=1, row=3)
mountainfield = tk.Label(root, text="US/Mountain", font="Raleway", fg="white", bg="black")
mountainfield.grid(columnspan=1, column=2, row=3)

pacificitsfield = tk.Label(root, text="It's", font="Raleway", fg="white", bg="black")
pacificitsfield.grid(columnspan=1, column=0, row=4)
pacifictimefield = tk.Label(root, text=" ", font="Raleway", fg="white", bg="black")
pacifictimefield.grid(columnspan=1, column=1, row=4)
pacificfield = tk.Label(root, text="US/Pacific", font="Raleway", fg="white", bg="black")
pacificfield.grid(columnspan=1, column=2, row=4)

# Its button time!
start_button=tk.Button(root,text="Start",command=timeupdate)       # This creates the button that starts the clock and calls the the workhorse function above
start_button.grid(columnspan=1, column=1, row=5)                   # Places the button on the grid, yes, I know I'm outside my grid

start_button=tk.Button(root,text="Exit",command=root.destroy)      # This destroys the canvas on the button click allowing for a clean exit
start_button.grid(columnspan=1, column=2, row=5)                   # Places the button on the grid.

root.mainloop()    # Finally, we launch the canvas and all of the magic that goes along with it.
