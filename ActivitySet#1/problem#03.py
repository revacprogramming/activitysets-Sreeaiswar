# Variables, Expressions & Statements

#hrs = float(input("Enter hours? "))

hrs = input("Enter Hours:")
rate=input("Enter rate:")
gpay=float(hrs)*float(rate)
print("Pay:",str(gpay))



def compute(hrs,rate):
  earn=hrs*rate
  return earn
def output(earn):
  print(earn)
def main():
  hrs = float(input("Enter hours? "))
  rate=float(input("enter Rate :"))
  earn=compute(hrs,rate)
  output(earn)
main()