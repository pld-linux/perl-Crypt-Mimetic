#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	Crypt
%define	pnam	Mimetic
Summary:	Crypt::Mimetic - Crypt a file and mask it behind another file
Summary(pl):	Modu³ Crypt::Mimetic - szyfruj±cy plik i ukrywaj±cy go w innym
Name:		perl-Crypt-Mimetic
Version:	0.02
Release:	2
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	8c37e1950f944d1259c238c73af4e705
BuildRequires:	perl-devel >= 5.6
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl-Error
BuildRequires:	perl-Term-ReadKey
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module allows you to hide a file by encrypting in and then
attaching it to another file of your choice. This mimetic file then
looks and behaves like a normal file, and can be stored, used or
emailed without attracting attention.

%description -l pl
Ten modu³ pozwala na ukrycie pliku poprzez zaszyfrowanie i do³±czenie
do innego wybranego pliku. Taki plik wygl±da i zachowuje siê jak
normalny, mo¿e byæ zapisywany, u¿ywany albo przesy³any bez
przyci±gania uwagi.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{perl_vendorlib}/%{pdir}/%{pnam}
%{perl_vendorlib}/Error/*.pm
%{_bindir}/*
%{_mandir}/man[13]/*
