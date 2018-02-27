# Copyright (c) 2017, Xiphos Systems Corp. All rights reserved.
#
# SPDX-License-Identifier: GPL-2.0


env__spl_skipped = True

env__sf_configs = (
    {
        'offset':  0x00000000,
        'speed': 10000000,
        'writeable': True,
    },
    {
        'offset':  0x00000000,
        'len':  0x00040000,
        'speed': [10000000, 100000000],
        'writeable': True,
    },
    {
        'offset':  0x00010000,
        'writeable': False,
    },
    {
        'offset':  0x00020000,
        'writeable': True,
    },
    {
        'offset':  0x00030000,
        'writeable': True,
    },
    {
        'offset':  0x00040000,
        'writeable': True,
    },
)
