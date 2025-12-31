Name:		wayback
Version:	0.3
Release:	1
Summary:	X11 compatibility layer leveraging wlroots and Xwayland
URL:		https://gitlab.freedesktop.org/wayback/wayback
Source:		https://gitlab.freedesktop.org/wayback/wayback/-/archive/%{version}/%{name}-%{version}.tar.gz
# fix wayland-session -sesscmd
# https://gitlab.freedesktop.org/wayback/wayback/-/merge_requests/89
Patch:		0001-wayback-session-fix-sesscmd-handling.patch
License:	MIT
Group:		System/Wayland

BuildSystem:	meson

BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(xwayland)
BuildRequires:  pkgconfig(wlroots-0.19)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(scdoc)

Requires:       xwayland

%description
%{summary}.

%files
%license LICENSE
%doc README.md
%{_bindir}/X%{name}
%{_bindir}/%{name}-session
%{_mandir}/man1/*
%{_libexecdir}/%{name}-compositor

%dnl ----------------------------------------------------------------

%package	xserver
Summary:	%{name} shim to provide /usr/bin/X
Requires:	%{name} = %{EVRD}
Provides:	Xserver
Provides:	x11-server
Conflicts:	x11-server
Conflicts:	x11-server-xorg
Conflicts:	xlibre-xorg

%description	xserver
This package provides the shim links for %{name} to be automatically
used as the Xserver. This ensures that %{name} is used as the system
provider of the Xserver.

%files xserver
%{_bindir}/X

%dnl ----------------------------------------------------------------


%install -a
# Allow Xwayback to be called as X
ln -sr %{buildroot}%{_bindir}/Xwayback %{buildroot}%{_bindir}/X
