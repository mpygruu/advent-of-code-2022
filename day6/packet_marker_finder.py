def characters_before_start_of_packet(signal: str) -> int:
    for i in range(3, len(signal)):
        first, second, third, fourth = signal[i-3], signal[i-2], signal[i-1], signal[i]
        if __is_start_of_packet_marker(first, second, third, fourth):
            return i+1
    
    return None


def __is_start_of_packet_marker(s1,s2,s3,s4) -> bool:
    if(s1 == s2 or s1 == s3 or s1 == s4):
        return False
    if(s2 == s3 or s2 == s4):
        return False
    if(s3 == s4):
        return False
    
    return True