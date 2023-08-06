"""
Module for setup hostapd shared library
"""

import os
from distutils.command.build import build
from subprocess import call
from setuptools import setup

BASEPATH = os.path.dirname(os.path.abspath(__file__))
HOSTAPD_BUILD_PATH = os.path.join(BASEPATH, 'roguehostapd/hostapd-2.6/hostapd')


class HostapdBuild(build):
    """
    Class for build the shared library of hostapd
    """

    def run(self):

        build.run(self)
        make_cmd = ['make', 'hostapd_lib']
        cp_cmd = ['cp', 'defconfig', '.config']

        def compile_hostapd():
            """
            Compile the shared library of hostapd
            """
            call(cp_cmd, cwd=HOSTAPD_BUILD_PATH)
            call(make_cmd, cwd=HOSTAPD_BUILD_PATH)

        self.execute(compile_hostapd, [], 'Compiling hostapd shared library')

setup(
    name='test_roguehostapd',
    packages=['roguehostapd'],
    version='0.1.1',
    description='Hostapd wrapper for hostapd',
    author='Anakin',
    cmdclass={
        'build': HostapdBuild,
        }
)
