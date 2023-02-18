from heapq import heappush, heappop
from random import choice, choices
from dataclasses import dataclass


@dataclass
class Congratulation:
    id: int
    val: str
    frequency: int


class CongratulationsCreator:
    def __init__(self, congratulation_groups):
        self.congratulations_groups = {}
        id = 1
        for group_name, congratulations in congratulation_groups.items():
            self.congratulations_groups[group_name] = []
            for c in congratulations:
                self.congratulations_groups[group_name].append(Congratulation(id, c, 0))
                id += 1
        self.history = []

    @staticmethod
    def get_min_congratulations(cong_group):
        min_num = min([i.frequency for i in cong_group])
        return filter(lambda cong: cong.frequency == min_num, cong_group)

    def get_triad(self, deep=0):
        if deep > 10 ** 5:
            raise Exception("unable to generate a new triad")
        # print('self.congratulations_groups.values()', list(self.congratulations_groups.values()))
        group_names = choices(list(self.congratulations_groups.keys()), k=3)

        if len(set(group_names)) < 3:
            return self.get_triad(deep=deep+1)

        # print(group_names)
        triad = [choice(list(self.get_min_congratulations(self.congratulations_groups[group_name]))) for group_name in group_names]
        if self.triad_hash(*triad) in self.history:
            return self.not_used_triads(deep=deep+1)

        for congratulation in triad:
            congratulation.frequency += 1

        return triad

    @staticmethod
    def triad_hash(c1 : Congratulation, c2 : Congratulation, c3 : Congratulation, M=1000):
        a = sorted([c1, c2, c3], key=lambda c: c.frequency)
        return ((a[0].id * M + a[1].id) * M) + a[2].id

    # @staticmethod
    # def triad_frequency(c1: Congratulation, c2: Congratulation, c3: Congratulation):
    #     return c1.frequency + c2.frequency + c3.frequency


if __name__ == '__main__':

    c = CongratulationsCreator(["1", "2", "3", "4", "5", "6"])
    # not_used_triads = c.not_used_triads()
    for i in range(200):
        t = c.get_triad()
        print(t[0].val, t[1].val, t[2].val)
