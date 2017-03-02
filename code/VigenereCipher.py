class VigenereCipher (object):  
    def __init__(self, key, alphabet):
        self.k = key.decode('utf-8')
        self.a = alphabet.decode('utf-8')
        
    def encode(self, str):
        str = str.decode('utf-8')
        ekey = self.size_key(len(str))
        encoded = ''.join([self.shift_char(letter, self.a.index(ekey[i])) for i, letter in enumerate(str)])
        return encoded.encode('utf-8')
        
    def decode(self, str):
        str = str.decode('utf-8')
        ekey = self.size_key(len(str))
        decoded = ''.join([self.shift_char(letter, -1 * self.a.index(ekey[i])) for i,letter in enumerate(str)])
        return decoded.encode('utf-8')
        
    def shift_char(self, letter, shift):
        if letter in self.a: return self.a[(self.a.index(letter) + shift) % len(self.a)]
        else: return letter
    
    def size_key(self, length):
        key = self.k
        if len(key) > length:
            key = key[:length]
        ind = 0
        while len(key) < length:
            key += self.k[ind]
            ind = (ind + 1) % len(self.k)
        return key


# example usage
abc = "abcdefghijklmnopqrstuvwxyz";
key = "password"
c = VigenereCipher(key, abc);

c.encode('testing yo')