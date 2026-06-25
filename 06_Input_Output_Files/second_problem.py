#WAF to return read a line in text and return -1 if not exist (searching)
def check_for_line():
    word = "Hero"
    data = True
    line_no = 1
    with open(r"F:\Learn Python\Basics\06_Input_Output_Files\practice.txt","r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1
    return -1





