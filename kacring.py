import random
import matplotlib.pyplot as plt
import sys

class KacRing(object):
    size = 0
    gate_locs = []
    charges = []

    def __init__(self, num_sites, num_gates):
        self.size = num_sites
        self.gate_locs = random.sample(xrange(num_sites), num_gates)
        for i in xrange(self.size):
            self.charges.append(Charge(self, i))        

    def exists_gate_at(self, pos):
        #dfasdf profile this. repeated linear lookups bad
        return pos in self.gate_locs
    
    def step(self):
        # Would be great to use "map(rotate, charges)" somehow
        for i in self.charges:
            i.rotate()

    def net_charge(self):
        return 1.0 * sum(i.spin for i in self.charges) / len(self.charges)

class Charge(object):
    spin = 0 # Initialize to +1/-1 for up and down
    loc = 0 # Location on the Kac Ring
    kacring = None

    def __init__(self, kacring, loc):
        self.spin = 1 # random.choice([-1, 1])
        self.kacring = kacring
        self.loc = loc
    
    def rotate(self):
        self.loc = (self.loc + 1) % self.kacring.size
        if self.kacring.exists_gate_at(self.loc):
            self.flip()

    def flip(self):
        self.spin *= -1

def kac_graph(size, gates):
    kr = KacRing(size, gates)
    results = []

    # If gates is even, it deterministically repeats every "size"
    # amount of steps. If odd, every 2*size. Displaying 2*size number
    # of steps is redundant for the even case. 
    if gates % 2 == 1:
        step_limit = 2*size
    else:
        step_limit = size

    time = 0
    while (time < step_limit):
        results.append(kr.net_charge())
        kr.step()
        time += 1
    plt.plot(xrange(2*size), results)
    plt.show()

if __name__ == "__main__":
    kac_graph(1000, 67)
