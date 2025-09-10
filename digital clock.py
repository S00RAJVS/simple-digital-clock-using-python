from tkinter import Label, Tk  
import time  

app = Tk()  
app.title("🕒 Digital Clock")  
app.geometry("600x300")  
app.resizable(False, False)  

# Date label (centered at top)
date_label = Label(app, font=("Helvetica", 18))  
date_label.pack(pady=10)

# Time label (centered below date, digital font style)
clock_label = Label(app, font=("DS-Digital", 60, "bold"))  
clock_label.pack(pady=10)

def update_time():
    # Get current time & date
    current_time = time.strftime("%I:%M:%S %p")   # 12-hour format
    current_date = time.strftime("%A, %d %B %Y")  

    # Determine day/night mode
    hour = int(time.strftime("%H"))
    if 6 <= hour < 18:  # Day mode
        app.configure(bg="white")
        date_label.config(bg="white", fg="black")
        clock_label.config(bg="white", fg="black")
    else:  # Night mode
        app.configure(bg="black")
        date_label.config(bg="black", fg="white")
        clock_label.config(bg="black", fg="cyan")

    # Update text
    clock_label.config(text=current_time)
    date_label.config(text=current_date)

    # Refresh every second
    clock_label.after(1000, update_time)

update_time()  
app.mainloop()
