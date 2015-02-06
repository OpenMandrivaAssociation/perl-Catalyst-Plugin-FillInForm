%define upstream_name	 Catalyst-Plugin-FillInForm
%define upstream_version 0.12

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	FillInForm for Catalyst
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Catalyst) >= 2.99
BuildRequires:	perl(Catalyst::Action::RenderView)
BuildRequires:	perl(HTML::FillInForm)
BuildArch:	noarch

%description
Fill forms automatically, based on data from a previous HTML
form. Typically (but not necessarily) used in conjunction with
Catalyst::Plugin::FormValidator. This module automatically inserts
data from a previous HTML form into HTML input fields, textarea
fields, radio buttons, checkboxes, and select tags. It is an instance
of HTML::FillInForm, which itself is a subclass of HTML::Parser, which
it uses to parse the HTML and insert the values into the proper form
tags.

The usual application is after a user submits an HTML form without
filling out a required field, or with errors in fields having
specified constraints. FillInForm is used to redisplay the HTML form
with all the form elements containing the submitted info. FillInForm
can also be used to fill forms with data from any source,
e.g. directly from your database.


%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor <<EOF
EOF
%make

%check
make test

%install
%makeinstall_std

%files 
%doc Changes README
%{_mandir}/*/*
%{perl_vendorlib}/Catalyst


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.120.0-2mdv2011.0
+ Revision: 680733
- mass rebuild

* Sun Jul 12 2009 Jérôme Quelin <jquelin@mandriva.org> 0.120.0-1mdv2011.0
+ Revision: 395091
- update to 0.12
- using %%perl_convert_version
- fixed license field

* Sun Jan 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.10-1mdv2009.1
+ Revision: 324467
- update to new version 0.10

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.09-2mdv2009.0
+ Revision: 268393
- rebuild early 2009.0 package (before pixel changes)

* Tue May 06 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.09-1mdv2009.0
+ Revision: 201843
- update to new version 0.09

* Tue Apr 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.08-1mdv2009.0
+ Revision: 194195
- update to new version 0.08

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.06-2mdv2008.0
+ Revision: 86031
- rebuild


* Fri Jan 20 2006 Scott Karns <scott@karnstech.com> 0.06-1mdk
- Initial Mdv release

