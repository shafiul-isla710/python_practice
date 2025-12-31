ans = 10 <= 5

print(ans)  # This will print: True


letter = ord('a') == ord('A')

print(letter)  # This will print: False



#python if else condition and ternary operator
age = 22

if age >= 18:
  message = "Eligiable"
else:
  message = "Not Eligiable"
  
print(message)


message1 = "Eligiable" if age >= 18 else "Not Eligiable"

print(message1)

#python has three types of logical operators these are and , or , not

loggedin = True
paid = False
is_pass = True


if (loggedin or paid) and is_pass:
  print('Pro User')
else:
  print('Normal User')