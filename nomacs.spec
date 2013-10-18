Summary:	A Qt image viewer
Name:		nomacs
Version:	1.6.0.2
Release:	1
License:	GPL v2+
Group:		X11/Applications/Graphics
Source0:	http://downloads.sourceforge.net/project/%{name}/%{name}-1.6.0/%{name}-%{version}-source.tar.bz2
# Source0-md5:	a5556ca94053eec9539c11454f633316
URL:		http://www.nomacs.org
BuildRequires:	OpenCV-devel
BuildRequires:	QtGui-devel
BuildRequires:	QtNetwork-devel
BuildRequires:	cmake
BuildRequires:	exiv2-devel >= 0.23-2
BuildRequires:	libraw-devel
BuildRequires:	libtiff-devel
BuildRequires:	qt-linguist
BuildRequires:	zlib-devel
Requires(post,postun):	desktop-file-utils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
nomacs is a free image viewer for windows, linux, and mac systems,
which is licensed under the GNU General Public License v3.
nomacs is small, fast and able to handle the most common image formats
including RAW images. Additionally it is possible to synchronize
multiple viewers. A synchronization of viewers running on the same
computer or via LAN is possible. It allows to compare images and spot
the differences (e.g. schemes of architects to show the progress).

%prep
%setup -q

# use common qt locale location
%{__sed} -i "s|share/nomacs/translations|%{_datadir}/qt/translations|" CMakeLists.txt

%build
install -d build
cd build
%cmake ..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --without-mo --with-qm

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database

%postun
%update_desktop_database

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/nomacs
%{_desktopdir}/nomacs.desktop
%{_pixmapsdir}/nomacs.png
%{_mandir}/man1/nomacs.1*

