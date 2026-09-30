total_seconds = int(input('Enter the total number of seconds: '))
days = total_seconds // 86400
hours = (total_seconds % 86400) // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60

print(f"D: {days}, H: {hours}, M: {minutes}, S: {seconds}")