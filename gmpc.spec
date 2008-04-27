Summary:	Gnome Music Player Client
Summary(pl.UTF-8):	Odtwarzacz Gnome Music Player Client
Name:		gmpc
Version:	0.15.5.0
Release:	1
License:	GPL
Group:		X11/Applications/Sound
# http://download.sarine.nl/gmpc-0.15.5/
Source0:	http://download.sarine.nl/gmpc-0.15.5/%{name}-%{version}.tar.gz
# Source0-md5:	8d04d8f1bad663d037b107d1845d62e6
Patch0:		%{name}-plugins_path.patch
Patch1:		%{name}-desktop.patch
Patch2:		%{name}-locale.patch
URL:		http://gmpc.sarine.nl/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	curl-devel
BuildRequires:	glib2-devel >= 1:2.10.0
BuildRequires:	gob2
BuildRequires:	gtk+2-devel >= 2:2.8.0
BuildRequires:	intltool
BuildRequires:	libglade2-devel
BuildRequires:	libmpd-devel >= 0.15.0
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 0.9
Requires:	libmpd >= 0.14.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GMPC is a frontend for the mpd (Music Player Daemon). It's focused on
being fast and easy to use, while making optimal use of all the
functions in mpd. The latest release (0.13) features plugin support so
it can be easily extended where needed, plugins can range from showing
a small osd window to adding an extra view in the playlist browser.

%description -l pl.UTF-8
GMPC to frontend dla mpd (Music Player Daemon). Skupia się na byciu
najszybszym i prostym w użyciu, a jednocześnie optymalnym
wykorzystywaniu wszystkich funkcji mpd. Ostatnie wydanie (0.13) ma
obsługę wtyczek, więc można go łatwo rozszerzać w miarę potrzeby;
wtyczki mogą obsługiwać funkcjonalność od wyświetlania małego okienka
na ekranie do dodawania dodatkowego widoku do przeglądarki playlist.

%package devel
Summary:	Header files for GMPC plugin developement
Summary(pl.UTF-8):	Pliki nagłówkowe do tworzenia wtyczek dla GMPC
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libmpd-devel >= 0.13.0

%description devel
Header files for GMPC plugin developement.

%description devel -l pl.UTF-8
Pliki nagłówkowe do tworzenia wtyczek dla GMPC.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
mv po/nb_NO.po po/nb.po
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_libdir}/%{name},%{_datadir}/%{name}/plugins}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang gmpc

%clean
rm -rf $RPM_BUILD_ROOT

%files -f gmpc.lang
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*
%{_datadir}/%{name}
%{_libdir}/%{name}
%{_pixmapsdir}/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
%{_pkgconfigdir}/*
