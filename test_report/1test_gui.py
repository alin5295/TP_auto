import tkinter as tk

root = tk.Tk()  # Tk() 函数创建窗口是 Tkinter 中最基本的创建窗口的方法
root.title("My GUI Tool")  # 窗口的标题
root.geometry("500x200")  # 像素大小

# 添加标签
label = tk.Label(root, text="这是python的Gui窗口")
label.pack()

# 添加按钮
def print_input():
    input_text = text.get(1.0, tk.END).strip()  # 获取文本框的内容
    print("文本框被点击！！！")
    print(f"输入的文本为:{input_text}")

btn_2 = tk.Button(root, text="输入文本", command=lambda: print_input())
btn_2.pack()


# 添加文本框
text = tk.Text(root, height=6, font="Arial 12")
text.pack()

# 添加清除按钮
clear_btn = tk.Button(root, height=6, text="清除文本",command=lambda: text.delete(1.0, tk.END) or print("文本框已经被删除！！"))
clear_btn.pack()


root.mainloop()  # root.mainloop() 函数会循环执行窗口中的代码
