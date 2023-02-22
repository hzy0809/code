#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/1/26 14:02
# @File    : structure.py
# @Software: PyCharm
"""
生成下项目目录脚本
"""
import importlib
from pathlib import Path
import os

default_head = """
# CODE   

---
> 笔记  

## PROJECT STRUCTURE   
   

---
"""


def display_criteria(p):
    if p.name.startswith('__') and p.name.endswith('__'):
        return False
    if p.name == 'venv':
        return False
    if p.name.startswith('.'):
        return False
    return True


class DisplayablePath(object):
    display_filename_prefix_middle = '├──'
    display_filename_prefix_last = '└──'
    display_parent_prefix_middle = '    '
    display_parent_prefix_last = '│   '

    def __init__(self, path, parent_path, is_last, md=False):
        self.path = Path(str(path))
        self.parent = parent_path
        self.is_last = is_last
        self.md = md
        if self.parent:
            self.depth = self.parent.depth + 1
        else:
            self.depth = 0

    @classmethod
    def make_tree(cls, root, parent=None, is_last=False, criteria=None, md=False):
        root = Path(str(root))
        criteria = criteria or cls._default_criteria

        displayable_root = cls(root, parent, is_last, md)
        yield displayable_root

        children = sorted(
            list(
                p for p in root.iterdir() if criteria(p)
            ),
            key=lambda s: (s.is_dir(), str(s).lower()))
        count = 1
        for path in children:
            is_last = count == len(children)
            if path.is_dir():
                yield from cls.make_tree(
                    path,
                    parent=displayable_root,
                    is_last=is_last,
                    criteria=criteria,
                    md=md
                )
            else:
                yield cls(path, displayable_root, is_last, md=md)
            count += 1

    @classmethod
    def _default_criteria(cls, p):
        return True

    @property
    def display_name(self):
        suffix = ''
        if self.path.is_dir():
            suffix = '/'
        body = self.display_doc or self.path.name or self.path.absolute().stem
        if self.md:
            body = f'[{body}]({self.path.as_posix()})'
        return body + suffix

    @property
    def display_doc(self):
        text = ''
        if self.path.is_dir():
            return text
        if self.path.name.endswith('.py'):
            p = self.path.absolute().relative_to(Path('.').absolute())
            module = str(p).replace('.py', '').replace('\\', '.')
            try:
                doc = importlib.import_module(module).__doc__
                if doc:
                    text = '{!s}'.format(doc.strip().split("\n")[0])
            except Exception as e:
                print(module, e)
        return text

    def displayable(self):
        if self.parent is None:
            return self.display_name + '  \n'

        _filename_prefix = (self.display_filename_prefix_last
                            if self.is_last
                            else self.display_filename_prefix_middle)

        parts = ['{!s} {:<70s}  \n'.format(
            _filename_prefix,
            self.display_name,
        )]

        parent = self.parent
        while parent and parent.parent is not None:
            parts.append(self.display_parent_prefix_middle
                         if parent.is_last
                         else self.display_parent_prefix_last)
            parent = parent.parent

        return ''.join(reversed(parts))


if __name__ == '__main__':
    from const import ProjectPath
    os.chdir(ProjectPath)
    paths = DisplayablePath.make_tree(Path('.'), criteria=display_criteria, md=True)
    with open(ProjectPath.joinpath('README.md'), 'w', encoding="utf8") as f:
        f.write(default_head)
        for path in paths:
            f.write(path.displayable())
