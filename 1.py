import time
import tkinter as tk
from tkinter import messagebox

def start_focus_timer(minutes):
    seconds = minutes * 60
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer_display.set(f"{mins:02d}:{secs:02d}")
        root.update()
        time.sleep(1)
        seconds -= 1

    messagebox.showinfo("提示", "专注时间结束！")

# 创建主窗口
root = tk.Tk()
root.title("专注时钟")

# 设置专注时间（以分钟为单位）
focus_time = 25

# 创建计时器显示
timer_display = tk.StringVar()
timer_label = tk.Label(root, textvariable=timer_display, font=("Helvetica", 48))
timer_label.pack(pady=20)

# 启动专注计时器按钮
start_button = tk.Button(root, text="开始专注", command=lambda: start_focus_timer(focus_time))
start_button.pack(pady=10)

# 运行主事件循环
root.mainloop()
