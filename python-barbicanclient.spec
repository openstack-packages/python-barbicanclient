Name:           python-barbicanclient
Version:        XXX
Release:        XXX
Summary:        Client Library for OpenStack Barbican Key Management API

License:        ASL 2.0
URL:            https://pypi.python.org/pypi/python-barbicanclient
Source0:        https://pypi.python.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-pbr
BuildRequires:  python-setuptools

Requires:       python-setuptools
Requires:       python-requests
Requires:       python-six >= 1.9.0
Requires:       python-keystoneclient
Requires:       python-cliff
Requires:       python-oslo-i18n
Requires:       python-oslo-serialization
Requires:       python-oslo-utils
Requires:       python-iso8601
Requires:       python-babel
Requires:       python-oslo-config
Requires:       python-netaddr
Requires:       python-prettytable
Requires:       python-stevedore
Requires:       pyparsing
Requires:       python-cmd2
Requires:       pytz
Requires:       python-msgpack

%description
This is a client for the Barbican Key Management API. There is a
Python library for accessing the API (barbicanclient module), and
a command-line script (barbican).

%package doc
Summary: Documentation for OpenStack Barbican API client

BuildRequires:  python-sphinx
BuildRequires:  python-oslo-sphinx
BuildRequires:  python-oslo-utils
BuildRequires:  dos2unix
BuildRequires:  python-oslo-i18n
BuildRequires:  python-prettytable
BuildRequires:  python-keystoneclient

%description doc
Documentation for the barbicanclient module

%prep
%setup -q -n %{name}-%{upstream_version}
# let RPM handle deps
sed -i '/setup_requires/d; /install_requires/d; /dependency_links/d' setup.py

rm -rf {test-,}requirements.txt

%build
%{__python2} setup.py build
# doc
export PYTHONPATH="$( pwd ):$PYTHONPATH"
pushd doc
sphinx-build -b html -d build/doctrees   source build/html
popd
# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.buildinfo

%install
%{__python2} setup.py install --skip-build --root %{buildroot}
dos2unix doc/build/html/_static/jquery.js


%files
%license LICENSE
%doc AUTHORS CONTRIBUTING.rst README.rst PKG-INFO ChangeLog
%{_bindir}/barbican
%{python2_sitelib}/barbicanclient
%{python2_sitelib}/python_barbicanclient-%{upstream_version}-py?.?.egg-info

%files doc
%doc doc/build/html
%license LICENSE

%changelog
