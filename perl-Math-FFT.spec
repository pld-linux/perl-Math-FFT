#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Math
%define		pnam	FFT
Summary:	Math::FFT - Perl module to calculate Fast Fourier Transforms
Summary(pl.UTF-8):	Math::FFT - moduł Perla do obliczania szybkiej transformaty Fouriera
Name:		perl-Math-FFT
Version:	0.26
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	8d4c842169a8697cc92e7e0281dd528f
Patch0:		%{name}-types.patch
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module implements some algorithms for calculating Fast Fourier
Transforms for one-dimensional data sets of size 2^n.

%description -l pl.UTF-8
Ten moduł zawiera implementacje algorytmów do obliczania szybkiej
transformaty Fouriera dla jednowymiarowych zbiorów danych rozmiaru
2^n.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Math/FFT.pm
%dir %{perl_vendorarch}/auto/Math/FFT
%{perl_vendorarch}/auto/Math/FFT/FFT.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Math/FFT/FFT.so
%{_mandir}/man3/*