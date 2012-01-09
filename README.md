## More info

Everything about the process and current status can be found on this page: http://fedoraproject.org/wiki/JBossAS7

## How to build

Some packages aren't in Fedora Rawhide yet. For your convenience we provide them in `rpm/` dir.

    yum localinstall ~/git/jboss-as-rpm/rpm/*
    yum-builddep ~/git/jboss-as-rpm/jboss-as-7.1.0*.src.rpm
    rpmbuild --rebuild ~/git/jboss-as-rpm/jboss-as-7.1.0*.src.rpm

