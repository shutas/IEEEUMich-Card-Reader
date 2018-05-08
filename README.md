# IEEEUMich-Card-Reader
Creator: Shuta Suzuki (shutas@umich.edu)

Python program for signing in members at events for IEEE Student Branch at the University of Michigan - Ann Arbor.  

# Prerequisites
- Python 3.x
- Linux/MacOS

# Installation
Navigate to the project root directory (IEEEUMich-Card-Reader) in your terminal.

If you don't have pip, install by:  
`sudo easy_install pip`

If you already have pip installed, update pip if necessary:  
`pip install --upgrade pip`

Install the package using:  
`pip install -e .`

# Usage
Run the program:  
`ieee-signin`

After you started the program,
- Swipe as many MCards. The reader will keep track of all uniqnames and swipe counts per event.
- Type `done` to save and send data. The program will safely exit once it successfully sends the email.
- Type `help` to show the instructions/commands to operate the program.

# Uninstallation
In your terminal, run:  
`pip uninstall -y ieee-signin`
