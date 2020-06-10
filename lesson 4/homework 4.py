text1 = input('Введіть те що буде вставленне в другий рядок рядок: ')
text2 = input('Введіть куди буде вставлено перший рядок: ')
text2_cnt = text2[round(len(text2)/2)-1]
split_text2 = text2.index(text2_cnt)
print(f"{text2[:split_text2]} {text1} {text2[split_text2:]}")
