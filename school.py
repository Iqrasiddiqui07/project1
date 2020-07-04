import csv

def write_into_csv(info_list):
    with open ('student_info.csv','a', newline='') as csv_file:
        writer= csv.writer(csv_file)

        if csv_file.tell() == 0:
            writer.writerow(["Name", "Age", "Contact no.", "Email ID"])
        
            writer.writerow(info_list)
            
if __name__=='__main__':
    condition = True
    student_num = 1
    while(condition):
        student_info = input("Enter studen information for student #{} in the following format (Name Age Contact_no. Email_ID): ".format(student_num))
        print ("Entered information: " + student_info)

        student_info_list = student_info.split(' ')
        
        print("\nTHE ENTERD INFORMATION IS -\nName: {}\nAge: {}\nContact_no.: {}\nEmail_ID: {}".format(student_info_list[0], student_info_list[1], student_info_list[2], student_info_list[3]))

        choice_check= input("Enter(y/n) if the entered ifo is correct: ")
        if choice_check=="y":
            write_into_csv(student_info_list)

            condition_check = input("Enter (y/n) if you want to add another student information: ")
            if condition_check == "y":
                condition= True 
                student_num= student_num +1
            elif condition_check == "n":
                condition = False
        elif choice_check == "n":
            print("\nPlease re-enter the values!")
