import webbrowser


GIF_URL = "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExZmV2NDZ6Mm1nNzQ3dndscDlza2J6bmFraTYyMGZucnZmdndvcHQyZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/pAHAgWYYjWIE9DNLcC/giphy.gif"


def main():
    '''
    Ask the user to be your valentine until they say 'yes'
    '''
    while True:
        answer = ask_valentine()
        if answer == "yes":
            show_meme()
            break
        elif answer == "no":
            think_again()
        else:
            remind_valid_input()



def ask_valentine() -> str:
    """
    Ask the valentine question and return a standardized answer.
    
    :return: str
    :rtype: str
    """
    response = input("Would you be my valentine? yes/no")
    return standardize(response)


def standardize(answer: str) -> str:
    """
    standardize the answer by lowercasing and stripping spaces.
    
    :param answer: the user input for the valentine question
    :type answer: str
    :return: Description
    :rtype: str
    """
    return answer.lower().strip()


def show_meme():
    """
    Show a happy response and a gif when user says yes.
    """
    print("YAYYYYY!!! 🥳💖")
    print("Opening happy cats for you 😺")
    webbrowser.open(GIF_URL)

def think_again() -> None:
    print("🤨 Think again!")

def remind_valid_input() -> None:
    print("⚠️  Please only enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()