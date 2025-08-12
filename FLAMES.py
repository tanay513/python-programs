import time
print("                          F L A M E S               ")
time.sleep(2)
print("           Know the relation between a girl and a boy   ")
time.sleep(2)
print("                                                                  ")
print("(coution: this game is just only for fun purpose, dont take it seriously)")
time.sleep(2)
print(" ENJOY :)")
print("                                                                            ")
print("                                                                                   ")


name1=input("   enter boy name = ")
name2=input("  enter girl name = ")
print("                                                                                ")
print("                                                                                      ")

# Function to count uncommon letters between two names
def count_uncommon_letters(name1, name2):
    # Convert both names to lowercase to perform a case-insensitive comparison
    name1 = name1.lower()
    name2 = name2.lower()

    # Create sets of unique letters in each name
    set1 = set(name1)
    set2 = set(name2)

    # Calculate the uncommon letters by taking the symmetric difference of the sets
    uncommon_letters = set1.symmetric_difference(set2)

    # Count the number of uncommon letters
    count = len(uncommon_letters)

    return count

result = count_uncommon_letters(name1, name2)

# giving the number of uncommon letters


x=result-1

main="flames"
def set_function(main):

 main=main.lower()

 main_set=set(main)

 main_count=len(main_set)
 return  main_count
   

if x>5:
   new_x=x-6
else:
   new_x=x
#converting to new word 1
modified_main1 = main[:new_x] + main[new_x+ 1:]

main_count2=set_function(modified_main1)
if new_x>4:
   new_x2=new_x-5

elif new_x==0:
   new_x2=x-5


else:
   new_x2=new_x

#converting to new word 2

modified_main2 = modified_main1[:new_x2] + modified_main1[new_x2+ 1:]

main_count3=set_function(modified_main2)

if new_x2>3:
   new_x3=new_x2-4

elif new_x2==0:
   new_x3=x-4

else:
   new_x3=new_x2

#converting to new word 3

modified_main3= modified_main2[:new_x3] + modified_main2[new_x3+ 1:]
main_count4=set_function(modified_main3)



if new_x3>2:
   new_x4=new_x3-3

elif new_x3==0:
   new_x4=x-3

else:
   new_x4=new_x3

#converting to new word 4
modified_main4=modified_main3[:new_x4]+modified_main3[new_x4 +1:]
main_count5=set_function(modified_main4)

if new_x4>=1:
   new_x5=new_x4%2

else:
   new_x5=new_x4

#convertint to final letter
modified_main5=modified_main4[:new_x5]+modified_main4[new_x5 + 1:]


if modified_main5=="f":
   print("                  >>>>>friends<<<<<")
elif modified_main5=="l":
   print("                   >>>>>love<<<<<")
elif modified_main5=="a":
   print("                  >>>>>atraction<<<<<")
elif modified_main5=="m":
   print("                   >>>>>marriage<<<<<")
elif modified_main5=="e":
   print("                    >>>>>enimy<<<<<")
elif modified_main5=="s":
   print("                   >>>>>marriagess<<<<<")
else:
   print("                >>>>>no match found<<<<<")

print("                                                                                 ")

print("                         THANTKS FOR USING")
time.sleep(2)
print("                                                      made by -tanay")









