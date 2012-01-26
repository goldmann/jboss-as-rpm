%global namedreltag .CR1b
%global namedversion %{version}%{?namedreltag}

%global cachedir %{_var}/cache/%{name}
%global homedir %{_datadir}/%{name}
%global bindir %{homedir}/bin
%global logdir %{_var}/log/%{name}
%global confdir %{_sysconfdir}/%{name}

%global tcuid 92

%global modules controller-client controller deployment-repository domain-management ee embedded jmx naming network platform-mbean process-controller protocol remoting server

Name:             jboss-as
Version:          7.1.0
Release:          0.1%{namedreltag}%{?dist}
Summary:          JBoss Application Server 7
Group:            System Environment/Daemons
License:          LGPLv2+ and ASL 2.0
URL:              http://www.jboss.org/jbossas

# git clone git://github.com/jbossas/jboss-as.git
# cd jboss-as && git archive --format=tar --prefix=jboss-as-7.1.0.CR1b/ 7.1.0.CR1b | xz > jboss-as-7.1.0.CR1b.tar.xz
Source0:          jboss-as-%{namedversion}.tar.xz
Patch0:           0001-Disable-checkstyle.patch
Patch1:           0002-Fix-initd-script.patch
Patch2:           0003-Build-additional-modules.patch
# Modifications here are purely temporary until we solve issues in the Right Way (tm)
Patch3:           0004-Ugly-patch-nuff-said.patch

BuildArch:        noarch

# Please keep alphabetically
BuildRequires:    ant-apache-bsf
BuildRequires:    apache-james-project
BuildRequires:    bean-validation-api
BuildRequires:    bsf >= 2.4.0-10
BuildRequires:    dom4j
BuildRequires:    geronimo-annotation
BuildRequires:    h2
BuildRequires:    hibernate-validator >= 4.2.0
BuildRequires:    jandex >= 1.0.3
BuildRequires:    java-devel
BuildRequires:    jgroups
BuildRequires:    jboss-annotations-1.1-api
BuildRequires:    jboss-dmr >= 1.1.1-1
BuildRequires:    jboss-ejb-3.1-api
BuildRequires:    jboss-httpserver >= 1.0.0-0.3.Beta3
BuildRequires:    jboss-invocation
BuildRequires:    jboss-interceptor >= 2.0.0-1
BuildRequires:    jboss-interceptors-1.1-api
BuildRequires:    jboss-jad-1.2-api
BuildRequires:    jboss-parent
BuildRequires:    jboss-logging >= 3.1.0-0.1.CR1
BuildRequires:    jboss-logging-tools >= 1.0.0-0.1.CR4
BuildRequires:    jboss-logmanager-log4j >= 1.0.0
BuildRequires:    jboss-marshalling >= 1.3.4
BuildRequires:    jboss-metadata >= 7.0.0-0.1.Beta32
BuildRequires:    jboss-modules >= 1.1.0-0.1.CR4
BuildRequires:    jboss-msc >= 1.0.1
BuildRequires:    jboss-remoting >= 3.2.0-0.2.CR6
BuildRequires:    jboss-sasl >= 1.0.0-0.1.Beta9
BuildRequires:    jboss-stdio >= 1.0.1
BuildRequires:    jboss-specs-parent
BuildRequires:    jboss-threads >= 2.0.0
BuildRequires:    jboss-transaction-1.1-api
BuildRequires:    jboss-vfs >= 3.1.0-0.1.CR1
BuildRequires:    jline
BuildRequires:    jpackage-utils
BuildRequires:    maven
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-checkstyle-plugin
BuildRequires:    maven-resources-plugin
BuildRequires:    maven-surefire-plugin
BuildRequires:    staxmapper >= 1.0.0
BuildRequires:    xnio >= 3.0.0-0.2.CR5

Requires:         bean-validation-api
Requires:         dom4j
Requires:         geronimo-annotation
Requires:         h2
Requires:         hibernate-validator >= 4.2.0
Requires:         jandex >= 1.0.3
Requires:         java
Requires:         jboss-annotations-1.1-api
Requires:         jboss-dmr >= 1.1.1-1
Requires:         jboss-ejb-3.1-api
Requires:         jboss-httpserver >= 1.0.0-0.3.Beta3
Requires:         jboss-interceptor >= 2.0.0-1
Requires:         jboss-interceptors-1.1-api
Requires:         jboss-invocation
Requires:         jboss-logging >= 3.1.0-0.1.CR1
Requires:         jboss-logging-tools >= 1.0.0-0.1.CR4
Requires:         jboss-jad-1.2-api
Requires:         jboss-logmanager-log4j >= 1.0.0
Requires:         jboss-marshalling >= 1.3.4
Requires:         jboss-metadata >= 7.0.0-0.1.Beta32
Requires:         jboss-modules >= 1.1.0-0.1.CR4
Requires:         jboss-msc >= 1.0.1
Requires:         jboss-remoting >= 3.2.0-0.2.CR6
Requires:         jboss-sasl >= 1.0.0-0.1.Beta9
Requires:         jboss-stdio >= 1.0.1
Requires:         jboss-threads >= 2.0.0
Requires:         jboss-transaction-1.1-api
Requires:         jboss-vfs >= 3.1.0-0.1.CR1
Requires:         jgroups
Requires:         jline
Requires:         jpackage-utils
Requires:         staxmapper >= 1.0.0
Requires:         xnio >= 3.0.0-0.2.CR5

%description
JBoss Application Server 7 is the latest release in a series of JBoss
Application Server offerings. JBoss Application Server 7, is a fast,
powerful, implementation of the Java Enterprise Edition 6 specification.
The state-of-the-art architecture built on the Modular Service Container
enables services on-demand when your application requires them.

%package javadoc
Summary:          Javadocs for %{name}
Group:            Documentation
Requires:         jpackage-utils

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jboss-as-%{namedversion}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
# We don't have packaged all test dependencies (jboss-test for example)
mvn-rpmbuild -Dmaven.test.skip=true -Dminimalistic -e install javadoc:aggregate

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT%{_sysconfdir}/init.d
install -d -m 755 $RPM_BUILD_ROOT%{homedir}
install -d -m 755 $RPM_BUILD_ROOT%{confdir}
install -d -m 770 $RPM_BUILD_ROOT%{cachedir}/auth
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}

for mode in standalone domain; do
  install -d -m 755 $RPM_BUILD_ROOT%{homedir}/${mode}
  install -d -m 755 $RPM_BUILD_ROOT%{cachedir}/${mode}/data
  install -d -m 755 $RPM_BUILD_ROOT%{cachedir}/${mode}/tmp
  install -d -m 775 $RPM_BUILD_ROOT%{logdir}/${mode}
done

for m in %{modules} build-config ee-deployment threads; do
  # JAR
  cp -a ${m}/target/jboss-as-${m}-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-${m}.jar
  # POM
  cp -a ${m}/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}-${m}.pom
  # DEPMAP
  %add_maven_depmap JPP.%{name}-%{name}-${m}.pom %{name}/%{name}-${m}.jar
done

# Special case domain-http submodules
for m in interface error-context; do
  # JAR
  cp -a domain-http/${m}/target/jboss-as-domain-http-${m}-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-domain-http-${m}.jar
  # POM
  cp -a domain-http/${m}/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}-domain-http-${m}.pom
  # DEPMAP
  %add_maven_depmap JPP.%{name}-%{name}-domain-http-${m}.pom %{name}/%{name}-domain-http-${m}.jar
done

# Parent POM
cp -a pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}-parent.pom

# Depmap fo parent POM
%add_maven_depmap JPP.%{name}-%{name}-parent.pom

# Apidocs
cp -a target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

pushd build/target/jboss-as-%{namedversion}
  # We don't need Windows files
  find bin/ -type f -name "*.bat" -delete

  # init.d
  mv bin/init.d/jboss-as.conf $RPM_BUILD_ROOT%{confdir}
  mv bin/init.d/jboss-as-standalone.sh $RPM_BUILD_ROOT%{_sysconfdir}/init.d/%{name}
  rm -rf bin/init.d

  # standalone
  mv standalone/configuration $RPM_BUILD_ROOT%{confdir}/standalone
  mv standalone/deployments $RPM_BUILD_ROOT%{cachedir}/standalone
  # enable standalone-minimalistic.xml
  mv docs/examples/configs/standalone-minimalistic.xml $RPM_BUILD_ROOT%{confdir}/standalone/

  # domain
  mv domain/configuration $RPM_BUILD_ROOT%{confdir}/domain
  mv domain/content $RPM_BUILD_ROOT%{cachedir}/domain

  # Remove all jars from modules directory - we need to symlink them
  # TODO temporary with verbose, use -delete afterwards
  find . -type f -name "*.jar" -exec rm -rvf {} \;

  mv copyright.txt README.txt LICENSE.txt welcome-content docs bin appclient modules $RPM_BUILD_ROOT%{homedir}
popd

pushd $RPM_BUILD_ROOT%{homedir}

  # Dtandalone
  ln -s %{cachedir}/standalone/deployments standalone/deployments
  ln -s %{confdir}/standalone standalone/configuration

  # Domain
  ln -s %{confdir}/domain domain/configuration

  # Symlink jboss-modules
  ln -s $(build-classpath jboss/jboss-modules.jar) jboss-modules.jar
  
  # Symlinks to log dirs
  ln -s %{logdir}/standalone standalone/log
  ln -s %{logdir}/domain domain/log

  # temp dir
  ln -s %{cachedir}/standalone/tmp standalone/tmp
  ln -s %{cachedir}/domain/tmp domain/tmp

  # data dir
  ln -s %{cachedir}/standalone/data standalone/data
  ln -s %{cachedir}/domain/data domain/data

  # auth dir
  ln -s %{cachedir}/auth auth
  
  # Create symlinks to jars
  pushd modules
    ln -s $(build-classpath jboss/jboss-vfs.jar) org/jboss/vfs/main/jboss-vfs.jar
    ln -s $(build-classpath jboss/jboss-comon-core.jar) org/jboss/common-core/main/jboss-common-core.jar
    ln -s $(build-classpath jboss/jandex.jar) org/jboss/jandex/main/jandex.jar
    ln -s $(build-classpath jboss/jboss-annotations-1.1-api.jar) javax/annotation/api/main/jboss-annotations-api.jar
    ln -s $(build-classpath jboss/jboss-interceptors-1.1-api.jar) javax/interceptor/api/main/jboss-interceptors-api_1.1.jar
    ln -s $(build-classpath jboss/jboss-remoting.jar) org/jboss/remoting3/main/jboss-remoting.jar
    ln -s $(build-classpath jboss/jboss-dmr.jar) org/jboss/dmr/main/jboss-dmr.jar
    ln -s $(build-classpath jboss/jboss-marshalling-river.jar) org/jboss/marshalling/river/main/jboss-marshalling-river.jar
    ln -s $(build-classpath jboss/jboss-marshalling.jar) org/jboss/marshalling/main/jboss-marshalling.jar
    ln -s $(build-classpath jboss/jboss-logging.jar) org/jboss/logging/main/jboss-logging.jar
    ln -s $(build-classpath jboss/jboss-msc.jar) org/jboss/msc/main/jboss-msc.jar
    ln -s $(build-classpath jboss/jboss-threads.jar) org/jboss/threads/main/jboss-threads.jar
    ln -s $(build-classpath jboss/jboss-invocation.jar) org/jboss/invocation/main/jboss-invocation.jar
    ln -s $(build-classpath jboss/jboss-logmanager.jar) org/jboss/logmanager/main/jboss-logmanager.jar
    ln -s $(build-classpath jboss/jboss-logmanager-log4j.jar) org/jboss/logmanager/log4j/main/jboss-logmanager-log4j.jar
    ln -s $(build-classpath jboss/jboss-sasl.jar) org/jboss/sasl/main/jboss-sasl.jar
    ln -s $(build-classpath jboss/xnio-api.jar) org/jboss/xnio/main/xnio-api.jar
    ln -s $(build-classpath jboss/xnio-nio.jar) org/jboss/xnio/nio/main/xnio-nio.jar
    ln -s $(build-classpath jboss/jboss-stdio.jar) org/jboss/stdio/main/jboss-stdio.jar
    ln -s $(build-classpath jboss/staxmapper.jar) org/jboss/staxmapper/main/staxmapper.jar
    ln -s $(build-classpath log4j.jar) org/apache/log4j/main/log4j.jar

    # JBoss AS modules (without build-config and threads)
    for m in %{modules}; do
      ln -s $(build-classpath jboss-as/jboss-as-${m}.jar) org/jboss/as/${m}/main/jboss-as-${m}-%{namedversion}.jar
    done

    # special case naming
    ln -s $(build-classpath %{name}/%{name}-domain-http-interface.jar) org/jboss/as/domain-http-interface/main/jboss-as-domain-http-interface-%{namedversion}.jar
    ln -s $(build-classpath %{name}/%{name}-ee-deployment.jar) org/jboss/as/ee/deployment/main/jboss-as-ee-deployment-%{namedversion}.jar
  popd
popd

%pre
# Add jboss-as user and group
%{_sbindir}/groupadd -g %{jbuid} -r %{name} 2>/dev/null || :
%{_sbindir}/useradd -c "JBoss AS" -u %{jbuid} -g %{name} -s /bin/nologin -r -d %{homedir} %{name} 2>/dev/null || :

%files
%defattr(0664,root,jboss-as,0755)
%{homedir}/appclient
%{bindir}/*.conf
%attr(0755,root,root) %{bindir}/*.sh
%attr(0755,root,root) %{bindir}/util/*.sh
%{homedir}/auth
%{homedir}/domain
%{homedir}/standalone
%{homedir}/modules
%{homedir}/welcome-content
%{homedir}/jboss-modules.jar
%{cachedir}/standalone/deployments/README.txt
%attr(0775,root,jboss-as) %dir %{cachedir}/standalone/data
%attr(0775,root,jboss-as) %dir %{cachedir}/standalone/tmp
%attr(0775,root,jboss-as) %dir %{cachedir}/domain/data
%attr(0775,root,jboss-as) %dir %{cachedir}/domain/tmp
%attr(0700,jboss-as,jboss-as) %dir %{cachedir}/auth
%attr(0770,root,jboss-as) %dir %{logdir}
%attr(0775,root,jboss-as) %dir %{confdir}/standalone
%attr(0775,root,jboss-as) %dir %{confdir}/domain
%attr(0664,jboss-as,jboss-as) %config(noreplace) %{confdir}/%{name}.conf
%attr(0664,jboss-as,jboss-as) %config(noreplace) %{confdir}/standalone/*.properties
%attr(0664,jboss-as,jboss-as) %config(noreplace) %{confdir}/standalone/*.xml
%attr(0664,jboss-as,jboss-as) %config(noreplace) %{confdir}/domain/*.properties
%attr(0664,jboss-as,jboss-as) %config(noreplace) %{confdir}/domain/*.xml
%attr(0755,root,root) %config(noreplace) %{_sysconfdir}/init.d/%{name}
%doc %{homedir}/docs
%doc %{homedir}/copyright.txt
%doc %{homedir}/LICENSE.txt
%doc %{homedir}/README.txt
%doc README.md
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/*

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Mon Jan 09 2012 Marek Goldmann <mgoldman@redhat.com> 7.1.0-0.1.CR1b
- Initial packaging

