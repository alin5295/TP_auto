import tkinter as tk

root = tk.Tk()
root.title("My GUI Tool")
root.geometry("500x200")

# 添加标签
label = tk.Label(root, text="这是python的Gui窗口")
label.pack()

# 添加按钮
def print_input():
    input_text = text.get(1.0, tk.END).strip()  # 获取文本框的内容
    print("文本框已经被输入！！！")
    print(f"输入的内容为{input_text}")

btn_2 = tk.Button(root, text="input", command=print_input)
btn_2.pack()

# 添加文本框
text = tk.Text(root, height=6, font="Arial 12")
text.pack()

# 添加清除按钮
def clear_text():
    text.delete(1.0, tk.END)
    print("文本框已经被删除！！！")

clear_btn = tk.Button(root, height=6, text="Clear",command=clear_text)
clear_btn.pack()

root.mainloop()