def correct_polish_letters(s):
    return s.translate(str.maketrans("ąćęłńóśźż", "acelnoszz"))


print(correct_polish_letters("Jędrzej Błądziński"))


def correct_polish_letters(st):
    l = "ąćęłńóśźż"
    lt = "acelnoszz"
    for i in range(len(l)):
        st = st.replace(l[i], lt[i])
    return st


print(correct_polish_letters("Jędrzej Błądziński"))
