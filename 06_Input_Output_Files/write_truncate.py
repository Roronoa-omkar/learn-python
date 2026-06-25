f = open(r"F:\Learn Python\Basics\06_Input_Output_Files\demo.txt","w+")
f.write("abc") #w+ truncated the demo.txt file and included abc into the file
print(f.read()) #here we can see nothing gets printed
f.close()



