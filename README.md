## More info

Everything about the process and current status can be found on this page: http://fedoraproject.org/wiki/JBossAS7


## How to build

All commands specified here assume you are in the repo root directory.

### Source RPM

    rpmbuild --define "_topdir $PWD" -bs SPECS/jboss-as.spec

### RPM

For development you can use `rpmbuild` command, like this:

    rpmbuild --define "_topdir $PWD" -bb SPECS/jboss-as.spec

Please note the `-bb` switch change - it'll build the binary only. If you want to build `.src.rpm` and `.rpm` - use `-ba` switch. 

If you want to skip `--define` parameter, you can add it to your `.rpmmacros` file, like this:

    echo '%_topdir %(echo `pwd`)' >> ~/.rpmmacros

Note that this will affect all executions of `rpmbuild` command.

### Using mock

Mock builds provide clean builds, this means that if you want to be shure that the package has correct `BuildRequires` you should always use mock. It's slower than running `rpmbuild` command directly, but it ensure the build is executed in a clean environment.

#### Setup

    yum install mock

I prepared a mock configuration file: `mock/fedora-rawhide-x86_64.cfg`. Make sure you edit the file and point the `as7` repository baseurl to the correct location of the `rpm/` directory.

#### Build

First of all build JBoss AS 7 source RPM - mock will rebuild it into a RPM.

    mock -v --configdir mock/ -r fedora-rawhide-x86_64 --rebuild SRPMS/jboss-as-*.src.rpm

The resulting packages: both `.rpm` and `.src.rpm` and build logs will be stored in `/var/lib/mock/fedora-rawhide-x86_64/result/` directory.

## Status

20 / 56 modules are packaged

## Development VMs

We prepared VM's which can be used to jump-start you. There is everything installed which is needed to start work on AS 7 packaging. Every VM is based on Fedora Rawhide. To login use `root` user with `boxgrinder` password.

* [KVM 64 bit](http://d25oih0l5muvfx.cloudfront.net/jboss-as-dev-1.0-fedora-rawhide-x86_64-raw.tgz) [411 MB]
* [VMware 64 bit](http://d25oih0l5muvfx.cloudfront.net/jboss-as-dev-1.0-fedora-rawhide-x86_64-vmware.tgz) [355 MB]

### KVM installation instructions

    wget http://d25oih0l5muvfx.cloudfront.net/jboss-as-dev-1.0-fedora-rawhide-x86_64-raw.tgz
    tar -xf jboss-as-dev-1.0-fedora-rawhide-x86_64-raw.tgz
    sudo cp jboss-as-dev-1.0-fedora-rawhide-x86_64-raw/jboss-as-dev-sda.qcow2 /var/lib/libvirt/images/
    sudo virt-install -n jboss-as-dev-1.0-fedora-rawhide-x86_64 -r 2048 --vcpus 2 --os-type linux --os-variant fedora16 --disk path=/var/lib/libvirt/images/jboss-as-dev-sda.qcow2,bus=virtio,cache=writeback --network network=default,model=virtio --noautoconsole --import

After running these commands you can connect to your `jboss-as-dev-1.0-fedora-rawhide-x86_64` domain using mentioned above credentials.

