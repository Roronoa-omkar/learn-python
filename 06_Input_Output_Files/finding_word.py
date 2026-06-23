def check_for_word():
    word = "omkar"
    with open(r"F:\Learn Python\Basics\06_Input_Output_Files\practice.txt","r") as f:
        data = f.read()
        if(data.find(word) != -1):
            print("Found")
        else:
            print("Not Found")
check_for_word()