# CCC 2012
# Problem J1: Speed fines are not fine!

speedLimit = int(input())
yourSpeed = int(input())

if yourSpeed >speedLimit and yourSpeed < speedLimit+21:
    print("You are speeding and your fine is $100.")
elif yourSpeed >speedLimit+20 and yourSpeed < speedLimit+31:
    print("You are speeding and your fine is $270.")
elif yourSpeed > speedLimit+30:
    print("You are speeding and your fine is $500.")
else:
    print("Congratulations, you are within the speed limit!")