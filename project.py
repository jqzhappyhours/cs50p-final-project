import webbrowser
import os

HTML_FILE_YES = 'yes.html'
HTML_FILE_NO = "index.html"


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
    Show a happy response and open the webpage when user says yes.
    """
    # Get the full path to yes.html
    file_path = os.path.abspath(HTML_FILE_YES)
    
    # Open the HTML file in the default browser
    webbrowser.open('file://' + file_path)
    

def think_again() -> None:
    
    # Get the full path to index.html
    file_path = os.path.abspath(HTML_FILE_NO)
    
    # Open the HTML file in the default browser
    webbrowser.open('file://' + file_path)

def remind_valid_input() -> None:
    print("⚠️  Please only enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()