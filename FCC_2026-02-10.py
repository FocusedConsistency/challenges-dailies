def get_relative_results(results):
    relative_times = ["0"]
    winner = str_to_seconds(results[0])

    for r in results[1:]:
        time_behind_s = str_to_seconds(r) - winner
        relative_times.append(seconds_to_str(time_behind_s))
    return relative_times

def str_to_seconds(string):
    h, m, s = map(int, string.split(":"))
    return 3600 * h + 60 * m + s

def seconds_to_str(time):
    return f"+{time // 60}:{time % 60:02d}"
