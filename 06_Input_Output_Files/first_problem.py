with open(r"F:\Learn Python\Basics\06_Input_Output_Files\practice.txt","w") as f:
    f.write("I am man programmer\n")
    f.write("Hero\n")
    f.write("iron man\n")
    f.write("hulku re\n")
    f.close()

with open(r"F:\Learn Python\Basics\06_Input_Output_Files\practice.txt","r") as f:
    data = f.read()
    new_data = f.read()
    new_data = data.replace("man","woman")
    # print(new_data)

#now i want this replace should be in my real program as well
with open(r"F:\Learn Python\Basics\06_Input_Output_Files\practice.txt","w") as f:
    print(f.write(new_data))



