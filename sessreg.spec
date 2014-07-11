Name:		sessreg
Version:	1.0.8
Release:	11
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
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
%makeinstall_std

%files
%{_bindir}/sessreg
%{_mandir}/man1/sessreg.*


%changelog
* Mon Feb 20 2012 abf
- The release updated by ABF

* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.6-2mdv2011.0
+ Revision: 669968
- mass rebuild

* Wed Jul 21 2010 Thierry Vignaud <tv@mandriva.org> 1.0.6-1mdv2011.0
+ Revision: 556465
- new release

* Wed Nov 11 2009 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.0.5-1mdv2010.1
+ Revision: 464640
- New version: 1.0.5

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.0.4-3mdv2010.0
+ Revision: 427067
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.0.4-2mdv2009.1
+ Revision: 351527
- rebuild

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 1.0.4-1mdv2009.0
+ Revision: 219398
- new release
- fix summary

* Tue Feb 12 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.3-3mdv2008.1
+ Revision: 166416
- Revert to use upstream tarball, build requires and remove non mandatory local patches.

* Tue Jan 22 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.3-2mdv2008.1
+ Revision: 156430
- Updated BuildRequires and resubmit package.

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Aug 20 2007 Thierry Vignaud <tv@mandriva.org> 1.0.3-1mdv2008.0
+ Revision: 67222
- new release


* Thu Dec 14 2006 Thierry Vignaud <tvignaud@mandriva.com> 1.0.2-1mdv2007.0
+ Revision: 97065
- new release
- new release
- fix description

  + Gustavo Pichorim Boiko <boiko@mandriva.com>
    - rebuild to fix cooker uploading
    - increment release
    - Adding X.org 7.0 to the repository

  + Andreas Hasenack <andreas@mandriva.com>
    - renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

