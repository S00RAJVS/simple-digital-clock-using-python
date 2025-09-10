# 🕒 Digital Clock with Tkinter

A simple **Digital Clock GUI application** built using Python’s **Tkinter** library.  
It displays the **current time and date**, with an **automatic day/night theme** and customizable fonts.  

---

## ✨ Features
- 🕰 Real-time clock (updates every second).  
- 📅 Displays current date in a friendly format (`Monday, 10 September 2025`).  
- 🌗 Day/Night theme:  
  - Daytime (6 AM – 6 PM) → White background, black text.  
  - Nighttime (6 PM – 6 AM) → Black background, cyan time, white date.  
- 🎨 Customizable fonts for both **date** and **time**.  
- 🔲 Simple, lightweight, and runs on any system with Python.  

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/S00RAJVS/simple-digital-clock-using-python.git
cd simple-digital-clock-using-python
````

### 2. Run the Application

```bash
python digital clock.py
```

---

## 📸 Preview

**Day Mode (10:30 AM):**

```
Tuesday, 10 September 2025
10:30:45 AM
```

**Night Mode (10:30 PM):**

```
Tuesday, 10 September 2025
10:30:45 PM
```

---

## 🔧 Customization

* Change fonts in the code:

```python
date_label = Label(app, font=("Helvetica", 18))
clock_label = Label(app, font=("DS-Digital", 60, "bold"))
```

* To see all available fonts on your system:

```python
import tkinter as tk
from tkinter import font
root = tk.Tk()
print(font.families())
root.destroy()
```

---

## 📦 Requirements

* Python 3.x
* Tkinter (comes pre-installed with Python)

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).
You are free to use, modify, and distribute this project, but it comes **without warranty**.

---

## 👨‍💻 Author

Created by **Sooraj VS** ✨
If you like this project, ⭐ it on GitHub!
