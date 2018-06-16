def adding_report(report = "T"):
    total = 0
    items = "Items" 
    while True:
        answer = (input("Enter a integer or \"Q\": ")).upper()
        if answer.isdigit() == True:
            total += int(answer)
            items += "\n" + answer
          
        
        elif answer.startswith("Q"):
            if report == "A":
                print(items,"\nTotal\n",total)
                break
            else:
                print("Total\n",total)
                break
        else:
            print("Invalid input. Try again.")
            

report = "T"
adding_report(report)