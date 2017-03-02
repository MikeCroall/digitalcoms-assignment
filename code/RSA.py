def repeated_squaring(n, exponent, mod, print_steps=False):

    # NOTE assignment spec says must not use any BigIntegers or Power functions etc, just multiplication, modulo, etc.

    powers = [1]
    results = [n % mod]

    while powers[-1] <= exponent / 2:
        if print_steps:
            print("{}^{} = {} mod {}".format(n, powers[-1], results[-1], mod))
        powers.append(2 * powers[-1])
        results.append((results[-1] * results[-1]) % mod)
    if print_steps:
        print("{}^{} = {} mod {}".format(n, powers[-1], results[-1], mod))

    ret = results[-1]
    remaining_power = exponent - powers[-1]
    done_power = powers[-1]
    if print_steps:
        print("\nStarting with {0}^{1} mod {2}".format(n, done_power, mod))
    while remaining_power > 0:
        i = len(powers) - 1
        while powers[i] + done_power > exponent:
            i -= 1
        next_power = powers[i]
        remaining_power -= next_power
        done_power += next_power
        if print_steps:
            print("Multiplying by {0}^{1}, to reach {0}^{2} mod {3}".format(n, next_power, done_power, mod))
        index = powers.index(next_power)
        ret = (ret * results[index]) % mod

    return ret


# print("Question 4\n")
# print("Calculated 17^54 mod 139 = {}\n\n".format(repeated_squaring(17, 54, 139, True)))
# print("Calculated 2345^65531 mod 265189 = {}\n\n".format(repeated_squaring(2345, 65531, 265189, True)))
# print("Calculated 4733459^65537 mod 75968647 = {}\n\n".format(repeated_squaring(4733459, 65537, 75968647, True)))
