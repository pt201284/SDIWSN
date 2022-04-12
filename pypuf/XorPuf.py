from PUF import PUF
import random
import itertools
import time

class XorPUF:
    def __init__(self, bits, nr):
        self.bits = bits
        self.pufs = [ PUF(bits) for _ in range(nr) ]

    def get_response(self, challenge):
        response = challenge.copy()

        response_bits = []
        for puf in self.pufs:
            resp = puf.calculate_one(challenge).pop()
            response_bits.append(resp)
        
        result = 0
        for bit in response_bits:
            result ^= bit

        response.append(result)
        return response

    def calculate_responses(self):
        response = []
        
        counter = 0
        for seq in itertools.product("01", repeat=self.bits):
            challenge = [int(item) for item in seq]
            response.append(self.get_response(challenge))

        return response

    def calculate_responses_with_random_challenges(self, nr):
        response = []

        challenges = []
        for _ in range(nr):
            chal = []
            for _ in range(self.bits):
                chal.append(random.randint(0, 1))
            challenges.append(chal)
        
        for challenge in challenges:
            response.append(self.get_response(challenge))

        return response

i = 1
num = 500
summ = 0
while(i<=num):
    start = time.time()
    newp = XorPUF(5,random.randint(0,31))
    print((newp.calculate_responses()))
    end = time.time()
    e = (end-start)*1000
    summ = summ + e
    i += 1

print(summ/num)

