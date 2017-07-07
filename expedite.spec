%define		eet_ver		1.7.10
%define		eina_ver	1.7.10
%define		evas_ver	1.7.10

Summary:	Evas benchmarking tool
Summary(pl.UTF-8):	Narzędzie do testowania szybkości Evas
Name:		expedite
Version:	1.7.10
Release:	4
License:	BSD
Group:		Applications/Graphics
Source0:	http://download.enlightenment.org/releases/%{name}-%{version}.tar.bz2
# Source0-md5:	9114093970804f74d7673ddbece06a14
URL:		http://trac.enlightenment.org/e/wiki/Expedite
BuildRequires:	DirectFB-devel
BuildRequires:	SDL-devel
BuildRequires:	eet-devel >= %{eet_ver}
BuildRequires:	eina-devel >= %{eina_ver}
BuildRequires:	evas-devel >= %{evas_ver}
BuildRequires:	libxcb-devel
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
BuildRequires:	xcb-util-keysyms-devel
BuildRequires:	xorg-lib-libX11-devel
Requires:	eet >= %{eet_ver}
Requires:	eina >= %{eina_ver}
Requires:	evas >= %{evas_ver}
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
