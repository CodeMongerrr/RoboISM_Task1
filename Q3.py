n1 = int(input("N1"))
n2 = int(input("N2"))
op = input("Operator")
def calc(n1, op, n2):
    if op == '+':
        print(n1+n2)
    if op == '-':
        print(n1-n2)
    if op == '/':
        print(float(n1/n2))
    if op == '.':
        print(n1*n2)

calc(n1, op, n2)