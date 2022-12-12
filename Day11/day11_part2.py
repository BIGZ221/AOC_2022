from operator import mul
import re

with open("input.txt") as f:
    data = f.read().split("\n\n")

class Monkey:
    id_regex = re.compile(r"Monkey (?P<id>\d+)")
    items_regex = re.compile(r"Starting items: (?P<inv>(?:\d+,?\s)+)")
    operation_regex = re.compile(r"Operation: new = (?P<operation>old [+\-*/] [^\s]+)")
    test_denominator_regex = re.compile(r"Test: [^\d]*(?P<denominator>\d+)")
    destination_monkey_regex = re.compile(r"(?P<case>true|false): [^\d]*(?P<destination>\d+)")

    inspections = 0

    def __init__(self, inv_description) -> None:
        self.parse(inv_description)

    def parse(self, inv_description):
        items_match = self.items_regex.search(inv_description).groupdict()["inv"]
        self.id = self.id_regex.search(inv_description).groupdict()["id"]
        self.items = list(map(int, items_match.replace(",", "").split()))
        self.operation = self.operation_regex.search(inv_description).groupdict()["operation"]
        self.test_denominator = int(self.test_denominator_regex.search(inv_description).groupdict()["denominator"])
        self.destination_monkeys = dict(self.destination_monkey_regex.findall(inv_description))

    def inspect(self):
        self.inspections += 1
        self.items[0] = eval(self.operation.replace("old", str(self.items[0]))) % self.denom

    def test(self):
        self.inspect()
        if self.items[0] % self.test_denominator == 0:
            return self.destination_monkeys["true"]
        else:
            return self.destination_monkeys["false"]

    def throw_to(self, monkey: 'Monkey'):
        item = self.items.pop(0)
        monkey.catch(item)

    def catch(self, item):
        self.items.append(item)

monkeys = {}

for monkey_description in data:
    m = Monkey(monkey_description)
    monkeys[m.id] = m

div_product = 1
for monkey in monkeys.values():
    div_product *= monkey.test_denominator

for monkey in monkeys.values():
    monkey.denom = div_product

monkey: Monkey
for round in range(10_000):
    for monkey in monkeys.values():
        while len(monkey.items) > 0:
            destination_monkey = monkeys[monkey.test()]
            monkey.throw_to(destination_monkey)

print(mul(*sorted(map(lambda m: m.inspections, monkeys.values()), reverse=True)[:2]))
