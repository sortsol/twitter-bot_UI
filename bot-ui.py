#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from tkinter import *

master = Tk()


Label(master, text="Consumer Token").grid(row=0)
Label(master, text="Consumer Secret").grid(row=1)
Label(master, text="Access Token").grid(row=2)
Label(master, text="Access Secret").grid(row=3)



c_token = Entry(master)
c_secret = Entry(master)
a_token = Entry(master)
a_secret = Entry(master)


c_token.grid(row=0, column=1)
c_secret.grid(row=1, column=1)
a_token.grid(row=2, column=1)
a_secret.grid(row=3, column=1)

# return user-entered values for all tokens and secrets
def return_vals():
	c1 = c_token.get()
	c2 = c_secret.get()
	a1 = a_token.get()
	a2 = a_secret.get()
	return c1,c2,a1,a2

# exit window when clicking "Cancel"
Button(master, text='Cancel', command=master.quit).grid(row=4, column=0, sticky=W, pady=4)

# retrieve entered values and go to next page
Button(master, text='Next', command=printkeys).grid(row=4, column=1, sticky=W, pady=4)

mainloop()