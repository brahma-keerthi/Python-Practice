class Booking:
    @staticmethod
    def __init__():
        print("....Welcome to ticket booking....")
        print("Available seats => ")

    list = ["Available Seats>> ", 1,2,3,4,5,6,7,8,9,10]
    seatsBooked = ["Booked seats appear here>> "]

    seat = 0
    def seatsAvailableSeatNum(self):
        print(self.list)

    def bookSeats(self):
        print("Already booked seats>> ", self.seatsBooked)
        self.seat = int(input("Select seat num>> "))

    def seatup(self):
        self.seatsBooked.append(self.seat)
        self.list.remove(self.seat)


    def printDetails(self):
        print("-------------!!!!!TICKET!!!!!------------")
        print("Seat Num>>  ", self.seatsBooked)
        print(f"Total >> 10 * {len(self.seatsBooked)-1} = {10*(len(self.seatsBooked)-1)}")
        print(".........................................")

while(True):
    booking = Booking()
    booking.seatsAvailableSeatNum()
    booking.bookSeats()
    booking.seatup()

    i = int(input("Do you want to book again??\nPress 0 to stop>> "))

    if(i==0):
        booking.printDetails()
        exit(0)