def get_fastest_speed(times):
    max_speed = 0
    segment_n = -1
    segments = [320, 280, 350, 300, 250]
    for i, (segment, time) in enumerate(zip(segments, times)):
        speed = segment / time
        if speed > max_speed:
            max_speed = speed
            segment_n = i + 1
    print(max_speed, segment_n)
    return f"The luger's fastest speed was {max_speed:.2f} m/s on segment {segment_n}."
