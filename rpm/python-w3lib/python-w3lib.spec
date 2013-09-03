%if 0%{?fedora} < 13 || 0%{?rhel} < 6
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}
%endif

%global tarball_name w3lib 

Name:           python-w3lib
Version:        1.3
Release:        1%{?dist}
Summary:        Library of web-related functions

Group:          Development/Languages
License:        BSD
URL:            https://github.com/scrapy/w3lib
Source0:        https://pypi.python.org/packages/source/w/%{tarball_name}/%{tarball_name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  python-devel python-setuptools

%description
This is a Python library of web-related functions, such as:
  remove comments, or tags from HTML snippets
  extract base url from HTML snippets
  translate entites on HTML strings
  encoding mulitpart/form-data
  convert raw HTTP headers to dicts and vice-versa
  construct HTTP auth header
  converting HTML pages to unicode
  RFC-compliant url joining
  sanitize urls (like browsers do)
  extract arguments from urls

%prep
%setup -qn %{tarball_name}-%{version}


%build
%{__python} setup.py build


%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

 
%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{python_sitelib}/*


%changelog
* Mon Sep 02 2013 Daniel Bruno dbruno@fedoraproject.org - 0.18.1-1
- First version of RPM Package of w3lib
