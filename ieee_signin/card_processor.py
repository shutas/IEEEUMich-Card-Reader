"""Card Processor Class for IEEE UMich Card Reader."""

# Written by Shuta Suzuki (shutas@umich.edu)

import smtplib
import datetime
import json
import gspread
from getpass import getpass
from oauth2client.service_account import ServiceAccountCredentials
from .config import SENDER_EMAIL, DESTINATION_EMAIL, CREDENTIALS_FILENAME, SHEET_FILENAME

class CardProcessor(object):
    """Card Processor Class."""

    def __init__(self):
        """Construct Card Processor Class."""
        self.event_name = ""
        self.sender_email = SENDER_EMAIL
        self.sender_password = ""
        self.destination_email = DESTINATION_EMAIL
        self.sheet = None
        self.uniqname_count_dict = {}
        self.registered_members_dict = {}

    def initialize(self):
        """Retrieve Email Credentials for Sending Email."""
        print("\n<=== Card Processor Started Execution ===>\n")

        # Load Database from Google Sheets
        print("Loading Database... ")
        self.open_sheet()
        self.construct_members_set()
        print("-> SUCCESS: Database Loaded\n")

        # Append Today's Date to Event Name
        self.event_name = input("Enter event name: ") + " " +\
            datetime.datetime.today().strftime('(%m/%d/%Y)')

    def send_email(self):
        """Send the Result via Email."""
        # Print Newline for Aesthetics
        print()

        # Set Up SMTP Server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()

        # Authenticate User
        authenticated = False

        while not authenticated:
            # Get Password from User Input
            self.sender_password = getpass("Enter password for " +
                                           self.sender_email + ": ")

            # Check if Password is Correct
            try:
                server.login(self.sender_email, self.sender_password)
                authenticated = True
                print()
            # If Password is Incorrect
            except smtplib.SMTPAuthenticationError:
                print("-> FAIL: Password incorrect\n")

        # Get Destination Email
        destination_email = input("Enter email destination address " +
                                  "(if not specified, " +
                                  "it will send to " + DESTINATION_EMAIL +
                                  "): ")

        # Update Destination Email if Necessary
        if destination_email:
            self.destination_email = destination_email

        # Create Email Message
        message_content = ""

        for uniqname, count in self.user_dict.items():
            message_content += uniqname + " " + str(count) + "\n"

        message = '\r\n'.join(['To: %s' % self.destination_email,
                               'From: %s' % self.sender_email,
                               'Subject: %s' % self.event_name,
                               '', message_content])

        # Start Sending Email
        print("\nSending Email...")

        # Check if Email was Sent Successfully
        try:
            server.sendmail(self.sender_email,
                            [self.destination_email],
                            message)
            print("-> SUCCESS: Email sent to " + self.destination_email + "\n")
        # If Sending Failed for Some Reason
        except smtplib.SMTPException:
            print("-> FAIL: Email was NOT sent\n")

        # Terminate SMTP Server
        server.quit()

    def process_mcard(self, input_data):
        """Parse MCard Data and Add to Spreadsheet."""
        # Sanitize Input Data
        uniqname = input_data.lower()

        # Update User Dictionary
        if uniqname in self.user_dict:
            self.user_dict[uniqname] += 1
        else:
            self.user_dict[uniqname] = 1

        # Print Newline for Aesthetics
        print()

    def open_sheet(self):
        """Open Google Sheet."""
        # Specify Scope
        scope = ['https://spreadsheets.google.com/feeds',
                 'https://www.googleapis.com/auth/drive']

        # Retrieve Credentials from JSON
        credentials = \
        ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILENAME,
                                                         scope)

        # Authenticate Credentials
        google_credentials = gspread.authorize(credentials)

        # Open Sheet
        self.sheet = google_credentials.open(SHEET_FILENAME).sheet1

    def construct_members_set(self):
        """Construct Set of Registered Members."""
        # Retrieve List of Registered Uniqnames and Values
        registered_uniqname_list = self.sheet.col_values(1)
        registered_value_list = self.sheet.col_values(2)

        # Assert Properties of Retrieved Data
        assert(registered_uniqname_list[0] == "uniqname")
        assert(registered_value_list[0] == "value")

        # Load Registered Uniqnames to Card Processor
        num_registered_members = len(registered_uniqname_list) - 1

        for i in range(num_registered_members):
            self.registered_members_dict[registered_value_list[i + 1]] = registered_uniqname_list[i + 1]

    def terminate(self):
        """Terminate Card Processor."""
        # Print Newline for Aesthetics
        print()
        
        # Ask for Confirmation
        while True:

            input_data = input("Are you sure you want to terminate the " +
                               "program WITHOUT saving data? (y/n): ")

            # If Termination is Requested
            if input_data.lower() == "y" or input_data.lower() == "yes":
                print()
                return True

            # If Termination is NOT Requested
            elif input_data.lower() == "n" or input_data.lower() == "no":
                print()
                return False

            # If Input is Unrecognized
            else:
                print("Error: Please select (y)es or (n)o.\n")
