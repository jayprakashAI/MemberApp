import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class MemberApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Member App")
        self.geometry("1920x1200")
        self.minsize(700, 450)

        self.members = []

        self._build_ui()

    def _build_ui(self):
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        title = ttk.Label(self, text="Member Management", font=("Arial", 18, "bold"))
        title.grid(row=0, column=0, columnspan=2, padx=20, pady=(15, 10), sticky="w")

        form_frame = ttk.LabelFrame(self, text="Add Member", padding=15)
        form_frame.grid(row=1, column=0, padx=20, pady=(0, 10), sticky="nsew")

        fields = [
            ("Full Name", "name"),
            ("Email", "email"),
            ("Phone", "phone"),
            ("Gothra", "gothra"),
            ("Rashi", "rashi"),
            ("Nakshatra", "nakshtra"),
            ("Membership Type", "membership"),
        ]

        self.entries = {}

        for index, (label_text, key) in enumerate(fields):
            label = ttk.Label(form_frame, text=f"{label_text}:")
            label.grid(row=index, column=0, sticky="w", padx=(0, 10), pady=8)

            if key == "membership":
                value = ttk.Combobox(form_frame, state="readonly", width=30)
                value["values"] = ["Basic", "Premium", "VIP"]
                value.set("Basic")
                value.grid(row=index, column=1, sticky="ew")
            else:
                value = ttk.Entry(form_frame, width=35)
                value.grid(row=index, column=1, sticky="ew")

            self.entries[key] = value

        form_frame.columnconfigure(1, weight=1)

        button_row = ttk.Frame(form_frame)
        button_row.grid(row=4, column=0, columnspan=2, sticky="ew", pady=(15, 0))
        button_row.columnconfigure(0, weight=1)
        button_row.columnconfigure(1, weight=1)

        add_btn = ttk.Button(button_row, text="Add Member", command=self.add_member)
        add_btn.grid(row=0, column=0, sticky="ew", padx=(0, 5))

        clear_btn = ttk.Button(button_row, text="Clear", command=self.clear_form)
        clear_btn.grid(row=0, column=1, sticky="ew", padx=(5, 0))

        list_frame = ttk.LabelFrame(self, text="Members", padding=(10, 10))
        list_frame.grid(row=1, column=1, padx=(0, 20), pady=(0, 10), sticky="nsew")

        columns = ("name", "email", "phone", "membership")
        self.tree = ttk.Treeview(list_frame, columns=columns, show="headings")
        self.tree.heading("name", text="Name")
        self.tree.heading("email", text="Email")
        self.tree.heading("phone", text="Phone")
        self.tree.heading("membership", text="Membership")

        self.tree.column("name", width=160, anchor="center")
        self.tree.column("email", width=180, anchor="center")
        self.tree.column("phone", width=120, anchor="center")
        self.tree.column("membership", width=110, anchor="center")

        self.tree.pack(fill="both", expand=True)

        status = ttk.Label(self, text="Total members: 0", anchor="w")
        status.grid(row=2, column=0, columnspan=2, padx=20, pady=(0, 15), sticky="w")
        self.status_var = tk.StringVar(value="Total members: 0")
        status.configure(textvariable=self.status_var)

    def add_member(self):
        name = self.entries["name"].get().strip()
        email = self.entries["email"].get().strip()
        phone = self.entries["phone"].get().strip()
        gothra = self.entries["gothra"].get().strip()
        rashi = self.entries["rashi"].get().strip()
        nakshatra = self.entries["nakshatra"].get().strip()
        membership = self.entries["membership"].get().strip()

        if not name or not email or not phone:
            messagebox.showwarning("Missing data", "Please fill in all required fields.")
            return

        self.members.append({
            "name": name,
            "email": email,
            "phone": phone,
            "gothra":gothra,
            "rashi": rashi,
            "nakshatra": nakshatra,
            "membership": membership,
        })

        self.tree.insert("", "end", values=(name, email, phone, membership))
        self.status_var.set(f"Total members: {len(self.members)}")
        self.clear_form()

    def clear_form(self):
        for key in ["name", "email", "phone", "gothra", "rashi", "nakshatra"]:
            self.entries[key].delete(0, "end")
        self.entries["membership"].set("Basic")


if __name__ == "__main__":
    app = MemberApp()
    app.mainloop()
