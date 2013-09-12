%global tarball_name pyrax 

Name:           python-pyrax
Version:        1.5.0
Release:        1%{?dist}
Summary:        Python SDK for OpenStack/Rackspace APIs

Group:          Development/Languages
License:        MIT
URL:            https://github.com/rackspace/pyrax
Source0:        https://pypi.python.org/packages/source/p/%{tarball_name}/%{tarball_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel python-setuptools

%description
pyrax should work with most OpenStack-based cloud deployments, though it
specifically targets the Rackspace public cloud. For example, the code for
cloudfiles contains the ability to publish your content on Rackspace's CDN
network, even though CDN support is not part of OpenStack Swift. But if you
don't use any of the CDN-related code, your app will work fine on any standard
Swift deployment.


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
* Wed Sep 11 2013 Daniel Bruno <dbruno@fedoraproject.org> - 1.5.0-1
- Initial spec file for Fedora

