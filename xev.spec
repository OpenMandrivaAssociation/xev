Name:		xev
Version:	1.2.0
Release:	1
Summary:	Print contents of X events
Group:		Development/X11
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License:	MIT

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: pkgconfig(xrandr) >= 1.2
BuildRequires: x11-util-macros >= 1.0.1

%description
Xev creates a window and then asks the X server to send it events whenever
anything happens to the window (such as it being moved, resized, typed in,
clicked in, etc.). It is useful for testing input devices.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
%makeinstall_std

%files
%{_bindir}/xev
%{_mandir}/man1/xev.*
