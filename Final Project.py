
import tkinter as tk

root = tk.Tk()

root.geometry("500x500")
root.title ("Workout GUI")
def four_day():
    current_frame = tk.Frame(main_frame)
    current_frame.pack()
    four_label = tk.Label(current_frame, text="All Workouts you will use a heavy enough weight where you will fail in the 6-8 rep range", font=('Arial', 10))
    four_label.pack(pady=20)

def home_page():
    home_frame = tk.Frame(main_frame)
    lb = tk.Label(home_frame, text='Welcome to your workout generator!', font=('Arial', 18))
    lb.pack()
    home_frame.pack(pady=20)

def fav_page():
    fav_frame = tk.Frame(main_frame)
    lb = tk.Label(fav_frame, text='These are your favorite workouts.', font=('Arial', 18))
    lb.pack()
    fav_frame.pack(pady=20)

def current_page():
    current_frame = tk.Frame(main_frame)
    lb = tk.Label(current_frame, text='This is your current workout plan.', font=('Arial', 18))
    lb.pack()
    current_frame.pack(pady=20)

def profile_page():
    profile_frame = tk.Frame(main_frame)
    lb = tk.Label(profile_frame, text='This is your profile', font=('Arial', 18))
    lb.pack()
    profile_frame.pack(pady=20)
    name_entry = tk.Entry(profile_frame, font=('Bold', 15))
    name_entry.place(pady=20)
    fourdays_btn = tk.Button(main_frame, text = 'Four', font=('Bold',15))
    fourdays_btn.place(x=169, y=250)
    sixdays_btn = tk.Button(main_frame, text = 'Six', font=('Bold',15))
    sixdays_btn.place(x=175, y=295)

def delete_pages():
    for frame in main_frame.winfo_children():
        frame.destroy()

def hide_indicators():
    home_indicate.config(bg='#c3c3c3')
    Fav_indicate.config(bg='#c3c3c3')
    Current_indicate.config(bg='#c3c3c3')
    Profile_indicate.config(bg='#c3c3c3')

def indicate(lb, page):
    hide_indicators()
    lb.config(bg='#158aff')
    delete_pages()
    page()

options_frame = tk.Frame(root, bg='#c3c3c3')

home_btn = tk.Button(options_frame, text='Home', font=('Bold', 15), fg='#158aff', bd=0, bg='#c3c3c3', command=lambda: indicate(home_indicate, home_page))
home_btn.place(x=10, y=50)
home_indicate = tk.Label (options_frame, text='', bg='#c3c3c3')
home_indicate.place(x=3, y=50, width=5, height=40)

Fav_btn = tk.Button(options_frame, text='Favorites', font=('Bold', 15), fg='#158aff', bd=0, bg='#c3c3c3', command=lambda: indicate(Fav_indicate, fav_page))
Fav_btn.place(x=10, y=150)
Fav_indicate = tk.Label (options_frame, text='', bg='#c3c3c3')
Fav_indicate.place(x=3, y=150, width=5, height=40)

Current_btn = tk.Button(options_frame, text='Workout', font=('Bold', 15), fg='#158aff', bd=0, bg='#c3c3c3', command=lambda: indicate(Current_indicate, current_page))
Current_btn.place(x=10, y=250)
Current_indicate = tk.Label (options_frame, text='', bg='#c3c3c3')
Current_indicate.place(x=3, y=250, width=5, height=40)

Profile_btn = tk.Button(options_frame, text='Profile', font=('Bold', 15), fg='#158aff', bd=0, bg='#c3c3c3', command=lambda:indicate(Profile_indicate, profile_page))
Profile_btn.place(x=10, y=350)
Profile_indicate = tk.Label (options_frame, text='', bg='#c3c3c3')
Profile_indicate.place(x=3, y=350, width=5, height=40)

options_frame.pack(side=tk.LEFT)
options_frame.pack_propagate(False)
options_frame.configure(width=100, height=500)

main_frame = tk.Frame(root, highlightbackground='black', highlightthickness=2)
main_frame.pack(side=tk.LEFT)
main_frame.pack_propagate(False)
main_frame.configure(height=500, width = 500)

root.mainloop()

    