#!/usr/bin/env python
import string
from hashlib import sha256

import yaml
from ordered_set import OrderedSet as _set

from starname.dir import database_path

__all__ = ("Starname",)


class Starname:
    def __init__(self, component_file=database_path("components.yaml")):
        with open(component_file) as f:
            components = yaml.safe_load(f)

        self.initial_consonants = list(
            _set(string.ascii_lowercase) - _set("aeiou")
            # remove those easily confused with others
            - _set("qxc")
            # add some crunchy clusters
            | _set(sum(components["initials"], []))
        )

        self.final_consonants = list(
            _set(string.ascii_lowercase) - _set("aeiou")
            # remove the confusables
            - _set("qxcsj")
            # crunchy clusters
            | _set(sum(components["finals"], []))
        )

        self.vowels = list(_set(sum(components["vowels"], [])))

    def clean(self, designation: str) -> str:
        """Cleans a star designation to remove variable elements like spacing and capitalization.
        Increases consistency of the name to be generated."""
        cleaned_designation = ""
        for char in designation:
            if char in string.ascii_letters or char in string.digits:
                cleaned_designation += char
        return cleaned_designation.lower()

    def generate(self, designation: str) -> str:
        clean_designation: str = self.clean(designation)
        seed = int(sha256(clean_designation.encode("utf-8")).hexdigest(), 16)
        name = self.generate_word(seed)
        return name.title()

    def generate_word(
        self, seed: int, vowel_consonant_repeats=3, start_vowel=False, end_vowel=False
    ) -> str:
        """Returns a random consonant-(vowel-consonant)*wc pseudo-word."""
        if not start_vowel:
            letter_list = [self.initial_consonants]
        else:
            letter_list = []
        for i in range(vowel_consonant_repeats):
            letter_list.extend([self.vowels, self.final_consonants])
        if end_vowel:
            letter_list.pop()

        key = seed
        result: str = ""
        for s in letter_list:
            index = key % len(s)
            key = key // len(s)
            result += s[index]
        return result


def console_main():
    import argparse

    parser = argparse.ArgumentParser(
        description="Generate a star name from that unpronouncable designation!"
    )
    parser.add_argument(
        "designation", type=str, nargs="?", help="The existing star designation."
    )

    args = parser.parse_args()

    print(Starname().generate(args.designation))


if __name__ == "__main__":
    console_main()
