#########################################
#
#         70-100pt - Making a game
#
#########################################


# 70pt - Add buttons for left, right and down that move the player circle
# 100pt - using lab 11 as an example, add in three horizontally scrolling "enemies"
# Make them scroll at different speeds and directions.



from Tkinter import *
root = Tk()

drawpad = Canvas(root, width=800,height=600, background='white')
player = drawpad.create_oval(390,580,410,600, fill="red")

# Create your "enemies" here, before the class
enemy1 = drawpad.create_oval(100,250,150,300, fill="black")
enemy2 = drawpad.create_oval(200,350,250,400, fill="black")
enemy3 = drawpad.create_oval(10,60,70,120, fill="black")

class MyApp:
	def __init__(self, parent):
       	    global drawpad
       	    self.myParent = parent  
       	    self.myContainer1 = Frame(parent)
       	    self.myContainer1.pack()
       	    # Up Button
       	    self.up = Button(self.myContainer1)
       	    self.up.configure(text="up", background= "green")
       	    self.up.grid(row=0,column=3)
       	    # Down Button
       	    self.down = Button(self.myContainer1)
       	    self.down.configure(text="down", background= "green")
       	    self.down.grid(row=0,column=2)
       	    # Left Button
       	    self.left = Button(self.myContainer1)
       	    self.left.configure(text="left", background= "green")
       	    self.left.grid(row=0,column=1)
       	    # Right Button 
       	    self.right = Button(self.myContainer1)
       	    self.right.configure(text="right", background= "green")
       	    self.right.grid(row=0,column=4)
       	    # Bind an event to the first button
       	    self.up.bind("<Button-1>", self.upClicked)
       	    self.down.bind("<Button-1>", self.downClicked)
       	    self.left.bind("<Button-1>", self.leftClicked)
       	    self.right.bind("<Button-1>", self.rightClicked)
       	    drawpad.pack(side=BOTTOM)
	
	def animate(self):
	    global drawpad
	    global player
	    global enemy1
	    global enemy2
	    global enemy3
	   
	def upClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,0,-20)
		
	def downClicked(self,event):
	    global oval
	    global player
	    drawpad.move(player,0,20)
	    
	def leftClicked(self,event):
	    global oval
	    global player
	    drawpad.move(player,-20,0)
	
	def rightClicked(self,event):
	    global oval
	    global player
	    drawpad.move(player,20,0)
	    
app = MyApp(root)
root.mainloop()