Name:		sessreg
Version:	1.1.4
Release:	1
Summary:	Manage utmp/wtmp entries for non-init clients
Group:		Development/X11
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.xz
License:	MIT

BuildRequires:	pkgconfig(x11)
BuildRequires:	x11-util-macros >= 1.0.1

%description
Sessreg is a simple program for managing utmp/wtmp entries for xdm sessions.

%prep
%autosetup -p1

%build
%configure \
	--x-includes=%{_includedir}\
	--x-libraries=%{_libdir}

%make_build

%install
%make_install

%files
%{_bindir}/sessreg
%doc %{_mandir}/man1/sessreg.*
