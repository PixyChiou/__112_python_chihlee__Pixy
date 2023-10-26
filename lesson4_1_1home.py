import pyinputplus as pyip
scorces = pyip.inputInt('請輸入學生分數:',min=0,max=300)
print(f"學生分數為{scorces}")
isYes = pyip.inputMenu(['y','n'],prompt="學生符合加分條件嗎?(請輸入1或2)\n",numbered=True)
if isYes == 'y':
    print('加分')
else:
    print('不加')