def characters_before_start_of_message(signal: str) -> int:
    for i in range(13, len(signal)):
        if __is_start_of_message(signal[i-13:i+1]):
            return i+1


def __is_start_of_message(signal_part: str) -> bool:
    signal_set = set([i for i in signal_part])
    return len(signal_set) == len(signal_part)
