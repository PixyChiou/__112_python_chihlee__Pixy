#輸入顧客購買金額,若金額在
#100000打8折,
#50000打85折,
#30000打9折,
#10000打95折,
#請輸入購買金額:130000
#實付金額是:104000.0元
x = int(input('輸入購買金'))
if x >= 100000:
    x *= 0.8
elif x >= 50000:
    x *= 0.85
elif x >= 30000:
    x *= 0.9
elif x >= 10000:
    x *= 0.95
else:
    x
print(x)