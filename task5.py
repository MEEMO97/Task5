your_name= input("Enter your name")
age = input("ُEnter your age")
new_age=str(int(age)-5)
street = input("Enter your street")
city = input("Enter your city")
country = input("Enter your country")
address = street+", "+city+", "+country
print("\"name: "+your_name+"\"\n"+"\"Age: "+age+"\"\n"+"\"Address: "+address+"\"")
print("\"Hello {"+your_name+"} Your age is "+new_age+" Years Old, Your Adress is "+address+".\"")
print(type(your_name),type(age))
print(type(street),type(city))
print(type(country))
print("\"Hello \'"+your_name+"\', How Are You? \\\"\"\"Your Age Is \""+new_age+"\"\"+ And Your Country Is: "+country)
print("\"Hello \'"+your_name+"\', How Are You? \\\n\"\"\"Your Age Is \""+new_age+"\"\"+ And\n Your Country Is: "+country)
name = 'Doaa Reem'
print("First Letter Is \""+name[0]+"\"")
print("Third Letter Is \""+name[2]+"\"")
print("Third Letter Is \""+name[len(name)-1]+"\"")
print(name[6:])
print(name[:4])
print(name[2:4].capitalize(),name[5:7])#required output "Aa Re"
print(name[9:4:-1])
print(name[:6:2],name[5::2])#required output "Da Re"
name2 = "$&$&Mohammed$&$&"
print(name2.strip("$&"))
msg = "I %7 Python And Although I %7 GSG with Zakaria"
print(msg.replace("%7","Love"))