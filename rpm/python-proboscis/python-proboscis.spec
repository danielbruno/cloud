%global tarball_name proboscis

Name:           python-proboscis
Version:        1.2.6.0
Release:        0%{?dist}
Summary:        Proboscis is a Python test framework that extends Python's built-in unittest

Group:          Development/Languages
License:        ASL 2.0
URL:            https://github.com/rackerlabs/python-proboscis
Source0:        https://pypi.python.org/packages/source/p/%{tarball_name}/%{tarball_name}-%{version}.tar.gz
Source1:        LICENSE_PROBOSCIS
BuildArch:      noarch
BuildRequires:  python2-devel python-setuptools
Requires:       python-nose 

%description
Proboscis is a Python test framework that extends Python’s built-in unittest
module and Nose with features from TestNG, such as:

- Uses decorators instead of naming conventions.
- Allows for TestNG style test methods, in which a class is initialized once
  as an alternative to using class fields (see the example below).
- Allows for explicit test dependencies and skipping of dependent tests
  on failures.
- Runs xUnit style clases if desired or needed for backwards compatability.
- Uses Nose if available (but doesn't require it), and works with many of
  its plugins.
- Runs in IronPython and Jython (although if you're targetting the JVM you
  should consider using TestNG instead).


%prep
%setup -qn %{tarball_name}-%{version}
rm -fr %{tarball_name}.egg-info
mv README.rst README

%build
%{__python2} setup.py build


%install
rm -rf %{buildroot}
%{__python2} setup.py install -O1 --skip-build --root %{buildroot}
%{__install} -p -m644 %SOURCE1 LICENSE

%files
%{python2_sitelib}/*
%doc README LICENSE

%changelog
