# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *

class Tintin(AutotoolsPackage):
    """TinTin++ (aka tt++) is a free Mud client for Android, iOS, Linux, Mac OS
    X and Windows."""

    homepage = "https://tintin.mudhalla.net"
    url      = "https://downloads.sf.net/tintin/tintin-2.02.12.tar.gz"

    maintainers = ['dlkuehn',]

    version('2.02.12', sha256='b6f9fd4f2c1e7cdc8cff4172d7a80014961b0394380ced9182209dc34d781a00')

    depends_on('zlib')
    depends_on('pcre')
    depends_on('gnutls')

    configure_directory = 'src'

