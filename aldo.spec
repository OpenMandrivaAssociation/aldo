Name: 		aldo
Version: 	0.7.8
Summary: 	Console-based morse tutor 
Release: 	1
License: 	GPLv2+
Group: 		Networking/Other 
Url: 		https://www.nongnu.org/aldo
Source0: 	http://savannah.nongnu.org/download/aldo/%{name}-%{version}.tar.bz2
BuildRequires:	libao-devel
BuildRequires:	readline-devel

%description
Console-based morse tutor which has four kinds of exercises:
*  Classic exercise: With this exercise you must guess some random 
   strings of characters that aldo plays in morse code
*  Koch method
*  Read from file (text file)
*  Callsign exercise (random callsigns)

%prep
%autosetup -p1
[ -e configure ] || sh bootstrap

%build
%configure
%make_build

%install
%make_install

%files -n %{name}
%doc AUTHORS ChangeLog NEWS README THANKS
%{_bindir}/aldo
%{_mandir}/man1/aldo*
