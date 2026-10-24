def classify_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("sides must be positive")
    if a >= b + c or b >= a + c or c >= a + b:
        raise ValueError("sides break the triangle inequality")

    if a == b == c:
        return "equilateral"
    if a == b or b == c or a == c:
        return "isosceles"
    return "scalene"


def course_result(coursework, final, attendance):
    if not 0 <= coursework <= 40:
        raise ValueError("coursework must be between 0 and 40")
    if not 0 <= final <= 60:
        raise ValueError("final must be between 0 and 60")
    if not 0 <= attendance <= 100:
        raise ValueError("attendance must be between 0 and 100")

    if attendance < 75:
        return "barred"
    if final < 18:
        return "fail"
    if coursework + final < 60:
        return "fail"
    return "pass"


def fizzbuzz(n):
    result = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result


def is_prime(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def primes_below(n):
    result = []
    for i in range(2, n):
        if is_prime(i):
            result.append(i)
    return result


def first_repeated(values):
    for i in range(len(values)):
        for j in range(i):
            if values[j] == values[i]:
                return values[i]
    return None


def count_pairs(n):
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            count += 1
    return count

def count_pairs(n):
    return n * (n - 1) // 2


def calculator(command):
    parts = command.split()
    try:
        match parts:
            case ["add", a, b]:
                return int(a) + int(b)
            case ["mul", a, b]:
                return int(a) * int(b)
            case ["neg", a]:
                return -int(a)
            case ["sum", *nums] if nums:
                return sum(int(x) for x in nums)
            case _:
                raise ValueError("unknown command")
    except ValueError:
        raise ValueError(f"bad command: {command!r}")


def parse_int(text, default=None):
    try:
        return int(text)
    except ValueError:
        return default


def stats(*numbers):
    if len(numbers) == 0:
        raise ValueError("stats needs at least one number")

    smallest = numbers[0]
    largest = numbers[0]
    total = 0

    for x in numbers:
        if x < smallest:
            smallest = x
        if x > largest:
            largest = x
        total += x

    return (smallest, largest, total / len(numbers))


def append_to(item, target=None):
    if target is None:
        target = []
    target.append(item)
    return target


def make_multiplier(k):
    def multiplier(x):
        return x * k
    return multiplier



def apply_n(f, x, n):
    result = x
    for _ in range(n):
        result = f(result)
    return result



    