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

## Status

20 / 56 modules are packaged

## Development VMs

We prepared VM's which can be used to jump-start you. There is everything installed which is needed to start work on AS 7 packaging. Every VM is based on Fedora Rawhide. To login use `root` user with `boxgrinder` password.

* [KVM 64 bit](http://d25oih0l5muvfx.cloudfront.net/jboss-as-dev-1.0-fedora-rawhide-x86_64-raw.tgz) [411 MB]
* [VMware 64 bit](http://d25oih0l5muvfx.cloudfront.net/jboss-as-dev-1.0-fedora-rawhide-x86_64-vmware.tgz) [355 MB]

