Summary:	Latvian dictionary for aspell
Summary(pl.UTF-8):   Słownik łotewski dla aspella
Name:		aspell-lv
Version:	0.5.5
%define	subv	1
Release:	1
Epoch:		1
License:	GPL v2+
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/aspell/dict/lv/aspell6-lv-%{version}-%{subv}.tar.bz2
# Source0-md5:	cd120047c0b160a40361cbf03913e91f
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 3:0.60
Requires:	aspell >= 3:0.60
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Latvian dictionary (i.e. word list) for aspell.

%description -l pl.UTF-8
Słownik łotewski (lista słów) dla aspella.

%prep
%setup -q -n aspell6-lv-%{version}-%{subv}

%build
# note: configure is not autoconf-generated
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Copyright README
%{_libdir}/aspell/*
%{_datadir}/aspell/*
