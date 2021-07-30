"""A suite of failing tests that demonstrate what diffs look like before and
after migrating unittest from `difflib.ndiff` to `difflib.unified_diff` for
better performance."""
import unittest
import random
from itertools import cycle
import string



class TestChanges(unittest.TestCase):

    maxDiff = None

    def test_short_comparison(self):
        self.assertEqual('foo', 'bar')

    def test_long_comparison(self):
        a = """\
Once upon a time,
there was a boy named Tim.
Here had some tiny knuckles
and in his pocket, a slim jim."""
        b = """\
Once upon an age,
there was a boy named Tim.
He had some wise old sages
who told him how to swim."""

        self.assertEqual(a, b)

    def test_short_sequence(self):
        self.assertSequenceEqual(['foo', 'bar'], ['buzz', 'bar'])

    def test_long_sequenece(self):
        choices = ('foo', 'bar', 'buzz', 'baz', 'biz') * 10
        a, b = [random.sample(choices, 50) for _ in range(2)]
        self.assertSequenceEqual(a, b)

    def test_small_dict(self):
        self.assertDictEqual({'foo': 1, 'bar': 2}, {'foo': 2, 'bar': 2})

    def test_large_dict(self):
        def random_dict():
            keys = tuple(string.printable)
            values = [i for i in range(100)]
            return {k: v for k, v in zip(keys, random.sample(values, 50))}
        self.assertDictEqual(random_dict(), random_dict())


if __name__ == '__main__':
    unittest.main()
