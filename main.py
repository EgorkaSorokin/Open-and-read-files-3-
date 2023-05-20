import os

text = {}
for i in range(1, 4):
    name = f'{i}.txt'
    with open(name, 'r', encoding='utf-8') as f:
        text[name] = [x for x in f.read().splitlines() if x]
 
with open('final_text.txt', 'w', encoding='utf-8') as file:
    for file_name, number_of_lines in sorted(text.items(), key=lambda x: len(x[-1])):
        file.write(file_name + '\n')
        file.write(str(len(number_of_lines)) + '\n')
        file.write('\n'.join(number_of_lines))
        file.write('\n')
