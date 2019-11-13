# -*- coding: utf-8 -*-

"""NeuroMMSig Knowledge."""

import os

from bel_repository import BELMetadata, BELRepository

__all__ = ['repository', 'metadata', 'main']

HERE = os.path.dirname(__file__)
VERSION = '0.0.2-dev'

metadata = BELMetadata(
    name='NeuroMMSig',
    version=VERSION,
    description='',
    authors='',
    contact='',
)
repository = BELRepository(HERE, metadata=metadata)
main = repository.build_cli()
