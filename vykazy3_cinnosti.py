# Checks if the line is valid
def is_valid(line) -> bool:
    if len(line) < 5:
        return False
    if line[0] != line[-2]:
        return False
    return True

# Converts tome in format H:mm:ss to seconds
def time2sec(time) -> int:
    time = time.split(":")
    sec_time = int(time[2]) + int(time[1])*60 + int(time[0])*3600
    return sec_time

# Converts time from seconds to format H:mm:ss
def sec2time(time):
    seconds = time % 60
    if seconds < 10:
        seconds = "0" + str(seconds)
    time = time // 60
    minutes = time % 60
    if minutes < 10:
        minutes = "0" + str(minutes)
    time = time // 60
    hours = time

    result = f"{hours}:{minutes}:{seconds}"
    return result

# Sticks month and year from line date together like this: mm/yyyy
def month_year_join(date):
    date = date.split(".")
    month = date[1]
    year = date[2]
    month_year = f"{month}/{year}"
    return month_year


total_time = 0
current_line = input().split()
activity_time = {}

while current_line != ["."]:
    if is_valid(current_line):
        activity_name = ""
        for i in range(2, len(current_line) - 2):
            activity_name = activity_name + " " + current_line[i]
        time = time2sec(current_line[-1]) - time2sec(current_line[1])
        # get(key, Value) returns key value if key is in dictionary if not it returns Value
        activity_time[activity_name] = activity_time.get(activity_name, 0) + time
        total_time += time
    current_line = input().split()
# Sorts dictionary by value
activity_time = sorted(activity_time.items(), key=lambda x: x[1], reverse=True)
# Prints max 10 values and keys
for activity_name, time in activity_time[:10]:
    print(f"{sec2time(time)} {activity_name}")