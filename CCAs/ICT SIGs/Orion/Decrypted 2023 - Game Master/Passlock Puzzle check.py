conditions = str(input("Which conditions: "))
#from complicated calc and math, mostly that because we don't use it everytime because the ocnditons aren't alwasy laoded and even if they are not always all of them,
#the processing load of calluing the fucntion not worth it. Besides, it's basically just the same thing, if it was different fuctiion would be goood buyt here might as well just copy paste - it's too simple here to warrqant a function, the complex feature isn't needed   
# and you can't make a function for it anyway     
if '02' in conditions: #2    more than this year or too old
    while True:#this is the format
        birthyear = input('birthyear: ')
        if len(birthyear) != 4: #also check cannot be more than current year
            print("Valid birthyear please")
        else:
            break
        
if '04' in conditions:
    ptable = ('hydrogen', 'helium', 'lithium', 'beryllium', 'boron', 'carbon', 'nitrogen', 'oxygen', 'fluorine', 'neon', 
'sodium', 'magnesium', 'aluminium', 'silicon', 'phosphorus', 'sulphur', 'chlorine', 'argon', 'potassium', 'calcium', 'scandium', 
'titanium', 'vanadium', 'chromium', 'manganese', 'iron', 'cobalt', 'nickel', 'copper', 'nickel', 'copper', 'zinc', 'gallium', 
'germanium', 'arsenic', 'selenium', 'bromine', 'krypton', 'rubidium', 'strontium', 'yttrium', 'zirconium', 'niobium', 'molybdenum', 
'technetium', 'ruthenium', 'rhodium', 'palladium', 'silver', 'cadmium', 'indium', 'tin', 'antimony', 'tellurium', 'iodine', 
'xenon', 'caesium', 'barium', 'lanthanum', 'cerium', 'praseodymium', 'praseodymium', 'neodymium', 'promethium', 'samarium', 
'europium', 'gadolinium', 'terbium', 'dysprosium', 'holmium', 'erbium', 'thulium', 'ytterbium', 'lutetium', 'hafnium', 'tantalum', 
'tungsten', 'rhenium', 'osmium', 'iridium', 'platinum', 'gold', 'm                      ranium', 'neptunium', 'plutonium', 'americium', 'curium',  
'berkelium', 'californium', 'einsteinium', 'fermium', 'mendelevium', 'nobemium', 'lawrencium', 'rutherfordium', 'dubnium', 
'seaborgium', 'bohrium', 'hassium', 'meitnerium', 'darmstadtium', 'roentgenium', 'copernicium', 'nihonium', 'flerovium', 
'moscovium', 'livermorium', 'tennessine', 'oganesson')
    element = (input("Which element: "))
    while True:
        if element.lower() not in ptable:#islpha true
            print("Valid element please")
        else:
            break
if '05' in conditions:#1
    country = input('Country: ') #clarify that shortahand name, so check if digit
if '07' in conditions:#1
    chairs = input("Number of chairs: ") #reject if not digit
if '08' in conditions:
    comp = input("Company: ")
if '11' in conditions:
    prime = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101,
             103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199)
if '12' in conditions:#2
    time = input("time of requirement drawn: ")
    while True:
        if len(time) != 4:
            print("24h time please")
        elif int(time) > 2359:
            print("Valid time please") #for time checl, string the first two postions and concatentte and then string the other two
        else:
            break
if '13' in conditions:
    while True:
        date = input("Date(DD/MM/YYYY): ")
        if len(date) != 10:
            print("DD/MM/YYYY format")
        elif '/' not in date:
            print("Use /")
        elif date[2] != '/' or date[5] != '/':
            print("DD/MM/YYYY format")
        elif int(date[0] + date[1]) > 31:
            print("Valid day please")
        elif int(date[3] + date[4]) > 12:
            print("Valid month please")
        elif int(date[6] + date[7] + date[8] + date[9]) != 2023:
            print("This year please") # customise year, or just use datetime function
        else:
            break
if "18" in conditions:
    ppl = input("Number of people: ")#expcetion hnadling for digit

if '20' in conditions:
    wheels = input("Number of wheels: ")#expcetion hnadling for digit

if '25' in conditions:
    names = []
    count_names = 0
    while True:
        name = input("What is your real name: ")
        names.append(name)
        if len(names) == 3:
            break


pw = input("Password here: ")
if '03' in conditions:
    count_total = 0
    for element in list(pw):
        if element.isdigit() == True:
            count_total += int(element)
if '06' in conditions:
    count_pi = 0
    count_pi_ones = 0
    pi_digits = '31415'
    for element in list(pi_digits):
        if element in pw:
            count_pi += 1
    for element in list(pw):
        if element == '1':
            count_pi_ones += 1
if '14' or '21' in conditions:
    count_lower = 0
    for element in list(pw):
          if element.islower() == True:
            count_lower += 1              
if '15' or '21' in conditions:
    count_upper = 0
    for element in list(pw):
          if element.isupper() == True:
            count_upper += 1   
if '16' in conditions:
    count_letters = 0
    count_nums = 0
    item = 0
    for element in list(pw):
        if list(pw).pop(item).isdigit() == True: 
            count_nums += 1
        elif list(pw).pop(item).isalpha() == True:
            count_letters += 1
        item += 1
if '17' in conditions:
    count_roman_1 = 0
    count_roman_5 = 0
    count_roman_10 = 0
    for element in list(pw):
        if element == 'I':
            count_roman_1 += 1
        elif element == 'V':
            count_roman_5 += 1
        elif element == 'X':
            count_roman_10 += 1
if '24' in conditions: #cetain number os special cahracters
    count_spec = 0
    for chara in list(pw):
        if chara.isdigit() == False and chara.isalpha() is False:
            count_spec += 1


if '25' in conditions: #cettain number of names
    for word in names:
        if word in pw:
            count_names += 1
   
def check(req,num):        
        if req :
            print(str(num) + ". fulfilled\n")            
        else:
            print(str(num) + ". error\n")

if "01" in conditions:
    check(pw[0] == pw[-1],1)
if "02" in conditions:    
    check(birthyear in pw,2) #vulnerability - you check the element variable, the one you input so even if you don't put the element in the final pw it will show fine
    #then again for this game they already made the pw
if "03" in conditions: 
    print(count_total) 
    check(count_total == 150,3)
if '04' in conditions:
    check(element.lower() in pw.lower(),4)
if '05' in conditions:
    check(country.lower() in pw.lower(),5)
if '06' in conditions:
    check(count_pi == 5 and count_pi_ones >= 2,6)
if '07' in conditions:
    check(chairs in pw,7)
if '08' in conditions:
    check(comp in pw,8)
if '09' in conditions:
    check(len(pw)%2 == 0,9)
if '10' in conditions:
    check('624' in pw,10)
if '11' in conditions:
    check(len(pw) in prime,11)
if '12' in conditions:
    check(time in pw,12)
if '13' in conditions:
    check(date in pw,13)
if '14' in conditions:
    print("lowercase: " + str(count_lower))
    check(count_lower >= 20,14)
if "15" in conditions:
    print("uppercase: " + str(count_upper))
    check(count_upper >= 15,15)
if "16" in conditions:
    print("numbers: " + str(count_nums))
    print("letters: " + str(count_letters))
    check(count_letters == count_nums,16)
if "17" in conditions:
    print("Roman count: " + str((count_roman_1)+(5*count_roman_5)+(10*count_roman_10)))
    check((count_roman_1)+(5*count_roman_5)+(10*count_roman_10) == 68, 17)
if '18' in conditions:
    check(ppl in pw,18)
if '19' in conditions:
    check('883' in pw,19)
if '20' in conditions:
    check(wheels in pw,20)
if '21' in conditions:
    check(count_lower == count_upper,21)
if '22' in conditions:
    check("Ngee Ann Poly" in pw,22)
if '23' in conditions:
    check('599489' in pw,23)
if '24' in conditions:
    check(count_spec >= 5,24)
if '25' in conditions:
    check(count_names == 3,25)#don't need while loop, no need to break just go through all once

# 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25
# chairs = 33
# wheels = 120
# 25, 17, 07, 15, 10, 12, 05, 18, 03, 13
# limbs = 12
# people = 3
# date = 09/08/2023