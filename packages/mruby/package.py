# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Mruby(Package):
    """mruby is the lightweight implementation of the Ruby language complying
    to (part of) the ISO standard. Its syntax is Ruby 2.x compatible."""

    homepage = "https://mruby.org/"
    url      = "https://github.com/mruby/mruby/archive/refs/tags/3.0.0.tar.gz"

    maintainers = ['mdorier']

    version('3.0.0', sha256='95b798cdd931ef29d388e2b0b267cba4dc469e8722c37d4ef8ee5248bc9075b0')
    version('2.1.2', sha256='4dc0017e36d15e81dc85953afb2a643ba2571574748db0d8ede002cefbba053b')
    version('2.1.1', sha256='bb27397ee9cb7e0ddf4ff51caf5b0a193d636b7a3c52399684c8c383b41c362a')
    version('2.1.0', sha256='d6733742a07e553c52ab71df08b0604b3b571768bbc0c2729fbf0389d1bb5d13')

    depends_on('ruby@3.0.0:', type=('build'))
    depends_on('bison', type=('build'))

    def patch(self):
        """Create a config.rb file for rake to use
        by patching build_config/default.rb."""
        copy('build_config/default.rb',
             'build_config/spack.rb')
        filter_file("conf.gembox 'default'",
                    "conf.gembox 'full-core'",
                    'build_config/spack.rb')

    def install(self, spec, prefix):
        rb = spec['ruby']
        env['MRUBY_CONFIG'] = 'build_config/spack.rb'
        env['GEM_PATH'] = rb.prefix+'/lib/ruby/gems/'+str(rb.version)
        rake()
        build_path = 'build/host'
        for d in ['include', 'lib', 'bin', 'mrblib', 'mrbgems']:
            mkdirp(prefix+'/'+d)
            install_tree(build_path+'/'+d, prefix+'/'+d)
        install_tree('include', prefix.include)
