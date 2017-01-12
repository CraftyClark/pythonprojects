"""
Show how to use exceptions to save a high score for a game.

Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/
"""

def main():
    """ Main program is here. """
    # Default high score
    high_score = 0

    # Try to read the high score from a file
    try:
        high_score_file = open("high_score.txt", "r")
        high_score = int(high_score_file.read())
        high_score_file.close()
        print("The high score is", high_score)
    except IOError:
        # Error reading file, no high score
        print("There is no high score yet.")
    except ValueError:
        # There's a file there, but we don't understand the number.
        print("I'm confused. Starting with no high score.")

    # Get the score from the current game
    current_score = 0
    try:
        # Ask the user for his/her score
        current_score = int(input("What is your score? "))
    except ValueError:
        # Error, can't turn what they typed into a number
        print("I don't understand what you typed.")

    # See if we have a new high score
    if current_score > high_score:
        print("Yea! New high score!")

        # We do! Save to disk
        try:
            # Write the file to disk
            high_score_file = open("high_score.txt", "w")
            high_score_file.write(str(current_score))
            high_score_file.close()
        except IOError:
            # Hm, can't write it.
            print("Too bad I couldn't save it.")
    else:
        print("Better luck next time.")

# Call the main function, start up the game
if __name__ == "__main__":
    main()
