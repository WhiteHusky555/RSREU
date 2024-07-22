import random
def find_longest_abd_sequence(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()
    abd_line_max=''
    i_max=0
    abd_lines=[[] for i in range(len(lines))]
    for i in range(len(lines)):
        abd_line=''
        abd_line_count=0
        for j in range(len(lines[i])):
            if j==len(lines[i])-1:
                if len(abd_line_max)<len(abd_line):
                    i_max=i
            if (abd_line=='' and lines[i][j]=='A') or (abd_line_count>0 and abd_line[abd_line_count-1]=='D' and lines[i][j]=='A'):
                abd_line=abd_line+lines[i][j]
                abd_line_count+=1
            elif (abd_line_count>0 and abd_line[abd_line_count-1]=='A' and lines[i][j]=='B'):
                abd_line = abd_line + lines[i][j]
                abd_line_count += 1
            elif (abd_line_count>0 and abd_line[abd_line_count-1]=='B' and lines[i][j]=='D'):
                abd_line = abd_line + lines[i][j]
                abd_line_count += 1
            else:
                abd_lines[i]+=[len(abd_line)]
                abd_line=''
                abd_line_count=0
    for l in range(len(abd_lines)):
        abd_lines[l] = [max(abd_lines[l])]
    return max(abd_lines)[0], abd_lines.index(max(abd_lines))+1

with open('Data.txt', 'w') as f:
    for i in range(10):
        f.write(''.join(random.choice('ABCD') for _ in range(10)) + '\n')
dlina, stroka=find_longest_abd_sequence('Data.txt')
print(f'Длина строчки типа ABD: {dlina}\nНомер строки: {stroka}')