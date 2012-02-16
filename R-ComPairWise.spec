%global packname  ComPairWise
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          1.01
Release:          1
Summary:          Compare phylogenetic or population genetic data alignments
Group:            Sciences/Mathematics
License:          GNU GPL
URL:              http://cran.r-project.org/web/packages/ComPairWise/index.html
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
