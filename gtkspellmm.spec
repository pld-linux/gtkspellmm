#
# Conditional build:
%bcond_without	static_libs	# static library

Summary:	C++ binding for the gtkspell library
Summary(pl.UTF-8):	Interfejs C++ do biblioteki gtkspell
Name:		gtkspellmm
Version:	3.0.5
Release:	1
License:	GPL v2+
Group:		X11/Libraries
Source0:	http://downloads.sourceforge.net/gtkspell/%{name}-%{version}.tar.xz
# Source0-md5:	abaf93ff39eec716d056edfc1ff8490b
URL:		http://gtkspell.sourceforge.net/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	glibmm-devel >= 2.16
BuildRequires:	gtk+3-devel >= 3.0
BuildRequires:	gtkmm3-devel >= 3.0
BuildRequires:	gtkspell3-devel >= 3.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libstdc++-devel >= 6:4.3
BuildRequires:	libtool >= 2:1.5
BuildRequires:	mm-common >= 0.9
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	glibmm >= 2.16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gtkspellmm is the C++ binding for the gtkspell library.

This module is part of the GNOME C++ bindings effort
<http://www.gtkmm.org/>.

%description -l pl.UTF-8
gtkspellmm to wiązanie C++ do biblioteki gtkspell.

Jest to część projektu wiązań C++ dla GNOME <http://www.gtkmm.org/>.

%package devel
Summary:	Header files for gtkspellmm
Summary(pl.UTF-8):	Pliki nagłówkowe dla gtkspellmm
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glibmm-devel >= 2.16
Requires:	gtk+3-devel >= 3.0
Requires:	gtkmm3-devel >= 3.0
Requires:	gtkspell3-devel >= 3.0
Requires:	libstdc++-devel >= 6:4.3

%description devel
Header files for gtkspellmm.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla gtkspellmm.

%package static
Summary:	Static gtkspellmm library
Summary(pl.UTF-8):	Biblioteka statyczna gtkspellmm
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static gtkspellmm library.

%description static -l pl.UTF-8
Biblioteka statyczna gtkspellmm.

%package apidocs
Summary:	gtkspellmm API documentation
Summary(pl.UTF-8):	Dokumentacja API gtkspellmm
Group:		Documentation
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
gtkspellmm API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API gtkspellmm.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I build
%{__autoconf}
%{__autoheader}
%{__automake}
CXXFLAGS="%{rpmcxxflags} -std=c++0x"
%configure \
	--disable-silent-rules \
	%{?with_static_libs:--enable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libgtkspellmm-3.0.la

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_libdir}/libgtkspellmm-3.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgtkspellmm-3.0.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgtkspellmm-3.0.so
%{_includedir}/gtkspellmm-3.0
%dir %{_libdir}/gtkspellmm-3.0
%{_libdir}/gtkspellmm-3.0/include
%{_pkgconfigdir}/gtkspellmm-3.0.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libgtkspellmm-3.0.a
%endif

%files apidocs
%defattr(644,root,root,755)
%{_docdir}/gtkspellmm-3.0
%{_datadir}/devhelp/books/gtkspellmm-3.0
