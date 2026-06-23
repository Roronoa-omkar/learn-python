f = open(r"F:\Learn Python\Basics\06_Input_Output_Files\demo.txt","r+")
f.write("omkar")
Value = f.read()
print(Value)

#important note: r+ it does not truncate the file and the pointer is at the start and from there
#it starts reading the file