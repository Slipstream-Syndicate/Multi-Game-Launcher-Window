# Game Launcher

import tkinter.messagebox as tkmb
import customtkinter as ctk
import time



#__________ IMPORTING OTHER PROJECTS ___________________

def Play_MMG():
    tkmb.showinfo(title = 'Navigation Instruction', message = 'This game in running on Python Shell. Open Shell to play the game!')
    import mastermind_game

def Play_OE():
    tkmb.showinfo(title = 'Navigation Instruction', message = 'This game in running on Python Shell. Open Shell to play the game!')
    import OE_game

def Play_RPS():
    tkmb.showinfo(title = 'Navigation Instruction', message = 'This game in running on Python Shell. Open Shell to play the game!')
    import RPS_game

def Play_SP():
    import single_player

def Play_sudoku():
    tkmb.showinfo(title = 'Navigation Instruction', message = 'This game in running on Python Shell. Open Shell to play the game!')
    import sudoku_solver


window = ctk.CTk()
window.geometry("1370x380")
window.title("Welcome to Game Launcher")
window.resizable()

font1 = ('Arial', 25, 'bold')
font2 = ('Arial', 20, 'bold')
font3 = ('Arial', 17, 'bold')

main_label = ctk.CTkLabel(master = window, font = font1, text_color = "white", text = "Welcome to Game Launcher!")
main_label.place(x = 520, y = 12)
#_____________________________________________________________________________________________________

frame1 = ctk.CTkFrame(master = window, border_width = 2, border_color = '#ff0000', bg_color = '#141414', fg_color = '#444547', corner_radius = 10, width = 250, height = 250)
frame1.place(x = 20, y = 60)

label1 = ctk.CTkLabel(master = frame1, font = font2, text_color = "white", text = "Mastermind Game")
label1.place(x = 10, y = 12)

label2 = ctk.CTkLabel(master = frame1, font = font3, text_color = "white", text = "\n      Can you guess the \n      correct number? \n\n Game modes: \n\n  > Easy \n > Hard")
label2.place(x = 10, y = 42)

button1 = ctk.CTkButton(master = frame1, border_width = 2, border_color = "#ff0000", corner_radius = 10, fg_color = "#444547", hover = True, hover_color = 'black', text = "PLAY", text_color = 'white', command = Play_MMG, height = 40, width = 25)
button1.place(x = 100, y = 200)

#_____________________________________________________________________________________________________

frame2 = ctk.CTkFrame(master = window, bg_color = '#141414', fg_color = '#444547', corner_radius = 10, border_width = 2, border_color = '#fff700', width = 250, height = 250)
frame2.place(x = 290, y = 60)

label3 = ctk.CTkLabel(master = frame2, font = font2, text_color = "white", text = "MyPL")
label3.place(x = 10, y = 12)

label4 = ctk.CTkLabel(master = frame2, font = font3, text_color = "white", text = "\n Interesting Cricket \n   Premiere League \n\n > 8 teams to choose from!!! \n\n  View Points Table to see \n who is on Top!")
label4.place(x = 10, y = 42)

button2 = ctk.CTkButton(master = frame2, border_width = 2, border_color = "#fff700", corner_radius = 10, fg_color = "#444547", hover = True, hover_color = 'black', text = "PLAY", text_color = 'white', command = Play_OE, height = 40, width = 25)
button2.place(x = 100, y = 200)

#_____________________________________________________________________________________________________

frame3 = ctk.CTkFrame(master = window, bg_color = '#141414', fg_color = '#444547', corner_radius = 10, border_width = 2, border_color = '#11ff00', width = 250, height = 250)
frame3.place(x = 560, y = 60)

label5 = ctk.CTkLabel(master = frame3, font = font2, text_color = "white", text = "Rock, Paper, Scissors")
label5.place(x = 10, y = 12)

label6 = ctk.CTkLabel(master = frame3, font = font3, text_color = "white", text = "\n       Can you defeat the \n      computer in: \n\n       Rock \n       Paper \n       Scissors?")
label6.place(x = 10, y = 42)

button3 = ctk.CTkButton(master = frame3, border_width = 2, border_color = "#11ff00", corner_radius = 10, fg_color = "#444547", hover = True, hover_color = 'black', text = "PLAY", text_color = 'white', command = Play_RPS, height = 40, width = 25)
button3.place(x = 100, y = 200)

#_____________________________________________________________________________________________________

frame4 = ctk.CTkFrame(master = window, bg_color = '#141414', fg_color = '#444547', corner_radius = 10, border_width = 2, border_color = '#1120f2', width = 250, height = 250)
frame4.place(x = 830, y = 60)

label7 = ctk.CTkLabel(master = frame4, font = font2, text_color = "white", text = "Fun Rectangle Controller")
label7.place(x = 10, y = 12)

label8 = ctk.CTkLabel(master = frame4, font = font3, text_color = "white", text = "\n   Race your token around \n    the screen and have fun!")
label8.place(x = 10, y = 42)

button4 = ctk.CTkButton(master = frame4, border_width = 2, border_color = "#1120f2", corner_radius = 10, fg_color = "#444547", hover = True, hover_color = 'black', text = "PLAY", text_color = 'white', command = Play_SP, height = 40, width = 25)
button4.place(x = 100, y = 200)

#_____________________________________________________________________________________________________

frame5 = ctk.CTkFrame(master = window, bg_color = '#141414', fg_color = '#444547', corner_radius = 10, border_width = 2, border_color = '#9e00fa', width = 250, height = 250)
frame5.place(x = 1100, y = 60)

label9 = ctk.CTkLabel(master = frame5, font = font2, text_color = "white", text = "Sudoku Solver")
label9.place(x = 10, y = 12)

label10 = ctk.CTkLabel(master = frame5, font = font3, text_color = "white", text = "\n Stuck on a hard Sudoku? \n\n Take help of Sudoku Solver!")
label10.place(x = 10, y = 42)

button5 = ctk.CTkButton(master = frame5, border_width = 2, border_color = "#9e00fa", corner_radius = 10, fg_color = "#444547", hover = True, hover_color = 'black', text = "PLAY", text_color = 'white', command = Play_sudoku, height = 40, width = 25)
button5.place(x = 100, y = 200)

#_____________________________________________________________________________________________________

button6 = ctk.CTkButton(master = window, border_width = 2, border_color = '#ff0000', corner_radius = 10, fg_color =  '#595957', hover = True, hover_color = 'black', text = "EXIT", text_color  ="white", command = window.destroy, height = 45, width = 30)
button6.place(x = 660, y =325)
window.mainloop()
