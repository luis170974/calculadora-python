from tkinter import *
from tkinter import ttk

# cores

# comando para rodar aplicação = py .\main.py

cor1 = "#3b3b3b" # cor preta
cor2 = "#feffff" # cor branca
cor3 = "#38576b" # cor azul
cor4 = "#ECEFF1" # cor cinza
cor5 = "#FFAB40" # cor laranja

window = Tk()
window.title("Calculadora")
window.geometry("235x310")
window.config(bg=cor1)

# criando frames

frame_screen = Frame(window, width=235, height=50, bg=cor3)
frame_screen.grid(row=0, column=0)

frame_body = Frame(window, width=235, height=268)
frame_body.grid(row=1, column=0)

# variavel todos os valores

all_values = ''

# criando funçao pegar valores

def get_values(event):

    global all_values

    all_values = all_values + str(event) # adicionando mais valores a string
    

    # passando valor para tela

    text_value.set(all_values)



# funçao calcular

def calculate():
    result = eval(all_values)

    text_value.set(result)


# funçao limpar tela

def clean_screen():
    global all_values

    all_values = ""

    text_value.set("")


# criando label

text_value = StringVar()

app_label = Label(frame_screen, textvariable=text_value, width=16, height=2, 
                  padx=7, relief=FLAT, anchor="e",
                  justify=RIGHT,
                  font=('Ivy 18'),
                  bg=cor3,
                  fg=cor2)

app_label.place(x=0, y=0)

# criando botões

# 1 linha

b_clear = Button(frame_body, command= clean_screen, text="C", width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_clear.place(x=0, y=0)

b_perc = Button(frame_body, command= lambda: get_values('%'), text="%", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_perc.place(x=118, y=0)

b_div = Button(frame_body, command= lambda: get_values('/'), text="/", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_div.place(x=177, y=0)

# 2 linha

b_seven = Button(frame_body, command= lambda: get_values('7'), text="7", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_seven.place(x=0, y=52)

b_eight = Button(frame_body, command= lambda: get_values('8'), text="8", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_eight.place(x=59, y=52)

b_nine = Button(frame_body, command= lambda: get_values('9'), text="9", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_nine.place(x=118, y=52)

b_mult = Button(frame_body, command= lambda: get_values('*'), text="*", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_mult.place(x=177, y=52)

# 3 linha

b_four = Button(frame_body, command= lambda: get_values('4'), text="4", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_four.place(x=0, y=104)

b_five = Button(frame_body, command= lambda: get_values('5'), text="5", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_five.place(x=59, y=104)

b_six = Button(frame_body, command= lambda: get_values('6'), text="6", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_six.place(x=118, y=104)

b_sub = Button(frame_body, command= lambda: get_values('-'), text="-", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_sub.place(x=177, y=104)

# 4 linha


b_one = Button(frame_body, command= lambda: get_values('1'), text="1", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_one.place(x=0, y=156)

b_two = Button(frame_body, command= lambda: get_values('2'), text="2", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_two.place(x=59, y=156)

b_three = Button(frame_body, command= lambda: get_values('3'), text="3", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_three.place(x=118, y=156)

b_adic = Button(frame_body, command= lambda: get_values('+'), text="+", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_adic.place(x=177, y=156)

# 5 linha


b_zero = Button(frame_body, command= lambda: get_values('0'), text="0", width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_zero.place(x=0, y=208)

b_virg = Button(frame_body, command= lambda: get_values(','), text=",", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_virg.place(x=118, y=208)

b_igual = Button(frame_body, command= calculate, text="=", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_igual.place(x=177, y=208)




window.mainloop()