#
Summary:	Gnome Music Player Client
Name:		gmpc
Version:	0.13.0
Release:	1
License:	GPL
Group:		X11/Applications/Sound
# http://sarine.nl/gmpc-downloads
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	dbbb1880feb8b9c2493ece670520299b
URL:		http://sarine.nl/gmpc
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2.4
BuildRequires:	intltool
BuildRequires:	libglade2-devel
BuildRequires:	libmpd-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GMPC is a frontend for the mpd (Music Player Daemon). It's focused on
being fast and easy to use, while making optimal use of all the
functions in mpd. The latest release (0.13) features plugin support so
it can be easily extended where needed, plugins can range from showing
a small osd window to adding an extra view in the playlist browser.

%package devel
Summary:	Header files for GMPC plugin developement
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for GMPC plugin developement.

%prep
%setup -q

%build
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
%{_pixmapsdir}/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
%{_pkgconfigdir}/*
#%doc extras/*.gz
#%{_datadir}/%{name}-ext
