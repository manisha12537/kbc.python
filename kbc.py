question_list = ["1).How many continents are there?","2).What is the capital of India?","3).NG mei kaun se course padhaya jaata hai?"]
options_list = [["Four", "Nine", "Seven", "Eight"],["Chandigarh", "Bhopal", "Chennai", "Delhi"],["Software Engineering", "Counseling", "Tourism", "Agriculture"]]
answer_list=[["1.Four","3.Eight"],["3.Chennai","4.Delhi"],["2.Tourism","1.Software Engineering"]]
solution_list = [3, 4, 1]
question_num=1
print("WEL-COME TO KBC GAME")
i=0
win_RS=0
life_line_count=0
while i<len(question_list):
    print(question_list[i])
    j=0
    while j<len(options_list):
        print(j+1,options_list[j][i])
        j+=1
    life_line=input("do you want life-line")
    if(life_line=="yes"):
        if(life_line_count<1):
            print(answer_list[i])
            ans=int(input("enter your answer"))
            if(ans==solution_list[i]):
                print("your answer is correct")
                print("win",win_RS)
                win_RS+=5000
            else:
                print("your answer is incorrect")
                print("win",win_RS)
                break
            life_line_count+=1
        else:
            print("you alrady used life-line")
            ans=int(input("enter your answer"))
            if(ans==solution_list[i]):
                print("your answer is correct")
                print("win",win_RS)
                win_RS+=5000
            else:
                print("your answer is wrong")
                print("win",win_RS)
                break
    else:
        ans=int(input("enter answer"))
        if ans==solution_list[i]:
            print("correct answer")
            print("win",win_RS)
            win_RS+=5000
        else:
            print("incorrect answer")
            print("win",win_RS)
            break
    i+=1

        


