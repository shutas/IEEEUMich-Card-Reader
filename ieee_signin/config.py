"""IEEE UMich Card Reader Configuration."""

# Written by Shuta Suzuki (shutas@umich.edu)

import os

# Email Address of Sender
SENDER_EMAIL = "ieee.umich.donotreply@gmail.com"

# Destination Email Address
DESTINATION_EMAIL = "IEEE.VPComm@umich.edu"

# Credentials JSON Absolute Path
CREDENTIALS_FILENAME = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
    "ieee_signin", "credentials.json"
)

# Google Sheet Filename
SHEET_FILENAME = "IEEE Members Fall 2018"