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


def task():
    """
    Request user to choose from two different tasks.
    1st task is to register a new employee
    2nd task is record an employees sick absence
    """
    print("To record new staff details, please select '1'")
    print("For staff attendance records, please select '2' \n")

    choice = int(input("Please make your selection: \n"))
    if choice == 1:
        print("Place holder to run: new_staff function")
    elif choice == 2:
        print("Place holder to run: attendance_records function")
    else:
        print("To record new staff details, please select '1' and press 'ENTER")
        print("For staff attendance records, please select '2' and press 'ENTER' \n")


task()
