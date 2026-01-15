def add_time(current_minutes: int, minutes_to_add: int, max_minutes: int) -> int:
    if minutes_to_add <= 0:
        raise ValueError

    else:
        new_total = current_minutes + minutes_to_add
        if new_total > max_minutes:
            return max_minutes
        else:
            return new_total
def convert_minutes(time_minutes: int) -> tuple[int, int]:
    hours = time_minutes // 60
    remaining_minutes = time_minutes % 60
    return hours, remaining_minutes
def format_time(hours: int, minutes: int) -> str:
    if hours == 0:
        return f"{minutes} minute(s)"
    elif minutes == 0:
        return f"{hours} hour(s)"
    else:
        return f"{hours} hour(s) {minutes} minute(s)"
