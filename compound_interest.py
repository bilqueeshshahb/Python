import  math

principal = float(input("enter the principal amount: "))
rate = float (input("enter rate of interest: "))
time = float(input("enter time in years: "))

total_amount = principal + (math.pow((1+rate/100),time))

compound_interest = total_amount - principal

print(f"Principal Amount: {principal:.2f}")
print(f" Interest Rate: {rate}%")
print(f" Time Period: {time} years")
print(f" Total Amount after{time} years: {total_amount:.2f}")
print(f"Total Compound Interest: {compound_interest:.2f}")
      
      
