import tkinter as tk
import sys
import tkinter.messagebox

window = tk.Tk()
window.title('tic tac toe')
window.geometry("400x400")
window.columnconfigure(1, minsize=75)
window.rowconfigure([0, 1], minsize=50)

bclick = True
flag = 0

def btnclicked(buttons):
    global bclick, flag
    if buttons["text"] == " " and bclick == True:
        buttons['fg'] = "red"
        buttons['text'] = "X"
        bclick = False
        CheckForWin()
        flag += 1

    elif buttons["text"] == " " and bclick == False:
        buttons['fg'] = "blue"
        buttons['text'] = "O"
        bclick = True
        CheckForWin()
        flag += 1
    else:
        tkinter.messagebox.showinfo("tic tac toe", "This button is already clicked!")

def CheckForWin():
    if(button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
        button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or
        button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X' or
        button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or
        button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X' or
        button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
        button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or
        button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or
        button7['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X' or
        button3['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X'):
        tkinter.messagebox.showinfo("tic tac toe", "X won!")
        sys.exit()

    elif(flag == 8):
        tkinter.messagebox.showinfo("tic tac toe", "it's a tie!")
        sys.exit()

    elif(button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
        button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O' or
        button7['text'] =='O' and button8['text'] == 'O' and button9['text'] == 'O' or
        button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O' or
        button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O' or
        button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
        button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O' or
        button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O' or
        button7['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O' or
        button3['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O'):
        tkinter.messagebox.showinfo("tic tac toe", "O won!")
        sys.exit()


button1 = tk.Button(text=" ", width=5, height=2, font='Times 20 bold', bg="gray", fg="white",
command = lambda: btnclicked(button1) )
button1.grid(row=0, column=0, sticky="nsew")
 
button2 = tk.Button(text=" ", width=5, height=2, font='Times 20 bold', bg="gray", fg="white",
command = lambda: btnclicked(button2))
button2.grid(row=0, column=1, sticky="nsew")
 
button3 = tk.Button(text=" ", width=5, height=2, font='Times 20 bold', bg="gray", fg="white",
command = lambda: btnclicked(button3))
button3.grid(row=0, column=2, sticky="nsew")
 
button4 = tk.Button(text=" ", width=5, height=2, font='Times 20 bold', bg="gray", fg="white",
command = lambda: btnclicked(button4))
button4.grid(row=1, column=0, sticky="nsew")
 
button5 = tk.Button(text=" ", width=5, height=2, font='Times 20 bold', bg="gray", fg="white",
command = lambda: btnclicked(button5))
button5.grid(row=1, column=1, sticky="nsew")
 
button6 = tk.Button(text=" ", width=5, height=2, font='Times 20 bold', bg="gray", fg="white",
command = lambda: btnclicked(button6))
button6.grid(row=1, column=2, sticky="nsew")
 
button7 = tk.Button(text=" ", width=5, height=2, font='Times 20 bold', bg="gray", fg="white",
command = lambda: btnclicked(button7))
button7.grid(row=2, column=0, sticky="nsew")
 
button8 = tk.Button(text=" ", width=5, height=2, font='Times 20 bold', bg="gray", fg="white",
command = lambda: btnclicked(button8))
button8.grid(row=2, column=1, sticky="nsew")
 
button9 = tk.Button(text=" ", width=5, height=2, font='Times 20 bold', bg="gray", fg="white",
command = lambda: btnclicked(button9))
button9.grid(row=2, column=2, sticky="nsew")
 
window.mainloop()
 

