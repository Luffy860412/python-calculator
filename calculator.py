# 定義一個函數來執行加法運算
def 加法(num1, num2):
    return num1 + num2

# 定義一個函數來執行減法運算
def 減法(num1, num2):
    return num1 - num2

# 定義一個函數來執行乘法運算
def 乘法(num1, num2):
    return num1 * num2

# 定義一個函數來執行除法運算
def 除法(num1, num2):
    if num2 == 0:
        return "錯誤！除數不能為零。" # 處理除以零的錯誤
    return num1 / num2

print("歡迎使用簡易計算機！")

while True: # 使用迴圈讓計算機能持續運作
    print("\n請選擇運算符號 (+, -, *, /), 或輸入 'exit' 離開:")
    運算符號 = input("輸入運算符號: ")

    if 運算符號 == 'exit':
        print("感謝使用，再見！")
        break # 離開迴圈，結束程式

    if 運算符號 not in ('+', '-', '*', '/'):
        print("輸入無效的運算符號，請重新輸入。")
        continue # 回到迴圈開始，要求重新輸入

    try: # 使用 try-except 區塊來處理可能的輸入錯誤
        num1 = float(input("請輸入第一個數字: ")) # 嘗試將輸入轉換為浮點數
        num2 = float(input("請輸入第二個數字: ")) # 嘗試將輸入轉換為浮點數
    except ValueError: # 如果使用者輸入的不是數字，會產生 ValueError 錯誤
        print("輸入錯誤，請輸入數字。")
        continue # 回到迴圈開始，要求重新輸入

    if 運算符號 == '+':
        結果 = 加法(num1, num2)
    elif 運算符號 == '-':
        結果 = 減法(num1, num2)
    elif 運算符號 == '*':
        結果 = 乘法(num1, num2)
    elif 運算符號 == '/':
        結果 = 除法(num1, num2)
    else:
        結果 = "未知的運算符號" # 理論上不會執行到這裡，因為前面已檢查過運算符號

    print("計算結果:", 結果)