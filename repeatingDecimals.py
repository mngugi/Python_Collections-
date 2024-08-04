def find_repeating_length(n):
    remainder = 1 % n
    remainders = {}
    position = 0

    while remainder not in remainders:
        remainders[remainder] = position
        remainder = (remainder * 10) % n
        position += 1

        if remainder == 0:
            return 0  # Terminates, so no repeating portion

    return position - remainders[remainder]

length_1_19 = find_repeating_length(19)
length_1_21 = find_repeating_length(21)
length_1_29 = find_repeating_length(29)

length_1_19, length_1_21, length_1_29
