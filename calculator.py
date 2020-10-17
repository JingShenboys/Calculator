import re  # 处理字符串的模块，如查找特定字符，删除特定字符，字符串分割等
import tkinter  # Tkinter模块("Tk 接口")是Python的标准Tk GUI工具包的接口，位Python的内置模块，直接import tkinter即可使用。
import tkinter.messagebox  # 调用tkinter模块中的messagebox函数，这个是消息框，对话框的关键，会弹出一个小框
import pickle

# 按钮操作，点击按钮后需要做的处理
def buttonClik(btn):
    content = contentVar.get()  # 获取文本框中的内容
    # 如果已有内容是以小数点开头的，在前面加0
    if content.startswith('.'):
        content = '0' + content  # 字符串可以直接用+来增加字符
    # 根据不同的按钮作出不同的反应
    if btn in '0123456789':
        content += btn  # 0-9中哪个键按下了，就在content字符串中增添
    elif btn == '.':
        # re.split，支持正则及多个字符切割
        lastPart = re.split(r'\+|-|\*|/', content)[-1]  # 将content从+-*/这些字符的地方分割开来，[-1]表示获取最后一个字符
        if '.' in lastPart:
            tkinter.messagebox.showerror('错误', '重复出现的小数点')  # 出现对话框，并提示信息
            return
        else:
            content += btn
    elif btn == 'C':
        content = ''  # 清除文本框
    elif btn == '=':
        try:
            # 对输入的表达式求值
            content = str(eval(content))  # 调用函数eval，用字符串计算出结果
        except:
            tkinter.messagebox.showerror('错误', '表达式有误')
            return
    elif btn in operators:
        if content.endswith(operators):  # 如果content中最后出现的+-*/
            tkinter.messagebox.showerror('错误', '不允许存在连续运算符')
            return
        content += btn
    elif btn == 'Sqrt':
        n = content.split('.')  # 从.处分割存入n，n是一个列表
        if all(map(lambda x: x.isdigit(), n)):  # 如果列表中所有的都是数字，就是为了检查表达式是不是正确的
            content = eval(content) ** 0.5
        else:
            tkinter.messagebox.showerror('错误', '表达式错误')
            return
    contentVar.set(content)  # 将结果显示到文本框中


root = tkinter.Tk()  # 生成主窗口，用root表示，后面就在root操作
# 设置窗口大小和位置
root.geometry('300x270+400+100')  # 指定主框体大小
# 不允许改变窗口大小
root.resizable(False, False)  # 框体大小可调性，分别表示x,y方向的可变性；
# 设置窗口标题
root.title('计算器')

# 文本框和按钮都是tkinter中的组件
# Entry        　　 文本框（单行）；
# Button        　　按钮；
# 放置用来显示信息的文本框，设置为只读
# tkinter.StringVar    能自动刷新的字符串变量，可用set和get方法进行传值和取值
contentVar = tkinter.StringVar(root, '')
contentEntry = tkinter.Entry(root, textvariable=contentVar)  # 括号里面，可见第一个都是root,即表示都是以root为主界面的，将文本框中的内容存在contentVar中
contentEntry['state'] = 'readonly'  # 文本框只能读，不能写
contentEntry.place(x=10, y=10, width=280, height=20)  # 文本框在root主界面的xy坐标位置，以及文本框自生的宽和高
# x:        　　　 组件左上角的x坐标；
# y:        　　   组件右上角的y坐标；
# 放置清除按钮和等号按钮
btnClear = tkinter.Button(root, text='C', bg='red', command=lambda: buttonClik('C'))  # 在root主界面中放置按钮，按钮上显示C，红色，点击按钮后进入buttonClik回调函数做进一步的处理，注意传入了参数‘C’，这样就能分清是哪个按钮按下了
# 下面的内容和上面的模式都是一样的
btnClear.place(x=30, y=40, width=40, height=20)
btnCompute = tkinter.Button(root, text='=', bg='yellow', command=lambda: buttonClik('='))
btnCompute.place(x=100, y=40, width=40, height=20)


def caluli():
    def f1():
        caluli_need.set(height.get() * 30)
        caluli_eat.set(zaocan.get() + wucan.get() + wancan.get())  #######################
    # 定义长在窗口上的窗口
    window_sign_up = tkinter.Toplevel(root)
    window_sign_up.geometry('450x300')
    window_sign_up.title('卡路里计算器')

    height = tkinter.IntVar()  # 将输入的注册名赋值给变量
    height.set(0)  # 将最初显示定为'example@python.com'
    tkinter.Label(window_sign_up, text='体重(kg): ').place(x=25, y=10)  # 将`User name:`放置在坐标（10,10）。
    entry_height = tkinter.Entry(window_sign_up, textvariable=height)  # 创建一个注册名的`entry`，变量为`new_name`
    entry_height.place(x=130, y=10)  # `entry`放置在坐标（150,10）.
    
    
    def f3():
        window_sign_up2 = tkinter.Toplevel(window_sign_up)
        window_sign_up2.geometry('200x250')
        window_sign_up2.title('早餐')
        
        sb = tkinter.Scrollbar(window_sign_up2)
        sb.pack(side = tkinter.RIGHT, fill = tkinter.Y)
        lb = tkinter.Listbox(window_sign_up2, height = 8, yscrollcommand = sb.set)
        lb.pack(side = tkinter.LEFT, fill = tkinter.BOTH)
        
        for item in[mantou, mifan, shuijiao, dousha, xianrou]:
        
        mantou = tkinter.IntVar()  # 将输入的注册名赋值给变量
        mantou.set(0)  # 将最初显示定为'example@python.com'
        tkinter.Label(window_sign_up2, text='馒头(个): ').place(x=10, y=10)  # 将`User name:`放置在坐标（10,10）。
        entry_mantou = tkinter.Entry(window_sign_up2, textvariable=mantou, width = 10)  # 创建一个注册名的`entry`，变量为`new_name`
        entry_mantou.place(x=80, y=10)  # `entry`放置在坐标（150,10）
        
        mifan = tkinter.IntVar()  # 将输入的注册名赋值给变量
        mifan.set(0)  # 将最初显示定为'example@python.com'
        tkinter.Label(window_sign_up2, text='米饭(小碗): ').place(x=10, y=30)  # 将`User name:`放置在坐标（10,10）。
        entry_mifan = tkinter.Entry(window_sign_up2, textvariable=mifan, width = 10)  # 创建一个注册名的`entry`，变量为`new_name`
        entry_mifan.place(x=80, y=30)  # `entry`放置在坐标（150,10）
        
        shuijiao = tkinter.IntVar()  # 将输入的注册名赋值给变量
        shuijiao.set(0)  # 将最初显示定为'example@python.com'
        tkinter.Label(window_sign_up2, text='水饺(个)：').place(x=10, y=50)  # 将`User name:`放置在坐标（10,10）。
        entry_shuijiao = tkinter.Entry(window_sign_up2, textvariable=shuijiao, width = 10)  # 创建一个注册名的`entry`，变量为`new_name`
        entry_shuijiao.place(x=80, y=50)  # `entry`放置在坐标（150,10）
        
        dousha = tkinter.IntVar()  # 将输入的注册名赋值给变量
        dousha.set(0)  # 将最初显示定为'example@python.com'
        tkinter.Label(window_sign_up2, text='豆沙包(个)：').place(x=10, y=70)  # 将`User name:`放置在坐标（10,10）。
        entry_dousha = tkinter.Entry(window_sign_up2, textvariable=dousha, width = 10)  # 创建一个注册名的`entry`，变量为`new_name`
        entry_dousha.place(x=80, y=70)  # `entry`放置在坐标（150,10）
        
        xianrou = tkinter.IntVar()  # 将输入的注册名赋值给变量
        xianrou.set(0)  # 将最初显示定为'example@python.com'
        tkinter.Label(window_sign_up2, text='鲜肉包(个)：').place(x=10, y=90)  # 将`User name:`放置在坐标（10,10）。
        entry_xianrou = tkinter.Entry(window_sign_up2, textvariable=xianrou, width = 10)  # 创建一个注册名的`entry`，变量为`new_name`
        entry_xianrou.place(x=80, y=90)  # `entry`放置在坐标（150,10）
        
        def f4():
            zaocan.set(mantou.get()*280+ mifan.get()*140 + shuijiao.get()*42 + dousha.get()*215+xianrou.get()*225) ############要改的部分
        #zaocan.set(entry_mantou.get())
        btn_comfirm_sign_up2 = tkinter.Button(window_sign_up2, text='确定', command=f4)
        btn_comfirm_sign_up2.place(x=80, y=180)
    btnCompute2 = tkinter.Button(window_sign_up, text='▼', bg='white', command=f3)
    btnCompute2.place(x=270, y=50, width=20, height=20)

    def f5():
        window_sign_up3 = tkinter.Toplevel(window_sign_up)
        window_sign_up3.geometry('200x250')
        window_sign_up3.title('午餐')
        
        mantou = tkinter.IntVar()  # 将输入的注册名赋值给变量
        mantou.set(0)  # 将最初显示定为'example@python.com'
        tkinter.Label(window_sign_up3, text='馒头(个): ').place(x=10, y=10)  # 将`User name:`放置在坐标（10,10）。
        entry_mantou = tkinter.Entry(window_sign_up3, textvariable=mantou, width = 10)  # 创建一个注册名的`entry`，变量为`new_name`
        entry_mantou.place(x=80, y=10)  # `entry`放置在坐标（150,10）
        
        mifan = tkinter.IntVar()  # 将输入的注册名赋值给变量
        mifan.set(0)  # 将最初显示定为'example@python.com'
        tkinter.Label(window_sign_up3, text='米饭(小碗): ').place(x=10, y=30)  # 将`User name:`放置在坐标（10,10）。
        entry_mifan = tkinter.Entry(window_sign_up3, textvariable=mifan, width = 10)  # 创建一个注册名的`entry`，变量为`new_name`
        entry_mifan.place(x=80, y=30)  # `entry`放置在坐标（150,10）
        
        shuijiao = tkinter.IntVar()  # 将输入的注册名赋值给变量
        shuijiao.set(0)  # 将最初显示定为'example@python.com'
        tkinter.Label(window_sign_up3, text='水饺(个)：').place(x=10, y=50)  # 将`User name:`放置在坐标（10,10）。
        entry_shuijiao = tkinter.Entry(window_sign_up3, textvariable=shuijiao, width = 10)  # 创建一个注册名的`entry`，变量为`new_name`
        entry_shuijiao.place(x=80, y=50)  # `entry`放置在坐标（150,10）
        
        dousha = tkinter.IntVar()  # 将输入的注册名赋值给变量
        dousha.set(0)  # 将最初显示定为'example@python.com'
        tkinter.Label(window_sign_up3, text='豆沙包(个)：').place(x=10, y=70)  # 将`User name:`放置在坐标（10,10）。
        entry_dousha = tkinter.Entry(window_sign_up3, textvariable=dousha, width = 10)  # 创建一个注册名的`entry`，变量为`new_name`
        entry_dousha.place(x=80, y=70)  # `entry`放置在坐标（150,10）
        
        xianrou = tkinter.IntVar()  # 将输入的注册名赋值给变量
        xianrou.set(0)  # 将最初显示定为'example@python.com'
        tkinter.Label(window_sign_up3, text='鲜肉包(个)：').place(x=10, y=90)  # 将`User name:`放置在坐标（10,10）。
        entry_xianrou = tkinter.Entry(window_sign_up3, textvariable=xianrou, width = 10)  # 创建一个注册名的`entry`，变量为`new_name`
        entry_xianrou.place(x=80, y=90)  # `entry`放置在坐标（150,10）
        
        def f6():
            wucan.set(mantou.get()*280+ mifan.get()*140 + shuijiao.get()*42 + dousha.get()*215+xianrou.get()*225)
        btn_comfirm_sign_up3 = tkinter.Button(window_sign_up3, text='确定', command=f6)
        btn_comfirm_sign_up3.place(x=80, y=180)
    btnCompute3 = tkinter.Button(window_sign_up, text='▼', bg='white', command=f5)
    btnCompute3.place(x=270, y=90, width=20, height=20)   


    def f7():
        window_sign_up4 = tkinter.Toplevel(window_sign_up)
        window_sign_up4.geometry('200x250')
        window_sign_up4.title('晚餐')
        
        mantou = tkinter.IntVar()  # 将输入的注册名赋值给变量
        mantou.set(0)  # 将最初显示定为'example@python.com'
        tkinter.Label(window_sign_up4, text='馒头(个): ').place(x=10, y=10)  # 将`User name:`放置在坐标（10,10）。
        entry_mantou = tkinter.Entry(window_sign_up4, textvariable=mantou, width = 10)  # 创建一个注册名的`entry`，变量为`new_name`
        entry_mantou.place(x=80, y=10)  # `entry`放置在坐标（150,10）
        
        mifan = tkinter.IntVar()  # 将输入的注册名赋值给变量
        mifan.set(0)  # 将最初显示定为'example@python.com'
        tkinter.Label(window_sign_up4, text='米饭(小碗): ').place(x=10, y=30)  # 将`User name:`放置在坐标（10,10）。
        entry_mifan = tkinter.Entry(window_sign_up4, textvariable=mifan, width = 10)  # 创建一个注册名的`entry`，变量为`new_name`
        entry_mifan.place(x=80, y=30)  # `entry`放置在坐标（150,10）
        
        shuijiao = tkinter.IntVar()  # 将输入的注册名赋值给变量
        shuijiao.set(0)  # 将最初显示定为'example@python.com'
        tkinter.Label(window_sign_up4, text='水饺(个)：').place(x=10, y=50)  # 将`User name:`放置在坐标（10,10）。
        entry_shuijiao = tkinter.Entry(window_sign_up4, textvariable=shuijiao, width = 10)  # 创建一个注册名的`entry`，变量为`new_name`
        entry_shuijiao.place(x=80, y=50)  # `entry`放置在坐标（150,10）
        
        dousha = tkinter.IntVar()  # 将输入的注册名赋值给变量
        dousha.set(0)  # 将最初显示定为'example@python.com'
        tkinter.Label(window_sign_up4, text='豆沙包(个)：').place(x=10, y=70)  # 将`User name:`放置在坐标（10,10）。
        entry_dousha = tkinter.Entry(window_sign_up4, textvariable=dousha, width = 10)  # 创建一个注册名的`entry`，变量为`new_name`
        entry_dousha.place(x=80, y=70)  # `entry`放置在坐标（150,10）
        
        xianrou = tkinter.IntVar()  # 将输入的注册名赋值给变量
        xianrou.set(0)  # 将最初显示定为'example@python.com'
        tkinter.Label(window_sign_up4, text='鲜肉包(个)：').place(x=10, y=90)  # 将`User name:`放置在坐标（10,10）。
        entry_xianrou = tkinter.Entry(window_sign_up4, textvariable=xianrou, width = 10)  # 创建一个注册名的`entry`，变量为`new_name`
        entry_xianrou.place(x=80, y=90)  # `entry`放置在坐标（150,10）
        
        def f8():
            wancan.set(mantou.get()*280+ mifan.get()*140 + shuijiao.get()*42 + dousha.get()*215+xianrou.get()*225)
        btn_comfirm_sign_up4 = tkinter.Button(window_sign_up4, text='确定', command=f8)
        btn_comfirm_sign_up4.place(x=80, y=180)
    btnCompute4 = tkinter.Button(window_sign_up, text='▼', bg='white', command=f7)
    btnCompute4.place(x=270, y=130, width=20, height=20)
    
    
    zaocan = tkinter.IntVar()  # 将输入的注册名赋值给变量
    zaocan.set(0)  # 将最初显示定为'example@python.com'
    tkinter.Label(window_sign_up, text='早餐: ').place(x=30, y=50)  # 将`User name:`放置在坐标（10,10）。
    entry_zaocan = tkinter.Entry(window_sign_up, textvariable=zaocan) 
    entry_zaocan['state'] = 'readonly'
    entry_zaocan.place(x=130, y=50)  # `entry`放置在坐标（150,10）.
    #btnCompute3 = tkinter.Button(window_sign_up, text='▼', bg='white', command=f3)
    #btnCompute3.place(x=270, y=90, width=20, height=20)

    wucan = tkinter.IntVar()  # 将输入的注册名赋值给变量
    wucan.set(0)  # 将最初显示定为'example@python.com'
    tkinter.Label(window_sign_up, text='午餐: ').place(x=30, y=90)  # 将`User name:`放置在坐标（10,10）。
    entry_wucan = tkinter.Entry(window_sign_up, textvariable=wucan)  # 创建一个注册名的`entry`，变量为`new_name`
    entry_wucan['state'] = 'readonly'
    entry_wucan.place(x=130, y=90)  # `entry`放置在坐标（150,10）.

    wancan = tkinter.IntVar()  # 将输入的注册名赋值给变量
    wancan.set(0)  # 将最初显示定为'example@python.com'
    tkinter.Label(window_sign_up, text='晚餐: ').place(x=30, y=130)  # 将`User name:`放置在坐标（10,10）。
    entry_wancan = tkinter.Entry(window_sign_up, textvariable=wancan)  # 创建一个注册名的`entry`，变量为`new_name`
    entry_wancan['state'] = 'readonly'
    entry_wancan.place(x=130, y=130)  # `entry`放置在坐标（150,10）.

    caluli_need = tkinter.IntVar()
    caluli_need.set(height.get()*30)
    tkinter.Label(window_sign_up, text='今日所需卡路里: ').place(x=10, y=180)
    entry_caluli_need = tkinter.Entry(window_sign_up, textvariable=caluli_need)
    entry_caluli_need['state'] = 'readonly'
    entry_caluli_need.place(x=130, y=180)

    caluli_eat = tkinter.IntVar()
    caluli_eat.set(zaocan.get() + wucan.get() + wancan.get())
    tkinter.Label(window_sign_up, text='今日摄入卡路里: ').place(x=10, y=220)
    entry_caluli_eat = tkinter.Entry(window_sign_up, textvariable=caluli_eat)
    entry_caluli_eat['state'] = 'readonly'
    entry_caluli_eat.place(x=130, y=220)

    btn_comfirm_sign_up = tkinter.Button(window_sign_up, text='计算', command=f1)
    btn_comfirm_sign_up.place(x=180, y=260)


btnCompute = tkinter.Button(root, text='卡路里', bg='pink', command=caluli)
btnCompute.place(x=170, y=40, width=40, height=20)


def exercise():
    def f2():


        if ((height.get() > 17.9) & (height.get() < 23.9)):
            score1.set(100)
        elif ((height.get() < 17.9) | ((height.get() < 27.9) & (height.get() > 24))):
            score1.set(80)
        else:
            score1.set(60)
        tkinter.Label(window_sign_up, text=score1.get()).place(x=50, y=10)


        if(feihuoliang.get()>5040):
            score2.set(100)
        elif (feihuoliang.get()>4920):
            score2.set(95)
        elif (feihuoliang.get()>4800):
            score2.set(90)
        elif (feihuoliang.get()>4550):
            score2.set(85)
        elif (feihuoliang.get()>4300):
            score2.set(80)
        elif (feihuoliang.get()>4180):
            score2.set(78)
        elif (feihuoliang.get()>3700):
            score2.set(70)
        elif (feihuoliang.get()>3100):
            score2.set(60)
        elif (feihuoliang.get()>2620):
            score2.set(30)
        else:
            score2.set(0)
        tkinter.Label(window_sign_up, text=score2.get()).place(x=50, y=50)


        if (wushi.get() <6.9):
            score3.set(100)
        elif (wushi.get() <7.1):
            score3.set(80)
        else:
            score3.set(60)
        tkinter.Label(window_sign_up, text=score3.get()).place(x=50, y=90)


        if (tiqianqu.get() >21.3):
            score4.set(100)
        elif (tiqianqu.get() >3.7):
            score4.set(80)
        else:
            score4.set(60)
        tkinter.Label(window_sign_up, text=score4.get()).place(x=50, y=130)


        if (tiaoyuan.get() >263):
            score5.set(100)
        elif (tiaoyuan.get() >208):
            score5.set(80)
        else:
            score5.set(60)
        tkinter.Label(window_sign_up, text=score5.get()).place(x=50, y=170)


        if (yinti.get() >263):
            score6.set(100)
        elif (yinti.get() >208):
            score6.set(80)
        else:
            score6.set(60)
        tkinter.Label(window_sign_up, text=score6.get()).place(x=50, y=210)


        if (naili.get() <207):
            score7.set(100)
        elif (naili.get() <272):
            score7.set(80)
        else:
            score7.set(60)
        tkinter.Label(window_sign_up, text=score7.get()).place(x=50, y=250)
        zongfen.set(score1.get() * 0.15 + score2.get() * 0.15 + score3.get() * 0.2 + score4.get() * 0.1 + score5.get() * 0.1 + score6.get() * 0.1 + score7.get() * 0.2)

    # 定义长在窗口上的窗口
    window_sign_up = tkinter.Toplevel(root)
    window_sign_up.geometry('440x400')
    window_sign_up.title('体测成绩计算器')

    height = tkinter.DoubleVar()  # 将输入的注册名赋值给变量
    height.set(0)  # 将最初显示定为'example@python.com'
    tkinter.Label(window_sign_up, text='BMI ').place(x=10, y=10)  # 将`User name:`放置在坐标（10,10）。
    entry_height = tkinter.Entry(window_sign_up, textvariable=height)  # 创建一个注册名的`entry`，变量为`new_name`
    entry_height.place(x=130, y=10)  # `entry`放置在坐标（150,10）.
    score1=tkinter.DoubleVar()
    score1.set(1.0)




    feihuoliang = tkinter.IntVar()  # 将输入的注册名赋值给变量
    feihuoliang.set(0)  # 将最初显示定为'example@python.com'
    tkinter.Label(window_sign_up, text='肺活量 ').place(x=10, y=50)  # 将`User name:`放置在坐标（10,10）。
    entry_feihuoliang = tkinter.Entry(window_sign_up, textvariable=feihuoliang)  # 创建一个注册名的`entry`，变量为`new_name`
    entry_feihuoliang.place(x=130, y=50)  # `entry`放置在坐标（150,10）.
    score2=tkinter.DoubleVar()
    score2.set(0)


    wushi = tkinter.DoubleVar()  # 将输入的注册名赋值给变量
    wushi.set(0)  # 将最初显示定为'example@python.com'
    tkinter.Label(window_sign_up, text='50米: ').place(x=10, y=90)  # 将`User name:`放置在坐标（10,10）。
    entry_wushi = tkinter.Entry(window_sign_up, textvariable=wushi)  # 创建一个注册名的`entry`，变量为`new_name`
    entry_wushi.place(x=130, y=90)  # `entry`放置在坐标（150,10）.
    score3 = tkinter.DoubleVar()
    score3.set(0)

    tiqianqu = tkinter.DoubleVar()  # 将输入的注册名赋值给变量
    tiqianqu.set(0)  # 将最初显示定为'example@python.com'
    tkinter.Label(window_sign_up, text='体前屈: ').place(x=10, y=130)  # 将`User name:`放置在坐标（10,10）。
    entry_tiqianqu = tkinter.Entry(window_sign_up, textvariable=tiqianqu)  # 创建一个注册名的`entry`，变量为`new_name`
    entry_tiqianqu.place(x=130, y=130)  # `entry`放置在坐标（150,10）.
    score4 = tkinter.DoubleVar()
    score4.set(0)

    tiaoyuan = tkinter.DoubleVar()  # 将输入的注册名赋值给变量
    tiaoyuan.set(0)  # 将最初显示定为'example@python.com'
    tkinter.Label(window_sign_up, text='跳远: ').place(x=10, y=170)  # 将`User name:`放置在坐标（10,10）。
    entry_tiaoyuan = tkinter.Entry(window_sign_up, textvariable=tiaoyuan)  # 创建一个注册名的`entry`，变量为`new_name`
    entry_tiaoyuan.place(x=130, y=170)  # `entry`放置在坐标（150,10）.
    score5 = tkinter.DoubleVar()
    score5.set(0)

    yinti = tkinter.DoubleVar()  # 将输入的注册名赋值给变量
    yinti.set(0)  # 将最初显示定为'example@python.com'
    tkinter.Label(window_sign_up, text='引体: ').place(x=10, y=210)  # 将`User name:`放置在坐标（10,10）。
    entry_yinti = tkinter.Entry(window_sign_up, textvariable=yinti)  # 创建一个注册名的`entry`，变量为`new_name`
    entry_yinti.place(x=130, y=210)  # `entry`放置在坐标（150,10）.
    score6 = tkinter.DoubleVar()
    score6.set(0)


    naili = tkinter.DoubleVar()  # 将输入的注册名赋值给变量
    naili.set(0)  # 将最初显示定为'example@python.com'
    tkinter.Label(window_sign_up, text='耐力跑: ').place(x=10, y=250)  # 将`User name:`放置在坐标（10,10）。
    entry_naili = tkinter.Entry(window_sign_up, textvariable=naili)  # 创建一个注册名的`entry`，变量为`new_name`
    entry_naili.place(x=130, y=250)  # `entry`放置在坐标（150,10）.
    score7 = tkinter.DoubleVar()
    score7.set(0)


    zongfen = tkinter.DoubleVar()
    zongfen.set(0)
    tkinter.Label(window_sign_up, text='总分: ').place(x=10, y=290)
    entry_zongfen = tkinter.Entry(window_sign_up, textvariable=zongfen)
    entry_zongfen['state'] = 'readonly'
    entry_zongfen.place(x=130, y=290)

    #caluli_eat = tkinter.IntVar()
    #caluli_eat.set(feihuoliang.get() * 210+wushi.get()*280+tiqianqu.get()*42)
   # tkinter.Label(window_sign_up, text='摄入卡路里: ').place(x=10, y=220)
  #  entry_caluli_eat = tkinter.Entry(window_sign_up, textvariable=caluli_eat)
 #   entry_caluli_eat['state'] = 'readonly'
#    entry_caluli_eat.place(x=130, y=220)

    btn_comfirm_sign_up = tkinter.Button(window_sign_up, text='计算', command=f2)
    btn_comfirm_sign_up.place(x=180, y=330)


btnCompute2 = tkinter.Button(root, text='体测', bg='pink', command=exercise)
btnCompute2.place(x=240, y=40, width=40, height=20)



# 放置10个数字、小数点和计算平方根的按钮
digits = list('0123456789.') + ['Sqrt']  # 序列list是Python中最基本的数据结构。序列中的每个元素都分配一个数字 - 它的位置，或索引，第一个索引是0，第二个索引是1，依此类推。
index = 0
# 用循环的方式将上面数字、小数点、平方根这12个按钮分成四行三列进行放置
for row in range(4):
    for col in range(3):
        d = digits[index]  # 按索引从list中取值，和c语言中的数组类似
        index += 1  # 索引号递增
        btnDigit = tkinter.Button(root, text=d, command=lambda x=d: buttonClik(x))  # 和上面的是类似的
        btnDigit.place(x=20 + col * 70, y=80 + row * 50, width=50, height=20)  # 很显然，每次放一个按钮的位置是不一样的，但是它们之间的关系时确定的
# 放置运算符按钮
operators = ('+', '-', '*', '/', '**', '//')  # Python的元组与列表类似，不同之处在于元组的元素不能修改。
# 元组使用小括号，列表使用方括号。
# enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
for index, operator in enumerate(operators):
    btnOperator = tkinter.Button(root, text=operator, bg='orange',
                                 command=lambda x=operator: buttonClik(x))  # 创建的过程和上面类似
    btnOperator.place(x=230, y=80 + index * 30, width=50, height=20)

root.mainloop()  # 进入消息循环（必需组件）