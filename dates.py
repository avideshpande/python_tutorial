import datetime

x = datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A"))
print(x.strftime("%B"))

x = datetime.datetime(2020,5,17)

print(x)
print(x.strftime("%B"))