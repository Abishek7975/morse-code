import pandas as pd

morse_df = pd.read_csv('morse.csv')

morse_code = ''

code = (morse_df.loc[morse_df['letter']=='L', 'code'])
print(code)
print(code.iloc[0])
user_string = str(input("Input the string you want to encode: "))


for s in user_string.upper():
    print(s)
    if s == ' ':
        morse_code += " "*7
        continue
    code = morse_df.loc[morse_df['letter'] == s, 'code']
    morse_code += str(code.iloc[0])
    morse_code += " "*3



print(morse_code)
