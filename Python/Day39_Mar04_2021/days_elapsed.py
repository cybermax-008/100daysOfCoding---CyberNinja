"""
PROBLEM:
Given a start date and end date, find the number of days between them.
Using datetime module in python.
"""
from datetime import date, datetime
# YYYY-MM-DD is iso format
start_date = date.fromisoformat(input("Start date:"))
end_date = date.fromisoformat(input("End date"))
if start_date >end_date:
    print("Invlaid input!")
elapsed_days = end_date -start_date
print(elapsed_days.days)


