Name: 		aldo
Version: 	0.7.7
Summary: 	Console-based morse tutor 
Release: 	%mkrel 1
License: 	GPLv2+
Group: 		Networking/Other 
Url: 		http://www.nongnu.org/aldo
Source0: 	http://savannah.nongnu.org/download/aldo/%{name}-%{version}.tar.bz2
Source1:	http://savannah.nongnu.org/download/aldo/%{name}-%{version}.tar.bz2.sig
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
%makeinstall_std

%files -n %{name}
%doc AUTHORS ChangeLog NEWS README THANKS
%{_bindir}/aldo
%{_mandir}/man1/aldo*


%changelog
* Tue Jun 05 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.7.7-1mdv2012.0
+ Revision: 802629
- version update 0.7.7

* Wed Oct 13 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.7.6-1mdv2011.0
+ Revision: 585391
- add signature
- new version 0.7.6

* Wed Oct 06 2010 Jani Välimaa <wally@mandriva.org> 0.7.5-2mdv2011.0
+ Revision: 583573
- more spec cleaning
  - fix summary and description
  - fix license
  - drop unused patch
  - fix requires
  - use %%configure2_5x, %%make and  %%makeinstall_std

* Tue Oct 05 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.7.5-1mdv2011.0
+ Revision: 583034
- fixed the --prefix bug
- cleaned spec
- cleaned spec
- Initial upload
- Initial upload
- Created package structure for aldo.

