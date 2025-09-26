print("WELCOME TO THE TIP CALCULATOR!")
bill=float(input("WHAT IS YOUR TOTAL BILL? $"))
tip=int(input("HOW MUCH PERCENT TIP DO YOU WANT TO GIVE?0,10,15,20,30"))
added_amount=bill*(tip/100)+bill
people=int(input("WITHIN HOW MANY PEOPLE DOU YOU WANT TO SPLIT THE BILL?"))
total_bill=added_amount/people
print("THE AMOUNT YOU HAVE TO PAY IS:")
print(round(total_bill,2))
