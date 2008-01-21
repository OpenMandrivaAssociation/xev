Name:		xev
Version:	1.0.2
Release:	%mkrel 3
Summary:	Print contents of X events
Group:		Development/X11
Source:		http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License:	MIT
BuildRoot:	%{_tmppath}/%{name}-root

BuildRequires:	x11-util-macros	>= 1.1.5
BuildRequires:	libx11-devel	>= 1.1.3

%description
Xev creates a window and then asks the X server to send it events whenever
anything happens to the window (such as it being moved, resized, typed in,
clicked in, etc.). It is useful for testing input devices.

%prep
%setup -q -n %{name}-%{version}

%build
%configure	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/xev
%{_mandir}/man1/xev.1x*
