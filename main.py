from art import logo

#Addition
def add(n1,n2):
  return n1+n2

#Subtract
def sub(n1,n2):
  return n1-n2

#Multiplication
def multiply(n1,n2):
  return n1*n2

#Division
def divide(n1,n2):
  return n1/n2

operations ={
  "+" : add,
  "-" : sub,
  "*" : multiply,
  "/" : divide
}
def calculator():
  print(logo)
  num1 = float(input("What is your first Number: "))
  for opt in operations:
    print(opt)
  calculation_finished = True
  while calculation_finished:
    operation_symbol = input("Pick an operation from the above: ")
    num2 = float(input("What is your next Number: "))
    calculate = operations[operation_symbol]
    result = calculate(num1,num2)
    cal_finished = input( f"Type 'y' to continue calculationg with {result}, or type 'n' to start new calculation : ")
    if cal_finished == 'y':
      num1 = result
    else :
      calculation_finished = False     
  print(f"Result : {result}")
  calculator()

calculator()
