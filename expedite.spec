Summary:	Evas benchmarking tool
Summary(pl.UTF-8):	Narzędzie do testowania szybkości Evas
Name:		expedite
Version:	1.7.2
Release:	1
License:	BSD
Group:		Applications/Graphics
Source0:	http://download.enlightenment.org/releases/%{name}-%{version}.tar.bz2
# Source0-md5:	1d2a5b7c073bacb7d447373243be5b19
URL:		http://trac.enlightenment.org/e/wiki/Expedite
BuildRequires:	DirectFB-devel
BuildRequires:	SDL-devel
BuildRequires:	eina-devel >= 1.7.0
BuildRequires:	eet-devel >= 1.7.0
BuildRequires:	evas-devel >= 1.7.0
BuildRequires:	libxcb-devel
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
BuildRequires:	xcb-util-keysyms-devel
BuildRequires:	xorg-lib-libX11-devel
Requires:	eet >= 1.7.0
Requires:	eina >= 1.7.0
Requires:	evas >= 1.7.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Expedite is the official Evas benchmark tool. It can test different
engines, such as X11, XRender, OpenGL (also ES variant), SDL, DirectFB
and so on. Its tests are quite extensive, trying to reproduce real
world usage cases.

%description -l pl.UTF-8
Expedite to oficjalne narzędzie do testowania szybkości Evas. Potrafi
testować różne silniki, takie jak X11, XRender, OpenGL (także w
wariancie ES), SDL, DirectFB itd. Testy są obszerne, próbują odtworzyć
rzeczywiste przypadku użycia.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

sed -i -e '1s,/usr/bin/env python,/usr/bin/python,' $RPM_BUILD_ROOT%{_bindir}/expedite-cmp

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING COPYING-PLAIN ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/expedite
%attr(755,root,root) %{_bindir}/expedite-cmp
%{_datadir}/expedite
