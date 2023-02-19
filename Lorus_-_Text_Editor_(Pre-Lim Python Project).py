import tkinter as tk
from tkinter import filedialog
import re
import time


#THIS CLASS IS WHERE TH MAIN FUNCTINALITY OF THE CODE WILL OCCUR
#SEARCH, COUNT, REPLACE WORDS OR SENTENCES
class Lorus:
    def __init__(self,user_email,user_password,user_file_path,user_file_content):
        self.user_email = user_email
        self.user_password = user_password
        self.user_file_path = user_file_path
        self.user_file_content = user_file_content
    
    #MAIN  METHOD OF THE FUNCTIONALITY
    def app_lorus(self):
        
        #FUNCTION FOR WORD REPLACEMENT
        def word_replace():
            
            #ASSIGNED THE OBJECTS TO SIMILAR VALUES
            unpacked_file_content_1 = self.user_file_content[0]
            unpacked_file_path_1 = self.user_file_path[0]
            
            #ASKED REPLACEMENT WORD
            word_as_replace = input("Type the word you want as your replacement: ")
            
            #WILL LOOP LINE OF CODES IN VARIOUS CONDITIONS
            while True:
                time.sleep(2)
                print ("Searching your desired word...")
                time.sleep(2)
                print ("Please wait...")
                
                #WILL FIND THE WORD SELECTED FOR REPLACEMENT USING REGEX
                #SEE LINE 236
                count_word = re.findall(which_word, *self.user_file_content, re.IGNORECASE)
                time.sleep(4)
                
                #CONDITIONS
                if count_word:
                    print ("Word found!")
                    
                    #WHERE THE WORD REPLACEMENT OCCURS
                    word_new_file_content = unpacked_file_content_1.replace(which_word,word_as_replace)
                    word_new_replaced_content = open(unpacked_file_path_1,'w')
                    time.sleep(2)
                    print ("Word successfully replaced!")
                    time.sleep(3)
                    print ()
                    print ()
                    word_new_replaced_content.write(word_new_file_content)
                    break
                else:
                    
                    #IF WORDS ARE NOT FOUND IN THE TEXT FILE
                    print ("Word not found.")
                    time.sleep(2)
                    print ("Please try again.")
        
        #FUNCTION FOR COUNTING SELECTED WORD
        def word_count():
            time.sleep(2)
            while True:
                time.sleep(2)
                
                #WILL FIND THE SELECTED WORD FOR COUNTING USING REGEX
                #SEE LINE 236
                count_word = re.findall(which_word, *self.user_file_content, re.IGNORECASE)
                time.sleep(3)
                print ("Searching your desired word...")
                time.sleep(2)
                print ("Please wait...")
                time.sleep(4)
                    
                #CONDITIONS
                if count_word:
                    print ("Hunting your word...")
                    time.sleep(2)
                    print ("WORD FOUND!")
                    time.sleep(3)
                    print ()
                    print ("----------------")
                    print ()
                    
                    #WILL PRINT THE NUMBER OF WORD OCCURRENCE
                    print ("\tWord count:", len(count_word))
                    print ()
                    print ("----------------")
                    break
        
                else:
                    #IF WORD NOT FOUND
                    print ("Word not found.")
                    time.sleep(2)
                    print ("Please try again.")
                    break
        
        #FUNCTION FOR SENTENCE REPLACEMENT
        def sentence_replace():
            
            #ASSIGNED THE OBJECTS TO SIMILAR VALUES
            unpacked_file_content_2 = self.user_file_content[0]
            unpacked_file_path_2 = self.user_file_path[0]
            print ("What sentence do you want to search for replacement? ")
            time.sleep(2)
            
            #ASK FOR SENTENCE FOR REPLACEMENT
            which_sentence_1 = input("Type your sentence:  ")
            time.sleep(2)
            
            #AS FOR A SENTENCE AS A REPLACEMENT
            sentence_as_replace = input("Type the word you want as your replacement: ")
            
            #WILL LOOP LINE OF CODES IN VARIOUS CONDITIONS 
            while True:
                time.sleep(2)
                print ("Searching your desired sentence...")
                time.sleep(2)
                print ("Please wait...")
                time.sleep(4)
                
                #CONDITIONS
                if which_sentence_1 in unpacked_file_content_2:
                    print ("Sentence found!")
                    
                    #WHERE THE WORD REPLACEMENT OCCURS
                    sentence_new_file_content = unpacked_file_content_2.replace(which_sentence_1,sentence_as_replace)
                    sentence_new_replaced_content = open(unpacked_file_path_2,'w')
                    time.sleep(2)
                    print ("Sentence successfully replaced!")
                    time.sleep(3)
                    print ()
                    print ()
                    sentence_new_replaced_content.write(sentence_new_file_content)
                    sentence_new_replaced_content.close()

                else:
                    #IF WORD NOT FOUND
                    print ("Word not found.")
                    time.sleep(2)
                    print ("Please try again.")
                    break
                    
        #FUNCTION FOR COUNTING SELECTED SENTENCE
        def sentence_count():
            print ("What sentence's first word do you want to search for editing? ")
            time.sleep(2)
            
            #ASK FOR THE FIRST WORD OF YOUR SENTENCE
            which_sentence_2 = input("Type your sentence's first word':  ")
            time.sleep(2)
            
            #WILL LOOP LINE OF CODES IN VARIOUS CONDITIONS 
            while True:
                time.sleep(2)
                
                #WILL FIND THE SELECTED SENTENCE FOR COUNTING USING REGEX
                #SEE LINE __
                count_sentence = re.findall(which_sentence_2 + ".+", *self.user_file_content, re.IGNORECASE)
                time.sleep(2)
                print ("Searching your desired sentence...")
                time.sleep(2)
                print ("Please wait...")
                time.sleep(4)
                
                #CONDITIONS
                if count_sentence:
                    print ("Compiling your sentences...")
                    place = 1
                    time.sleep(2)
                    print ("Sentences compiled!")
                    time.sleep(2)
                    print ("Preparing your sentences...")
                    time.sleep(3)
                    
                    #WILL PRINT THE NUMBER OF SENTENCE OCCURRENCE
                    print ("----------------")
                    print ("\tSentence count:", len(count_sentence))
                    time.sleep(3)
                    print ()
                    print ()
                    print ("\t\tAll sentences:")
                    time.sleep(1)
                    print ()
                    
                    #WILL PRINT ALL THE SENTENCE HAVING THE FIRST WORD OF THE SENTENCES
                    for each in count_sentence:
                        time.sleep(2)
                        print ("\t", str(place) + ".", each)
                        time.sleep(1)
                        print ()
                        place += 1
                    break
                else:
                    
                    #IF SENTENCE NOT FOUND
                    print ("Sentence not found.")
        
        
                    
                    
        print ("File selected! What do you want to edit in your file?")
        time.sleep(2)
        print ("Type \"SENTENCE\" if you prefer to edit sentence.")
        time.sleep(3)
        print ("Type \"WORD\" if you prefer to edit word.")
        time.sleep(3)
        
        #WILL LOOP LINE OF CODES IN VARIOUS CONDITIONS
        while True:
            
            #ASK FOR INPUT WHETHER SENTENCE OR WORD TO BE EDITED IN THE TEXT FILE
            search = input("Enter which you would edit: ")
            
            #SEARCHFOR WORD/SENTENCE USING REGEX
            regwords = re.search("(Words|Word)",search,re.IGNORECASE)
            regsentences = re.search("(Sentence|Sentences)",search,re.IGNORECASE)
            
            #CONDITIONS
            
            #IF WORD IS SELECTED
            if regwords:
                time.sleep(2)
                
                #ASSIGN VALUE TO TRUE
                A = True
                
                #WILL LOOP LINE OF CODES IN VARIOUS CONDITIONS
                while A:
                    print ("What word do you want to edit? ")
                    time.sleep(2)
                    
                    #ASK FOR WORD FROM A TEXT FILE TO BE EDITED
                    which_word = input("type your word: ")
                    time.sleep(2)
                    
                    #ASSIGNED VALUE TO TRUE
                    B = True
                    
                    #WILL LOOP LINE OF CODES IN VARIOUS CONDITIONS
                    while B:
                        print ("What do you want to do with your word?")
                        time.sleep(2)
                        print ("If you wish to replace your word in the file, type \"REPLACE\".")
                        time.sleep(4)
                        print ("If you wish to count your word in the file, type \"COUNT\"")
                        time.sleep(3)
                        
                        #ASK INPUT WHETHER TO REPLACE OR COUNT THE WORD
                        word_action = input("Type your action: ")
                        
                        replace_word_act = re.search("REPLACE",word_action,re.IGNORECASE)
                        count_word_act = re.search("COUNT",word_action,re.IGNORECASE)
                        
                        #CONDIIONS
                        if count_word_act:
                            
                            #CALL WORD COUNT FUNCTION
                            word_count()
                            
                            #VALUES ASSIGNED FROM TRUE TO FALSE
                            A = False
                            B = False
                                    
                        elif replace_word_act:
                            time.sleep(2)
                            
                            #CALL WORD REPLACEMENT FUNCTION
                            word_replace()
                            
                            #VALUES ASSIGNED FROM TRUE TO FALSE
                            A = False
                            B = False
                            
                        else:
                            #IF ACTION IS INVALID
                            time.sleep(2)
                            print ("Invalid action.")
                            time.sleep(2)
                            print ("Please try again.")
            
            #IF SENTENCE IS SELECTED
            elif regsentences:
                time.sleep(2)
                
                #ASSIGNED VALUE TO TRUE
                C = True
                
                #WILL LOOP LINE OF CODES IN VARIOUS CONDITIONS
                while C:
                    print ("What do you want to do with your sentence?")
                    time.sleep(2)
                    print ("If you wish to replace your sentence in the file, type \"REPLACE\".")
                    time.sleep(4)
                    print ("If you wish to count your sentence in the file, type \"COUNT\"")
                    time.sleep(3)
                    
                    ##ASK INPUT WHETHER TO REPLACE OR COUNT THE SENTENCE
                    sentence_action = input("Type your action: ")
                    replace_sentence_act = re.search("REPLACE",sentence_action,re.IGNORECASE)
                    count_sentence_act = re.search("COUNT",sentence_action,re.IGNORECASE)
                    
                    #CONDITIONS
                    if count_sentence_act:
                        time.sleep(2)
                        
                        #CALL SENTENCE COUNT FUNCTION
                        sentence_count()
                        
                        #VALUE ASSIGNED FROM TRUE TO FALSE
                        C = False
                    elif replace_sentence_act:
                        time.sleep(2)
                        
                        #CALL SENTENCE REPLACEMENT FUNCTION
                        sentence_replace()
                        
                        #VALUE ASSIGNED FROM TRUE TO FALSE
                        C = False
                        
                    else:
                        time.sleep(2)
                        
                        #IF ACTION IS INVALID
                        print ("Invalid action.")
                        time.sleep(2)
                        print ("Please try again.")
            
            #IF ACTION IS INVALID
            else:
                time.sleep(2)
                print ("Invalid action.")
                time.sleep(2)
                print ("Please try again.")
                
            #CODES AFTER THE SEARCH, COUNT, REPLACE FUNCTIONS
            time.sleep(3)
            print ()
            print ("Search finished!")
            time.sleep(2)
            print ("What do you want to do next?")
            time.sleep(3)
            print ("Type \"SEARCH\" if you desire to search more.")
            time.sleep(3)
            print ("Type \"SIGNOUT\" if you are finished searching and wished to sign out")
            time.sleep(3)
            
            #ASK INPUT OF WHETHER TO SEARCH MORE OR TO SIGN OUT INSTEAD
            final_act = input("Type your action: ")
            time.sleep(2)
            final_act_search = re.search("SEARCH", final_act,re.IGNORECASE)
            final_act_signout = re.search("SIGNOUT", final_act,re.IGNORECASE)
            
            #CONDITIONS
            
            #WILL LOOP TO CONTINUE TO SEARCH FOR MORE
            if final_act_search:
                print ("Continuing search...")
            elif final_act_signout:
                
                #WILL END THE LOOP CONTINUE
                print ("Signing out...")
                time.sleep(2)
                
                #CALL SIGNING OUT FUNCTION
                sign_out()
                break
    
    #METHOD OF REPLACING FILE CONTENT FOR EXISTING FILE WHEN SIGNING IN IS SELECTED
    def file_content_replacement(self):
        
        #OPEN FILE PATH
        file_rep = open(*self.user_file_path,'r')
        file_content_rep_read = file_rep.read()
        
        #ASSIGNED VARIABLE EMPTY LIST
        file_list = []
        
        #WILL APPEND THE FILE READABLE FILE CONTENT TO THE LIST ABOVE
        file_list.append(file_content_rep_read)
        
        #THE LIST IS ASSIGNED
        #AND WILL BE THE NEW VALUE THE OBJECT USER FILE CONTENT
        self.user_file_content = file_list
        
        
    #THIS METHOD WILL CONNECT YOUR ACCOUNT INFO ALONG WITH YOUR SELECTED FILE
    #WILL APPEND IN A DESIGNATED ACCOUNT-TO-FILE DISTRBIUTION TEXT FILE AS A TEXT
    def account_to_file_distribution(self):
        
        #CLASS OBJECTS ASSIGNED TO 3 VARIABLES
        acc_email,acc_pass,acc_file_path = *self.user_email,*self.user_password,*self.user_file_path
        
        #READS THE DESIGNATED ACCOUNT-TO-FILE DISTRBIUTION TEXT FILE
        account_to_file = open("account_to_file_distribution.txt", 'a')
        
        #WILL WRITE/APPEND/STORE THE VALUES INTO THE DESIGNATED ACCOUNT-TO-FILE DISTRBIUTION TEXT FILE
        account_to_file.write(acc_email+":"+acc_pass+"="+acc_file_path+"\n")
                
            
#ASSIGNED VALUES
user_email = []
user_password = []
user_file_path = []
user_file_content = []


#FUNCTION FOR SELECTION OF NEW TEXT FILE
def lorus_file_selection():
    print ("To continue with the app,")
    time.sleep(1)
    print ("select the desired text file you want to edit:")
    time.sleep(2)
    
    #OPENS THE FILE EXPLORER USING TKINTER
    root = tk.Tk()
    root.withdraw()
    lorus_file_path = filedialog.askopenfilename()
    with open(lorus_file_path, 'r') as l_file:
        
        #ALLOWS THE FILE TO BE READ
        lorus_file_content = l_file.read()
    
    #SELECTED FILE PATH WILL BE APPENDED TO ASSIGNED FILE PATH LIST
    #SEE LINE 270
    user_file_path.append(lorus_file_path)
    
    #READABLE TEXT FILE WILL BE APPENDED TO ASSIGNED FILE CONTENT LIST
    #SEE LINE 271
    user_file_content.append(lorus_file_content)



#FUNCTION FOR SEARCHING AN EXISTING TEXT FILE
def lorus_existing_file_selection():
    existing_file = open("account_to_file_distribution.txt", 'r')
    existing_file_1 = existing_file.read().split()
    exist_email,exist_pass = *user_email,*user_password
    exist_acc_file = exist_email+':'+exist_pass
    
    for accounts in existing_file_1:
        removed_last = accounts.split("=")
        if removed_last[0] == exist_acc_file:
            user_file_path.append(removed_last[-1])
            
        

#FUNCTION FOR SIGNING UP
def sign_up():
        #READ FILE ACCOUNT EMAIL AND PASSWORD DISTRIBUTION
        #PREPARATION FOR STORING THE ACCOUNT
        file =  open("account_distribution.txt", 'a')
        
        #ASSIGNED EMPTY VALUES FOR EMAIL AND PASSWORD
        email_confirmed_1 = ""
        pass_confirmed_1 = ""
        
        #WILL LOOP LINE OF CODES IN VARIOUS CONDITIONS
        while True:
            
            #WILL LOOP LINE OF CODES IN VARIOUS CONDITIONS
            while True:
                
                #ASK INPUT OF YOUR EMAIL ADDRESS
                email_1 = input("Enter your email address: ")
                confirm_email_1 = re.search(".+@gmail|hotmail|outlook|yahoo|\.com", email_1)
                
                #CONDITIONS
                if confirm_email_1:
                    time.sleep(2)
                    time.sleep(3)
                    
                    #INPUTTED EMAIL WILL BE ASSIGNED TO THE ASSIGNED EMPTY CONFIRMED EMAIL VALUE
                    #SEE LINE 457
                    email_confirmed_1 += email_1
                    
                    #VALUE OF THE CONFIRMED EMAIL WILL BE APPENDED TO THE ASSIGNED VALUES
                    user_email.append(email_confirmed_1)
                    break
                
                else:
                    #IF EMAIL IS INVALID
                    time.sleep(2)
                    print ("Invalid email address!")
                    time.sleep(2)
                    print ("Please try again.")
                    time.sleep(2)
                    
            #WILL LOOP LINE OF CODES IN VARIOUS CONDITIONS
            while True:
                pattern = r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$"
                
                #ASK INPUT FOR PASSWORD MAKING
                pass_1 = input("Please choose a strong password: ")
                confirm_pass_1 = re.search(pattern,pass_1)
                
                #CONDITIONS
                if confirm_pass_1:
                    time.sleep(2)
                    
                    #ASK INPUT FOR RE-ENTERING PASSWORD
                    reenter_pass_1 = input("Re-enter your password: ")
                    if reenter_pass_1 == pass_1:
                        
                        #INPUTTED PASSWORD WILL BE ASSIGNED TO THE ASSIGNED EMPTY CONFIRMED PASSWORD VALUE
                        #SEE LINE 458
                        pass_confirmed_1 += pass_1
                        
                        #VALUE OF THE CONFIRMED PASSWORD WILL BE APPENDED TO THE ASSIGNED VALUES
                        user_password.append(pass_confirmed_1)
                        break
                    else:
                        #IF PASSWORD DO NOT MATCH
                        time.sleep(2)
                        print ("Password do not match.")
                        time.sleep(2)
                        print ("Please try again.")
                else:
                    #IF PASSWORD CONDITIONS DID NOT MEET
                    time.sleep(2)
                    print("Password must be at least 8 characters long")
                    time.sleep(2)
                    print ('Password should also contain both letters and numbers.')
                    time.sleep(2)
            
            #READS THE FILE
            file_r =  open("account_distribution.txt", 'r')
            file_read = file_r.read()
            
            #CONDITIONS
            #IF EMAIL ALREADY REGISTERED
            if email_confirmed_1+':'+pass_confirmed_1+'\n' in file_read:
                time.sleep(2)
                print ("email address already registered.")
                time.sleep(2)
                print ("Please use other email instead.")
                
            else:
                #IF EMAIL NOT YET REGISTERED
                
                #EMAIL AND PASSWORD APPENDED TO THE DESIGNATED ACCOUNT DISTRIBUTION FILE
                file.write(email_confirmed_1+':'+pass_confirmed_1+'\n')
                time.sleep(2)
                print ()
                time.sleep(2)
                print ()
                time.sleep(2)
                
                #PRINTS THE SUMMARY OF INFORMATION
                print ("Account information:")
                time.sleep(2)
                print ("\t"+"Email Address: "+email_confirmed_1)
                time.sleep(2)
                print ("\t"+"Password: "+len(pass_confirmed_1)*"*")      
                file.close()
                break
            
         
            
#FUNCTION FOR SIGNING IN
def sign_in():
    
    #READS THE FILE
    file = open("account_distribution.txt", 'r')
    contents = file.read()
    
    #ASSIGNED EMPTY VALUES FOR EMAIL AND PASSWORD
    email_confirmed_2 = ""
    pass_confirmed_2 = ""
    
    #WILL LOOP LINE OF CODES IN VARIOUS CONDITIONS
    while True:
        time.sleep(2)
        
        #WILL LOOP LINE OF CODES IN VARIOUS CONDITIONS
        while True:
            email_2 = input("Enter your email address: ")
            
            #ASK INPUT OF YOUR EMAIL ADDRESS
            confirm_email_2 = re.search(".+@gmail|hotmail|outlook|yahoo|\.com", email_2)
            
            #CONDITIONS
            if confirm_email_2:
                
                #INPUTTED EMAIL WILL BE ASSIGNED TO THE ASSIGNED EMPTY CONFIRMED EMAIL VALUE
                #SEE LINE 570
                email_confirmed_2 = email_2
                
                #VALUE OF THE CONFIRMED EMAIL WILL BE APPENDED TO THE ASSIGNED VALUES
                user_email.append(email_confirmed_2)
                break
            else:
                
                #IF EMAIL IS INVALID
                time.sleep(2)
                print ("Invalid email address!")
                time.sleep(3)
                print ("Please try again.")
                
        time.sleep(3)
        pass_2 = input("Please enter your password: ")
        
        #INPUTTED PASSWORD WILL BE ASSIGNED TO THE ASSIGNED EMPTY CONFIRMED PASSWROD VALUE
        #SEE LINE 571
        pass_confirmed_2 = pass_2
        
        #VALUE OF THE CONFIRMED PASSWORD WILL BE APPENDED TO THE ASSIGNED VALUES
        user_password.append(pass_confirmed_2)
        
        d = email_confirmed_2+':'+pass_confirmed_2
        
        #CONDITIONS
        
        #IF EMAIL AND PASSWORD ALREADY IN THE DESIGNATED ACCOUNT DISTRIBUTION FILE
        if d in contents:
            time.sleep(3)
            pass
            break
        else:
            #IF EMAIL AND PASSWORD IS NOT YET IN THE DESIGNATED ACCOUNT DISTRIBUTION FILE
            time.sleep(3)
            print ("Account not yet registered.")
            time.sleep(2)
            print ("Please sign up first and try again.")



#FUNCTION FOR SIGNING OUT
def sign_out():
    
    #READS TEXT FILE
    file = open("account_distribution.txt", 'r')
    contents = file.read()
    
    #ASSIGNED EMPTY VALUES FOR EMAIL AND PASSWORD
    email_confirmed_3 = ""
    pass_confirmed_3 = ""
    
    #WILL LOOP LINE OF CODES IN VARIOUS CONDITIONS
    while True:
        time.sleep(2)
        
        #ASKS FOR RE-ENTERING EMAIL AND PSSWORD FOR SIGNING OUT
        print ("Re-enter your credentials to proceed signing out.")
        while True:
            time.sleep(2)
            
            #ASK INPUT OF EMAIL ADDRESS
            email_3 = input("Please re-type your email address: ")
            confirm_email_3 = re.search(".+@.+\.com", email_3)
            
            #CONDITIONS
            if confirm_email_3:
                
                #INPUTTED EMAIL WILL BE ASSIGNED TO THE ASSIGNED EMPTY CONFIRMED EMAIL VALUE
                #SEE LINE 638
                email_confirmed_3 = email_3
                break
            else:
                
                #IF EMAIL IS INVALID
                time.sleep(2)
                print ("Invalid email address!")
                time.sleep(2)
                print ("Please try again.")
                
        time.sleep(2)
        
        #ASKS INPUT FOR PASSWORD
        pass_3 = input("Please re-type your password: ")
        
        #INPUTTED PASSWORD WILL BE ASSIGNED TO THE ASSIGNED EMPTY CONFIRMED PASSWORD VALUE
        #SEE LINE 639
        pass_confirmed_3 = pass_3
        
        d = email_confirmed_3+':'+pass_confirmed_3
        
        #CONDITIONS
        if d in contents:
            time.sleep(2)
            print ("Successfully signed out!")
            time.sleep(2)
            print ("Exiting...")
            time.sleep(2)
            break
        else:
            #IF ENCOUNTERS UNKNOWN ERROR
            #MOSTLY INVALID ACTIONS
            #OR INVALID EMAIL ADDRESS
            time.sleep(2)
            print ("Error signing out.")
            time.sleep(2)
            print ("Please try again.")
              



#STARTS HERE
#WILL GIVE YOU SHORT INTRODUCTION OF THE PROGRAM
print ("Hey there!")
time.sleep(2)
print ("Welcome to Lorus - Text Editor.")
time.sleep(3)
print ("A free tool for you to Search, Replace, and Count  for words or sentence")
time.sleep(5)
print ()
print ()


#ASK TO SIGN-UP OR SIGN-IN IN ORDER TO PROCEED
while True:
    print ("To continue, type \"SIGNUP\". ")
    time.sleep(2)
    print ("If you already have an account, type \"SIGNIN\".")
    time.sleep(2)
    
    #ASK INPUT SIGNUP OR SIGNIN RESPONSE
    action = input("Type your action: ")
    act_signup = re.search("SIGNUP", action,re.IGNORECASE)
    act_signin = re.search("SIGNIN", action,re.IGNORECASE)
    
    
    #CONDITIONS TO YOUR RESPONSE
    #WHERE MOST FUNCTIONS ARE CALLED
    if act_signup:
        print ("You selected SIGN UP.")
        time.sleep(2)
        print ("Signing up...")
        time.sleep(2)
        print ("Please wait...")
        time.sleep(4)
        
        #SIGNING UP FUNCTION CALLED HERE
        sign_up()
        time.sleep(4)
        
        #SELECTION OF TEXT FILE FUNCTION CALLED HERE
        lorus_file_selection()
        time.sleep(2)
        
        #LORUS CLASS VALUE ASSIGNED HERE
        user = Lorus(user_email,user_password,user_file_path,user_file_content)
        
        #LORUS CLASS' METHOD OF FILE HANDLING CALLED HERE
        #HERE, WILL APPEND THE ACCOUNT INFORMATION ALONG THE CORRESPONDING TEXT FILE
        #THIS WILL BIND ACCOUNT INFORMATION TO THE SELECTED TEXT FILE TO AVOID LOST
        user.account_to_file_distribution()
        time.sleep(3)
        
        #LORUS CLASS' METHOD OF COUNTING, SEARCHING, AND REPLACING WORDS OR SENTENCES CALLED HERE
        user.app_lorus()
        break
    
    elif act_signin:
        print ("You selected SIGN IN.")
        
        #SIGNING IN FUNCTION CALLED HERE
        sign_in()
        
        #WILL LOOP LINE OF CODES IN VARIOUS CONDITIONS
        while True:
            time.sleep(3)
            print ("Please select whether to choose a NEW file, or an EXISTING file.")
            time.sleep(3)
            print ("Type \"SELECT NEW\" if you want to select a new file.")
            time.sleep(3)
            print ("and type \"SELECT EXISTING\" if you want to select an existing file.")
            time.sleep(4)
            
            #ASK INPUT WHETHER TO SELECT A NEW FILE OR EXISTING FILE
            file_act = input("Enter file action: ")
            new_file_act = re.search("SELECT NEW", file_act,re.IGNORECASE)
            existing_file_act = re.search("SELECT EXISTING", file_act,re.IGNORECASE)\
                
            #CONDITIONS
            if new_file_act:
                time.sleep(2)
                
                #CALL FILE SELECTION FUNCTION
                lorus_file_selection()
                break
            elif existing_file_act:
                time.sleep(2)
                
                #CALL EXISTING FILE FUNCTION
                lorus_existing_file_selection()
                break
            else:
                
                #IF FILE ACTION IS INVALID
                time.sleep(2)
                print ("Invalid File action.")
                time.sleep(2)
                print ("Please try again.")
                
        #LORUS CLASS VALUE ASSIGNED HERE
        user = Lorus(user_email,user_password,user_file_path,user_file_content)
        time.sleep(2)
        
        #LORUS CLASS' METHOD OF FILE CONTENT REPLACEMENT CALLED HERE
        user.file_content_replacement()
        time.sleep(2)
        
        #LORUS CLASS' METHOD OF COUNTING, SEARCHING, AND REPLACING WORDS OR SENTENCES CALLED HERE
        user.app_lorus()
        break
    else:
        #IF ACTION IS INVALID
        time.sleep(2)
        print ("Invalid action.")
        time.sleep(2)
        print ("Please try again.")