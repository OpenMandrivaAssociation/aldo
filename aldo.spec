Name: 		aldo
Version: 	0.7.5
Summary: 	Console-based morse tutor 
Release: 	%mkrel 2
License: 	GPLv2+
Group: 		Networking/Other 
Url: 		http://www.nongnu.org/aldo
Source: 	http://savannah.nongnu.org/download/aldo/%{name}-%{version}.tar.bz2
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
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files -n %{name}
%defattr(-,root,root,0755)
%doc AUTHORS ChangeLog NEWS README THANKS
%{_bindir}/aldo
%{_mandir}/man1/aldo*
