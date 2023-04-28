%{?opt_qt5_default_filter}

Summary: This module provides custom UI components and QML-accessible interfaces for Cutie UI/UX.
Name: qml-module-cutie
Version: 0.0.1
Release: 1%{?dist}

# See LGPL_EXCEPTIONS.txt, LICENSE.GPL3, respectively, for exception details
License: GPLv3
Url:     https://cutie-shell.org/
Source0: %{name}-%{version}.tar.bz2

BuildRequires: make
BuildRequires: opt-qt5-qtbase-devel >= 5.15
BuildRequires: pkgconfig(zlib)
BuildRequires: opt-qt5-qtbase-private-devel
BuildRequires: opt-qt5-qtdeclarative-devel >= 5.15
BuildRequires: pulseaudio-devel
Requires: opt-qt5-qtbase-gui >= 5.15

%description
%{summar}

%prep
%autosetup -n %{name}-%{version}/upstream


%build
export QTDIR=%{_opt_qt5_prefix}
touch .git

%{opt_qmake_qt5}

%make_build


%install
make install INSTALL_ROOT=%{buildroot}

%files
%{_opt_qt5_libdir}/qt5/qml/Cutie/Button.qml
%{_opt_qt5_libdir}/qt5/qml/Cutie/Label.qml
%{_opt_qt5_libdir}/qt5/qml/Cutie/ListItem.qml
%{_opt_qt5_libdir}/qt5/qml/Cutie/ListView.qml
%{_opt_qt5_libdir}/qt5/qml/Cutie/Menu.qml
%{_opt_qt5_libdir}/qt5/qml/Cutie/MenuItem.qml
%{_opt_qt5_libdir}/qt5/qml/Cutie/Page.qml
%{_opt_qt5_libdir}/qt5/qml/Cutie/PageHeader.qml
%{_opt_qt5_libdir}/qt5/qml/Cutie/PageStack.qml
%{_opt_qt5_libdir}/qt5/qml/Cutie/Slider.qml
%{_opt_qt5_libdir}/qt5/qml/Cutie/TextField.qml
%{_opt_qt5_libdir}/qt5/qml/Cutie/Tile.qml
%{_opt_qt5_libdir}/qt5/qml/Cutie/Toast.qml
%{_opt_qt5_libdir}/qt5/qml/Cutie/ToastHandler.qml
%{_opt_qt5_libdir}/qt5/qml/Cutie/Toggle.qml
%{_opt_qt5_libdir}/qt5/qml/Cutie/Window.qml
%{_opt_qt5_libdir}/qt5/qml/Cutie/libqmlcutieplugin.so
%{_opt_qt5_libdir}/qt5/qml/Cutie/qmldir
