# NOTE
#
# The code for the VigenereCipher class was adapted from my own VignereCipher code
# originally used for a challenge on CodeWars.com


class VigenereCipher(object):
    def __init__(self, key):
        self.k = key
        self.a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def update_key(self, new_key):
        self.k = new_key

    def encode(self, inp):
        return ''.join(
            [self.shift_char(letter, self.a.index(self.size_key(len(inp))[i])) for i, letter in enumerate(inp)])

    def decode(self, inp):
        return ''.join(
            [self.shift_char(letter, -1 * self.a.index(self.size_key(len(inp))[i])) for i, letter in enumerate(inp)])

    def shift_char(self, letter, shift):
        # if letter in self.a:
        return self.a[(self.a.index(letter) + shift) % len(self.a)]
        # else:
        #     return letter

    def size_key(self, length):
        sized_key = self.k
        ind = 0
        if len(sized_key) > length:
            sized_key = sized_key[:length]
        while len(sized_key) < length:
            sized_key += self.k[ind]
            ind = (ind + 1) % len(self.k)
        return sized_key


# Given test case
q0_key = "YOHOHO"
q0_m = "BLACKBEARDISSAILINGTOJAMAICA"
q0_c = "ZZHQRPCOYRPGQOPZPBEHVXHAYWJO"
c = VigenereCipher(q0_key)
if q0_c == c.encode(q0_m):
    print("Test case successful\n\tk: {}\n\tm: {}\n\tc: {}".format(q0_key, q0_m, q0_c))
else:
    raise AssertionError("q0 (given test case) failed")

# Question 1
q1_key = "PIECESOFEIGHT"
q1_m = "LETSSAILFORTHESPANISHMAIN"
c.update_key(q1_key)
q1_c = c.encode(q1_m)
print("\n\nQuestion 1 encode m -> c\n\tk: {}\n\tm: {}\n\tc: {}".format(q1_key, q1_m, q1_c))

# Question 2
q2_key = "GOLDCOINS"
q2_c = "ZVTVKGVBLNWYJVCLBOOHSSKFIGWYOEDNZ"
c.update_key(q2_key)
q2_m = c.decode(q2_c)
print("\n\nQuestion 2 decode c -> m\n\tk: {}\n\tm: {}\n\tc: {}".format(q2_key, q2_m, q2_c))

# Question 3
q3_c1 = "KPKWETQKAODLZMERBOCAPNEERINWHQYBUOQUWTXMKIIBLNISOQAFRQHFHBEYXUPDMIMHEJNURXYQCXMULOVEKKXZZQWUUIBVSLMDJYQGBEVBIXDSJVXVPMYAAZROGEBGWIEVHLADXKRUIUYZDNCJTTKXDCHKNWGDNCKQGCBZVZNJPOFDYWWYRDMKFHKXFMFRGLMKHRWHFRJVNSGAQJHNCBYGSCEOPDVRRPPFWLOGUSRHZRIIAKYGZBJVPPQLRMMFGFBXTSMBJFLBOAWBKCD"
q3_c2 = "IXYVAGYZLHMRCLAGUGXEQSMFXAZTHFCKNSGXINVHWDOOUPVUNYIZFMKYTOVKKEADYZPZGXWJFVSXGMXAZMHQTRPYGIXTESRVIGWWSLTHXIZIDPEVSSDRHIKKGDTYHWICSYTOIWPUBZNFVEZCHWWGHUAJBBXIJTGLRJHGLHXRNJANPNPZWZYCIPHPYOANIPHOBKKRPYJHVTTEHROJYQCDTRDOWUKGCEEPLVNZSRCMTOUYLHWNHXGHNMWJEMHCIOHKNIHXSOTMDRSCBQYZYNU"
q3_c3 = "YAGNKAIHHXBZDQPTWHMSHWINSAZDWTJXNRTWAISMEPXCAKFGSPINWPZTEAKMFOLSKKRYGHYGCELHQHCOUFFMBDWGHVUGYEWHJYOUDTJJJKLHYLPENAOOUKHOXIFSDSUNACTFCPGKLTAINMULRBNXBUMTCMYPAXLQDLAJMFPSDKEKEOKNRRHQPXDKXMHEPWJBINLDIZTOYPQCIAMBXLIJZDKQRVOFTNRQNGIYOOBSXKZEBHCLYNUTALHFXZVNZNFJZGOSBKCPLEKFOKIEWYX"
# Find Kb
c.update_key(q3_c1)
q3_kb = c.decode(q3_c2)
print("\n\nQuestion 3\n\tKb: {}".format(q3_kb))
# Check Kb encrypts c1 -> c2 (otherwise Kb is wrong)
c.update_key(q3_kb)
q3_c2_test = c.encode(q3_c1)
if q3_c2 == q3_c2_test:
    print("\tKb confirmed correct, decrypting c3 to get M...")
    c.update_key(q3_kb)
    q3_m = c.decode(q3_c3)
    print("\tM: {}".format(q3_m))
else:
    raise AssertionError("Kb was incorrectly calculated, question 3 aborted")