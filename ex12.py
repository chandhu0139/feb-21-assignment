# Flight Ticket Booking System

# Prompt the user for their details
print("Welcome to the Flight Ticket Booking System!")
name = input("Please enter your full name: ")
departure_city = input("Enter the departure city: ")
destination_city = input("Enter the destination city: ")
departure_date = input("Enter the departure date (YYYY-MM-DD): ")
return_date = input("Enter the return date (YYYY-MM-DD): ")
seat_preference = input("Enter your seat preference (Window/Aisle): ")

# Display the booking confirmation using f-strings
print("\nThank you for booking with us! Here are your flight details:")
print(f"Name: {name}")
print(f"Departure City: {departure_city}")
print(f"Destination City: {destination_city}")
print(f"Departure Date: {departure_date}")
print(f"Return Date: {return_date}")
print(f"Seat Preference: {seat_preference}")

print("\nYour flight ticket has been successfully booked. Have a great journey!")r