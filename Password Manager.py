# 5. Password Manager: A program that securely stores and manages passwords using Python lists.
# Users can add, delete, and update passwords, and the program can encrypt the data for added security,
# Its good exercises to apply understanding Python list programs. 
# Users can add
# delete
# update passwords
import time
import os
#-----------------* loadind animation-------------------------------------------------#
def loading():
    list=[".",".|","../","...-","....\\","...../"]
    a,b=0,0
    while True:
        print("Loading:",list[a])
        time.sleep(0.2); os.system('cls')    
        if a == 5:
            a=0
            b+=1
        if b==2:
            print("Loading:","Done ✓ ")
            time.sleep(0.2); os.system('cls')       
            break
        a+=1
#==============={ User data Base }====================================================#
user_data=["8328414522","9442797657"]
pwd_data=["19052004@@","Pubg2004@@"]
#---------------*Check in Password Special Character include or not list--------------#
pwd_sp_sym=["","!","@","#","$","%","^","&","*"]
#-------------*In create : User May be Get Error or Program End *----------------------------------------------------------------------#
def error_1():
    print("-"*53);go_home=input("| Do you want Try Again    Enter :[ Y ] or [ N ]  :").capitalize();print("-"*53)
    if 'Y' == go_home:
        print("Please Wait Refreshing Current Page ....")
        time.sleep(2)
        loading()
        createaccount()
    elif 'N' == go_home:
        print("-"*45);print("|          Thank You Visit Again !          |");print("-"*45)
        time.sleep(2)
        print("Please Wait Redirect To Home Page....")
        time.sleep(2)
        loading()
        os.system('cls')
        home()
    else:
        print("-"*50);print("|   Invaild Input...   |");print("-"*50)
        time.sleep(1)
        print("Refreshing page.......")
        time.sleep(2)
        os.system('cls')
        error_1()
#----------------*In Account Deletation : User May be Get Error or Program End *--------------------#
def error_2():
    print("-"*53);go_home=input("| Do you want Try Again    Enter :[ Y ] or [ N ]  :").capitalize();print("-"*53)
    if 'Y' == go_home:
        print("Please Wait Refreshing Current Page ....")
        time.sleep(2)
        loading()
        deleteaccount()
    elif 'N' == go_home:
        print("-"*45);print("| Thank You Visit Again ! |");print("-"*45)
        time.sleep(2)
        print("Please Wait Redirect To Home Page....")
        time.sleep(2)
        loading()
        os.system('cls')
        home()

    else:
        print("Invaild Input...")
        time.sleep(1)
        print("Refreshing page.......")
        time.sleep(2)
        os.system('cls')
        error_2()
#----------------*In Update : User May be Get Error or Program End *---------------------------------#
def error_3():
    print("-"*53);go_home=input("| Do you want Try Again    Enter :[ Y ] or [ N ]  :").capitalize();print("-"*53)
    if 'Y' == go_home:
        print("Please Wait Refreshing Current Page ....")
        time.sleep(2)
        loading()
        updateaccount()
    elif 'N' == go_home:
        print("-"*45);print("|          Thank You Visit Again !          |");print("-"*45)
        time.sleep(2)
        print("Please Wait Redirect To Home Page....")
        time.sleep(2)
        loading()
        os.system('cls')
        home()

    else:
        print("Invaild Input...")
        time.sleep(1)
        print("Refreshing page.......")
        time.sleep(2)
        os.system('cls')
        error_3()
#---------------------* Select option In Program Startup  *-------------------------------------------#
def home():
    print("-"*45);print("|  >+< P-A-S-S-W-O-R-D  M-A-N-A-G-E-R  >+<  |");print("-"*45)
    print("-"*45)
    print("| Create New Account            Enter [ C ] |")
    print("-"*45)
    print("| Delete My Account Permanently Enter [ D ] |")
    print("-"*45)
    print("| Password updation             Enter [ P ] |")
    print("-"*45)
    print("| User Data Base Print          Enter [ U ] |")
    print("-"*45)
    option=input("| Select Your Option                   :").capitalize()
    print("-"*45)
    if 'C'==option:
        createaccount()
    elif 'D'==option:
        deleteaccount()
    elif 'P'==option:
        updateaccount()
    elif 'U'==option:
        def boy():
            print("-"*55);in_1=input("Enter  Your  Four  Digit  Admin  PIN      :");print("-"*55)
            if '0000'==in_1:
                print("-"*55);print("|      <+>      'USER DATA BASE-SYSTEM'        <+>    |");print("-"*55)
                print("-"*55);print("| User Mobile Number :>",user_data," |");print("-"*55)
                print("-"*55);print("| User Password      :>",pwd_data," |");print("-"*55)
                def second_call():
                    a = 9
                    while a >= 1:
                        print("\r           Show On Countdown ",(a)," Seconds", end="")
                        time.sleep(0.5)
                        a -= 1
                second_call()
                os.system('cls')
                def tryagain():            
                    print("-"*55);U_1=str(input("|   Do You Want Show Again Enter [ Y ] or [ N ] :")).capitalize();print("-"*55)
                    if 'Y'==U_1:
                        print("-"*55);print("|       <+>     'USER DATA BASE-SYSTEM'        <+>       |");print("-"*55)
                        print("-"*55);print("| User Mobile Number :>",user_data," |");print("-"*55)
                        print("-"*55);print("| User Password      :>",pwd_data," |");print("-"*55)
                        second_call();os.system('cls');tryagain()
                    if 'N'==U_1:
                        print("-"*55);print("|          Thank You Visit Again !          |");print("-"*55);os.system('cls');loading();home()
                    else:
                        print("-"*55);print("Error :  Invaild Input....   Try Again !              |");print("-"*55);tryagain()
                tryagain()
            else:
                print("-"*55);print("Error : Invaild Admin PIN....      Try Again !        |");print("-"*55);boy()
        boy()
    else:
        print("-"*45);print("|         Error:  Invalid Input             |");print("-"*45)
        time.sleep(0.5)
        print("    please wait redirect to home page.... ")
        time.sleep(1)
        loading()
        os.system('cls')
        home()
#==================================================={ Create New Account }=============================#
def createaccount():
    os.system('cls');print("-"*45);print("|            Create New Account             |");print("-"*45)

    try:
        user_2=int(input("| Enter The Mobile Number  :"));print("-"*45)
    except ValueError:
        print("-"*45);print("|    Error: Enter vaild mobile number !     |");print("-"*45)
        error_1()
        exit()
        
    user=str(user_2)

    if user not in user_data:
        pass
    else:
        print("-"*45);print("|  This Moble number is Alerady registered !|"); print("-"*45)
        time.sleep(1)
        error_1()
        exit()

    if len(user) == 10:
        pass
    else:
        print("-"*45);print("| Error : Please enter a valid 10-digit mobile number |");print("-"*45);error_1()
        time.sleep(3)
        exit()

    print("-"*45);pwd=str(input("| Create New Password      :"));print("-"*45)

    conforming=0
    add=0
    while add <= len(pwd)-1:
        if pwd[add].isupper():
            break
        if add == len(pwd)-1:
            pass
            if pwd[add].isupper():
                pass
            else:
                print("-"*45);print("| Error :* Must including uppercase         |");print("-"*45)
                conforming+=1
        add+=1
    add=0
    while add <= len(pwd)-1:
        if pwd[add].islower():
            break
        if add == len(pwd)-1:
            pass
            if pwd[add].islower():
                pass
            else:
                print("-"*45);print("| Error :* Must including lowercase letters |");print("-"*45)
                conforming+=1
        add+=1
        
    add=0
    while add <= len(pwd)-1:
        if pwd[add].isdigit():
            break
        if add == len(pwd)-1:
            pass
            if pwd[add].isdigit():
                pass
            else:
                print("-"*45);print("| Error :* Must including numbers           |");print("-"*45)
                conforming+=1
        add+=1

    if conforming == 0:
        pass
    else:
        time.sleep(1)
        error_1()
        exit()

    if len(pwd) >= 6 and len(pwd)<=12:
        i=1
        while i<=8:
            if pwd_sp_sym[i] in pwd:
                user_data.append(user)
                pwd_data.append(pwd)
                print("-"*45);print("|~ You are successfully created new account |");print("-"*45)
                break
            if i ==7:
                pass
                if pwd_sp_sym[i] in pwd:
                    pass
                else:
                    print("-"*45);print("| Error : Pwd Must Contain A Special Char   |");print("-"*45)
            i+=1
    else:
        print("-"*45);print("| Error : pwd minimum 6 char maximum 12 char|");print("-"*45)



    print("created password",user_data)
    print("password created",pwd_data)
    time.sleep(1);error_1()
    
#==================================================={ Account Deletation Permanently }==================#
def deleteaccount():
    os.system('cls')
    print("-"*55);print("|    <+>     Delete My Account Permanently     <+>    |");print("-"*55)

    try:
        print("-"*55);user_1=int(input("| Enter Registered Mobile Number  :"));print("-"*55)
    except ValueError:
        print("-"*55);print("| Enter vaild mobile number ! |");print("-"*55)
        time.sleep(2)
        error_2()
    user=str(user_1)
    if user not in user_data:
        print("-"*55);print("| Error : Mobile num is Not registered ! Cre New Acc   |");print("-"*55)
        error_2()


    if len(user)==10:    
        pass
    else:
        print("-"*55);print("| Error","Please enter a valid 10-digit mobile number |");print("-"*55)
        error_2()
    print("-"*55);pwd=str(input("| Enter your previous Password    :"));print("-"*55)

    if user not in user_data:
        pass
    else:    
        if len(pwd) >= 6 and len(pwd)<=12: 
            abi=0
            while abi <= len(user_data)-1:
                len_temp=len(user_data)
                if user_data[abi] == user and pwd_data[abi] == pwd:
                    user_data.remove(user)
                    pwd_data.remove(pwd)
                    print("-"*55);print("|        Account has been permanently deleted !       |");print("-"*55)
                    break
                if abi == len(pwd_data)-1:
                    pass
                    if user_data[abi] == user and pwd_data[abi] == pwd:
                        pass
                    else:            
                        print("-"*55);print("|Error : Num or Pwd isn't connected to an account. !  |");print("-"*55)    
                abi+=1
        else:
            print("-"*55);print("| Error","Pwd Min 6 Char  Max 12 Char ! |");print("-"*55)

    print("created password",user_data)
    print("password created",pwd_data)
    time.sleep(1);error_2()

#==================================================={ Updation Password }=============================#
def updateaccount():
    os.system('cls');print("-"*55);print("|       <+> Update Your  Account Password         <+> |");print("-"*55)
    try:
        print("-"*55);user_1=int(input("| Enter Registered Mobile Number  :"));print("-"*55)
    except ValueError:
        print("-"*55);print("| Enter Vaild Mobile Number |");print("-"*55)
    user=str(user_1)
    if user not in user_data:         # mobile number is already in list Go to else 
        print("-"*55);print("| Error : Please enter registered mobile number       |");print("-"*55)
 
    print("-"*55);pwd=str(input("| Enter Your Old Password         :"));print("-"*55)



    i_plus=1
    while i_plus <= len(pwd_data):
        if user not in user_data:         # mobile number is already in list Go to else 
            pass    
        else:
            if pwd_data[i_plus] == pwd and user_data[i_plus]==user:  # mobile number and pass word in same stright line then allow to update 
                print("-"*55);print("|       Successfully Connected To Your Account        |")
                print("|           Now You can Change New Password           |");print("-"*55)
                break
        if i_plus == len(user_data)-1:     # Before the end loop run the condition 
            pass
            if pwd_data[i_plus] == pwd and user_data[i_plus]==user:
                pass
            else:
                print("-"*55);print("| Error :  Your Old Password Wroung !                 |");print("-"*55);error_3()
                break
        i_plus+=1

    print("-"*55);pwd_new=str(input("| Enter Your New Password         :"));print("-"*55)
    print("-"*55);pwd_con=str(input("| Enter Your Confirm Password     :"));print("-"*55)

    conforming=0
    add=0
    while add <= len(pwd_new)-1:
        if pwd_new[add].isupper():
            break
        if add == len(pwd_new)-1:
            pass
            if pwd_new[add].isupper():
                pass
            else:
                print("-"*55);print("| Error :* Must including uppercase                   |");print("-"*55)
                conforming+=1
        add+=1
    add=0
    while add <= len(pwd_new)-1:
        if pwd_new[add].islower():
            break
        if add == len(pwd_new)-1:
            pass
            if pwd_new[add].islower():
                pass
            else:
                print("-"*55);print("| Error :* Must including lowercase letters           |");print("-"*55)
                conforming+=1
        add+=1

    add=0
    while add <= len(pwd_new)-1:
        if pwd_new[add].isdigit():
            break
        if add == len(pwd_new)-1:
            pass
            if pwd_new[add].isdigit():
                pass
            else:
                print("-"*55);print("| Error :* Must including numbers                     |");print("-"*55)
                conforming+=1
        add+=1

    sym_plus=1
    while sym_plus <= 8: # Checking Special Character is include or not 
        if pwd_sp_sym[sym_plus] in pwd_new and pwd_con:
            break
        if sym_plus == 8: 
            pass
            if pwd_sp_sym[sym_plus] in pwd_new and pwd_con:
                pass
            else:
                print("-"*55);print("|  Error : Password Must Contain A Special Character !|");print("-"*55)
                exit()    
        sym_plus+=1
    
    if conforming == 0:
        pass
    else:
        exit()

    i_plus=1
    while i_plus <= len(pwd_data):
        if user not in user_data:         # mobile number is already in list Go to else 
            pass    
        else:
            if pwd_data[i_plus] == pwd and user_data[i_plus]==user:  # mobile number and pass word in same stright line then allow to update 
                pwd_data[i_plus]=pwd_con
                print("-"*55);print("|         Your Password Changed Successfully          |");print("-"*55)
                break
        if i_plus == len(user_data)-1:     # Before the end loop run the condition 
            pass
            if pwd_data[i_plus] == pwd and user_data[i_plus]==user:
                pass
            else:
                print("-"*55);print("| Error :  Your Old Password Wroung !                 |");print("-"*55)
                break
        i_plus+=1

    print("created password",user_data)
    print("password created",pwd_data)
    time.sleep(1);error_3()







































# def updateaccount():
#     os.system('cls');print("-"*55);print("|       <+> Update Your  Account Password         <+> |");print("-"*55)
#     try:
#         print("-"*55);user_1=int(input("| Enter Registered Mobile Number  :"));print("-"*55)
#     except ValueError:
#         print("-"*55);print("| Enter Vaild Mobile Number |");print("-"*55)
#     user=str(user_1)
#     if user not in user_data:         # mobile number is already in list Go to else 
#         print("-"*55);print("| Error : Please enter registered mobile number       |");print("-"*55)
#         error_3()
#     print("-"*55);pwd=str(input("| Enter Your Old Password         :"));print("-"*55)
#     print("-"*55);pwd_new=str(input("| Enter Your New Password         :"));print("-"*55)
#     print("-"*55);pwd_con=str(input("| Enter Your Confirm Password     :"));print("-"*55)
    
#     if len(pwd) >= 6 and len(pwd)<=12 and len(pwd_new) >= 6 and len(pwd_new)<=12 and len(pwd_con) >= 6 and len(pwd_con)<=12: # condition is min 6 len and max 12 len then allow to next line 
#         pass
#     else:
#         print("-"*55);print("| Error : password minimum 6 char maximum 12 char !   |");print("-"*55);error_3()
        
#     if pwd_new==pwd_con:  # Checking new pass and con pass same then allow
#         pass
#     else:
#         print("-"*55);print("| Error : Confirm Password Not Same                   |");print("-"*55)

#     conforming=0
#     add=0
#     while add <= len(pwd_new)-1:
#         if pwd_new[add].isupper():
#             break
#         if add == len(pwd_new)-1:
#             pass
#             if pwd_new[add].isupper():
#                 pass
#             else:
#                 print("-"*55);print("| Error :* Must including uppercase                   |");print("-"*55)
#                 conforming+=1
#         add+=1
#     add=0
#     while add <= len(pwd_new)-1:
#         if pwd_new[add].islower():
#             break
#         if add == len(pwd_new)-1:
#             pass
#             if pwd_new[add].islower():
#                 pass
#             else:
#                 print("-"*55);print("| Error :* Must including lowercase letters           |");print("-"*55)
#                 conforming+=1
#         add+=1

#     add=0
#     while add <= len(pwd_new)-1:
#         if pwd_new[add].isdigit():
#             break
#         if add == len(pwd_new)-1:
#             pass
#             if pwd_new[add].isdigit():
#                 pass
#             else:
#                 print("-"*55);print("| Error :* Must including numbers                     |");print("-"*55)
#                 conforming+=1
#         add+=1

#     sym_plus=1
#     while sym_plus <= 8: # Checking Special Character is include or not 
#         if pwd_sp_sym[sym_plus] in pwd_new and pwd_con:
#             break
#         if sym_plus == 8: 
#             pass
#             if pwd_sp_sym[sym_plus] in pwd_new and pwd_con:
#                 pass
#             else:
#                 print("-"*55);print("|  Error : Password Must Contain A Special Character !|");print("-"*55)
#                 exit()    
#         sym_plus+=1
    
#     if conforming == 0:
#         pass
#     else:
#         error_3()
#         exit()

#     i_plus=1
#     while i_plus <= len(pwd_data):
#         if user not in user_data:         # mobile number is already in list Go to else 
#             pass    
#         else:
#             if pwd_data[i_plus] == pwd and user_data[i_plus]==user:  # mobile number and pass word in same stright line then allow to update 
#                 pwd_data[i_plus]=pwd_con
#                 print("-"*55);print("|         Your Password Changed Successfully          |");print("-"*55)
#                 break
#         if i_plus == len(user_data)-1:     # Before the end loop run the condition 
#             pass
#             if pwd_data[i_plus] == pwd and user_data[i_plus]==user:
#                 pass
#             else:
#                 print("-"*55);print("| Error :  Your Old Password Wroung !                 |");print("-"*55)
#                 break
#         i_plus+=1

#     print("created password",user_data)
#     print("password created",pwd_data)
#     time.sleep(1)
#     error_3()
home()


