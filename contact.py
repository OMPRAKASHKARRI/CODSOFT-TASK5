import tkinter as tk
from tkinter import messagebox

class ContactList:
    def __init__(self, root):
        self.root = root
        self.contacts = []

        # Create frames
        self.frame1 = tk.Frame(self.root, bg='#000000')
        self.frame1.pack()
        self.frame2 = tk.Frame(self.root, bg='#000000')
        self.frame2.pack()
        self.frame3 = tk.Frame(self.root, bg='#000000')
        self.frame3.pack()

        # Create labels and entries
        tk.Label(self.frame1, text="Name:", font=('Segoe UI', 12, 'bold'), fg='#ffffff', bg= '#000000').pack(side=tk.LEFT)
        self.name_entry = tk.Entry(self.frame1, width=30, font=('Segoe UI', 12), fg='#032B44')
        self.name_entry.pack(side=tk.LEFT)
        self.name_entry.bind('<Return>', lambda event: self.add_contact())

        tk.Label(self.frame2, text="Phone:", font=('Segoe UI', 12, 'bold'), fg='#ffffff', bg= '#000000').pack(side=tk.LEFT)
        self.phone_entry = tk.Entry(self.frame2, width=30, font=('Segoe UI', 12), fg='#032B44')
        self.phone_entry.bind('<KeyRelease>', self.validate_phone_key)
        self.phone_entry.pack(side=tk.LEFT)

        # Create buttons
        tk.Button(self.frame3, text="Add", command=self.add_contact, font=('Arial', 12, 'bold'), fg='#ffffff', bg='#008000').pack(side=tk.LEFT)
        tk.Button(self.frame3, text="Delete", command=self.delete_contact, font=('Arial', 12, 'bold'), fg='#ffffff', bg='#FF0000').pack(side=tk.LEFT)
        tk.Button(self.frame3, text="Display", command=self.display_contacts, font=('Arial', 12, 'bold'), fg='#ffffff', bg='#03055B').pack(side=tk.LEFT)

        # Create listbox
        self.listbox = tk.Listbox(self.root, width=40, font=('Helvetica', 15), fg='#00698f', bg='#ffffff')
        self.listbox.pack()

    def validate_phone_key(self, event):
        phone_number = self.phone_entry.get()
        phone_number = ''.join(filter(str.isdigit, phone_number))
        if len(phone_number) > 10:
            messagebox.showerror("Error", "Phone number cannot exceed 10 digits")
            phone_number = phone_number[:10]
        self.phone_entry.delete(0, tk.END)
        self.phone_entry.insert(0, phone_number)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        if name and phone:
            if len(phone) != 10:
                messagebox.showerror("Error", "Phone number must be exactly 10 digits")
                return
            self.contacts.append((name, phone))
            self.listbox.insert(tk.END, f"{name}: {phone}")
            self.name_entry.delete(0, tk.END)
            self.phone_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter both name and phone number")

    def delete_contact(self):
        try:
            index = self.listbox.curselection()[0]
            self.listbox.delete(index)
            self.contacts.pop(index)
        except:
            messagebox.showerror("Error", "Select a contact to delete")

    def display_contacts(self):
        messagebox.showinfo("Contacts", "\n".join([f"{name}: {phone}" for name, phone in self.contacts]))

root = tk.Tk()
root.title("Contact List")
root.configure(bg='#000000')
contact_list = ContactList(root)
root.mainloop()
