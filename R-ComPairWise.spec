%global packname  ComPairWise
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          1.01
Release:          1
Summary:          Compare phylogenetic or population genetic data alignments
Group:            Sciences/Mathematics
License:          GNU GPL
URL:              None
Source0:          http://cran.r-project.org/src/contrib/Archive/ComPairWise/ComPairWise_1.01.tar.gz
BuildArch:        noarch
Requires:         R-core
BuildRequires:    R-devel texlive-collection-latex 
%rename R-cran-ComPairWise

%description
ComPairWise contains functions to compare DNA/RNA alignments.
%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/help


%changelog
* Thu Feb 16 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.01-1
+ Revision: 774624
- Update and rebuild with R2spec
- Update and rebuild with R2spec

* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.01-6mdv2011.0
+ Revision: 616439
- the mass rebuild of 2010.0 packages

* Tue Sep 08 2009 Thierry Vignaud <tv@mandriva.org> 1.01-5mdv2010.0
+ Revision: 433077
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 1.01-4mdv2009.0
+ Revision: 260126
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 1.01-3mdv2009.0
+ Revision: 248223
- rebuild

* Sun Feb 17 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.01-1mdv2008.1
+ Revision: 169917
- complete spec file
- fix Url
- add source and spec file
- Created package structure for R-cran-ComPairWise.

