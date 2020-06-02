from tkinter import *
import main_cashgame_copy as main_file
from main_cashgame_copy import * 

HEIGHT = 800
WIDTH = 1000

root = Tk()
frame = Frame(root, width=WIDTH, height=HEIGHT, bg="#80c1ff") # the frame
frame.pack()

btnFrame = Frame(root) # Button frame, placed top left corner 
btnFrame.place(rely=0.0, relx=0.0, height=HEIGHT)

btnNames = ["btnSet_players", "btnAdd_player", "btnRebuy", "btnStack_table", "btnFinal_stacks", "btnChange_chip_value", "btnChip_to_kr", "btnCalculate"] 

for i in range (len(main_file.all_states)): # Creating all button functions
    state = main_file.all_states[i]
    btnNames[i] = Button(btnFrame, text=main_file.all_states_names[i], bg="grey", command=eval(state))
    btnNames[i].pack(fill="x")

btnQuit = Button(btnFrame, text="Quit", bg="grey", command = root.destroy) # Quit button 
btnQuit.pack(fill="x")


root.mainloop()