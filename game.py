'''
assignment: PA5: Fifteen Puzzle

author: Riya Jaitly

date: October 4, 2022

file: game.py, fifteen.py, graph.py

Program Summary: This program runs the game Fifteen Puzzle. Fifteen puzzle is 
a game where you arrange tiles in order from 1 to 15.

'''
from tkinter import *
import tkinter.font as font
from fifteen import Fifteen
from tkinter import ttk

#updates board when tile is clicked (if valid move)
def clickButton(tiles, name):
    if name == " ":
        name = '0'
    if name != 0:
        Fifteen.update(tiles, int(name))
    drawBoard(tiles, 1)


#draws Fifften Puzzle board and stores value in each tile
def drawBoard(tiles, drawInitial):
    #BUTTON 1
    tiles.tiles[0]
    text1 = StringVar()
    text1.set(str(Fifteen.isZero(tiles.tiles[0])))
    name1 = str(Fifteen.isZero(tiles.tiles[0]))
    button1 = Button(gui, textvariable=text1, name=str(name1), text=text1, 
                    bg='white', fg='black', font=font, height=2, width=5,
                    command = lambda : clickButton(tiles, name1))
    button1.configure(bg='coral')
    button1.place(x=80, y=40)

    #BUTTON 2
    tiles.tiles[1]
    text2 = StringVar()
    text2.set(str(Fifteen.isZero(tiles.tiles[1])))
    name2 = str(Fifteen.isZero(tiles.tiles[1]))
    button2 = Button(gui, textvariable=text2, name=str(name2), text=text2,
                    bg='white', fg='black', font=font, height=2, width=5,
                    command = lambda : clickButton(tiles, name2))
    button2.configure(bg='coral')
    button2.place(x=160, y=40)

    #BUTTON 3
    tiles.tiles[2]
    text3 = StringVar()
    text3.set(str(Fifteen.isZero(tiles.tiles[2])))
    name3 = str(Fifteen.isZero(tiles.tiles[2]))
    button3 = Button(gui, textvariable=text3, name=str(name3), text=text3,
                      bg='white', fg='black', font=font, height=2, width=5,
                      command = lambda : clickButton(tiles, name3))
    button3.configure(bg='coral')
    button3.place(x=240, y=40)

    #BUTTON 4
    tiles.tiles[3]
    text4 = StringVar()
    text4.set(str(Fifteen.isZero(tiles.tiles[3])))
    name4 = str(Fifteen.isZero(tiles.tiles[3]))
    button4 = Button(gui, textvariable=text4, name=str(name4), text=text4,
                      bg='white', fg='black', font=font, height=2, width=5,
                      command = lambda : clickButton(tiles, name4))
    button4.configure(bg='coral')
    button4.place(x=320, y=40)

    #BUTTON 5
    tiles.tiles[4]
    text5 = StringVar()
    text5.set(str(Fifteen.isZero(tiles.tiles[4])))
    name5 = str(Fifteen.isZero(tiles.tiles[4]))
    button5 = Button(gui, textvariable=text5, name=str(name5), text=text5,
                      bg='white', fg='black', font=font, height=2, width=5,
                      command = lambda : clickButton(tiles, name5))
    button5.configure(bg='coral')
    button5.place(x=80, y=100)

    #BUTTON 6
    tiles.tiles[5]
    text6 = StringVar()
    text6.set(str(Fifteen.isZero(tiles.tiles[5])))
    name6 = str(Fifteen.isZero(tiles.tiles[5]))
    button6 = Button(gui, textvariable=text6, name=str(name6), text=text6,
                      bg='white', fg='black', font=font, height=2, width=5,
                      command = lambda : clickButton(tiles, name6))
    button6.configure(bg='coral')
    button6.place(x=160, y=100)

    #BUTTON 7
    tiles.tiles[6]
    text7 = StringVar()
    text7.set(str(Fifteen.isZero(tiles.tiles[6])))
    name7 = str(Fifteen.isZero(tiles.tiles[6]))
    button7 = Button(gui, textvariable=text7, name=str(name7), text=text7,
                      bg='white', fg='black', font=font, height=2, width=5,
                      command = lambda : clickButton(tiles, name7))
    button7.configure(bg='coral')
    button7.place(x=240, y=100)

    #BUTTON 8
    tiles.tiles[7]
    text8 = StringVar()
    text8.set(str(Fifteen.isZero(tiles.tiles[7])))
    name8 = str(Fifteen.isZero(tiles.tiles[7]))
    button8 = Button(gui, textvariable=text8, name=str(name8), text=text8,
                      bg='white', fg='black', font=font, height=2, width=5,
                      command = lambda : clickButton(tiles, name8))
    button8.configure(bg='coral')
    button8.place(x=320, y=100)

    #BUTTON 9
    tiles.tiles[8]
    text9 = StringVar()
    text9.set(str(Fifteen.isZero(tiles.tiles[8])))
    name9 = str(Fifteen.isZero(tiles.tiles[8]))
    button9 = Button(gui, textvariable=text9, name=str(name9), text=text9,
                      bg='white', fg='black', font=font, height=2, width=5,
                      command = lambda : clickButton(tiles, name9))
    button9.configure(bg='coral')
    button9.place(x=80, y=160)

    #BUTTON 10
    tiles.tiles[9]
    text10 = StringVar()
    text10.set(str(Fifteen.isZero(tiles.tiles[9])))
    name10 = str(Fifteen.isZero(tiles.tiles[9]))
    button10 = Button(gui, textvariable=text10, name=str(name10), text=text10,
                      bg='white', fg='black', font=font, height=2, width=5,
                      command = lambda : clickButton(tiles, name10))
    button10.configure(bg='coral')
    button10.place(x=160, y=160)

    #BUTTON 11
    tiles.tiles[10]
    text11 = StringVar()
    text11.set(str(Fifteen.isZero(tiles.tiles[10])))
    name11 = str(Fifteen.isZero(tiles.tiles[10]))
    button11 = Button(gui, textvariable=text11, name=str(name11), text=text11,
                      bg='white', fg='black', font=font, height=2, width=5,
                      command = lambda : clickButton(tiles, name11))
    button11.configure(bg='coral')
    button11.place(x=240, y=160)

    #BUTTON 12
    tiles.tiles[11]
    text12 = StringVar()
    text12.set(str(Fifteen.isZero(tiles.tiles[11])))
    name12 = str(Fifteen.isZero(tiles.tiles[11]))
    button12 = Button(gui, textvariable=text12, name=str(name12), text=text12,
                      bg='white', fg='black', font=font, height=2, width=5,
                      command = lambda : clickButton(tiles, name12))
    button12.configure(bg='coral')
    button12.place(x=320, y=160)

    #BUTTON 13
    tiles.tiles[12]
    text13 = StringVar()
    text13.set(str(Fifteen.isZero(tiles.tiles[12])))
    name13 = str(Fifteen.isZero(tiles.tiles[12]))
    button13 = Button(gui, textvariable=text13, name=str(name13), text=text13,
                      bg='white', fg='black', font=font, height=2, width=5,
                      command = lambda : clickButton(tiles, name13))
    button13.configure(bg='coral')
    button13.place(x=80, y=220)

    #BUTTON 14
    tiles.tiles[13]
    text14 = StringVar()
    text14.set(str(Fifteen.isZero(tiles.tiles[13])))
    name14 = str(Fifteen.isZero(tiles.tiles[13]))
    button14 = Button(gui, textvariable=text14, name=str(name14), text=text14,
                      bg='white', fg='black', font=font, height=2, width=5,
                      command = lambda : clickButton(tiles, name14))
    button14.configure(bg='coral')
    button14.place(x=160, y=220)

    #BUTTON 15
    tiles.tiles[14]
    text15 = StringVar()
    text15.set(str(Fifteen.isZero(tiles.tiles[14])))
    name15 = str(Fifteen.isZero(tiles.tiles[14]))
    button15 = Button(gui, textvariable=text15, name=str(name15), text=text15,
                      bg='white', fg='black', font=font, height=2, width=5,
                      command = lambda : clickButton(tiles, name15))
    button15.configure(bg='coral')
    button15.place(x=240, y=220)

    #BUTTON 16
    tiles.tiles[15]
    text16 = StringVar()
    text16.set(str(Fifteen.isZero(tiles.tiles[15])))
    name16 = str(Fifteen.isZero(tiles.tiles[15]))
    button16 = Button(gui, textvariable=text16, name=str(name16), text=text16,
                      bg='white', fg='black', font=font, height=2, width=5,
                      command = lambda : clickButton(tiles, name16))
    button16.configure(bg='coral')
    button16.place(x=320, y=220)

    #Button that shows text when you win
    if drawInitial == 0:
        #BUTTON 17
        text17 = StringVar()
        text17=""
        button17 = Button(gui, bg='white', fg='black', font=font, height=2, width=30, 
                            text=text17)
        button17.configure(bg='coral')
        button17.place(x=0, y=350)
    else:
        if Fifteen.is_solved(tiles) == True:
            #BUTTON 17
            text17 = StringVar()
            text17="You solved the puzzle!"
            button17 = Button(gui, bg='white', fg='black', font=font, height=2, width=30, 
                                text=text17)
            button17.configure(bg='coral')
            button17.place(x=0, y=350)

        else: 
            #BUTTON 17
            text17 = StringVar()
            text17=""
            button17 = Button(gui, bg='white', fg='black', font=font, height=2, width=30, 
                                text=text17)
            button17.configure(bg='coral')
            button17.place(x=0, y=350)



#runs program
if __name__ == '__main__': 
    tiles = Fifteen()
    gui = Tk()
    gui.geometry("1000x1000")
    gui.title("Fifteen")
    font = font.Font(family='Helveca', size='25', weight='bold')

    #SHUFFLES BOARD
    Fifteen.shuffle(tiles)

    #DRAWS BOARD
    drawBoard(tiles, drawInitial=0)

    gui.mainloop()






