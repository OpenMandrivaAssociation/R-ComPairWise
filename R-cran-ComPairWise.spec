%define modulename ComPairWise
%define realver 1.01
%define r_library %{_libdir}/R/library

Summary:	Compare phylogenetic or population genetic data alignments for R
Name:		R-cran-%{modulename}
Version:	%realver
Release:	%mkrel 6
License:	GPLv2+
Group:		Sciences/Mathematics
Url:		http://cran.r-project.org/web/packages/%{modulename}/index.html
Source0:	http://cran.r-project.org/src/contrib/%{modulename}_%{realver}.tar.gz
BuildRequires:	R-base
Requires:	R-base
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
ComPairWise contains functions to compare DNA/RNA alignments.

%prep
%setup -q -c

%build

R CMD build %{modulename}

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

mkdir -p %{buildroot}/%{r_library}

# (tpg) install
R CMD INSTALL %{modulename} --library=%{buildroot}/%{r_library}

# (tpg) provided by R-base
rm -rf %{buildroot}/%{r_library}/R.css

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{r_library}/%{modulename}
