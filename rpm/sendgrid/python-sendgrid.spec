%global tarball_name sendgrid

Name:           python-sendgrid
Version:        0.1.4
Release:        1%{?dist}
Summary:        SendGrid library for Python

Group:          Development/Languages
License:        MIT
URL:            https://github.com/sendgrid/sendgrid-python/
Source0:        https://pypi.python.org/packages/source/s/%{tarball_name}/%{tarball_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel python-setuptools
Requires:       python-simplejson
%description
This library allows to quickly and easily send emails through
SendGrid using Python.

%prep
%setup -qn %{tarball_name}-%{version}
rm -fr %{tarball_name}.egg-info
sed -i 's/\r$//' README.md

%build
%{__python2} setup.py build


%install
%{__python2} setup.py install -O1 --skip-build --root %{buildroot}


%files
%{python2_sitelib}/*
%doc README.md

%changelog
* Mon Sep 23 2013 Daniel Bruno <dbruno@fedoraproject.org> - 0.1.4-1
- Initial package for Fedora

