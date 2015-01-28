#!/usr/bin/python
## -*- coding: utf-8 -*-

from sys import argv
import random
import math
from Tkinter import *


def clear_msg():
	msg[ 'text' ] = ''
	return

def input_val( event ):
	clear_msg()
	msg[ 'text' ] += ent.get()
	ent.delete(0, END)
	return

def new_game():
	clear_msg()
	msg[ 'text' ] += 'New game!'
	return

        
wnd = Tk()
wnd.title( 'Some random title' ) 
wnd.geometry( '200x200' )

Label( wnd, text='Let\'s play' ).pack( side=TOP )

ent = Entry( wnd, width=20 )    
ent.pack( side=TOP )
ent.focus() 
ent.bind( '<Return>', input_val )

Button( wnd, text=' Add word ', command=new_game ).pack( side=BOTTOM )

Label( wnd, text='\n' ).pack( side=TOP )
msg = Message( wnd, bg='black', fg='green', width=110, borderwidth=2 )
msg.pack( side=TOP )            
wnd.mainloop()
