from datetime import datetime
import time, webbrowser

current_time = datetime.today() 
user_dt = input("Enter a date and time: ")
converted_user_input = datetime.strptime(user_dt, '%B %d, %Y %H%M')
time_until_alarm = converted_user_input - current_time
total_seconds = time_until_alarm.total_seconds()
time.sleep(total_seconds)
webbrowser.open_new("https://youtu.be/LdWbPJOrW4c")
