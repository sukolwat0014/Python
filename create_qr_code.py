import tkinter as tk
from tkinter import messagebox, filedialog, ttk
from PIL import Image, ImageTk
import qrcode

qr_img = None  # เก็บภาพล่าสุดเพื่อใช้ตอน save

def generate_qr():
    global qr_img
    data = entry.get()
    size = int(size_var.get())
    if not data:
        messagebox.showwarning("คำเตือน", "กรุณากรอกข้อความก่อนสร้าง QR Code")
        return
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white").resize((size, size))
    qr_img = img
    img_tk = ImageTk.PhotoImage(img)
    qr_label.config(image=img_tk)
    qr_label.image = img_tk

def save_qr():
    global qr_img
    if qr_img is None:
        messagebox.showwarning("ไม่มี QR", "กรุณาสร้าง QR Code ก่อนบันทึก")
        return
    file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                             filetypes=[("PNG files", "*.png")])
    if file_path:
        qr_img.save(file_path)
        messagebox.showinfo("บันทึกแล้ว", f"บันทึก QR Code ที่:\n{file_path}")

# สร้างหน้าต่างหลัก
app = tk.Tk()
app.title("QR Code Generator")
app.geometry("400x500")
app.config(bg="#f0f8ff")

# กล่องกรอกข้อความ
tk.Label(app, text="ใส่ข้อมูลเพื่อสร้าง QR code", font=("Helvetica", 12), bg="#f0f8ff").pack(pady=10)
entry = tk.Entry(app, width=40, font=("Helvetica", 12))
entry.pack()

# เลือกขนาดภาพจาก Combobox
tk.Label(app, text="เลือกขนาดรูป (พิกเซล)", font=("Helvetica", 12), bg="#f0f8ff").pack(pady=10)
size_var = tk.StringVar(value="200")
size_combo = ttk.Combobox(app, textvariable=size_var, values=["150", "200", "300", "400", "500"], state="readonly", font=("Helvetica", 12))
size_combo.pack()

# ปุ่มสร้าง QR
tk.Button(app, text="สร้าง QR Code", command=generate_qr,
          bg="#03315e", fg="white", font=("Helvetica", 12)).pack(pady=15)

# พื้นที่แสดงภาพ QR Code
qr_label = tk.Label(app, bg="#f0f8ff")
qr_label.pack(pady=10)

# ปุ่มบันทึก
tk.Button(app, text="บันทึกรูปภาพ", command=save_qr,
          bg="#52d671", fg="white", font=("Helvetica", 12)).pack(pady=10)

app.mainloop()
