# -*- coding=utf-8 -*-
# Copyied from pip's vendoring process
# see https://github.com/pypa/pip/blob/95bcf8c5f6394298035a7332c441868f3b0169f4/tasks/__init__.py
import invoke

from . import vendoring
from . import news
from . import release

ns = invoke.Collection(vendoring, news, release)
