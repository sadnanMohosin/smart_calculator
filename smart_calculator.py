from tkinter import *

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def divide(a,b):
    return a/b

def multiply(a,b):
    return a*b 

def mod(a,b):
    return a%b 

def lcm(a,b):
    L = a if a>b else b
    while L <= a*b:
        if L%a ==0 and L%b ==0:
            return L
        L +=1

def hcf(a,b):
    H = a if a<b else b
    while H >=1:
        if a%H == 0 and b%H == 0:
            return H
        H -=1
def extraxt_from_text(text):
    l = []
    for t in text.split(' '):
        try:
            l.append(float(t))
        except ValueError:
            pass
    return l

def calculate():
    text = textin.get()
    for word in text.split(' '):
        if word.upper() in operations.keys():
            try:
                l = extraxt_from_text(text)
                r = operations[word.upper()](l[0] , l[1])
                list.delete(0,END)
                list.insert(END,r)
            except:
                list.delete(0,END)
                list.insert(END,'something went wrong please enter again')
            finally:
                break
        elif word.upper() not in operations.keys():
            list.delete(0,END)
            list.insert(END,'something went wrong please enter again')



operations = {'ADD':add , 'ADDITION':add , 'SUM':add , 'PLUS':add ,
                'SUB':subtract , 'DIFFERENCE':subtract , 'MINUS':subtract , 'SUBTRACT':subtract,
                 'LCM':lcm , 'HCF':hcf , 'PRODUCT':multiply , 'MULTIPLICATION':multiply,
                 'MULTIPLY':multiply , 'DIVISION':divide , 'DIV':divide ,'DIVIDE':divide, 'MOD':mod ,
                  'REMANDER':mod , 'MODULUS':mod}







win = Tk()
win.geometry('500x300')
win.title('Smart calculator')
win.configure(bg='sky blue')

l1 = Label(win, text = 'I am a smart Calculator', width=20, padx=4)
l1.place(x = 150, y = 10)
l2 = Label(win, text = 'My name is stupid', padx=0)
l2.place(x = 180, y = 40)
l3 = Label(win, text = 'What can I help you', padx=3)
l3.place(x =176, y = 130)

textin = StringVar()
e1 = Entry(win,width=30,textvariable = textin)
e1.place(x=140,y=160)

b1  = Button(win, text='Just this',command = calculate)
b1.place(x= 210,y=200)

list = Listbox(win, width=20,height=3)
list.place(x=175,y=230)






win.mainloop()
