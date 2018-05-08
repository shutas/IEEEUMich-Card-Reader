"""Card Processor Class for IEEE UMich Card Reader."""

# Written by Shuta Suzuki (shutas@umich.edu)

import smtplib
import datetime


class CardProcessor(object):
    """Card Processor Class."""

    def __init__(self):
        """Construct Card Processor Class."""
        self.event_name = ""
        self.sender_email = "ieee.umich.donotreply@gmail.com"
        self.sender_password = ""
        self.destination_email = "IEEE.VPComm@umich.edu"
        self.user_dict = {}

    def initialize(self):
        """Retrieve Email Credentials for Sending Email."""
        print("\n<=== Card Processor Started Execution ===>\n")

        # TODO: Load Database

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
            self.sender_password = input("Enter password for " +
                                         "ieee.umich.donotreply@gmail.com: ")

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
                                  "it will send to VPComm): ")

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
