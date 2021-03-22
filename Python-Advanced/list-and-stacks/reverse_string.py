def reverse_string(text):
    st = []
    for ch in text:
        st.append(ch)

    reversed_text_characters = []

    while st:
        ch = st.pop()
        reversed_text_characters.append(ch)

    return "".join(reversed_text_characters)

print(reverse_string(input()))