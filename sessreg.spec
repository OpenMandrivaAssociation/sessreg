Name:		sessreg
Version:	1.1.0
Release:	4
Summary:	Manage utmp/wtmp entries for non-init clients
Group:		Development/X11
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License:	MIT

BuildRequires:	pkgconfig(x11)
BuildRequires:	x11-util-macros >= 1.0.1

%description
Sessreg is a simple program for managing utmp/wtmp entries for xdm sessions.

%prep
%setup -q

%build
%configure \
	--x-includes=%{_includedir}\
	--x-libraries=%{_libdir}

%make

%install
%makeinstall_std

%files
%{_bindir}/sessreg
%{_mandir}/man1/sessreg.*
