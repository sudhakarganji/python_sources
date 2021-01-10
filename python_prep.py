''''
height=input("please eneter height: ")
weight=input("please eneter weight: ")
BMI= int(weight) / float(height)**2
print(f'(BMI value is {round(BMI,2)})')


score =90
height =1.21
isdone = True
print(f" I scored {score} my height is {height} what i heard is {isdone} ")



age = int(input("enter you Age "))
months_left = 90*12 -(age*12)
weeks_left = 90*52 - (age*52)
days_left = 90*365 - (age*365)

print(f" you have {days_left} days,  {weeks_left} weeks and {months_left } months left")


print("Welcome to tip calculator")
bill=int(input("what was the total bill? $"))
tip =int(input("what % you want to tip? 10 12 15?"))
people=int(input("How many people to split? ")) 
total_bill=  bill+ (bill*tip/100)
each_person= round(total_bill/people,2)
print(f"Each person should pay ${each_person}")



print("Welcome to the rollercoster Ride ")
height = int(input ("what is your height?"))
if height >1:
  print("enjoy ride")
else:
  print("sorry no ride")

number=int(input("enter the number "))
if number%2==0:
  print ("the number is even")
else:
  print("the number is odd")




year = int(input("enter the year:"))
if year%4 == 0:
      if year%100!=0:
          print("year is leap year")
      else:
        if year%400==0:
           print("year is leap year")
        else:
          print("year is Not a leap year")
else:
    print("not a leap year")
  


print("Welocme to the python pizza Deliveries")
size=input("Please Enter the size pls S M L :")
add_pep=input("Do you want extra pep Y or N ? ")
extra_cheese=input("Do you want extra cheese Y or N ? ")
bill=0
if size=="S":
   bill=15
elif size=="M":
   bill=15
else:
   bill=20  

if  add_pep=="Y" and  size=="S" :
  bill=bill+2
if  add_pep=="Y" and  size!="S" :
  bill=bill+3

if extra_cheese=="Y":
  bill=bill+1

  print(f"the total bill is ${bill}")
   



name = input("enter your name: ")
pname =input("enter your partner's name: ")
name =  name.lower()
pname = pname.lower()
tcount=0
lcount =0
tcount= tcount+  name.count('t') + pname.count('t') 
tcount= tcount+  name.count('r') + pname.count('r')
tcount= tcount+  name.count('u') + pname.count('u')
tcount= tcount+  name.count('e') + pname.count('e')

lcount=lcount+ name.count('l') + pname.count('l') 
lcount=lcount+ name.count('o') + pname.count('o') 
lcount=lcount+ name.count('v') + pname.count('v') 
lcount=lcount+ name.count('e') + pname.count('e') 

print(f"result is {tcount}{lcount}")



import random
dec=random.randint(3,56)
print(dec)




import random
dec=random.randint(0,1)
if dec==0:
  print ("tails")
else:
  print("Heads") 


states = ["ap","ka","bi","tn"]

import random
names =" sudhakar raji karthik Hemish "
names=input("Enter the list of names ")
name_list= names.split(" ")
#rand_num=random.randint(0,len(name_list)-1)
rand_num =random.choice(name_list)
print(f"The bill will be paid by {rand_num}" )

import random


choice= int(input("what do you choose? type 0 fro rock, 1 for paper or 2 for scissors"))

ran=random.randint(0,2)

if choice ==0:
  print(rock)
elif choice ==1:
  print(paper)
else:
  print(scissors)


print("Computer chose")

if ran == 0:
  print(rock)
elif ran ==1:
  print(paper)
else:
  print(scissors)

if choice==0 and ran == 1:
   print ("you win")
if choice==0 and ran == 2:
   print ("you lose")

if choice==1 and ran == 0:
   print ("you lose")
if choice==1 and ran == 2:
   print ("you win")

if choice==2 and ran == 0:
   print ("you lose")
if choice==2 and ran == 1:
   print ("you win")


#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
llist=[]
slist=[]
nlist=[]
for i  in range(1,nr_letters+1):
   r= random.randint(0,25)
   llist.append(r)
for j in range(1,nr_numbers+1):
  n= random.randint(0,9)
  nlist.append(n)
for k in range(1,nr_symbols+1):
  s=random.randint(0,8)
  slist.append(s)

print ("password is \n")
password=[]
for i in llist:
  print(letters[i])
  password+=letters[i]
for j in nlist:
  print(numbers[j])
  password+=numbers[j]
for k in slist:
  print(symbols[k])
  password+=symbols[k]

print(f"password is {password}")

random.shuffle(password)
print(f"password is {password}")
fpassword =""
for k in password:
   fpassword+=k
print(fpassword)




#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P




#Step 1 

import random
word_list = ["aardvark", "baboon", "camel"]


#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
display=[]
randword = random.choice(word_list)
for j  in range(len(randword)):
  #print("_" , end =" ",flush=True)
  display+="_"
print(display) 
lives=6
has_underscore = True
print(stages[lives])
while (has_underscore):  
  gues_a_letter=input("\n\nplease  guess a letter: ") 
  for i in range(len(randword)):
    if randword[i] ==gues_a_letter :
      display[i]=gues_a_letter
      #print("_" , end =" ",flush=True)
  if gues_a_letter not in randword:
    lives-=1
    print(stages[lives])
    if lives ==0:
      print("you lose")
      has_underscore=False
  else:
    print(stages[lives])    
  print(f"lives = {lives}")
  print(f" the word is {display}")
  if  "_" not in display:
    has_underscore=False
    print("You Win")
  







#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.



import math
def paint_calc(height,width,cover):
  area=height*width
  cans_for_area=math.ceil(area/cover)
  print (f"cans needed = {cans_for_area}" ) 


test_h=int(input("Enter the height"))
test_w=int(input("Enter the width"))
coverage =5
paint_calc(height=test_h, width=test_w, cover=coverage)




def prime_checker(number):
  isprime=True
  for i in range(2,number):
    if number%i==0:
      isprime=False

  if isprime:
    print("The number is prime")    
  else:
    print("The number is not prime")


n= int(input("Check this number: "))
prime_checker(number=n)



alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encode(text_str,shift):
 etext="" 
 for t in text_str:
  etext +=chr(ord(t) + shift)
 print(f"The encoded string is {etext}")    
 
def decode(text_str,shift):
  dtext=""
  for t in text_str:
   dtext +=chr(ord(t) - shift)
  print(f"The decoded string is {dtext}")

if direction=="encode":
  encode(text,shift)

if direction=="decode":
  decode(text,shift)

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 


my_dict = { "key1":"value1", "key2":"value2", "key3" : "value3" }
print(my_dict["key3"])
my_dict["key4"]="value4"


emptydict={}
my_dict["key4"]="value44"
print(my_dict)

for key in my_dict:
  print(key)
  print(my_dict[key])

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(country,visits,cities):
  dict_country={ "country":country ,"visits":visits,"cities":cities}
 # visits_no= {"visits":visits}
  #cities_all={"cities":cities }
  travel_log.append(dict_country)



#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

  '''

