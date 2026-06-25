# with open("F:\\Learn Python\\Basics\\06_Input_Output_Files\\demo.txt","r") as f:
#     data = f.read() 
#     print(data)
#     print(type(data))

# with open(r"F:\Learn Python\Basics\06_Input_Output_Files\demo.txt" ,"r") as f:
#           data = f.read()
#           print(data)

f = open(r"F:\Learn Python\Basics\06_Input_Output_Files\demo.txt","r")
# data = f.read(6)

data = f.readline()
print(data)
print(type(data))
f.close()
