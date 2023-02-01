import re
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]
CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("hr_space")


def welcome():
    """
    Request input: username spaces or special characters.
    Change username, first letter to capital. With loop, until input is valid.
    """
    print(
        "Please enter a valid user name which only consists of letters. "
        "Spaces and special characters are not allowed...\n"
    )
    while True:
        username = input("Enter your username: \n")

        if username.isalpha() is False:
            print("Please input a user name which only consists of letters.")
            print("Spaces and special characters are not allowed...\n")
        else:
            print("Welcome " + username.capitalize())
            break
    return False


def choose_task():
    """
    Request user to choose from two different tasks, by entering 1 or 2.
    1 is to register a new employee. 2 is to record an employees sick absence.
    The loop will repeatedly ask the user to select 1 or 2.
    """
    while True:
        print("New staff records, select '1', then 'ENTER'")
        print("For staff attendance records, select '2', then 'ENTER' \n")

        choice = int(input("Please make your selection: \n"))
        if choice == 1:
            get_valid_fullname()
            break
        elif choice == 2:
            print("Place holder to run: attendance_records function")
            return False


def get_valid_fullname():
    """
    Request user input, new staff's full name. No special characters.
    Return with Capital letter start to each word.
    RegEx code for this function borrowed from this site:
    https://bobbyhadz.com/blog/python-input-only-letters-allowed
    """
    print("Input new staff's full name, seperated by spaces.")
    print("Names must only consist of letters and spaces.")
    print("Special characters are not allowed...\n")

    name = ""
    while True:
        name = input("Please input new staff's full: ")
        if not re.match(r"^[a-zA-Z\s]+$", name):
            print("Special charater are not allowed.")
            continue
        return name.title()
    return False


welcome()
choose_task()
get_valid_fullname()
