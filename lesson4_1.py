import pyinputplus as pyip

scores = pyip.inputInt("輸入分數(最高300):",min=0,max=300)
print(scores)
isYes = pyip.inputMenu(['y','n'],prompt="學生是否符合加分(選擇1或2)?\n",numbered=True)
if isYes == 'y':
    print("加分")
else:
    print("不加分")