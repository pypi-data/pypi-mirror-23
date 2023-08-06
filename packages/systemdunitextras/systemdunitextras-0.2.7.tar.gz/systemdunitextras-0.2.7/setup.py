import importlib
import os
import re
import sys
from glob import glob, iglob

from distutils.core import setup
from distutils.sysconfig import get_python_lib
from setuptools import find_packages
from shutil import copy
from subprocess import Popen, PIPE

module_name = 'systemdunitextras'
data_dirname = "data"


def rsync(src, dst):
    src = os.path.normpath(src)
    p1 = Popen(["rsync", "-avHAXx", "--ignore-existing", src, dst], stdout=PIPE)  # (4)
    print(p1.communicate())


def listdir_fullpath(d):
    return [os.path.join(d, f) for f in os.listdir(d)]


setup(
    name=module_name,
    version="0.2.7",
    author="eayin2",
    author_email="eayin2@gmail.com",
    packages=find_packages(),
    description="Provides watchdog_ping python module and a systemd unit fail handler, allowing to limit \
                 a notification for an OnFailure event of a specific systemd unit to a specified time span.",
    entry_points={
        'console_scripts': [
            'systemd_fail_handler = systemdunitextras.fail_handler:argparse_entry',
        ],
    },
    install_requires=['gymail', 'sqlalchemy', 'helputils'],
    include_package_data=True,
)

# (2)
site_packages = get_python_lib()
egg_path = None
for file in listdir_fullpath(site_packages):
    if re.search("{0}$".format(module_name), file):
        egg_path = file
        pip = True
        break
    elif re.search("{0}\-.*egg.*".format(module_name), file):  # (1)
        egg_path = file
        pip = False
if egg_path:
    if pip is True:
        data_path = os.path.normpath(os.path.join(egg_path, data_dirname))
        for file in glob("{0}/*".format(data_path)):
            relpath = os.path.relpath(file, data_path)
            rsync(file, "/")
    elif pip is False:
        data_path = os.path.normpath(os.path.join(egg_path, module_name, data_dirname))
        for file in glob("{0}/*".format(data_path)):
            relpath = os.path.relpath(file, data_path)
            rsync(file, "/")
print("\n\033[31mNotice: Installation of system files happens automatically, but uninstalling doesn't. You have to manually \
look in <site-packages>/<package>/data/*, where files were installed on the system and delete them manually.")  # (5)


# Code notes:
# (1) If package is installed with `python3 setup.py install`, then the package is within
#     site-packages/<package_name><version><egg>/<package_name>. If installed with pip
#     the package is in site-packages/<package_name>. If both directories exist, then latter
#     will be favoured.
# (2) Here we copy files inside <package>/data/* to system dirs, where data/ resemebles the root
# (3) Wrong approach:
#     site_packages = os.path.join("/usr/lib/", "python{0}.{1}".format(sys.version_info.major, sys.version_info.minor), "site-packages")
#     Better: >>> distutils.sysconfig.get_python_lib()
# (4) --ignore-existing switch makes sure no system files will be overwritten.
# (5) \033[1m ansi escape sequence for bold text.
#
# Notice:
# - Installation of system files happens automatically, but uninstalling doesn't. You have to manually
#   look in <package>/data/*, where files were installed on the system and delete them manually.
# - All system files could be copied into a file in e.g. /var/lib/pipextras/<package_name>.txt
#   so after uninstalling the pip package possible file relicts can be tracked down there.
#   Since this distribution approach is not consistent such features, should not be implemented
#   and rather the use of fpm should be enforced. This distribution way is only for
#   site specific (not meant for public distribution) setups. It saves some time (for python projects)
#   in the respect that you don't have to care about resolving python dependencies in e.g. rpm or deb repositories,
#   because you distribute with pip, where are all needed python packages.
