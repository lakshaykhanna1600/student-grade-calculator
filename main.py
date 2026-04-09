
def main():
    num= int(input("How many subjects? "))
    for i in range(num):
        data= input(f"write the name of the subject {i+1} and its score seprated by a colon; example: Math:98?")
        name , number= data.split(":")
        number=int(number)
        calculate(name,number)


def calculate(sub,score):
    if 0>score or score>100:
        print("please enter a vaild score")
    elif 90<= score <= 100:
        print(f"Grade A in {sub}")
    elif 80<= score < 90:
        print(f"Grade B in {sub}")
    elif 70<= score < 80:
        print(f"Grade C in {sub}")
    elif 60<= score < 70:
        print(f"Grade D in {sub}")
    else:
        print(f"Grade F in {sub}")

main()