Name:          libtalloc
Version:       2.1.14
Release:       4
Summary:       A memory pool system
License:       LGPLv3+
URL:           https://talloc.samba.org/talloc/doc/html/index.html
Source:        https://www.samba.org/ftp/talloc/talloc-%{version}.tar.gz

Patch6000:     6000-lib-talloc-Fix-undefined-behavior-in-talloc_memdup.patch
Patch6001:     6001-talloc-Fix-alignment-issues-for-casting-pointers.patch

BuildRequires: gcc git docbook-style-xsl python2-devel python3-devel doxygen

Provides:      bundled(libreplace)

# Patches

%description
A hierarchical, reference counted memory pool system with destructors

%package       -n libtalloc-devel
Summary:       Files for libtalloc development
Requires:      libtalloc = %{version}-%{release}

%description   -n libtalloc-devel
Files for libtalloc development

%package        help
Summary:        Including man files for libtalloc
Requires:       man

%description    help
This contains man files for the using of libtalloc


%package       -n python2-talloc
Summary:       Provide the python rely for libtalloc
Requires:      libtalloc = %{version}-%{release}
Provides:      pytalloc%{?_isa} = %{version}-%{release}
Provides:      pytalloc = %{version}-%{release}
Obsoletes:     pytalloc < 2.1.3
%{?python_provide:%python_provide python2-talloc}

%description   -n python2-talloc
Provide the python 2 when using the libtalloc

%package       -n python2-talloc-devel
Summary:       Files for python2-talloc development
Requires:      python2-talloc = %{version}-%{release}
Provides:      pytalloc-devel%{?_isa} = %{version}-%{release}
Provides:      pytalloc-devel = %{version}-%{release}
Obsoletes:     pytalloc-devel < 2.1.3
%{?python_provide:%python_provide python2-talloc-devel}

%description   -n python2-talloc-devel
Files for python2-talloc development

%package       -n python3-talloc
Summary:       Provide the python rely for libtalloc
Requires:      libtalloc = %{version}-%{release}
%{?python_provide:%python_provide python3-talloc}

%description   -n python3-talloc
Provide the python 3 when using the libtalloc

%package       -n python3-talloc-devel
Summary:       Files for python3-talloc development
Requires:      python3-talloc = %{version}-%{release}
%{?python_provide:%python_provide python3-talloc-devel}

%description   -n python3-talloc-devel
Files for python3-talloc development

%prep
%autosetup     -n talloc-%{version} -p1

%build
export python_LDFLAGS=""

pathfix.py -n -p -i %{__python2} buildtools/bin/waf

%configure --disable-rpath \
           --disable-rpath-install \
           --bundled-libraries=NONE \
           --builtin-libraries=replace \
           --disable-silent-rules \
           --extra-python=%{__python3}

%make_build V=1
doxygen doxy.config

%check
%make_build check

%install
%make_install

find $RPM_BUILD_ROOT -name "*.so*" -exec chmod -c +x {} \;

rm -f $RPM_BUILD_ROOT%{_libdir}/libtalloc.a
rm -f $RPM_BUILD_ROOT/usr/share/swig/*/talloc.i

mkdir -p $RPM_BUILD_ROOT/%{_mandir}

cp -a doc/man/* $RPM_BUILD_ROOT/%{_mandir}

%files
%{_libdir}/libtalloc.so.*

%files devel
%{_includedir}/talloc.h
%{_libdir}/libtalloc.so
%{_libdir}/pkgconfig/talloc.pc

%files help
%{_mandir}/man3/*

%files -n python2-talloc
%{_libdir}/libpytalloc-util.so.*
%{python2_sitearch}/talloc.so

%files -n python2-talloc-devel
%{_includedir}/pytalloc.h
%{_libdir}/pkgconfig/pytalloc-util.pc
%{_libdir}/libpytalloc-util.so

%files -n python3-talloc
%{_libdir}/libpytalloc-util.cpython*.so.*
%{python3_sitearch}/talloc.cpython*.so

%files -n python3-talloc-devel
%{_includedir}/pytalloc.h
%{_libdir}/pkgconfig/pytalloc-util.cpython-*.pc
%{_libdir}/libpytalloc-util.cpython*.so

%ldconfig_scriptlets

%ldconfig_scriptlets -n python2-talloc

%ldconfig_scriptlets -n python3-talloc

%changelog
* Tue Sep 3 2019 shidongdong <shidongdong5@huawei.com> - 2.1.14-4
- Type:enhancement
- ID:NA
- SUG:NA
- DESC:openEuler Debranding

* Tue Aug 20 2019 zhanghaibo <ted.zhang@huawei.com> - 2.1.14-3
- correct patch name

* Wed Apr 17 2019 gaoyi<gaoyi15@huawei.com> - 2.1.14-2.h1
- Type:bugfix
- ID:NA
- SUG:NA
- DESC: backport patches from https://github.com/samba-team/samba
- Package init
