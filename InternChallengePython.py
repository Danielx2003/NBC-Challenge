# GolfNow intern challenge Python instructions.

# The code below has several bugs and is ripe for improvement.
# NOTE: Do not change the 'Booking' class - its implementation is not part of the challenge.

# Hint 1: The structure of the 'players' variable can definitely be improved!
# Hint 2: Some of the logic involved in passing a player's details to the Booking class is faulty.

from datetime import datetime


class Booking:
    def __init__(self, tee_date, tee_time):
        # This will create a booking instance (do not change this!)
        pass

    def add_player(self, name, rate):
        # This will add a player to booking (do not change this!)
        print("Player added " + name + "! Rate: " + str(rate))

    def store(self):
        # This will store the booking (do not change this!)
        print("Booking stored!")


# Anything under this line can be changed!
class Program:
    def Main():

        ENTRY_FEE = 20

        players = [
            {"name": "David", "member": True},
            {"name": "Andy", "member": False},
            {"name": "Jim", "member": False},
            {"name": "Laura", "member": True},
            {"name": "Niamh", "member": True},
            {"name": "Ryan", "member": False},
        ]

        # sets booking time and date for this session
        date = datetime.strptime("2024-02-01", "%Y-%m-%d").date()
        time = datetime.strptime("10:30", "%H:%M").time()
        booking = Booking(date, time)

        for player in players:
            # free for members, otherwise 20.
            booking.add_player(player["name"], ENTRY_FEE * (not player["member"]))

        booking.store()


Program.Main()
