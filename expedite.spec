Summary:	Evas benchmarking tool
Summary(pl.UTF-8):	Narzędzie do testowania szybkości Evas
Name:		expedite
Version:	1.1.0
Release:	2
License:	BSD
Group:		Applications/Graphics
Source0:	http://download.enlightenment.org/releases/%{name}-%{version}.tar.bz2
# Source0-md5:	360dbee8a9754c5f94f6a39a769cb7ea
URL:		http://trac.enlightenment.org/e/wiki/Expedite
BuildRequires:	DirectFB-devel
BuildRequires:	SDL-devel
BuildRequires:	eina-devel >= 1.1.0
BuildRequires:	eet-devel >= 1.5.0
BuildRequires:	evas-devel >= 1.0.0
BuildRequires:	libxcb-devel
BuildRequires:	pkgconfig
BuildRequires:	xcb-util-keysyms-devel
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
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING COPYING-PLAIN README
%attr(755,root,root) %{_bindir}/expedite
%attr(755,root,root) %{_bindir}/expedite-cmp
%{_datadir}/expedite
