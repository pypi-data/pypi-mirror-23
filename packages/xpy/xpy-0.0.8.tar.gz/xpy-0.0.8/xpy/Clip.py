#!/usr/bin/env python3

import os
import readline
from functools import reduce
import inspect

class Clip(object):
    @staticmethod
    def paste():
        result = None
        with os.popen('xsel -o') as infile:
            result = infile.read()
        return result

    @staticmethod
    def copy(buf):
        with os.popen('xsel -i', 'w') as outfile:
            outfile.write(buf)
        
    @staticmethod
    def show():
        print(Clip.paste().rstrip('\n'))

    @staticmethod
    def compile():
        result = None
        source = Clip.paste()
        if source:
            # fix indent
            lines = source.split('\n')
            lines = list(filter(lambda line: len(line.strip()) > 0, lines))
            min_indent = reduce(lambda i0, i1: min(i0, i1), map(lambda line: len(line) - len(line.lstrip('\t ')), lines))
            source = '\n'.join((map(lambda line: line[min_indent:], lines)))

            code = compile(source, __name__, 'exec')
            result = (source, code)
        return result

    @staticmethod
    def copy_from_history(line_count):
        l = readline.get_current_history_length()
        lines = []
        for i in range(max(l - line_count, 0), l):
            line = readline.get_history_item(i)
            lines.append(line)
        buf = '\n'.join(lines)
        Clip.copy(buf)

    @staticmethod
    def paste_into_history(is_split_lines = False):
        code = Clip.compile()
        if code is not None:
            (source, code) = code
            print(source)
            if is_split_lines:
                for line in source.split('\n'):
                    readline.add_history(line)
            else:
                readline.add_history(source)

    @staticmethod
    def run():
        """Run the contents of the clipboard within the caller's frame."""
        code = Clip.compile()
        if code is not None:
            (source, code) = code
            print(source)
            frame = inspect.currentframe()
            frame = frame.f_back
            exec(code, frame.f_globals, frame.f_locals)
        else:
            print('failed to compile')


