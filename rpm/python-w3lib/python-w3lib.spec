%global tarball_name w3lib 

Name:           python-w3lib
Version:        1.3
Release:        2%{?dist}
Summary:        Library of web-related functions

Group:          Development/Languages
License:        BSD
URL:            https://github.com/scrapy/w3lib
Source0:        https://pypi.python.org/packages/source/w/%{tarball_name}/%{tarball_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel python-setuptools

%description
This is a Python library of web-related functions, such as:
- Remove comments, or tags from HTML snippets
- Extract base url from HTML snippets
- Translate entites on HTML strings
- Encoding mulitpart/form-data
- Convert raw HTTP headers to dicts and vice-versa
- Construct HTTP auth header
- Converting HTML pages to unicode
- RFC-compliant url joining
- Sanitize urls (like browsers do)
- Extract arguments from urls

%prep
%setup -qn %{tarball_name}-%{version}


%build
%{__python2} setup.py build


%install
rm -rf %{buildroot}
%{__python2} setup.py install -O1 --skip-build --root %{buildroot}


%files
%{python2_sitelib}/*


%changelog
* Mon Sep 09 2013 Daniel Bruno <dbruno@fedoraproject.org> - 1.3-2
- Adjusting the spec for Fedora patterns

* Mon Sep 02 2013 Daniel Bruno <dbruno@fedoraproject.org> - 1.3-1 
- First version of RPM Package of w3lib
