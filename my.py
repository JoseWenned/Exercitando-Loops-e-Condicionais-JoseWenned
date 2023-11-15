# Function 1

def corresponding(input_string):
    stack = []

    unmatched = ''

    for i, char in enumerate(input_string):
        if char == "(":
            stack.append(i)
        elif char == ")":
            if stack:
                stack.pop()
            else:
                unmatched += char

    unmatched += "".join(["(" for index in stack])

    return unmatched

# Exemplos de uso:


result1 = corresponding("()()")
print(result1)  # Saída: ''

result2 = corresponding("()))")
print(result2)  # Saída: '))'

result3 = corresponding(")))(((((")
print(result3)  # Saída: '(('

# ---- // ----


def remove_more_than_two_repetitions(text):
    if len(text) < 3:
        return text


result = "text"[0]

count = 1

for i, in range(1, len("text")):
    if "text"[1] == "text"[i - 1]:
        count += 1
    else:
        count = 1

    if count <= 2:
        result += "text"[i]

return result

# Exemplo

text = "Ollloco meuuuu, taaa peegaando fogoo biiiiichooo"
text = remove_more_than_two_repetitions(text)
print(text)>'Olloco meuu, taa peegaando fogoo biichoo'