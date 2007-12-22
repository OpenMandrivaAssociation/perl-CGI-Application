%define module	CGI-Application
%define name	perl-%{module}
%define version	4.06
%define release	%mkrel 2

Name:		%{name}
Version: 	%{version}
Release:	%{release}
Summary:	Framework for building reusable web-applications
License: 	GPL or Artistic
Group:		Development/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/CGI/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}/
Requires: 	perl-HTML-Template
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(CGI)
BuildRequires:	perl(HTML::Template)
BuildArch: 	noarch
BuildRoot: 	%{_tmppath}/%{name}-%{version}

%description
%{module} is intended to make it easier to create sophisticated,
reusable web-based applications. This module implements a methodology
which, if followed, will make your web software easier to design,
easier to document, easier to write, and easier to evolve.

%prep
%setup -q -n %{module}-%{version}
chmod 755 Examples/Mailform/mailform.cgi

%build
 %{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
%{__rm} -rf %{buildroot}
%{makeinstall_std}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README Examples
%{perl_vendorlib}/CGI
%{_mandir}/*/*



