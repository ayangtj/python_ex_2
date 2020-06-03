# Python refresher exercises 2 - task 2

# - as part of some app, the user has to create a valid email address
# - any address will do as long as it's valid
# - your validation will only allow a number of retries if a invalid email is given (default 3)
# - once the number of attempts is exhausted (you should show how many retries are left!), set the
#   variable (flag) gave_up to True and bail out.
# 
# - it's OK to start with my solution from the lecture in flow control, although I 
#   encourage you to try you own solution first (if you can't remember). Any other, working
#   solution is fine, too!
# - when it comes to how to react to an error, your user MUST re-enter a string, but it's up to 
#   you how helpful you want to be:
#   - you could just list all the rules on error and demand a new input
#   - you could list the appropriate error message returned from you function and demand a new input
#   - you could do something fancy and only require re-typing of what's wrong (if that's technically possible):
#       e.g. if the pre @ is wrong (too long, contains a invalid char) you could demand that
#       only that incorrect part is re-entered. Warning - this can be complicated and laborious to test!
# - Note that the check for a valid email is a bit weird (b/c of how I set it up):
#   - iff the first return is None (r == None), the email is valid (yes, None doesn't sound like an OK ...)
#   - if you didn't get None (r != None), then r contains an error code, which you could use in your 
#     flow control for branching, if you want to do something fancy

# Optionally, you can use regex for all this!

# Once you're solved this, run some tests to show me that it works. 
# Again, manually copy/paste the console output in a text file (results2.txt)



# import your function from the previous .py file as a module (you can abbreviate it)
# use ex_2_task_2 here instead once your function works!
from ex_2_task_1_solution import is_valid_email_address as is_valid 

gave_up = False
attempts_left = 3

# your code - start

# def create_email(): #Function already exits using module, no need to create new funtion 
# while gave_up = False: #attempted to write string asking to input email address before 3 attempts are up, not sure why it's telling me "invalid syntax"


'''
if not gave_up: #changing this part to a while true loop for continuing asking for email address input after 1 failed attempt 
    user_input = input ('Enter an email address you would like to create:')
    #if is_valid_email_address(user_input) != None: #forgot is_valid_email_address has been redefined in module
    if is_valid(user_input) != None:
        #gave_up -= 1 #wrong variable. Results show "you have -1 attempts"
        attempts_left -= 1
        print(is_valid(user_input), f'you have {attempts_left} attempts remaining. Please tray again.')
    elif gave_up == True: #It does not work. Because after first failed attempt, it's not asking for the second attempt. Thinking loop needs to be involved for repeated checking. 
        attempts_left = 0
        print(is_valid(user_input), f'you have no attempts left.')
    else:
        print(f'Congrats, your new email address is {user_input}')
        '''

'''
while True:
    user_input = input('Enter an email address you would like to create:')

    if attempts_left == 1:
        gave_up == True
        print(is_valid(user_input), f'you have no attempts left.')
        break
    

    #if gave_up == False: #got a bit confused with fave_up = False. Now I think it might actually be in relations to while true loop? Hmm. 
    if is_valid(user_input) != None:
        attempts_left -= 1
        print(is_valid(user_input), f'you have {attempts_left} attempts remaining. Please tray again.')
        #break 
    
    if is_valid(user_input) == None:
        print(f'Congrats, your new email address is {user_input}')
        break
    '''

'''

# This solution does not work right when email is valid, it still returns "you have 2/1 attempts left please try again. Not sure why. 

while gave_up == False:
    user_input = input('Enter an email address you would like to create:')
    if is_valid(user_input) != None:
        attempts_left -= 1
        print(is_valid(user_input), f'you have {attempts_left} attempts remaining. Please tray again.')
        #break 
    elif gave_up == True:
        attempts_left == 0
        print(is_valid(user_input), f'you have no attempts left.')
        break
    else: 
        print(f'Congrats, your new email address is {user_input}')
        break 
 '''  

'''
#this soluiton seems to break it more. Need to look at more examples of while loops I suppose
while gave_up == False:
    user_input = input('Enter an email address you would like to create:')
    if is_valid(user_input) == None:
        print(f'Congrats, your new email address is {user_input}')
        break 

    elif gave_up == True:
        attempts_left == 0
        print(is_valid(user_input), f'you have no attempts left.')
        break
    
    else: 
        attempts_left -= 1
        print(is_valid(user_input), f'you have {attempts_left} attempts remaining. Please try again.')
        #break 
'''


while not gave_up:
    user_input = input('Enter an email address you would like to create:')
    if is_valid(user_input)[0] is None: #showing only first position of None from the function created  
        print(f'Congrats, your new email address is {user_input}')
        break
    else:
        attempts_left -= 1
        print(is_valid(user_input), f'you have {attempts_left} attempts remaining.')
        if attempts_left == 0:
            print(f'you have no attempts left.')
            gave_up = True

    
        


'''
while True:
    email = input("email address?")
    r, err_str = is_valid(email)

    if r == None:
        print(email, "is valid!")
        break
    
    # error
    attempts_left -= 1

    # no attempts left - bail out 
    if attempts_left == 0:
        gave_up = True
        print("No attempts left, bailing out")
        break

    print(email, "is invalid!")
    print("Reason:", err_str)
    print(f"Try again, {attempts_left} attempts left")

# your code - end
if not gave_up:
    print("valid email", email)
else:
    print("invalid email", email)
    '''