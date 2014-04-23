import random
import matplotlib.pyplot as plt
import sys

class KacRing(object):
    self.size = 0
    self.NUM_GATES = 0
    self.gate_locs = []
    self.charges = []

    def __init__(self, num_sites, num_gates):
        self.size = num_sites
        self.NUM_GATES = num_gates
        self.gate_locs = random.sample(xrange(num_sites), num_gates)
        for i in xrange(self.size):
            self.charges.append(Charge(self, i))        

    def exists_gate_at(self, pos):
        #dfasdf profile this. repeated linear lookups bad
        return pos in self.gate_locs
    
    def step(self):
        # Would be great to use "map(rotate, charges)" somehow
        for i in charges:
            i.rotate()

    def net_charge(self):
        return 1.0 * sum(i.spin for i in charges) / len(charges)

class Charge(object):
    self.spin = 0 # Initialize to +1/-1 for up and down
    self.loc = 0 # Location on the Kac Ring
    self.kacring = None

    def __init__(self, kacring, loc):
        self.spin = random.choice([-1, 1])
        self.kacring = kacring
        self.loc = loc
    
    def rotate(self):
        self.loc = self.loc + 1 % self.kacring.size
        if self.kacring.exists_gate_at(self.loc):
            flip()

    def flip(self):
        self.spin *= -1

def kac_graph(size, gates):
    kr = KacRing(size, gates)
    results = []
    while (time <= 2*size):
        results.append(kr.net_charge())
        time += 1
    plt.scatter(xrange(2*size), results)
    plt.show()

if __name__ == "__main__":
    kac_graph(10, 4)