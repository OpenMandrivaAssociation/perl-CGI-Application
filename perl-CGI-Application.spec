%define upstream_name	 CGI-Application
%define upstream_version 4.50

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Framework for building reusable web-applications
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/CGI/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(CGI)
BuildRequires:	perl(Class::ISA)
BuildRequires:	perl(HTML::Template)
Requires:	    perl(CGI)
Requires: 	    perl(HTML::Template)
BuildArch: 	noarch

%description
%{upstream_name} is intended to make it easier to create sophisticated,
reusable web-based applications. This module implements a methodology
which, if followed, will make your web software easier to design,
easier to document, easier to write, and easier to evolve.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
chmod 755 Examples/Mailform/mailform.cgi

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README Examples
%{perl_vendorlib}/CGI
%{_mandir}/*/*


%changelog
* Fri Jun 24 2011 Guillaume Rousse <guillomovitch@mandriva.org> 4.500.0-1mdv2011.0
+ Revision: 686968
- update to new version 4.50

* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 4.310.0-2
+ Revision: 680667
- mass rebuild

* Tue Aug 04 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 4.310.0-1mdv2011.0
+ Revision: 408830
- update to 4.31

* Wed Jul 29 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 4.210.0-1mdv2010.0
+ Revision: 402995
- rebuild using %%perl_convert_version

* Sun Jan 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 4.21-1mdv2009.1
+ Revision: 324472
- update to new version 4.21

* Mon Nov 03 2008 Guillaume Rousse <guillomovitch@mandriva.org> 4.20-1mdv2009.1
+ Revision: 299374
- update to new version 4.20

* Fri Oct 10 2008 Guillaume Rousse <guillomovitch@mandriva.org> 4.11-2mdv2009.1
+ Revision: 291382
- fix dependencies

* Mon Aug 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 4.11-1mdv2009.0
+ Revision: 270885
- update to new version 4.11

* Thu Jun 19 2008 Guillaume Rousse <guillomovitch@mandriva.org> 4.10-1mdv2009.0
+ Revision: 226197
- update to new version 4.10

* Sat Dec 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 4.06-2mdv2008.1
+ Revision: 136902
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Oct 28 2006 Nicolas LÃ©cureuil <neoclust@mandriva.org> 4.06-1mdv2007.0
+ Revision: 73351
- import perl-CGI-Application-4.06-1mdk

* Sun Apr 16 2006 Guillaume Rousse <guillomovitch@mandriva.org> 4.06-1mdk
- New release 4.06
- better source URL

* Mon Mar 06 2006 Guillaume Rousse <guillomovitch@mandriva.org> 4.05-1mdk
- New release 4.05

* Tue Oct 18 2005 Guillaume Rousse <guillomovitch@mandriva.org> 4.04-1mdk
- New release 4.04
- spec cleanup
- fix directory ownership
- better summary

* Thu Aug 18 2005 Nicolas Lécureuil <neoclust@mandriva.org> 4.03-1mdk
- New release 4.03
- mkrel

* Fri Jun 24 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 4.01-1mdk
- 4.01
- manually require perl-base

* Tue Nov 16 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 3.31-1mdk
- 3.31

* Tue May 11 2004 Michael Scherer <misc@mandrake.org> 3.22-1mdk
- New release 3.22
- rpmbuildupdate aware

