import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
import tkinter as tk
from tkinter import filedialog,messagebox,font,ttk
from tkinter import *
from tkinter.ttk import *
from pathlib import Path 
import camera
import videotest


root = tk.Tk()
root.title('AI masiac')
root.geometry('800x600')  # 尺寸
root.resizable(width=0, height=0) # 決定能用滑鼠拖曳來改變多少的視窗大小
file_path=r''
save_path=r''

style = ttk.Style()
style.configure('TButton',font=('calibri',25,'bold'),borderwidth = '16')
style.map('TButton',foreground = [('active','!disabled','green')],
                    background = [('active','black')])


def main():
  
  def read():
    global file_path
    file_path = filedialog.askopenfilename()   # 選擇檔案後回傳檔案路徑與名稱
    read_file_name = file_path
    read_file_name_lst = read_file_name.split('/')
    label5['text'] = read_file_name_lst[-1]
    #print(read_file_name_lst[-1])
    #print(file_path)

  def save():
    global save_path
    save_path = filedialog.askdirectory()
    label6['text'] = save_path
    #print(save_path)
    
  def open():
    p = Path(save_path)
    p.resolve()
    print(p)
    os.system(f"explorer {p} ")
  
  
  
  file_name = ''
  name = tk.Entry(root, textvariable=file_name)
  name.grid(row=3,column=2)  # 放入 Entry

  label1 = tk.Label(root,font=('標楷體',20,),wraplength=800,text='這是一個很牛的程式，你可以上傳一個影片，他會自己幫你碼掉中指 \n點擊開啟檔案選擇你要處理的影片，點擊"儲存於"選取你要儲存的位置')  # 建立 label 標籤
  label1.grid(row=0,column=0,columnspan=3) 

  label2 = tk.Label(root,font=('標楷體',20,),wraplength=800,text='你也可以點擊"使用你的鏡頭"讓電腦碼掉你比的中指')  # 建立 label 標籤
  label2.grid(row=5,column=0,columnspan=3) 

  label3 = tk.Label(root,font=('標楷體',20,),wraplength=800,text='開啟檔案')  # 建立 label 標籤
  label3.grid(row=1,column=0,columnspan=1)

  label4 = tk.Label(root,font=('標楷體',20,),wraplength=800,text='儲存於')  # 建立 label 標籤
  label4.grid(row=2,column=0,columnspan=1)

  label5 = tk.Label(root,font=('標楷體',20,),wraplength=800,text='')  # 建立 label 標籤
  label5.grid(row=1,column=1,columnspan=3)

  label6 = tk.Label(root,font=('標楷體',20,),wraplength=800,text='')  # 建立 label 標籤
  label6.grid(row=2,column=1,columnspan=3)

  label7 = tk.Label(root,font=('標楷體',20,),wraplength=800,text='請輸入你要存檔的檔名')  # 建立 label 標籤
  label7.grid(row=3,column=0,columnspan=1)

  openfiles = ttk.Button(text='開啟檔案',command=read,style='TButton')  # Button 設定 command 參數，點擊按鈕時執行 show 函式
  openfiles.grid(row=4,column=0)

  savefiles = ttk.Button(text='儲存檔案於',command=save,style='TButton')  # Button 設定 command 參數，點擊按鈕時執行 show 函式
  savefiles.grid(row=4,column=1)
  
  openvideo = ttk.Button(root,text='打開檔案位置',command=open,style='TButton')  # Button 設定 command 參數，點擊按鈕時執行 show 函式
  openvideo.grid(row=5,column=2)


  magic = ttk.Button(text='輸出',command=lambda:videotest.main(file_path,save_path,name.get()),style='TButton')  # Button 設定 command 參數，點擊按鈕時執行 show 函式
  magic.grid(row=4,column=2)

  cam = ttk.Button(text='使用你的鏡頭',command=camera.main,style='TButton')  # Button 設定 command 參數，點擊按鈕時執行 show 函式
  cam.grid(row=7,column=1)


  root.mainloop()