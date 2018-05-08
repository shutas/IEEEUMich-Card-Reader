"""Driver Program for IEEE UMich Card Reader."""

# Written by Shuta Suzuki (shutas@umich.edu)


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

    print("<=== Card Processor Finished Execution ===>\n")


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
