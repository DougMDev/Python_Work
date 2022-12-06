def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "Sorry, you didn't type that correctly :("
    return f"Hello there, {f_name.title()} {l_name.title()}"

formatted_str = format_name(input("What is your First Name? "), input("What is your Last Name? "))
print(formatted_str)