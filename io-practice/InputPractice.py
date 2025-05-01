import datetime

height = float(input("请输入你的身高(单位m)："))
weight = float(input("请输入你的体重(单位千克)："))

bmi = weight / (height * height)

if bmi < 18.5:
    result = '体重过轻'
elif bmi < 24.9:
    result = '体重正常'
elif bmi < 29.9:
    result = '体重过重'
else:
    result = '肥胖'
print("您的bmi是: ", bmi)
print(result)


