f = open(r"F:\Learn Python\Basics\06_Input_Output_Files\demo.txt","a+")
f.write("omkar")
print(f.read()) #it did not print anything because "a+" places my pointed at the very end
f.close()