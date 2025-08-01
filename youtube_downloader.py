import tkinter as tk
from tkinter import messagebox
import subprocess
import shutil

def dowload_video():
    url = entry.get()
    if not url:
        messagebox.showwarning("คำเตือน", "กรุณาใส่ลิงก์วิดีโอ Youtube")
        return
    if shutil.which("yt-dlp") is None:
        messagebox.showerror("ไม่พบ yt-dlp", "กรุณาติดตั้ง yt-dlp ก่อนใช้งาน")
        return
    try:
        subprocess.run(['yt-dlp', url], check=True)
        messagebox.showinfo("สำเร็จ", "ดาวน์โหลดวิดีโอสำเร็จแล้ว")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("ข้อผิดพลาด", f"เกิดข้อผิดพลาดในการดาวน์โหลด:\n{e}")

# UI
app = tk.Tk()
app.title("YouTube Video Downloader")
app.geometry("400x200")
app.config(bg="#f0f0f0")

tk.Label(app, text="ลิงก์วิดีโอ YouTube", font=("Helvetica", 12), bg="#f0f0f0").pack(pady=10)
entry = tk.Entry(app, width=45, font=("Helvetica", 12))
entry.pack(pady=5)

tk.Button(app, text="ดาวน์โหลดวิดีโอ", command=dowload_video,
          bg="#007bff", fg="white", font=("Helvetica", 12)).pack(pady=20)

app.mainloop()