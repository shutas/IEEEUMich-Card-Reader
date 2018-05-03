#!/usr/bin/bash

"""Card Reader for UMich IEEE."""

# Written by Shuta Suzuki (shutas@umich.edu)

import smtplib
import datetime
from email.mime.text import MIMEText

class CardProcessor(object):
    """Card Processor Class."""
    def __init__(self):
        self.event_name = ""
        self.sender_email = "ieee.umich.donotreply@gmail.com"
        self.sender_password = ""
        self.destination_email = "IEEE.VPComm@umich.edu"
        self.user_dict = {}


    def initialize(self):
        """Retrieve Email Credentials for Sending Email."""

        print("\n<=== Card Reader Started Execution ===>\n")

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
            self.sender_password = input("Enter password for ieee.umich.donotreply@gmail.com: ")
        
            # Check if Password is Correct
            try:
                server.login(self.sender_email, self.sender_password)
                authenticated = True
                print()
            # If Password is Incorrect
            except smtplib.SMTPAuthenticationError:
                print("-> FAIL: Password incorrect\n")

        # Get Destination Email
        destination_email = input("Enter email destination address (if not specified, it will send to VPComm): ")

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
            server.sendmail(self.sender_email, [self.destination_email], message)
            print ('-> SUCCESS: Email sent to ' + self.destination_email + "\n")
        # If Sending Failed for Some Reason
        except:
            print ('-> FAIL: Email was NOT sent\n')

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


def main():
    """Driver for Card Reader."""
    # Initialize CardProcessor Master
    master = CardProcessor()

    # Initialize Event Info
    master.initialize()

    # Print Menu to Start
    print_menu()

    while True:

        # Retrieve Input
        input_data = input("Swipe MCard or Enter Command: ").strip()

        # "done" Option Selected
        if input_data.lower() == "done":
            master.send_email()
            break

        # "help" Option Selected
        elif input_data.lower() == "help":
            print_menu()

        # MCard Swiped
        else:
            master.process_mcard(input_data)

    print("<=== Card Reader Finished Execution ===>\n")


def print_menu():
    """Print Main Menu."""
    print("""
                         Welcome to
        +-+-+-+-+ +-+-+-+-+-+ +-+-+-+-+ +-+-+-+-+-+-+
        |I|E|E|E| |U|M|I|C|H| |C|A|R|D| |R|E|A|D|E|R|
        +-+-+-+-+ +-+-+-+-+-+ +-+-+-+-+ +-+-+-+-+-+-+

        <<< Scan your MCard to begin registration >>>

        Options:
            done    Save data and exit program
            help    Prints main menu
        """)


if __name__ == "__main__":
    main()
