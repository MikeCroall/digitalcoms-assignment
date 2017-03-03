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

# Actual RSA - not just repeated_squaring

def encrypt(M, exponent, mod):
    return repeated_squaring(M, exponent, mod)


def decrypt(C, private_d, mod):
    return repeated_squaring(C, private_d, mod)


# A encrypts M as C = M^e mod n.
# B can decrypt using C^d = M^ed = M mod n.

# In the questions below, the bank’s RSA public key is (76282747,65537); your own
# public key is (9436709, 1676267) and your private key is d=3497603.
bank_public_mod = 76282747
bank_public_e = 65537

my_public_mod = 9436709
my_public_e = 1676267
my_private_d = 3497603

print("Question 5")
print("{}\n".format(encrypt(654733, bank_public_e, bank_public_mod)))

print("Question 6")
print("{}\n".format(decrypt(1684446, my_private_d, my_public_mod)))

print("Question 7")
q7_m = 337722
q7_s = decrypt(q7_m, my_private_d, my_public_mod)
q7_c_s = encrypt(q7_s, bank_public_e, bank_public_mod)
q7_c_m = encrypt(q7_m, bank_public_e, bank_public_mod)
# test signature validity
q7_message_from_sig = encrypt(q7_s, my_public_e, my_public_mod)
if q7_m == q7_message_from_sig:
    print("Signature matches, cannot test encrypted signature or message as don't have bank private d")
    print("\tS:{}\n\tC_s:{}\n\tC_m:{}\n".format(q7_s, q7_c_s, q7_c_m))
else:
    raise AssertionError("Message and signature un-done do not match")

