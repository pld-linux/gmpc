Summary:	Gnome Music Player Client
Summary(pl.UTF-8):	Odtwarzacz Gnome Music Player Client
Name:		gmpc
Version:	0.18.96
Release:	0
License:	GPL v2+
Group:		X11/Applications/Sound
Source0:	http://dl.sourceforge.net/musicpd/%{name}-%{version}.tar.gz
# Source0-md5:	f0e19c4c79ec9edf35e316df7f5a368a
Patch0:		%{name}-desktop.patch
URL:		http://gmpc.wikia.com
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	curl-devel
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.10.0
BuildRequires:	gob2
BuildRequires:	gtk+2-devel >= 2:2.12.0
BuildRequires:	intltool
BuildRequires:	libglade2-devel
BuildRequires:	libmpd-devel >= 0.18.96
BuildRequires:	libtool
BuildRequires:	libxspf-devel
BuildRequires:	pkgconfig >= 0.9
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	xorg-lib-libSM-devel
%requires_eq	libmpd
Requires(post,postun):	gtk+2
Obsoletes:	gmpc-plugin-serverstats
Obsoletes:	gmpc-plugin-favorites
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
Requires:	libmpd-devel >= 0.18.0

%description devel
Header files for GMPC plugin developement.

%description devel -l pl.UTF-8
Pliki nagłówkowe do tworzenia wtyczek dla GMPC.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}

RC=no \
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_libdir}/%{name}/plugins,%{_datadir}/%{name}/plugins}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# drop javanese translation, need glibc support first
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/jv

%find_lang gmpc

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f gmpc.lang
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/gmpc
%attr(755,root,root) %{_bindir}/gmpc-remote
%attr(755,root,root) %{_bindir}/gmpc-remote-stream
%{_desktopdir}/gmpc.desktop
%{_datadir}/%{name}
%{_libdir}/%{name}
%{_iconsdir}/hicolor/16x16/apps/gmpc.png
%{_iconsdir}/hicolor/22x22/apps/gmpc.png
%{_iconsdir}/hicolor/32x32/apps/gmpc.png
%{_iconsdir}/hicolor/48x48/apps/gmpc.png
%{_iconsdir}/hicolor/64x64/apps/gmpc.png
%{_iconsdir}/hicolor/72x72/apps/gmpc.png
%{_iconsdir}/hicolor/96x96/apps/gmpc.png
%{_iconsdir}/hicolor/128x128/apps/gmpc.png
%{_iconsdir}/hicolor/scalable/apps/gmpc.svg
%{_mandir}/man1/gmpc-remote.1*
%{_mandir}/man1/gmpc.1*

%files devel
%defattr(644,root,root,755)
%{_includedir}/gmpc
%{_pkgconfigdir}/gmpc.pc
