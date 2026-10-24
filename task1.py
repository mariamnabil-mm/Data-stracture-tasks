def seconds_to_hms(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    remaining_seconds = seconds % 60
    return f"{hours}h {minutes}m {remaining_seconds}s"


def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


def split_evenly(total, people):
    per_person = total / people
    remainder = total % people
    return per_person, remainder


def initials(full_name):
    name_parts = full_name.split()
    result = ""
    i = 0
    while i < len(name_parts):
        result += name_parts[i][0].upper()
        i += 1
    return result


def is_palindrome_word(word):
    word = word.strip().lower()
    return word == word[::-1]


def mask_email(email):
    at_index = email.index("@")
    masked_email = email[0] + "*" * (at_index - 1) + email[at_index:]
    return masked_email


def middle(values):
    num_values = len(values)

    if num_values == 0:
        return None
    
    elif num_values % 2 == 1:
        middle_index = num_values // 2
        return values[middle_index]
    
    else:
        middle_index1 = (num_values // 2) - 1
        middle_index2 = num_values // 2
        return (values[middle_index1] + values[middle_index2]) / 2


def rotate_left(values, k):
        if len(values) == 0:
            return []
        k = k % len(values)
        return values[k:] + values[:k]


def fib_list(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fib_sequence = [0, 1]
    for i in range(2, n):
        next_fib = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_fib)

    return fib_sequence


def collatz_steps(n):
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        steps += 1
    
    return steps
    