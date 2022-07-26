print("*****_Email Validter Software_*****")
k=0
m=0
d=0
email=input("Enter email to check : ")
if len(email)>=6:
    if email.count("@")==1 :
        if email[0].isalpha():
            if (email[-4]==".") or (email[-3]=="."):
                if  email.count(" ")==0:
                    for i in email:
                        if i=="#" or i=="$" or i=="%" or i=="*" or i==")" or i==";"or i=="," or i==">" or i=="/" or i=="<"or i=="`" or i=="=" or i=="_" or i=="-" or i=="["or i=="," or i=="]" or i=="}":
                            k=1
                           
                    if k==1 :
                             print("Don't use key word like %,$,#,^,& etc..")
                    else:
                             print(f' "{email}" is valid email')                                         
                else:
                    print("Don't use space in character")  
            else:
                print('Use ".com" ".in" etc...')       
        else:
            print("Use first letter alphabet ")     
    else:
        print(' Use "@" only one time  ')    
else:
    print("wrong email use minimum eight character")    