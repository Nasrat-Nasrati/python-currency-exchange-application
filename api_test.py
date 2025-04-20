import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

# بارگذاری داده‌های نرخ ارز
def load_currency_data():
    file_path = os.path.join("data", "currency.json")
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data
    else:
        return None

# تابع تبدیل ارز
def convert_currency():
    try:
        amount = float(amount_entry.get())
        source = source_currency.get()
        target = target_currency.get()

        if source == "" or target == "":
            raise ValueError("ارز مبدا و مقصد را انتخاب کنید.")

        rate = rates[target] / rates[source]
        result = amount * rate

        result_label.config(
            text=f"🔄 {amount} {source} ➡ {round(result, 2)} {target}"
        )
        error_label.config(text="")
    except ValueError as e:
        error_label.config(text=f"❌ خطا: {e}")

# تابع پاکسازی ورودی‌ها
def clear_fields():
    amount_entry.delete(0, tk.END)
    result_label.config(text="")
    error_label.config(text="")
    source_currency.set("")
    target_currency.set("")

# دریافت داده‌ها
data = load_currency_data()

if data:
    rates = data["conversion_rates"]
    currency_list = list(rates.keys())
else:
    messagebox.showerror("خطا", "❌ فایل نرخ ارز یافت نشد.")
    currency_list = []

# ایجاد پنجره اصلی
window = tk.Tk()
window.title("💱 Currency Converter - Nasrat")
window.geometry("300x350")
window.resizable(True, True)


# هدر خوش‌آمدگویی
header_label = tk.Label(
    window,
    text="🎉 Welcome to the Currency Exchange Application with Nasrat",
    font=("Helvetica", 12, "bold"),
    wraplength=380,
    justify="center",
    background="lightblue",
    

    
)
header_label.pack(pady=10)

# ارز مبدا
tk.Label(window, text="Source Currency:", font=("Helvetica", 10)).pack(pady=(10, 0))
source_currency = ttk.Combobox(window, values=currency_list, state="readonly")
source_currency.pack()

# ارز مقصد
tk.Label(window, text="Target Currency:", font=("Helvetica", 10)).pack(pady=(10, 0))
target_currency = ttk.Combobox(window, values=currency_list, state="readonly")
target_currency.pack()

# فیلد مقدار
tk.Label(window, text="Amount:", font=("Helvetica", 10)).pack(pady=(10, 0))
amount_entry = tk.Entry(window)
amount_entry.pack()

# دکمه‌ها
button_frame = tk.Frame(window)
button_frame.pack(pady=15)

convert_button = tk.Button(button_frame, text="Convert", command=convert_currency, bg="#4CAF50", fg="white", width=10)
convert_button.grid(row=0, column=0, padx=10)

cancel_button = tk.Button(button_frame, text="Cancel", command=clear_fields, bg="#f44336", fg="white", width=10)
cancel_button.grid(row=0, column=1, padx=10)

# نمایش نتیجه
result_label = tk.Label(window, text="", font=("Helvetica", 10, "bold"), fg="blue")
result_label.pack(pady=5)

# ناحیه خطا
error_label = tk.Label(window, text="", font=("Helvetica", 9), fg="red")
error_label.pack()

# اجرای برنامه
window.mainloop()
