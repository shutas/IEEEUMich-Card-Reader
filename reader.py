#!/usr/bin/bash

"""Card Reader for UMich IEEE."""

# Written by Shuta Suzuki (shutas@umich.edu)


def main():
    """Driver for Card Reader."""
    print_menu()

    while True:

        input_data = input()

        # "done" option selected
        if input_data.lower() == "done":
            save_and_send_spreadsheet()
            break

        # "help" option selected
        elif input_data.lower() == "help":
            print_menu()

        # MCard Swiped
        else:
            process_mcard(input_data)


def save_and_send_spreadsheet():
    """Save and Send Spreadsheet Data to Officers."""
    pass


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


def process_mcard(input_data):
    """Parse MCard Data and Add to Spreadsheet."""
    pass


if __name__ == "__main__":
    main()
