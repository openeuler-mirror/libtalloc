Name:          libtalloc
Version:       2.3.0
Release:       0
Summary:       A memory pool system
License:       LGPLv3+
URL:           https://talloc.samba.org/talloc/doc/html/index.html
Source0:       https://www.samba.org/ftp/talloc/talloc-%{version}.tar.gz

Patch0:        talloc-test-leak.patch

BuildRequires: gcc git docbook-style-xsl python3-devel doxygen
Provides:      bundled(libreplace)
Obsoletes:     python2-talloc, python2-talloc-devel

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
%autosetup -n talloc-%{version} -p1

%build
export python_LDFLAGS=""

%configure --disable-rpath --disable-rpath-install --bundled-libraries=NONE \
           --builtin-libraries=replace --disable-silent-rules

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
%{_mandir}/man*/*

%files -n python3-talloc
%{_libdir}/libpytalloc-util.cpython*.so.*
%{python3_sitearch}/talloc.cpython*.so

%files -n python3-talloc-devel
%{_includedir}/pytalloc.h
%{_libdir}/pkgconfig/pytalloc-util.cpython-*.pc
%{_libdir}/libpytalloc-util.cpython*.so

%ldconfig_scriptlets
%ldconfig_scriptlets -n python3-talloc

%changelog
* Mon Feb 10 2020 Ruijun Ge <geruijun@huawei.com> - 2.3.0-0
- Type:enhancement
- ID:NA
- SUG:NA
- DESC:update package

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
