%define module	Catalyst-Plugin-FillInForm
%define name	perl-%{module}
%define version 0.09
%define release %mkrel 2

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	FillInForm for Catalyst
License:	GPL or Artistic
Group:		Development/Perl
Source:		http://search.cpan.org/CPAN/authors/id/M/MR/MRAMBERG/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}/
BuildRequires:	perl(Catalyst) >= 2.99
BuildRequires:	perl(Catalyst::Action::RenderView)
BuildRequires:	perl(HTML::FillInForm)
Buildarch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

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
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor <<EOF
EOF
%make

%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc Changes README
%{_mandir}/*/*
%{perl_vendorlib}/Catalyst
