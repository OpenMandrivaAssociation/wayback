Name:		wayback
Version:	0.2
Release:	1
Source0:	https://gitlab.freedesktop.org/wayback/wayback/-/archive/%{version}/%{name}-%{version}.tar.gz
Summary:	X11 compatibility layer leveraging wlroots and Xwayland
URL:		https://gitlab.freedesktop.org/wayback/wayback
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

%description
%summary.

%prep
%autosetup -p1

%files
%license LICENSE
%doc README.md
%{_bindir}/X%{name}
%{_bindir}/%{name}-session
%{_mandir}/man1/*
%{_libexecdir}/%{name}-compositor
