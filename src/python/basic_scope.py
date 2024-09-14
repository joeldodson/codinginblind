subject:str = "world"
print(f"first: hello {subject}")


def get_subject() -> None:
    subject = input("enter a person, place, or thing: ")
    print(f"in function: hello {subject}")

get_subject()
print(f"last: hello {subject}")

