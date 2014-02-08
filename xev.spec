Name:		xev
Version:	1.2.0
Release:	3
Summary:	Print contents of X events
Group:		Development/X11
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License:	MIT

BuildRequires: pkgconfig(x11) >= 1.0.0
BuildRequires: pkgconfig(xrandr) >= 1.2
BuildRequires: x11-util-macros >= 1.0.1

%description
Xev creates a window and then asks the X server to send it events whenever
anything happens to the window (such as it being moved, resized, typed in,
clicked in, etc.). It is useful for testing input devices.

%prep
%setup -q -n %{name}-%{version}

%build
autoreconf -fi
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
%makeinstall_std

%files
%{_bindir}/xev
%{_mandir}/man1/xev.*


%changelog
* Mon Feb 27 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.2.0-1
+ Revision: 781032
- BR:pkgconfig(xrandr)
- version update 1.2.0

* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1.0-2
+ Revision: 671305
- mass rebuild

* Tue Nov 02 2010 Thierry Vignaud <tv@mandriva.org> 1.1.0-1mdv2011.0
+ Revision: 591821
- new release

* Wed Nov 11 2009 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.0.4-1mdv2010.1
+ Revision: 464706
- New version: 1.0.4
  fflush patch integrated upstream

* Thu Mar 19 2009 Olivier Blin <blino@mandriva.org> 1.0.3-4mdv2009.1
+ Revision: 357765
- flush stdout after each event, so that output is not be buffered when used in scripts (patch from Debian)

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.0.3-3mdv2009.1
+ Revision: 351199
- rebuild

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 1.0.3-2mdv2009.0
+ Revision: 266085
- rebuild early 2009.0 package (before pixel changes)

* Wed Apr 16 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.3-1mdv2009.0
+ Revision: 194818
- Update to version 1.0.3.
- Revert to use upstream tarball, build requires and remove non mandatory local patches.

* Mon Jan 21 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.2-3mdv2008.1
+ Revision: 155802
- Updated BuildRequires and resubmit package.

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Aug 31 2007 Adam Williamson <awilliamson@mandriva.org> 1.0.2-2mdv2008.0
+ Revision: 76515
- rebuild for 2008
- add a line to description
- minor spec clean

  + Thierry Vignaud <tv@mandriva.org>
    - do not hardcode lzma extension!!!

