import customtkinter  # 導入 customtkinter 函式庫

class CalculatorApp(customtkinter.CTk):  # 建立一個繼承自 customtkinter.CTk 的類別，作為計算機主視窗
    def __init__(self):
        super().__init__()

        self.title("圖形介面計算機 V2.0")  # 設定視窗標題
        self.geometry("380x430")  # 設定視窗初始大小
        self.minsize(380, 430) # 設定視窗最小大小，避免縮放太小
        self.grid_rowconfigure(0, weight=1)  # 讓第 0 列 (顯示框) 可以垂直方向縮放
        self.grid_columnconfigure(0, weight=1) # 讓第 0 欄 (按鈕框架) 可以水平方向縮放

        self.expression = ""  # 儲存使用者輸入的算式字串

        # 顯示區域 (Entry Widget)
        self.display_entry = customtkinter.CTkEntry(self,
                                                 width=340,
                                                 height=80,
                                                 font=customtkinter.CTkFont(family="Segoe UI", size=47, weight="normal"), # 設定字型、大小、粗體
                                                 justify='right',   # 設定文字靠右對齊
                                                 border_color="#242424", # 設定邊框顏色 (深灰色)
                                                 fg_color="#1b1b1b",      # 設定背景色 (深灰色)
                                                 text_color="#ffffff"      # 設定文字顏色 (白色)
                                                 )
        self.display_entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="ew")  # 使用 grid 佈局管理器  將顯示框放在第 0 列第 0 欄，並佔滿 4 欄  padx 和 pady 是左右和上下間距，sticky="ew" 代表讓 Entry 在水平方向上填滿整個視窗
        self.display_entry.insert(0, "0") # 預設顯示 0
        self.expression = "0" # 算式預設為 "0"


        # 按鈕框架 (Frame)
        self.button_frame = customtkinter.CTkFrame(self)
        self.button_frame.grid(row=1, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")  # 使用 grid 佈局管理器  將按鈕框架放在第 1 列第 0 欄，並佔滿 4 欄  padx 和 pady 是左右和上下間距，sticky="nsew" 代表讓 Frame 在水平和垂直方向上填滿整個視窗
        self.button_frame.grid_rowconfigure(tuple(range(4)), weight=1)  # 讓按鈕框架內的 row 0~3 可以垂直方向縮放
        self.button_frame.grid_columnconfigure(tuple(range(4)), weight=1) # 讓按鈕框架內的 column 0~3 可以水平方向縮放

        # 按鈕設定
        button_texts = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+', 'C'  # C 代表清除 (Clear)
        ]
        button_row = 0
        button_col = 0

        for text in button_texts: # 逐一設定按鈕
            button = customtkinter.CTkButton(self.button_frame, # 將按鈕放在 button_frame 框架中
                                                     text=text,   # 設定按鈕文字
                                                     width=85,  # 設定按鈕寬度
                                                     height=50, # 設定按鈕高度
                                                     font=customtkinter.CTkFont(family="Segoe UI", size=20, weight="normal"), # 設定字型、大小、粗體
                                                     command=lambda t=text: self.button_click(t),
                                                     corner_radius=10,  # 設定圓角
                                                     border_width=0,      # 設定邊框寬度
                                                     fg_color="#363636", # 設定按鈕背景色 (深灰色)
                                                     hover_color="#3f3f3f", # 設定滑鼠 hover 時的背景色 (淺灰色)
                                                     text_color="white"   # 設定文字顏色 (白色)
                                                     )
            button.grid(row=button_row, column=button_col, padx=3, pady=3, sticky="nsew") # 增加 padx（左右間距） 和 pady（上下間距）  值，增加按鈕間距
            button_col += 1
            if button_col > 3:  # 每列最多 4 個按鈕就換列
                button_col = 0
                button_row += 1

        customtkinter.set_appearance_mode("Dark")  #  "System" (跟隨系統), "Dark", "Light"

    def button_click(self, text):  # 按鈕點擊事件處理函數
        if text == '=':
            try:
                result = eval(self.expression)  # 使用 eval 函數計算算式結果
                formatted_result = self.format_number(result) # 使用千分位格式化數字
                self.display_entry.delete(0, customtkinter.END)  # 清空顯示框
                self.display_entry.insert(0, formatted_result)  # 將計算結果顯示在顯示框
                self.expression = str(result)  # 將計算結果更新為算式，方便後續運算
            except Exception as e:  # 捕捉計算錯誤 (例如除以零、無效算式)
                self.display_entry.delete(0, customtkinter.END)
                self.display_entry.insert(0, "錯誤")  # 顯示錯誤訊息
                self.expression = "0"  # 清空算式, 並預設為 "0"
                print(f"計算錯誤: {e}") # 在終端機印出更詳細的錯誤訊息，方便debug
        elif text == 'C':  # 清除按鈕
            self.display_entry.delete(0, customtkinter.END)  # 清空顯示框
            self.display_entry.insert(0, "0") # 清除後預設顯示 0
            self.expression = "0"  # 清空算式, 並預設為 "0"
        elif text.isdigit() or text == '.': # 數字或小數點按鈕
            if self.expression == "0" and text != '.': # 如果目前顯示為 "0" 且輸入不是小數點，則直接取代 "0"
                self.expression = text
                self.display_entry.delete(0, customtkinter.END)
                self.display_entry.insert(customtkinter.END, text)
            else:
                self.expression += text  # 將按鈕文字加入算式字串
                self.display_entry.insert(customtkinter.END, text)  # 將按鈕文字顯示在顯示框
        else:  # 運算符號按鈕
            self.expression += text
            self.display_entry.insert(customtkinter.END, text)  # 將按鈕文字顯示在顯示框

    def format_number(self, number): # 千分位格式化數字
        return "{:,}".format(number)

if __name__ == "__main__":
    calculator = CalculatorApp()  # 建立計算機主視窗實例
    calculator.mainloop()  # 啟動 GUI 程式的主迴圈