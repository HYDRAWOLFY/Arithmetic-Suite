import math 

def ci(p,r,n,t):
    a = p * (1 + r/(n*100)) ** (n * t)
    return round((a),2)

print("<----------------COMPOUND-INTEREST----------------->")

p = float(input("Enter The 'PRINCIPAL' or The Initial Amount: "))
r = float(input("Enter The Annual Rate of Interest: "))
n = float(input("Enter The Number of Times the Interest is Compounded Annually: "))
t = float(input("For How Much Time is the Money Invested or Borrowed?:"))
unit = input("Enter Unit of Currency: ")

a = ci(p,r,n,t)

print(f"The Interest Should be: {a} {unit}")
