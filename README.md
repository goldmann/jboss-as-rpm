## More info

Everything about the process and current status can be found on this page: http://fedoraproject.org/wiki/JBossAS7

## Setup

The best idea is to build RPMs in mock. This will create the package every time in a clean environment.

    yum install mock

I prepared a mock configuration file: `mock/fedora-rawhide-x86_64.cfg`. Make sure you edit the file and point the `as7` repository baseurl to the correct location of the `rpm/` directory.

## How to build

    rpmbuild -bs jboss-as.spec
    mock -v --configdir mock/ -r fedora-rawhide-x86_64 --rebuild ~/rpmbuild/SRPMS/jboss-as-*.src.rpm

The resulting package(s) (and build logs) will be stored in `/var/lib/mock/fedora-rawhide-x86_64/result/` directory.

