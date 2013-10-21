%global tarball_name mandrill 

Name:           python-mandrill
Version:        1.0.51
Release:        2%{?dist}
Summary:        A CLI client and API library for Mandrill email service

Group:          Development/Languages
License:        ASL 2.0
URL:            https://bitbucket.org/mailchimp/mandrill-api-python/
Source0:        https://pypi.python.org/packages/source/m/%{tarball_name}/%{tarball_name}-%{version}.tar.gz
Source1:		LICENSE_MANDRILL
BuildArch:      noarch
BuildRequires:  python2-devel python-setuptools
Requires:       python-ujson python-docopt python-requests

%description
A Python API client and suite of CLI-based tools for the Mandrill email
as a platform service

%prep
%setup -qn %{tarball_name}-%{version}
rm -fr %{tarball_name}.egg-info

%build
%{__python2} setup.py build


%install
rm -rf %{buildroot}
%{__python2} setup.py install -O1 --skip-build --root %{buildroot}
%{__install} -p -m644 %SOURCE1 LICENSE

%files
%{python2_sitelib}/*
%{_bindir}/mandrill
%{_bindir}/sendmail.mandrill
%doc README LICENSE

%changelog
* Mon Oct 21 2013 Daniel Bruno <dbruno@fedoraproject.org> - 1.0.51-2
- Add license file from the upstream repo

* Tue Oct 01 2013 Daniel Bruno <dbruno@fedoraproject.org> - 1.0.51-1
- Initial package for Fedora

