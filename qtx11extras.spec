#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : qtx11extras
Version  : 5.15.2
Release  : 26
URL      : https://download.qt.io/official_releases/qt/5.15/5.15.2/submodules/qtx11extras-everywhere-src-5.15.2.tar.xz
Source0  : https://download.qt.io/official_releases/qt/5.15/5.15.2/submodules/qtx11extras-everywhere-src-5.15.2.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.3 GPL-2.0 GPL-3.0 LGPL-3.0
Requires: qtx11extras-lib = %{version}-%{release}
Requires: qtx11extras-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-qmake
BuildRequires : mesa-dev
BuildRequires : pkgconfig(Qt5Gui)
BuildRequires : pkgconfig(Qt5Test)
BuildRequires : pkgconfig(Qt5Widgets)
BuildRequires : pkgconfig(xcb)

%description
No detailed description available

%package dev
Summary: dev components for the qtx11extras package.
Group: Development
Requires: qtx11extras-lib = %{version}-%{release}
Provides: qtx11extras-devel = %{version}-%{release}
Requires: qtx11extras = %{version}-%{release}

%description dev
dev components for the qtx11extras package.


%package lib
Summary: lib components for the qtx11extras package.
Group: Libraries
Requires: qtx11extras-license = %{version}-%{release}

%description lib
lib components for the qtx11extras package.


%package license
Summary: license components for the qtx11extras package.
Group: Default

%description license
license components for the qtx11extras package.


%prep
%setup -q -n qtx11extras-everywhere-src-5.15.2
cd %{_builddir}/qtx11extras-everywhere-src-5.15.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export GCC_IGNORE_WERROR=1
%qmake QMAKE_CFLAGS+=-fno-lto QMAKE_CXXFLAGS+=-fno-lto
test -r config.log && cat config.log
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1630804520
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/qtx11extras
cp %{_builddir}/qtx11extras-everywhere-src-5.15.2/LICENSE.FDL %{buildroot}/usr/share/package-licenses/qtx11extras/61907422fefcd2313a9b570c31d203a6dbebd333
cp %{_builddir}/qtx11extras-everywhere-src-5.15.2/LICENSE.GPL2 %{buildroot}/usr/share/package-licenses/qtx11extras/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/qtx11extras-everywhere-src-5.15.2/LICENSE.GPL3 %{buildroot}/usr/share/package-licenses/qtx11extras/8624bcdae55baeef00cd11d5dfcfa60f68710a02
cp %{_builddir}/qtx11extras-everywhere-src-5.15.2/LICENSE.GPL3-EXCEPT %{buildroot}/usr/share/package-licenses/qtx11extras/e93757aefa405f2c9a8a55e780ae9c39542dfc3a
cp %{_builddir}/qtx11extras-everywhere-src-5.15.2/LICENSE.LGPL3 %{buildroot}/usr/share/package-licenses/qtx11extras/f45ee1c765646813b442ca58de72e20a64a7ddba
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/qt5/QtX11Extras/QX11Info
/usr/include/qt5/QtX11Extras/QtX11Extras
/usr/include/qt5/QtX11Extras/QtX11ExtrasDepends
/usr/include/qt5/QtX11Extras/QtX11ExtrasVersion
/usr/include/qt5/QtX11Extras/qtx11extrasglobal.h
/usr/include/qt5/QtX11Extras/qtx11extrasversion.h
/usr/include/qt5/QtX11Extras/qx11info_x11.h
/usr/lib64/cmake/Qt5X11Extras/Qt5X11ExtrasConfig.cmake
/usr/lib64/cmake/Qt5X11Extras/Qt5X11ExtrasConfigVersion.cmake
/usr/lib64/libQt5X11Extras.prl
/usr/lib64/libQt5X11Extras.so
/usr/lib64/pkgconfig/Qt5X11Extras.pc
/usr/lib64/qt5/mkspecs/modules/qt_lib_x11extras.pri
/usr/lib64/qt5/mkspecs/modules/qt_lib_x11extras_private.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libQt5X11Extras.so.5
/usr/lib64/libQt5X11Extras.so.5.15
/usr/lib64/libQt5X11Extras.so.5.15.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/qtx11extras/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/qtx11extras/61907422fefcd2313a9b570c31d203a6dbebd333
/usr/share/package-licenses/qtx11extras/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/qtx11extras/e93757aefa405f2c9a8a55e780ae9c39542dfc3a
/usr/share/package-licenses/qtx11extras/f45ee1c765646813b442ca58de72e20a64a7ddba
