#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : qtx11extras
Version  : 5.10.0
Release  : 2
URL      : http://download.qt.io/official_releases/qt/5.10/5.10.0/submodules/qtx11extras-everywhere-src-5.10.0.tar.xz
Source0  : http://download.qt.io/official_releases/qt/5.10/5.10.0/submodules/qtx11extras-everywhere-src-5.10.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.3 GPL-2.0 GPL-3.0 LGPL-2.1 LGPL-3.0
Requires: qtx11extras-lib
BuildRequires : cmake
BuildRequires : mesa-dev
BuildRequires : pkgconfig(Qt5Gui)
BuildRequires : pkgconfig(Qt5Test)
BuildRequires : pkgconfig(Qt5Widgets)
BuildRequires : pkgconfig(xcb)
BuildRequires : qtbase-dev

%description
No detailed description available

%package dev
Summary: dev components for the qtx11extras package.
Group: Development
Requires: qtx11extras-lib
Provides: qtx11extras-devel

%description dev
dev components for the qtx11extras package.


%package lib
Summary: lib components for the qtx11extras package.
Group: Libraries

%description lib
lib components for the qtx11extras package.


%prep
%setup -q -n qtx11extras-everywhere-src-5.10.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
qmake QMAKE_CFLAGS="$CFLAGS" QMAKE_CXXFLAGS="$CXXFLAGS" QMAKE_LFLAGS="$LDFLAGS" \
    QMAKE_CFLAGS_RELEASE= QMAKE_CXXFLAGS_RELEASE=
test -r config.log && cat config.log
make  %{?_smp_mflags}

%install
make INSTALL_ROOT=%{buildroot} install

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
/usr/lib64/libQt5X11Extras.la
/usr/lib64/libQt5X11Extras.prl
/usr/lib64/libQt5X11Extras.so
/usr/lib64/pkgconfig/Qt5X11Extras.pc
/usr/lib64/qt5/mkspecs/modules/qt_lib_x11extras.pri
/usr/lib64/qt5/mkspecs/modules/qt_lib_x11extras_private.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libQt5X11Extras.so.5
/usr/lib64/libQt5X11Extras.so.5.10
/usr/lib64/libQt5X11Extras.so.5.10.0
