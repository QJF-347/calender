import datetime
from tkinter import * 

font = ("Aerial", 23)
fonts = ("Aerial", 17)

days = ["MON", "TUE", "WED", "THU", "FRI", "SAT","SUN"]
months = ["JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULLY", "AUGUST", 
          "SEPTRMBER", "OCTOBER", "NOVEMBER", "DECEMBER"]
months_length = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
current_month = datetime.date.today().month
current_year = datetime.date.today().year
cream = "#fffdd0"
holidays = {(1, 1) : "NEW YEAR", (1, 5):"LABOUR DAY", (1, 6):"MADARAKA DAY", 
            (20, 10) : "MASHUJA DAY", (12, 12) : "JAMHURI DAY", 
            (31, 12) : "NEW YEAR's EVE"}

def display_plans():
    print("here")

def change_month(change):
    global current_month, current_year
    current_month += change
    if 0 < current_month < 13:
        fill_month(current_year, current_month ) 
    else:
        current_month = 1 if current_month == 13 else 12
        current_year += change
        fill_month(current_year , current_month )

def change_year(change):
    global current_year, current_month
    current_year += change
    fill_month(current_year, current_month)
    
    
def fill_month(year, month):
    global months_length, holidays
    for row in range(6):
        for column in range(7):
            date_button[row][column].config(text='', bg="white")
    months_length[1] = 29 if month == 2 and year % 4 == 0 else 28
    year_month_label.config(text=(months[month - 1 ], ",", year))
    date1 = datetime.date(year=year, month=month, day= 1).weekday()
    date = 1
    week = 0
    for days in range(months_length[month - 1]):   
        date_button[week][date1].config(text=date, bg="#00ff00" if date1 == 6 or date1 == 5 else "orange")
        if current_month == datetime.date.today().month and current_year == datetime.datetime.today().year and date == datetime.date.today().day:
            date_button[week][date1].config(bg="light blue")
        
        if (date, month) in holidays:
            date_button[week][date1].config(bg="yellow")
            
        date1 +=1
        date += 1
        if date1 == 7:
            week += 1
            date1 = 0


def goto():
    global current_year, current_month
    current_month, current_year = datetime.date.today().month, datetime.date.today().year
    fill_month(year=current_year, month=current_month)


window = Tk()
window.geometry("990x770")
window.title("CALENDAR")
frame = Frame(window, bg=cream, width=500, height=500)
frame.pack()

previous_month = [0, 0]
for button in range(2):
    previous_month[button] = Button(frame, text="<" if button == 0 else ">" , font=fonts, 
                                    command= lambda change=-1 + 2* button:change_month(change))
    previous_month[button].grid(row=1, column=button*4+1)
    
previous_year = [0, 0]
for button in range(2):
    previous_year[button] = Button(frame, text="<<" if button == 0 else ">>" , font=fonts, 
                                    command= lambda change= -1 + 2*button:change_year(change))
    previous_year[button].grid(row=1, column=button*6)

year_month_label = Label(frame, text=(months[current_month - 1], ",", current_year), font=(font), bg=cream)
year_month_label.grid(row=1, column=2, columnspan=3)

day_label = [0 for days in range(7)]
for rows in range(len(days)):
    day_label[rows] = Label(frame, text=days[rows], font=fonts, bg=cream)
    day_label[rows].grid(row=2, column=rows) 

label = [[0 for column in range(7)] for row in range(6)]
date_button = [[0 for column in range(7)] for row in range(6)]
frame_button = [[0 for column in range(7)] for row in range(6)]
for row in range(6):
    for column in range(7):
        frame_button[row][column] = Frame(frame)
        frame_button[row][column].grid(row=row + 3, column=column)
        date_button[row][column] = Button(frame_button[row][column], font=fonts, width=7, height=3, 
                                          bg="white", command=display_plans)
        date_button[row][column].grid(row=0, column=0)
fill_month(current_year, current_month)

week_label = Label(frame, font=font, bg=cream, 
                   text=("Week : " +str((datetime.date.today() - datetime.date(year=datetime.date.today().year, month=1, day=1)).days // 7)))
week_label.grid(row=1, column=7, columnspan=2)
goto_button = Button(frame, text="TODAY", font=font, command=goto)
goto_button.grid(row=2, column=7, columnspan=2)

window.mainloop() 