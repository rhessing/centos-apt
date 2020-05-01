%define name apt
Name:           %{name}
Version:        1.7.5
Release:        1.el7
Summary:        Commandline package manager for Debian and its derivatives.
Group:          System/Packages
License:        GPLv2
Url:            https://packages.debian.org/apt
Source:         https://github.com/Debian/%{name}/archive/%{version}.tar.gz
Requires:       dpkg
BuildRequires:  gcc-c++
BuildRequires:  cmake3 cmake
BuildRequires:  libxml2-devel
BuildRequires:  bzip2-devel
BuildRequires:  lz4-devel
BuildRequires:  doxygen
BuildRequires:  dpkg-dev
BuildRequires:  libcurl-devel
BuildRequires:  dpkg
BuildRequires:  libxslt
BuildRequires:  docbook-style-xsl
BuildRequires:  libdb-devel
BuildRequires:  po4a
BuildRequires:  w3m
BuildRequires:  sed
BuildRequires:  gnutls-devel

%description
apt is the main commandline package manager for Debian and its derivatives. It provides commandline tools for searching and managing as well as querying information about packages as well as low-level access to all features provided by the libapt-pkg and libapt-inst libraries which higher-level package managers can depend upon.

%package devel
Group: Development/Libraries
Summary: Header files for apt
Requires: %{name} = %{version-%{release}

%description devel
Development files for gtkglarea.

%prep
%setup -q

%build
export CXXFLAGS="%{optflags}"
%cmake3 .
find . -name build.make -exec sed -i 's/add-location=file/add-location/' {} \;
make %{?_smp_mflags}

%install
%{__mkdir_p} %{buildroot}%{_sysconfdir}/apt
touch %{buildroot}%{_sysconfdir}/apt/sources.list
%makeinstall -e DESTDIR=%{buildroot}
for f in %{buildroot}%{_bindir}/* apt-utils libapt-inst2.0 libapt-pkg5.0 apt_preferences sources.list apt-secure; do
  %find_lang $(basename $f) --with-man
   cat $(basename $f).lang >> all.lang
done

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f all.lang
%defattr(-, root, root)
%{_bindir}/*
%{_libdir}/*
%{_libexecdir}/*
%dir %{_sysconfdir}/apt
%dir %{_sysconfdir}/apt/*.d
%config %{_sysconfdir}/apt/sources.list
%{_datadir}/bash-completion/completions/apt
%doc %{_mandir}/man?/*
%doc %{_docdir}/*

%files devel
%defattr(-, root, root)
%{_includedir}/*

%changelog
* Fri May 01 2020 rhessing <robbert@hessing.io> - 1.8.4-1.el7
- Private build and new apt version

* Tue Jan 29 2019 - harbottle@room3d3.com - 1.4.9-1
- Bump version

* Thu May 03 2018 Richard Grainger <grainger@gmail.com> - 1.4.7-1.el7.harbottle
- Bump version
