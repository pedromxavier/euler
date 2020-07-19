import math
import os


from search import binary_search

class Sieve:

    _LIMIT = 10_000_000

    ## Primes before 256 = 2 ** 8
    _PRIME = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251]
    ## Sieve before 256
    _SIEVE = [False, False, True, True, False, True, False, True, True, True, False, True, True, True, False, False, False, True, False, True, False, False, False, True, False, False, False, False, False, True, False, True, False, False, False, False, False, True, False, False, False, True, False, True, False, False, False, True, False, False, False, False, False, True, False, False, False, False, False, True, False, True, False, False, False, False, False, True, False, False, False, True, False, True, False, False, False, False, False, True, False, False, False, True, False, False, False, False, False, True, False, False, False, False, False, False, False, True, False, False, False, True, False, True, False, False, False, True, False, True, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, True, False, False, False, False, False, True, False, True, False, False, False, False, False, False, False, False, False, True, False, True, False, False, False, False, False, True, False, False, False, False, False, True, False, False, False, True, False, False, False, False, False, True, False, False, False, False, False, True, False, True, False, False, False, False, False, False, False, False, False, True, False, True, False, False, False, True, False, True, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, True, False, True, False, False, False, True, False, False, False, False, False, True, False, True, False, False, False, False, False, False, False, False, False, True, False, False, False, False]

    fname = 'sieve'

    def __init__(self, limit=256):
        self.limit = max(256, self._next_byte(limit)) ## 256 ** (ceil(log8(limit)))
        self.sieve = self.load_sieve(self.limit)
        self.prime = self.load_prime(self.sieve, self.limit)

    def __enter__(self, *args, **kwargs):
        return self

    def __exit__(self, *args, **kwargs):
        self.save_sieve()
        self.save_prime()
        return None

    @staticmethod
    def prime_range(start: int, stop: int):
        """ primes in 30 n ± 1, 30 n ± 7, 30 n ± 11, 30 n ± 13
        """
        if start <= 15:
        for n in range((start + 13) // 30, stop):
            for m in (1, 7, 11, 13):
                yield 30 * n - m
                yield 30 * n + m

    def save_sieve(self):
        fname = f"{self.fname}.dat"
        byte_array = self.encode_bool(self.sieve)
        with open(fname, 'wb') as file:
            return file.write(byte_array)
    
    def save_prime(self):
        nbytes = 0
        byte_array = self.encode(self.prime)
        for log in range(len(byte_array)):
            fname = f"{self.fname}-{log}.dat"
            with open(fname, 'wb') as file:
                nbytes += file.write(byte_array[log])
        return nbytes

    def __iter__(self):
        for log in range(self.bytelog(self.limit, math.ceil)):
            yield from self.prime[log]

    def __contains__(self, x: int):
        """ Primality test
        """
        if x <= 1:
            return False
        if x >= self.limit:
            self._set_limit(x)
        return binary_search(x, self.prime[self.bytelog(x)]) is not None

    def _set_limit(self, x: int):
        if x > self._LIMIT: raise OverflowError(f"{x} is above operational limit {self._LIMIT}.")
        self.save_sieve()
        self.save_prime()
        self.limit = max(256, x)
        self.sieve = self.load_sieve(self.limit)
        self.prime = self.load_prime(self.sieve, self.limit)

    @classmethod
    def _next_byte(cls, x: int):
        return 1 << (cls.bytelog(x, math.ceil) << 3)

    @classmethod
    def _last_true(cls, y: list):
        i = len(y) - 1
        while i >= 0:
            if y[i]:
                return i
            i -= 1
        return None

    @classmethod
    def load_sieve(cls, limit: int=255):
        fname = f"{cls.fname}.dat"
        if os.path.exists(fname):
            with open(fname, 'rb') as file:
                sieve = cls.decode_bool(file.read())
            last_true = cls._last_true(sieve)
            sieve = sieve + [True] * max(limit - len(sieve), 0)
        else:
            last_true = 256
            sieve = cls._SIEVE + [True] * max(limit - 256, 0)
        sieve = cls.run_sieve(sieve, last_true, cls._next_byte(max(limit, last_true)))
        return sieve
        
    @classmethod
    def run_sieve(cls, sieve: list, start: int, limit: int):
        test_limit = math.ceil(math.sqrt(limit))			
        for i in range(start, test_limit):
            for j in range(start, test_limit):
                # n = 4*i^2 + j^2
                n = 4*i*i + j*j
                if n <= limit and (n % 12 == 1 or n % 12 == 5):				
                    sieve[i] = not sieve[i]

                    # n = 3*i^2 + j^2
                    n = 3*i*i + j*j
                    if n <= limit and n % 12 == 7:				
                        sieve[i] = not sieve[i]				

                    # n = 3*i^2 - j^2
                    n = 3*i*i - j*j
                    if n <= limit and i > j and n % 12 == 11:					
                        sieve[i] = not sieve[i]				

        for i in range(max(5, start), test_limit):			
            if sieve[i]:
                k = i * i
                for j in range(k, limit, k):
                    try:
                        sieve[j] = False
                    except:
                        print(len(sieve), limit)
                        raise
        return sieve

    @classmethod
    def load_prime(cls, sieve: list, limit: int=256):
        if limit <= 256:
            return [cls._PRIME]

        prime_array = []
        for log in range(cls.bytelog(limit, math.ceil)):
            fname = f"{cls.fname}-{log}.dat"
            if os.path.exists(fname):
                with open(fname, 'rb') as file:
                    array = file.read()
            else:
                prime_array = cls.decode(prime_array)
                break
            prime_array.append(array)
        else:
            prime_array = cls.decode(prime_array)

        while log < cls.bytelog(limit, math.ceil):
            prime_array.append([x for x in range(1 << (log << 3) + 1, limit, 2) if sieve[x]])
            log += 1
        return prime_array
        
    @property
    def test_limit(self):
        if self.test_limit is None:
            self.test_limit = int(math.ceil(math.sqrt(self.limit)))
        return self.test_limit
    
    @staticmethod
    def bytelog(x: int, func: callable=None):
        if func is None:
            return math.log(x, 256)
        else:
            return func(math.log(x, 256))

    @classmethod
    def _load(cls, log: int, data: bytes):
        with open(f"{cls.fname}-{log}.dat", 'rb') as file:
            return file.read()
    
    @classmethod
    def _dump(cls, log: int, data: bytes):
        with open(f"{cls.fname}-{log}.dat", 'wb') as file:
            return file.write(data)

    @classmethod
    def encode_bool(cls, bool_array: (list, bool)) -> bytes:
        nbytes = cls.bytelog(len(bool_array), func=math.ceil)
        nbytes = 1 if nbytes == 0 else nbytes
        bool_array = bool_array + [True] * ((nbytes << 3) - len(bool_array))
        return bytes((sum((bool_array[(i << 3) + j] << j) for j in range(8)) for i in range(nbytes)))

    @classmethod
    def decode_bool(cls, byte_array: bytes) -> (list, bool):        
        return [bool((byte >> j) % 2) for byte in byte_array for j in range(8)]

    @staticmethod
    def encode(prime_array: (list, list)) -> (list, bytes):
        size = 1
        byte_array = []
        for log_array in prime_array:
            array = []
            for p in log_array:
                for _ in range(size):
                    array.append(p % 0b1_0000_0000)
                    p >>= 8
            byte_array.append(array)
            size += 1
        return [bytes(array) for array in byte_array]

    @staticmethod
    def decode(byte_array: (list, bytes)) -> (list, list):
        size = 1
        buffer = 0b0
        prime_array = []
        counter = 0
        for array in byte_array:
            prime_array.append([])
            for byte in array:
                buffer |= (byte << (counter << 3))
                counter += 1
                if counter == size:
                    prime_array[-1].append(buffer)
                    buffer = 0b0
                    counter = 0
            size += 1
        return prime_array        
            
if __name__ == '__main__':
    with Sieve(10_000) as sieve:
        print(sieve)