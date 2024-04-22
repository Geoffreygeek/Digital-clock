##Digital Clock, by Geoffrey Geek###################
##Displays a digital clock of the current time with a seven-segment
##display. Press Ctrl-C to stop.
##Tags: tiny, artistic

import time

# This function displays the current time in digital format
def display_time():
    # Get the current time
    current_time = time.strftime("%H:%M:%S")

    # Split the time into hours, minutes, and seconds
    hours, minutes, seconds = map(int, current_time.split(":"))

    # Print the time in digital format
    print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")

# This function runs the digital clock
def main():
    # Loop indefinitely
    while True:
        # Display the current time
        display_time()

        # Wait for 1 second
        time.sleep(1)

        # Clear the screen
        print("\033c")

# Run the main function
if __name__ == "__main__":
    main()