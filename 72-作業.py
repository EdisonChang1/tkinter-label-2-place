"""
==== 1. =====
請參考 73-tkinter-label-2文字擺放place.py

使用tkinter 建立
一個視窗
上面顯示label
產品的資料
"""
print("1.")
import tkinter as tk                     # 在Python 3.x 匯入該tkinter 函式庫

win = tk.Tk()                            # 建立GUI 應用程式的主視窗
win.wm_title("Product Information")      # 設定主視窗標題
win.resizable(width=False, height=False) # 設定主視窗不可以被調整大小
win.minsize(width=640, height=480)       # 最小尺寸
win.maxsize(width=640, height=480)       # 最大尺寸

label1 =tk.Label(win,text="product name：yeezy boost")  # 建立文字
label1.place(x=20, y=60)                 # 指定元件位置 x=20, y=60 的位置

label2 =tk.Label(win,text="price:$10000""\ncolor:white")  # 建立文字
label2.place(x=20, y=80)                 # 指定元件位置 x=20, y=60 的位置

win.mainloop()                           # 最後步驟：程式做無限循環

"""
==== 2. ======

使用 class 建立
一個class
儲存

產品的相關資料
"""
print("2.")
class ProductInformation(object):         # 繼承Python 最上層的object 類別
    shoeName="yeezy boost"                     #鞋子名稱
    shoeColor="white"                          #鞋子顏色
    shoeSiza=38
    shoeHeight="2公分"
    shoeModel=1234
    shoePrice=100
    shoeOrgin="Japan"
    shoeWeight="300克"
    shoeReleasedate="2022/07/04"
    shoeInstock=300

    def __init__(self,Name,Color,Siza,Height,Model,Price,Orgin,Weight,Releasedate,Instock): # 類別初始化的函數 initialize 一開始要做的函數
        self.shoeName=Name
        self.shoeColor = Color
        self.shoeSiza = Siza
        self.shoeHeight = Height
        self.shoeModel = Model
        self.shoePrice = Price
        self.shoeOrgin = Orgin
        self.shoeWeight = Weight
        self.shoeReleasedate = Releasedate
        self.shoeInstock = Instock

    def info(self):                  #  Method 方法
        print("鞋子名稱:",self.shoeName, "\n顏色:",self.shoeColor, "\n尺寸:",self.shoeSiza, "\n高度:",self.shoeHeight,
              "\n型號:",self.shoeModel , "\n價格:", self.shoePrice, "\n產地:", self.shoeOrgin, "\n重量:",self.shoeWeight,
              "\n發售日:",self.shoeReleasedate, "\n庫存:",self.shoeInstock)

ProductInformation1=ProductInformation(Name="yeezy boost",Color="white",Siza=38,Height="2公分",Model=1234,Price=100,
                                       Orgin="Japan",Weight="300克",Releasedate="2022/07/04",Instock=300)
ProductInformation1.info()


"""==== 3. ======
請參考
65-class-properties.py

把第一題的Label 上的文字
改成讀取 class properties
"""
print("3.")
import tkinter as tk                     # 在Python 3.x 匯入該tkinter 函式庫

win = tk.Tk()                            # 建立GUI 應用程式的主視窗
win.wm_title("Product Information")      # 設定主視窗標題
win.resizable(width=False, height=False) # 設定主視窗不可以被調整大小
win.minsize(width=640, height=480)       # 最小尺寸
win.maxsize(width=640, height=480)       # 最大尺寸


label21=tk.Label(win,text="鞋子名稱:yeezy boost")      #建立文字
label21.place(x=50,y=100)                            #指定元件位置

label22=tk.Label(win,text="顏色:white")               #建立文字
label22.place(x=50,y=120)                            #指定元件位置

label23=tk.Label(win,text="尺寸:38")                  #建立文字
label23.place(x=50,y=140)                            #指定元件位置

label24=tk.Label(win,text="高度:2公分")                #建立文字
label24.place(x=50,y=160)                            #指定元件位置

label25=tk.Label(win,text="型號:1234")                #建立文字
label25.place(x=50,y=180)                            #指定元件位置

label26=tk.Label(win,text="價格:100")                 #建立文字
label26.place(x=50,y=200)                            #指定元件位置

label27=tk.Label(win,text="產地:Japan")               #建立文字
label27.place(x=50,y=220)                            #指定元件位置

label28=tk.Label(win,text="重量:300克")               #建立文字
label28.place(x=50,y=240)                            #指定元件位置

label29=tk.Label(win,text="發售日:2022/07/04")        #建立文字
label29.place(x=50,y=260)                            #指定元件位置

label30=tk.Label(win,text="庫存:300")                 #建立文字
label30.place(x=50,y=280)                            #指定元件位置

win.mainloop()       # 最後步驟：程式做無限循環




