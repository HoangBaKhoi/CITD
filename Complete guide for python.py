price = 10
rating = 4.9
name = 'Khoi'
is_published = False #tên biến nên viết thường hết, còn false là 1 phần của python, nên phải viết hoa chữ F thì code mới hiểu.
print(price)

#We check in a patient named John Smith. He's 20 years old and is a new patient.
#Define 3 variables: His name, his age, another variable for if this is a new or an existing patient.
full_name = 'John Smith'
age = 20
new_patient = True

#Ask 2 question, person's name and favorite color. Then print a message like "Khôi thích màu cam"
name = input ('Tên bạn là gì? ')
color = input ('Okay, bạn tên là ' + name + ', vậy bạn thích màu gì? ')
print (name + ' thích ' + color)  

#Convert type of variables.
birth_year = input('Birth year: ')          # When you use input function, you always get the string "str"
print(type(birth_year))                     # Check type of varibles
age = 2025 - int(birth_year)                
int()       #convert 'str' into 'int'
float()     #convert 'str' into 'float'
bool()      #convert 'str' into 'bool'
print(age)

#Ask a user their weight (in pounds), convert it to kilograms and print on the terminal
weight_in_pounds = input('Your weight in pounds is: ')
print('Then your weight is ' + str(float(weight_in_pounds)*0.453592) + ' in kilograms')

#                                                                                              more syntax about string
course = 'Python for beginners'
         #01234
print(course[1])        #y
print(course[-2])       #r
print(course[0:3])      #Pyt
print(course[4:])       #on for beginners
print(len(course))      #20
print(course.upper())   #PYTHON FOR BEGINNERS
print(course.lower())   #python for beginners  
print(course.title())   #Python For Beginners 
print(course.replace('begin', 'absolute beginners'))        #Python for absolute beginnersners
print('Python' in course)   #True
print('python' in course)   #False

#f-string (nhúng biến vào chuỗi)    {variables}
first = 'Khoi'
last ='Hoang'
message = first + ' [' + last + '] is a coder'      #FIRST [LAST] is a coder
msg = f'{first} [{last}] is a coder'                #FIRST [LAST] is a coder, just put every thing inside f'', the string varibles inside []
print(msg)
print(message)

#math function
import math         #import math module. math like an object like a string, so we can acccess functions.
x = 2.9
print(round(x))     #3
print(abs(-2.9))    #2.9
print(math.floor(2.9))
#python 3 math module ->docs.python.org


#                                                                                                    IF FUNCTION
# If applicant has high income AND good credit. Eligible for loan.
has_high_income = True
has_high_credit = True
if has_high_income and has_high_credit:         # and, and not, or
    print("eligible for loan")

# If name is less than 3 characters long. Name must be at least 3 characters
# Otherwise if it's more than 50 characters long. Name can be a maximum of 50 characters
# Otherwise. Name looks goods!
name = input("What is your name? ")
character = len(name)
if character < 3:
    print("Name must be at least 3 characters")
elif character > 50:
    print("Name can be a maximum of 50 characters")
else:
    print("Name looks goods!")


#Input: Nhập số cân và Nhập L cho lbs, K cho kg. Output: In quy đổi số cân ra đơn vị còn lại.
weight = input("What is your weight? ")
unit_of_weight = input ("Type L(lbs) or K(kgs): ")
if unit_of_weight == 'L' or unit_of_weight == 'l':                                            #ở đây gán cái đó cho 1 chữ nên cần dấu ==
    print("Your weight is: " + str(int(weight)*0.45) + " kgs")
elif unit_of_weight.lower() == 'k':                                         #Dùng hàm lower()
    print(f"Your weight is: {round(float(weight)/0.45, 2)} lbs")            #Dùng f-string để dễ đọc hơn. Dùng round(float, 2) để làm tròn 2 số. float để só thập phân.
else:
    print("Invalid unit entered")

#error 1: gán variable là dấu =. Còn dấu == mới là dấu bằng. Vậy nên lúc đầu bấm unit_of_weight = L là sai!         Trong điều kiện luôn dùng ==
#error 2: unit_of_weight = L là sai! vì L ở đây không được defind. => phải thành 'L' tức là 1 str.
#error 3: weight/0.54 là sai. string không chia được cho float or int.
#error 4: int(weight)/0.54 vẫn chưa đủ. Tại chuỗi chỉ kết hợp với chuỗi được.
#error 5: if unit_of_weight == 'L' or 'l'. Func này bị lỗi vì 'l' luôn hiểu là 1 chuỗi không rỗng nên luôn đúng. Func thành if unit_of_weight == 'L' or True.


#                                                                                                  WHILE LOOP
#Làm 1 game đoán số từ 1-10, có 3 lần đoán.
secrect_nunber = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secrect_nunber:
        print("you won!")
        break                       #not going to evaluate the condition again
else:
    print("Sorry, you failed!")

#làm 1 program. Khi bấm help để biết thêm thông tin.                            Bài khó!!! cần xem kĩ bài này.
#vòng lặp là khung bao quanh - luôn nằm ngoài cùng. Input nằm đầu vòng lặp.
command = ""            #empty string
started = False         #thêm boolen để check trạng thái của xe.
while True:             #bấm quit thì chương trình kết thúc => phải có vòng lặp. Vậy nên bắt đầu từ while True để có 1 vòng lặp.     
    command = input ("> ").lower()      #tránh lặp lại lower bên dưới
    if command == "start":
        if started:
            print ("Car is already started!")
        else:
            started = True
            print ("Car started .....")
    elif command == "stop":
        if not started:
            print("Car is already stopped!")
        else:
            started = False
            print ("Car stopped.")
    elif command == "help":
        print ("""
start - to start the car. Nếu bấm start 2 lần thì sẽ ra cái khác
stop - to stop the car. Nếu bấm stop 2 lần sẽ ra cái khác
quit - to quit. Và kết thúc chương trình.
        """)
    elif command == "quit":
        break
    else:
        print ("Sorry, I don't understand!")

#                                                                             FOR ..... LOOP
#for loop là một cấu trúc lặp trong Python, được sử dụng để lặp qua các phần tử của một chuỗi, danh sách, tuple, từ điển, hoặc bất kỳ đối tượng nào có thể lặp (iterable).
#variable: Biến tạm thời nhận giá trị của từng phần tử trong đối tượng lặp.
#iterable: Một đối tượng có thể lặp qua, như danh sách (list), chuỗi (string), tuple, hoặc range.

#1. Lặp qua một danh sách
name_list = ['Khoi', 'Khoa', 'Hoang']
for name in name_list:           
    print(name)

#2. Lặp qua một chuỗi
for char in "python":
    print(char)

#Tính tổng số tiền trong 1 giỏ đồ
prices = [10, 20, 30]           #giả định số tiền trong giỏ.
total = 0                       #biến dùng để lưu tổng tiền
for price in prices:
    total += price              #total = total + price, Cộng giá từng món vào tổng.
    print(f"Tổng tiền là {total}")     #in ra mỗi lần cộng vì nó nằm trong vòng lặp.
print(f"Tổng tiền là {total}")         #in ra dòng cuối cùng kết quả vì nó nằm ngoài vòng lặp.

#sigma Σ
summation = sum(2*i for i in range(1,6))    #A summation is expressed as a sigma Σ and adds elements together        
print(summation)                            #=30

x = [1, 4, 6, 2]
n = len(x)
summation = sum(10*x[i] for i in range(0,2))
print(summation)

#nested loop (vòng lặp lồng nhau, một vòng lặp nằm trong 1 vòng lặp khác)
for x in range(4):                  #x trong khoảng 0 - 3, vòng lặp bên ngoài
    for y in range(1,3):            #y trong khoảng 1 - 2, vòng lặp bên trong
        print(f'({x}, {y})')

#tạo ra chữ F trên màn hình bằng loop.              #bài hơi lú
number_char_inline = [5, 2, 5, 2, 2]
for x_count in number_char_inline:               #không tự động thụt lề, trong Python, ko thụt lề lung tung!!! ex: không nằm trong một hàm, điều kiện if, hoặc một khối mã khác.
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)

#find the largest number in a list
numbers = [1, 76, 12, 13, 9, 10]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print (max)
