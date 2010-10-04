Name: 		aldo
Version: 	0.7.5
Summary: 	aldo is a console-based morse tutor 
Release: 	%mkrel 1
License: 	GPL
Group: 		Networking/Other 
Url: 		http://www.nongnu.org/aldo
Source: 	%{name}-%{version}.tar.bz2
Patch0:  	cwtone_rise_fall.diff
BuildRequires:  libao-devel readline-devel
Requires: 	libao




%description
aldo  is a morse tutor released under GPL.
At this moment Aldo has four kinds of exercises:
*  Classic exercise: With this exercies you must guess some random 
   strings of characters that aldo plays in morse code
*  Koch method
*  Read from file (text file)
*  Callsign exercies (random callsigns)

Prefix: /usr

%prep
rm -rf $RPM_BUILD_ROOT 
mkdir $RPM_BUILD_ROOT

%setup -q
#%patch0 -p1

%build
CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" \
./configure --prefix=%{prefix} || cat config.log
echo "################"
#cat config.log || true
echo "################"
make

%install

%makeinstall



%post


%clean


%files -n %{name}
%defattr(-,root,root,0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README THANKS
%{_bindir}/aldo
%{_mandir}/man1/aldo*


