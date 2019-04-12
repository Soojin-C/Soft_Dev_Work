# Soojin Choi
# SoftDev2 pd07
# K16 -- Do You Even List?
# 2019-04-12

alphabet = "abcdefghijklmnopqrstuvwxyz"
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
nums = "1234567890"

# Password contains:
#   - A mixture of lower and uppercase letter
#   - At least one number
def simple_check(pswd):
    list0 = [x for x in pswd if x in alphabet]
    list1 = [x for x in pswd if x in ALPHABET]
    list2 = [x for x in pswd if x in nums]
    
    #print(list0, list1, list2)
    
    if len(list1) * len(list2) * len(list0) == 0:
        print("false")
        return False
    print("true")
    return True
    
# Rates Password on a scale of 1-10
#   - mixture of upper and lowercase letters
#   - inclusion of numerals
#   - inclusion of these non-alphanumeric chars
non_alpha = ".?!&#,;:-_*"
def rating_check(pswd):
    ret_Score = 0
    if (simple_check(pswd)):
        ret_Score = 7
    else:
        list0 = [x for x in pswd if x in alphabet]
        if len(list0) > 0:
            #print("lower")
            ret_Score += 2
        list1 = [x for x in pswd if x in ALPHABET]
        if len(list1) > 0:
            #print("upper")
            ret_Score += 2
        list2 = [x for x in pswd if x in nums]
        if len(list2) > 0:
            #print("nums")
            ret_Score += 3
        #print(list0, list1, list2)
    list3 = [x for x in pswd if x in non_alpha]
    if len(list3) > 0:
        #print("alphanum")
        ret_Score += 3
    #print(list3)
    print(ret_Score)
    return ret_Score
        
 
simple_check("aA1") 
simple_check("aaa") 
simple_check("") 
simple_check("%$#@") 

rating_check("FancyRibbons!") #missing num
rating_check("1000FancyR1bb0ns!") #full
rating_check("password") #missing all but lowercase
rating_check("") #missing everything 
  
    