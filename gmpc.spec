#
# Conditional build:
%bcond_with	appindicator	# app indicators (pre-ayatana)

%define		libmpd_ver	0.20.95
Summary:	Gnome Music Player Client
Summary(pl.UTF-8):	Odtwarzacz Gnome Music Player Client
Name:		gmpc
Version:	11.8.16
Release:	5
License:	GPL v2+
Group:		X11/Applications/Sound
Source0:	https://download.sarine.nl/Programs/gmpc/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	223aeb000e41697d8fdf54ccedee89d5
Patch0:		%{name}-desktop.patch
Patch1:		window-title.patch
Patch2:		%{name}-types.patch
URL:		https://www.gmpclient.org/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.16.0
BuildRequires:	gnome-doc-utils >= 0.18.0
BuildRequires:	gob2 >= 2.0.17
BuildRequires:	gtk+2-devel >= 2:2.18
BuildRequires:	intltool >= 0.21
%{?with_appindicator:BuildRequires:	libappindicator-devel >= 0.3}
BuildRequires:	libmpd-devel >= %{libmpd_ver}
BuildRequires:	libsoup-devel >= 2.4
BuildRequires:	libtool >= 2:2
BuildRequires:	libunique-devel
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	libxspf-devel
BuildRequires:	pkgconfig >= 1:0.9
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	sqlite3-devel >= 3
BuildRequires:	vala >= 0.11.0
BuildRequires:	xorg-lib-libSM-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	zlib-devel
%requires_ge_to	libmpd libmpd-devel
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Obsoletes:	gmpc-plugin-discogs < 0.21
Obsoletes:	gmpc-plugin-extraplaylist < 0.21
Obsoletes:	gmpc-plugin-favorites < 0.16
Obsoletes:	gmpc-plugin-lastfm-provider < 0.21
Obsoletes:	gmpc-plugin-serverstats < 0.16
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
Requires:	libmpd-devel >= %{libmpd_ver}

%description devel
Header files for GMPC plugin developement.

%description devel -l pl.UTF-8
Pliki nagłówkowe do tworzenia wtyczek dla GMPC.

%prep
%setup -q
%patch -P0 -p1
# breaks compilation due to some timestamp dependencies
touch -r src/playlist3.c src/playlist3.c.foo
%patch -P1 -p1
touch -r src/playlist3.c.foo src/playlist3.c
# too old vala dialect is used - patch generated files instead
%patch -P2 -p1

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}

RC=no \
%configure \
	%{__enable_disable appindicator} \
	--enable-libxspf \
	--enable-unique

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir}/%{name}/plugins,%{_datadir}/%{name}/plugins}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# Ubuntu theme, not present in PLD
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/icons/Humanity
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/gmpc/icons/Humanity

# drop javanese translation, need glibc support first
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/jv

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/gmpc
%attr(755,root,root) %{_bindir}/gmpc-remote
%attr(755,root,root) %{_bindir}/gmpc-remote-stream
%{_desktopdir}/gmpc.desktop
%{_datadir}/%{name}
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
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
%{_mandir}/man1/gmpc-remote-stream.1*

%files devel
%defattr(644,root,root,755)
%{_includedir}/gmpc
%{_pkgconfigdir}/gmpc.pc
