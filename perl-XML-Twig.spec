Name:           perl-XML-Twig
Version:        3.34
Release:        1%{?dist}
Summary:        A perl module for processing huge XML documents in tree mode

Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/XML-Twig/
Source0:        http://www.cpan.org/authors/id/M/MI/MIROD/XML-Twig-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(XML::Parser) >= 2.23
BuildRequires:  perl(Tie::IxHash)
BuildRequires:  perl(XML::XPathEngine)
BuildRequires:  perl(XML::XPath)
#BuildRequires:  perl(Tree::XPathEngine) # not available in Fedora yet
BuildRequires:  perl(HTML::TreeBuilder)
BuildRequires:  perl(Text::Wrap)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(XML::Simple)
#BuildRequires:  perl(XML::Handler::YAWriter) # not available in Fedora yet
BuildRequires:  perl(XML::SAX::Writer)
BuildRequires:  perl(XML::Filter::BufferText)
BuildRequires:  perl(IO::Scalar)
BuildRequires:  perl(Unicode::Map8)
BuildRequires:  perl(Unicode::String)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter:
%filter_from_provides /perl(XML::XPathEngine::NodeSet)/d
%filter_from_requires /perl(XML::XPath)/d
%perl_default_filter
}

%description
This module provides a way to process XML documents. It is build on
top of XML::Parser.  XML::Twig offers a tree interface to the
document, while allowing you to output the parts of it that have been
completely processed.  It allows minimal resource (CPU and memory)
usage by building the tree only for the parts of the documents that
need actual processing, through the use of the twig_roots and
twig_print_outside_roots options.


%prep
%setup -q -n XML-Twig-%{version}


%build
%{__perl} Makefile.PL -y INSTALLDIRS=vendor
make %{?_smp_mflags}

cp Changes Changes.orig
iconv -f iso88591 -t utf8 < Changes.orig > Changes

%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc Changes README
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/man1/*.1*
%{_mandir}/man3/*.3pm*


%changelog
* Tue Jan 19 2010 Chris Weyl <cweyl@alumni.drew.edu> 3.34-1
- update prov/dep filtering to current guidelines
- auto-update to 3.34 (by cpan-spec-update 0.01)
- added a new br on perl(ExtUtils::MakeMaker) (version 0)
- altered br on perl(XML::Parser) (0 => 2.23)

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 3.33-2
- rebuild against perl 5.10.1

* Mon Oct 19 2009 Marcela Mašláňová <mmaslano@redhat.com> - 3.33-1
- new development release which should fix various bug reports e.g. 529220

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.32-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Mar  2 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 3.32-1
- update to 3.32

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 3.29-6
- Rebuild for perl 5.10 (again)

* Mon Jan 28 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 3.29-5
- rebuild for new perl

* Sun Jul 08 2007 Robin Norwood <rnorwood@redhat.com> - 3.29-4
- Resolves: rhbz#247247
- Remove bogus Provides: perl(XML::XPathEngine::NodeSet), and move
  Requires filter into spec file.

* Thu Jun 28 2007 Robin Norwood <rnorwood@redhat.com> - 3.29-3
- Add several buildrequires for tests and optional features

* Sat Feb 17 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 3.29-2
- Minor cleanups.

* Tue Feb 13 2007 Robin Norwood <rnorwood@redhat.com> - 3.29-1
- New version: 3.29

* Mon Jul 17 2006 Jason Vas Dias <jvdias@redhat.com> - 3.26-1
- Upgrade to 3.26

* Mon Jun 05 2006 Jason Vas Dias <jvdias@redhat.com> - 3.25-1
- Upgrade to 3.25

* Fri Feb 03 2006 Jason Vas Dias <jvdias@redhat.com> - 3.22-1.1
- Update to 3.23
- rebuild for new perl-5.8.8

* Mon Dec 19 2005 Jason Vas Dias<jvdias@redhat.com> - 3.22-1
- Update to 3.22

* Fri Dec 16 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt for new gcc

* Sun Apr 17 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 3.17-1
- Update to 3.17.
- Specfile cleanup. (#155168)

* Wed Sep 22 2004 Chip Turner <cturner@redhat.com> 3.13-6
- rebuild

* Mon May  3 2004 Chip Turner <cturner@redhat.com> 3.13-5
- bugzilla 122079, add dep filter to remove bad dependency

* Fri Apr 23 2004 Chip Turner <cturner@redhat.com> 3.13-4
- remove Packager tag

* Fri Apr 23 2004 Chip Turner <cturner@redhat.com> 3.13-2
- bump

* Fri Feb 13 2004 Chip Turner <cturner@redhat.com> 3.13-1
- update to 3.13

* Tue Dec 10 2002 Chip Turner <cturner@redhat.com>
- update to latest version from CPAN

* Mon Aug 26 2002 Chip Turner <cturner@redhat.com>
- rebuild for build failure

* Tue Aug  6 2002 Chip Turner <cturner@redhat.com>
- automated release bump and build

* Wed May 29 2002 cturner@redhat.com
- Specfile autogenerated
