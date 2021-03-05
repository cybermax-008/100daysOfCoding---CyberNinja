"""
PROBLEM:
Given a start date and no of days before or after, find the end date.
"""

from datetime import date, timedelta

start_date = date.fromisoformat(input("Start date:"))
days = int(input("No of days forward ot backward from the start days:"))

end_date = start_date + timedelta(days=days)
print(end_date)