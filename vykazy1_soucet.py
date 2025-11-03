# Zkontroluje zdali je radek validni
def is_valid(line) -> bool:
    if len(line) < 5:
        return False
    if line[0] != line[-2]:
        return False
    return True

# Prevede cas ve formatu H:mm:ss do sekund
def time2sec(time) -> int:
    time = time.split(":")
    sec_time = int(time[2]) + int(time[1])*60 + int(time[0])*3600
    return sec_time

# Prevede celkovy cas v sekundach na format H:mm:ss
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

    result = str(hours) + ":" + str(minutes) + ":" + str(seconds)
    return result

total_time = 0
current_line = input().split()

# Nacte radku ze vstupu a rovnou zkontroluje jestli je validni a pokud ano pripocita cas
while current_line != ["."]:
    if is_valid(current_line):
        total_time += time2sec(current_line[-1]) - time2sec(current_line[1])
    current_line = input().split()
print("celkem:",sec2time(total_time))