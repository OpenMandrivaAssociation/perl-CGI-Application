%define upstream_name	 CGI-Application
%define upstream_version 4.21

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Framework for building reusable web-applications
License: 	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/CGI/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl(CGI)
BuildRequires:	perl(HTML::Template)
Requires:	    perl(CGI)
Requires: 	    perl(HTML::Template)
BuildArch: 	noarch
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}

%description
%{upstream_name} is intended to make it easier to create sophisticated,
reusable web-based applications. This module implements a methodology
which, if followed, will make your web software easier to design,
easier to document, easier to write, and easier to evolve.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
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
