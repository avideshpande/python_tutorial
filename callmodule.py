"""#import mymodule
import mymodule as mx

#mymodule.greetings("Avinash")
mx.greetings("Avinash")

#print(mymodule.person1["age"])
print(mx.person1["age"])
"""
import platform

x = platform.system()
print(x)

x = dir(platform)
print(x)

from mymodule import person1

print(person1["age"])
#mymodule.greetings("Avinash")