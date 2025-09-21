import re
import time

#regex for email
reg1 = re.compile(r"\w+(?:[.+_-])*\w*(?:\.|-|_|\+)*@[a-zA-Z]+\.[a-zA-Z]{2,}(?:\.[a-zA-Z]+)?")
#regex for URL
reg2 = re.compile(r"http[s]?://[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*\.[a-zA-Z]{2,}(?:/[a-zA-Z0-9/+.?&=%-]*)?")
#regex for phone_number
reg3 = re.compile(r"(?:\(?\d{3}\)?)[.\s-]\d{3}[-.\s]\d{4}")
#regex for time
reg4 = re.compile(r"\b\d\d?:\d{2}\s?(?:am|pm)?\b")
#regex for credit card
reg5 = re.compile(r"(?:\d{4}[ \-]){3}+\d{4}")
#regex for html tags
reg6 = re.compile(r"<[a-zA-Z]+[^>]*>")
#regex for currency amounts
reg7 = re.compile(r"\$\d+(?:[,.]\d+)?\.?\d+\s")

#defining a function called match_finder to take input from user and check mathes
def match_finder():
    while True:
        print("1.Input email, URL, Phone_number, time, credit card num, html tags, and currency")
        print("2.Give file to check matches")
        print('3.Check matches in file "test_string.txt"')
        print("4.Exit")
        print('  ------------Note: "test_string" is the file I wrote to check the matches.')
        print('Download it from my GitHub repo.---------\n')
        choice = input("Please choose one of the menu above to validate your input(1,2,or 3 and 4 to exit): ")
        if choice == "1":
            while True:
                print(" 1.Email\n 2.URL\n 3.Phone_num\n 4.Time\n 5.Credit_card")
                print(" 6.HTML tags\n 7.Currency amounts\n 8.Back")
                find = input("Please input your choice: ")
                if find == "1":
                    email = input("Input email: ")
                    result = reg1.fullmatch(email)
                    if result:
                        print("----Valid email✅---")
                    else:
                        print("----Invalid email❌----")
                if find == "2":
                    url = input("Please input URL: ") 
                    if reg2.fullmatch(url):
                        print("----Valid URL✅-----")
                    else:
                        print("----Invalid URL❌----")
                if find == "3":
                    phone_num = input("Please input phone_number: ")
                    if reg3.fullmatch(phone_num):
                        print("----Valid phone number✅----")
                    else:
                        print("----Invalid phone number❌----")
                if find == "4":
                    tme = input("Please input time: ")
                    if reg4.fullmatch(tme):
                        print("----Valid time format✅----")
                    else:
                        print("----Invalid time format❌----")
                if find == "5":
                    credit_card = input("Please enter credit card number: ")
                    if reg5.fullmatch(credit_card):
                        print("----Valid credit card number✅----")
                    else:
                        print("----Invalid credit card number❌----")
                if find == "6":
                    tags = input("Please enter html tag: ")
                    if reg6.fullmatch(tags):
                        print("----Valid html tags✅----")
                    else:
                        print("----Invalid html tags❌----")
                if find == "7":
                    currency = input("Please input currency: ")
                    if reg7.fullmatch(currency):
                        print("----Valid currency✅----")
                    else:
                        print("----Invalid currency❌----")
                if find == "8":
                    break           
        
        elif choice == "2":
            text_file = input("Please input file to search matches: ")
            print("----Checking file----")
            time.sleep(4)
            try:
                with open(text_file, "r") as fi_ob:
                    filee = fi_ob.read()
            except FileNotFoundError:
                print("\n----❌file not found❌----\n")
                continue
            result_1 = reg1.findall(filee)
            if result_1:
                print("\nEmail Mathes: ")
                for result1 in result_1:
                    print(result1)
            else:
                print("\nNo email match")
            result_2 = reg2.findall(filee)
            if result_2:
                print("\nURL Mathes: ")
                for result2 in result_2:
                    print(result2)
            else:
                print("\nNo URL match")
            result_3 = reg3.findall(filee)
            if result_3:
                print("\nPhone number mathes: ")
                for result3 in result_3:
                    print(result3)
            else:
                print("\nNo phone number match")
            result_4 = reg4.findall(filee)
            if result_4:
                print("\nTime matches: ")
                for result4 in result_4:
                    print(result4)
            else:
                print("\nNo time matches.")
            result_5 = reg5.findall(filee)
            if result_5:
                print("\nCredit card number matches: ")
                for result5 in result_5:
                    print(result5)
            else:
                print("No credit card number matches.")
            result_6 = reg6.findall(filee)
            if result_6:
                print("\nHTML tag matches: ")
                for result6 in result_6:
                    print(result6)
            else:
                print("\nNo html tag match.")
            result_7 = reg7.findall(filee)
            if result_7:
                print("\nCurrency matches: ")
                for result7 in result_7:
                    print(result7)
            else:
                print("\nNo currency matches.")
            
        elif choice == "3":
            print("\n---Processing---")
            time.sleep(6)
            try:
                with open("test_string.txt","r") as myfi_ob:
                    myfile = myfi_ob.read()
            except FileNotFoundError:
                print("Error: file not found.")
                continue
            result_1 = reg1.findall(myfile)
            if result_1:
                print("\nEmail Mathes: ")
                for result1 in result_1:
                    print(result1)
            else:
                print("\nNo email match")
            result_2 = reg2.findall(myfile)
            if result_2:
                print("\nURL Mathes: ")
                for result2 in result_2:
                    print(result2)
            else:
                print("\nNo URL match")
            result_3 = reg3.findall(myfile)
            if result_3:
                print("\nPhone number mathes: ")
                for result3 in result_3:
                    print(result3)
            else:
                print("\nNo phone number match")
            result_4 = reg4.findall(myfile)
            if result_4:
                print("\nTime matches: ")
                for result4 in result_4:
                    print(result4)
            else:
                print("\nNo time matches.")
            result_5 = reg5.findall(myfile)
            if result_5:
                print("\nCredit card number matches: ")
                for result5 in result_5:
                    print(result5)
            else:
                print("\nNo credit card number matches.")
            result_6 = reg6.findall(myfile)
            if result_6:
                print("\nHTML tag matches: ")
                for result6 in result_6:
                    print(result6)
            else:
                print("\nNo html tag match.")
            result_7 = reg7.findall(myfile)
            if result_7:
                print("\nCurrency matches: ")
                for result7 in result_7:
                    print(result7)
            else:
                print("\nNo currency matches.\n")
        elif choice == "4":
            exit()
        else:
            continue
match_finder()
    
