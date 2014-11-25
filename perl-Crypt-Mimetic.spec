#
# Conditional build:
%bcond_without	tests	# Do not perform "make test"

%define		pdir	Crypt
%define		pnam	Mimetic
%include	/usr/lib/rpm/macros.perl
Summary:	Crypt::Mimetic - crypt a file and mask it behind another file
Summary(pl.UTF-8):	Crypt::Mimetic - szyfrowanie pliku i ukrywanie go w innym
Name:		perl-Crypt-Mimetic
Version:	0.02
Release:	4
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	8c37e1950f944d1259c238c73af4e705
URL:		http://search.cpan.org/dist/Crypt-Mimetic/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Error
BuildRequires:	perl-Term-ReadKey
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module allows you to hide a file by encrypting in and then
attaching it to another file of your choice. This mimetic file then
looks and behaves like a normal file, and can be stored, used or
emailed without attracting attention.

%description -l pl.UTF-8
Ten moduł pozwala na ukrycie pliku poprzez zaszyfrowanie i dołączenie
do innego wybranego pliku. Taki plik wygląda i zachowuje się jak
normalny, może być zapisywany, używany albo przesyłany bez
przyciągania uwagi.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{perl_vendorlib}/%{pdir}/%{pnam}
%{perl_vendorlib}/Error/*.pm
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man[13]/*
