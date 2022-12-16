from collections import Counter
import random
import string

from starname import Starname

generator = Starname()
generator2 = Starname()


def test_generate_is_consistent(rep=50, name="WD 1054-226"):
    sample = "Qaiocoptoops"
    for _ in range(rep):
        assert generator2.generate(name) == sample


def test_generate_is_various_sequential(rep=1_000_000):
    samples: Counter = Counter()
    for i in range(rep):
        samples.update([generator.generate(str(i))])
    assert len(samples) >= rep * 0.999999


def test_generate_is_various_random(rep=1_000_000, sample_length=14):
    samples: Counter = Counter()
    for _ in range(rep):
        s = "".join(
            [random.choice(string.ascii_lowercase) for _ in range(sample_length)]
        )
        samples.update([generator.generate(s)])
    assert len(samples) >= rep * 0.999999
