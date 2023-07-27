import tkinter as tk
import sqlite3
from tkinter import messagebox
from tkinter import PhotoImage

def create_table():
    conn = sqlite3.connect('contacts.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT NOT NULL,
            Phone TEXT NOT NULL,
            Mail TEXT,
            CompanyName TEXT
        )
    ''')

    conn.commit()
    conn.close()

def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    mail = entry_mail.get()
    company_name = entry_company_name.get()

    if name and phone:  # name ve phone girdileri boş değilse veri eklemeyi gerçekleştir
        conn = sqlite3.connect('contact_list.db')
        cursor = conn.cursor()

        # Eğer contactmail veya company_name girdileri boş ise, bunları None olarak atayalım
        if not contactmail:
            contactmail = None
        if not company_name:
            company_name = None

        # SQL sorgusunu parametrelerle hazırlayalım
        sql_query = 'INSERT INTO contact_list (Name, Phone, contactmail, CompanyName) VALUES (?, ?, ?, ?)'
        values = (name, phone, mail, company_name)

        cursor.execute(sql_query, values)
        conn.commit()
        conn.close()
        show_contacts()
        messagebox.showinfo("Mesaj!", "kişi ekleme başarıyla tamamlandı")
    else:
        messagebox.showwarning("Uyarı!", "Kişi adı ve telefon numarası boş olamaz!!!")
        
def delete_contact():
    selected_id = entry_id.get()

    conn = sqlite3.connect('contacts.db')
    cursor = conn.cursor()

    cursor.execute('DELETE FROM contacts WHERE ID = ?', (selected_id,))
    conn.commit()
    conn.close()
    messagebox.showinfo("Mesaj!","Silindi")
    show_contacts()

def show_contacts():
    conn = sqlite3.connect('contacts.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM contacts')
    contacts = cursor.fetchall()

    contact_list.delete(0, tk.END)
    for contact in contacts:
        contact_list.insert(tk.END, f"ID: {contact[0]}, Name: {contact[1]}, Phone: {contact[2]}, Mail: {contact[3]}, CompanyName: {contact[4]}")

    conn.close()

def clear_entries():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_mail.delete(0, tk.END)
    entry_company_name.delete(0, tk.END)
    entry_id.delete(0, tk.END)
    
    
# Veritabanı tablosunu oluştur
create_table()

root = tk.Tk()
root.title('Kişi Rehberi')

label_name = tk.Label(root, text='İsim:')
label_name.pack(pady=5)
entry_name = tk.Entry(root)
entry_name.pack(pady=5)

label_phone = tk.Label(root, text='Telefon:')
label_phone.pack(pady=5)
entry_phone = tk.Entry(root)
entry_phone.pack(pady=5)

label_mail = tk.Label(root, text='E-posta:')
label_mail.pack(pady=5)
entry_mail = tk.Entry(root)
entry_mail.pack(pady=5)

label_company_name = tk.Label(root, text='Şirket Adı:')
label_company_name.pack(pady=5)
entry_company_name = tk.Entry(root)
entry_company_name.pack(pady=5)

label_id = tk.Label(root, text='Silinecek ID:')
label_id.pack(pady=5)
entry_id = tk.Entry(root)
entry_id.pack(pady=5)

button1_add = tk.Button(root, text='Kişi Ekle', command=add_contact)
button1_add.pack(pady=5)

button2_delete = tk.Button(root, text='Kişi Sil', command=delete_contact)
button2_delete.pack(pady=5)

button3_show = tk.Button(root, text='Kişileri Göster', command=show_contacts)
button3_show.pack(pady=5)

button4_clear = tk.Button(root, text='Girişleri Temizle', command=clear_entries)
button4_clear.pack(pady=5)    

contact_list = tk.Listbox(root, width=100)
contact_list.pack(pady=10)


show_contacts()

#root.configure(bg="cyan")

bg = PhotoImage(file='C:/Users/ShadowDefender/Desktop/sql/photos/your_image_2.png')
canvas1 = tk.Canvas(root,width = 1366, height = 768)
canvas1.create_image(0, 0, anchor='nw', image=bg)


root.geometry('1280x720+50+50')

root.resizable(False, False)


root.mainloop()