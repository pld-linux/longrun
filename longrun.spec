Summary:	Utility to manage Transmeta Crusoe LongRun settings
Summary(pl.UTF-8):	Narzędzie do zarządzania ustawieniami LongRun procesorów Transmeta Crusoe
Name:		longrun
Version:	0.9
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	ftp://ftp.kernel.org/pub/linux/utils/cpu/crusoe/%{name}-%{version}.tar.bz2
# Source0-md5:	046a0e3f783d1d50b11a24b309bd40b1
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The longrun utility is used to control and query LongRun settings on
Transmeta Crusoe processors.

%description -l pl.UTF-8
Narzędzie longrun służy do sterowania i odczytywania ustawień LongRun
procesorów Transmeta Crusoe.

%prep
%setup -q -n %{name}

%build
%{__cc} %{rpmldflags} -o longrun %{rpmcflags} -Wall longrun.c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man8

# use */sbin and man8 - it needs uid 0
install -D longrun $RPM_BUILD_ROOT%{_sbindir}/longrun
sed -e 's/LONGRUN 1/LONGRUN 8/' longrun.1 >$RPM_BUILD_ROOT%{_mandir}/man8/longrun.8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/longrun
%{_mandir}/man8/longrun.8*
