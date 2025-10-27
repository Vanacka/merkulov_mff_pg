def is_valid(line) -> bool:
    if line[0] != line[-2]:
        return False
    if len(line) < 5:
        return False
    return True

def time2sec(time) -> int:
    time = time.split(":")
    sec_time = int(time[2]) + int(time[1])*60 + int(time[0])*3600
    return sec_time

def sec2time(time):
    return


total_time = 0
current_line = input().split()

while current_line != ["."]:
    if is_valid(current_line):
        total_time += time2sec(current_line[-1]) - time2sec(current_line[1])
    current_line = input().split()
print("celkem:",sec2time(total_time))