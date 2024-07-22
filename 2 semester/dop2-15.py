import random
import sympy
def solve_equation(file_name_input, file_name_output):
    with open(file_name_input, 'r') as input_file:
        lines = input_file.readlines()
    with open(file_name_output, 'w') as output_file:
        for i in range(len(lines)):
            x = sympy.Symbol('x')
            equation=(lines[i])[:-3]
            x=(sympy.solve(equation, x))
            if 'I' in str(x):
                x='0 решений'
                output_file.write(str(x)+'\n')
            else:
                x = [float(i) for i in x]
                output_file.write(str(len(x))+' решений: ' +str(x)+'\n')

with open('Data.txt', 'w') as f:
    for i in range(10):
        f.write(str(random.randint(-999, 999)) + '*x**2+' + str(random.randint(-999, 999)) + '*x+' + str(random.randint(-999, 999)) + '=0' + '\n')
    f.write('x**2+2*x+1=0'+ '\n')
solve_equation('Data.txt', 'Answers.txt')
with open('Answers.txt', 'r') as f:
    lines=f.readlines()
    for i in range(len(lines)):
        print(lines[i])