import ahocorasick


class Replacer(object):
    """Replacer to replace many string at onece

    Attribuets:
        automaton (ahocorasick.Automaton): Automaton object
    """
    def __init__(self, replacements={}):
        """Initialize automaton from dict

        Args:
            replacements (dict): Replacements dict to replace key to value
        """
        # type check
        if not isinstance(replacements, dict):
            raise ValueError(
                '`replacements` excpected type `dict`, but got type `{}`.'
                    .format(type(replacements).__name__)
            )

        # construct automaton
        self.automaton = ahocorasick.Automaton()
        for src, dst in replacements.items():
            self.automaton.add_word(src, (src, dst))

    def replace(self, content):
        """Replace str by dict at once

        Args:
            content (str): String for replace

        Returns:
            str: Result of replaced content
        """
        # type check
        if not isinstance(content, str):
            raise ValueError(
                '`content` excpected type `str`, but got type `{}`.'
                    .format(type(content).__name__)
            )

        # finalize automaton
        self.automaton.make_automaton()

        # do nothing if not finalized
        if self.automaton.kind != ahocorasick.AHOCORASICK:
            return content

        def _find_all():
            for end, (src, dst) in self.automaton.iter(content):
                start = end - len(src) + 1
                yield start, end, dst

        def _generator():
            cur = 0
            for start, end, dst in sorted(_find_all(), key=lambda x: (x[0], -x[1])):
                if start > cur:
                    yield content[cur:start]
                if start < cur or end < cur:
                    continue
                yield dst
                cur = end + 1
            yield content[cur:]

        return ''.join(_generator())
