# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Raylib(CMakePackage):
    """raylib is a simple and easy-to-use library to enjoy videogames programming"""

    homepage = "https://www.raylib.com/"
    url      = "https://github.com/raysan5/raylib/archive/refs/tags/4.0.0.tar.gz"
    git      = "https://github.com/raysan5/raylib.git"

    maintainers = ['mdorier']

    version('master', branch='master')
    version('4.0.0', sha256='11f6087dc7bedf9efb3f69c0c872f637e421d914e5ecea99bbe7781f173dc38c')

    """
    def install(self, spec, prefix):
        import glob
        with working_dir('src'):
            make('PLATFORM=PLATFORM_DESKTOP')
            for d in ['include', 'lib']:
                mkdirp(prefix+'/'+d)
            headers = glob.glob('*.h')+glob.glob('extras/*.h')
            for header in headers:
                install(header, prefix+'/include')
            install('libraylib.a', prefix+'/lib')
        mkdirp(prefix+'/share')
        install_tree('cmake', prefix+'/share')
    """
