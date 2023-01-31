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
    Request user to input their name, without spaces or special characters.
    Change username to capitalize fir letter.
    """
    print("Please enter a user name which only consists of letters.")
    print("Spaces and special characters are not allowed...\n")

    username = input("Enter your username: \n")

    if username.isalpha() is False:
        print("Please enter a user name which only consists of letters.")
        print("Spaces and special characters are not allowed...\n")
    else:
        print(f"Welcome " + f"{username}\n".capitalize())


def choose_task():
    """
    Request user to choose from two different tasks, by entering 1 or 2.
    1 is to register a new employee. 2 is to record an employees sick absence.
    The loop will repeatedly ask the user to select 1 or 2.
    """
    while True:
        print("To record new staff details, please select '1' and press 'ENTER'")
        print("For staff attendance records, please select '2' and press 'ENTER' \n")

        choice = int(input("Please make your selection: \n"))
        if choice == 1:
            print("Place holder to run: new_staff function")
            break
        elif choice == 2:
            print("Place holder to run: attendance_records function")
            return False


welcome()
choose_task()
