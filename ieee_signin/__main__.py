"""Driver Program for IEEE UMich Card Reader."""

# Written by Shuta Suzuki (shutas@umich.edu)


from .card_processor import CardProcessor

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
        input_data = input("Swipe MCard or enter command: ").strip()

        # "done" Command Selected
        if input_data.lower() == "done":
            master.send_email()
            break

        # "help" Command Selected
        elif input_data.lower() == "help":
            print_menu()

        # "terminate" Command Selected
        elif input_data.lower() == "terminate":
            if master.terminate():
                break

        # MCard Swiped
        elif len(input_data) > 65:
            master.process_mcard(input_data)

        # Unrecognized Command
        else:
            print("-> ERROR: Unrecognized command - Please try again.\n")

    print("<=== Card Processor Finished Execution ===>\n")


def print_menu():
    """Print Main Menu."""
    print("""
                         Welcome to
        +-+-+-+-+ +-+-+-+-+-+ +-+-+-+-+ +-+-+-+-+-+-+
        |I|E|E|E| |U|M|I|C|H| |C|A|R|D| |R|E|A|D|E|R|
        +-+-+-+-+ +-+-+-+-+-+ +-+-+-+-+ +-+-+-+-+-+-+

        <<< Scan your MCard to begin registration >>>

        Commands:
            done        Save data and exit program
            help        Prints main menu
            terminate   Terminate program without saving data
        """)


if __name__ == "__main__":
    main()
