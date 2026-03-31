def alarm_check(alarm_time, wake_time):
    def get_min(time):
        h, m = map(int, time.split(":"))
        return h * 60 + m
    
    alarm_min = get_min(alarm_time)
    wake_min = get_min(wake_time)
    
    if wake_min < alarm_min:
        return "early"
    if wake_min > alarm_min + 10:
        return "late"
    return "on time"
