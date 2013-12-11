%global tarball_name elasticsearch 

Name:           python-elasticsearch
Version:        0.4.3
Release:        2%{?dist}
Summary:        Client for Elasticsearch 

Group:          Development/Languages
License:        ASL 2.0
URL:            https://github.com/elasticsearch/elasticsearch-py
Source0:        https://pypi.python.org/packages/source/e/%{tarball_name}/%{tarball_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python2-devel python-setuptools
Requires:       python-thrift
Requires:       python-urllib => 3

%description
Low level client for Elasticsearch. It's goal is to provide common ground
for all Elasticsearch-related code in Python. The client's features include:

- Translating basic Python data types to and from json
- Configurable automatic discovery of cluster nodes
- Persistent connections
- Load balancing (with pluggable selection strategy) across all available nodes
- Failed connection penalization (time based - failed connections won't be
  retried until a timeout is reached)
- Thread safety
- Pluggable architecture

%prep
%setup -qn %{tarball_name}-%{version}
rm -fr %{tarball_name}.egg-info
rm README
cp README.rst README 

%build
%{__python2} setup.py build


%install
rm -rf %{buildroot}
%{__python2} setup.py install -O1 --skip-build --root %{buildroot}

%files
%{python2_sitelib}/*
%doc README LICENSE

%changelog
* Wed Dec 11 2013 Daniel Bruno <dbruno@fedoraproject.org> - 0.4.3-2
- Fixing lib require

* Tue Nov 26 2013 Daniel Bruno <dbruno@fedoraproject.org> - 0.4.3-1
- First RPM release

