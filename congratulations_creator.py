from heapq import heappush, heappop
from random import choice
from dataclasses import dataclass


@dataclass
class Congratulation:
    id: int
    val: str
    frequency: int


class CongratulationsCreator:
    def __init__(self, congratulations):
        self.congratulations = [Congratulation(i, congratulations[i], 0) for i in range(len(congratulations))]
        self.history = []

    def get_min_congratulations(self):
        min_num = min([i.frequency for i in self.congratulations])
        return filter(lambda cong: cong.frequency == min_num, self.congratulations)

    def not_used_triads(self):
        for c1 in self.congratulations:
            for c2 in self.congratulations:
                for c3 in self.congratulations:
                    if self.triad_hash(c1, c2, c3) not in self.history:
                        if len({c1.id, c2.id, c3.id}) == 3:
                            yield c1, c2, c3

    def get_triad(self):
        not_used_triads_list = list(self.not_used_triads())

        if len(not_used_triads_list) == 0:
            raise Exception("all triads have been used")

        min_frequency = min([CongratulationsCreator.triad_frequency(*t) for t in not_used_triads_list])
        not_used_min_triads = list(filter(lambda t: CongratulationsCreator.triad_frequency(*t) == min_frequency, not_used_triads_list))

        triad = choice(not_used_min_triads)
        self.history.append(self.triad_hash(*triad))

        for i in range(3):
            triad[i].frequency += 1

        return triad

    def triad_hash(self, c1 : Congratulation, c2 : Congratulation, c3 : Congratulation):
        a = sorted([c1, c2, c3], key=lambda c: c.frequency)
        sz = len(self.congratulations)
        return ((a[0].id * sz + a[1].id) * sz) + a[2].id

    @staticmethod
    def triad_frequency(c1: Congratulation, c2: Congratulation, c3: Congratulation):
        return c1.frequency + c2.frequency + c3.frequency


if __name__ == '__main__':

    c = CongratulationsCreator(["1", "2", "3", "4", "5", "6"])
    # not_used_triads = c.not_used_triads()
    for i in range(200):
        t = c.get_triad()
        print(t[0].val, t[1].val, t[2].val)
