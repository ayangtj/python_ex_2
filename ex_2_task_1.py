# Python refresher exercises 2 - task 1

# Write and test a function is_valid_email_address(s) that evaluates string s as a valid email address 
# Returns: tuple of 2 elements (res, err):
#          res contains the result (None or error code)
#          err contains an error string ("seems legit" for None,  a short error message for the error code
#
# Rules: (these are mine, not the official web standards!)
# must have 3 parts: <A>@<B>.<C>
# A must have between 3 and 16 alpha numeric chars (test: isalnum()) 
# B must have between 2 and 8 alpha numeric chars (test: isalnum()) 
# C must be one of these:  com edu org gov 
#
# Here are some tests and the expected results:
# 
# charding@iastate.edu (None, 'Seems legit')
# chris.edu (1, 'Must have exactly one @!')
# chris@edu (4, 'post @ part must have exactly one dot!')
# @bla.edu (2, 'pre @ part must contain 3 - 16 alfanum chars')
# throatwobblermangrove@mpfc.org (2, 'pre @ part must contain 3 - 16 alfanum chars')
# chris@X.com (5, 'part after @ and before . must contain 2 - 8 alfanum chars')
# chris.harding@iastate.edu (3, 'pre @ part must only contain alfanum chars')
# chris@pymart.biz (7, 'past-dot part invalid, must be from: com, edu, org, gov')
# chris@letsgo!.org (6, 'part after @ and before . must only contain alfanum chars')
# chris@megasavings.org (5, 'part after @ and before . must contain 2 - 8 alfanum chars')
# tc@tank.com (2, 'pre @ part must contain 3 - 16 alfanum chars')
#
# your function MUST react the same (OK or error) but you don't have to use my exact error messages or codes 
# just something similar to that effect. You could even be more helpful e.g. 
# "throatwobblermangrove is too long (21 chars), must be 3 - 16"
# It's OK to bail you at the first proven error, even if there would have been more errors later!
# Also, I prb. forgot some possible edge cases, please add more if needed!

# As proof, please manually copy/paste the console output for one run into a file called
# results1.txt


    
    # your code here
    '''
    A = vars() #problematic, cannot define each part to be character because it can also be int
    B = vars()
    C = vars()
    if s = (A + "@" + B + "." + C) #not quite sure how to define the variables to be without argument
    '''


    '''
    if s = (A, "@", B, ".", C) #attempted using unchangable values to define the required email structure, didn't work 
    and 
        i_a = A.isalnum() #using isalnum method
        i_b = B.isalnum() #using isalnum method
    and (3 =< i_a =< 16)
    and (2 =< i_b =< 8)
    and C in ("com", "edu", "gov", "org"):
        res = "Sucessful!"
        return res
    else 
        err = "invalid email address."
        return err

is_valid_email_address(ayang@gmail.com)
    '''

def is_valid_email_address(s):   

    i_mark = s.count("@") #string method, to count how many times @ appears in the entire string, without parameter 
    if i_mark != 1: #python not equal operator 
        return (1, 'Must have exactly one @!')

    w = s.split("@") #sting method, to split by specified separator (@) and return a list of 2 values
    part_1 = w[0]
    part_2 = w[1]
    #if part_1.count() < 3 or part_1.count() > 16: #count method needs a defined argument, and it's to count for certain specified value
    if len(part_1) < 3 or len(part_1) > 16: #where len() is a built in function that returns "the number of characters in a string"
        return (2, 'pre @ part must contain 3 - 16 alfanum chars')
    #elif part_1.alfanum() > 1: #using isalnum method #str object has no attribute alfanum, did not work 
    elif part_1.isalnum() == False: #boolean strings, to check if string is all alphanumeric characters 
        return (3, 'pre @ part must only contain alfanum chars')


    #if part_2.count() != 1: #wrong method, as it counts part_2 not the ".", hence returned message does not make sense 
    if part_2.count(".") != 1: #to count the "."
        return (4, 'post @ part must have exactly one dot!')

    w2 = part_2.split(".") #string method, split the second value by (.) 
    part_2_1 = w2[0]
    part_2_2 = w2[1]
    #if part_2.count() < 2 or part_2.count() > 8: #same mistake here 
    #if len(part_2) < 2 or len(part_2) > 8: #wrong part! 
    if len(part_2_1) < 2 or len(part_2_1) > 8:    
        return (5, 'part after @ and before . must contain 2 - 8 alfanum chars')
    elif part_2_1.isalnum() == False: #boolean strings, to check if string is all alphanumeric characters 
        return (6, 'part after @ and before . must only contain alfanum chars')

    if part_2_2 not in ("com", "edu", "org", "gov"):
        return (7, 'past-dot part invalid, must be from: com, edu, org, gov')

s = "tc@tank.com"
print (s) #have the email address printed + error message
is_valid_email_address(s)















    

# This if ensures that the following is NOT run if this file was imported as a module (which we'll do next!)
if __name__ == "__main__":

    # tests, including edge cases (incomplete? add more!)
    email_list = ["charding@iastate.edu", 
        "chris.edu",
        "chris@edu",
        "@bla.edu",
        "throatwobblermangrove@mpfc.org", 
        "chris@X.com",
        "chris.harding@iastate.edu",
        "chris@pymart.biz",
        "chris@letsgo!.org",
        "chris@megasavings.org",
        "tc@tank.com",
        ]
    # validate each email from the list
    for e in email_list:
        r, s = is_valid_email_address(e) 
        if r == None:
            print(e, s) # OK
        else:
            print(f"{e} - error: {s}, error code: {r}") # Error

        
