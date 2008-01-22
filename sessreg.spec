Name: sessreg
Version: 1.0.3
Release: %mkrel 2
Summary: Manage utmp/wtmp entries for non
Group: Development/X11
Source: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: x11-util-macros	>= 1.1.5
BuildRequires: x11-proto-devel	>= 7.3

%description
Sessreg is a simple program for managing utmp/wtmp entries for xdm sessions.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/sessreg
%{_mandir}/man1/sessreg.*
