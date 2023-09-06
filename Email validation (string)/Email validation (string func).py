email=input("Please Enter Your Email : ")
k=0
j=0
d=0
#the very short for of any email is 6 characters that is g@g.in 
if len(email)>=6: #condition 1
    if email [0].isalpha(): #condition 2 # is.alpha is for alphabet (i am defining it for 0 index in email) 
        if ("@" in email) and (email.count("@")==1): #condition 3 
            if (email[-4]==".") ^ (email[-3]=="."): #condition 4 ^ it represents xor # if we use or operator then 1 of them is has to be true
                for i in email:#we use for because it is a string and we have to itterate it #we can also use if to see that is space is exested b/w them or not
                    if i==i.isspace(): #is.space just represents space and i am checking the space bw the characters
                        k=1
                    elif i.isalpha():
                        if i==i.upper():
                            j=1
                    elif i.isdigit():
                        print("Digit can be ok") # You can also remove this if not needed
                        continue
                    elif i=="_"or i=="."or i=="@":
                        print("You also have special characters: Nice") # You can also remove this if not needed 
                        continue
                    else:
                        d=1
                if k==1 or j==1 or d==1:
                        print ("Your Email Is Wrong [5] ")
                else:
                    print ("Your Email Seems To Be Correct: Awsome") #Correct 
            else:
                print("Your Email Is Wrong [4] ")
        else:
            print("Your Email Is wrong [3]")  #[count] it will show which mistake have you done 
    else:
        print("Your Email Is wrong [2]")
else:
    print("Your Email Is Wrong [1] ")

