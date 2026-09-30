days = int(input('Enter the number of days in a week?'))
hours = int(input('Enter the number of hours ?'))
minutes = int(input('Enter the number of minutes?'))
seconds = int(input('Enter the number of seconds?'))

total_seconds = seconds + (minutes * 60) + (hours * 3600) + (days * 86400)
print(f"Total seconds in a week: {total_seconds}")