Name:		python-pyrfc3339
Version:	1.1
Release:	3
Source0:	https://files.pythonhosted.org/packages/source/p/pyrfc3339/pyRFC3339-%{version}.tar.gz
Summary:	Generate and parse RFC 3339 timestamps
URL:		https://pypi.org/project/pyrfc3339/
License:	MIT
Group:		Development/Python
BuildRequires:	python%{pyver}dist(pip)
BuildArch:	noarch

%description
Generate and parse RFC 3339 timestamps

%prep
%autosetup -p1 -n pyRFC3339-%{version}

%build
%py_build

%install
%py_install

%files
%{py_sitedir}/pyrfc3339
%{py_sitedir}/pyRFC3339-*.*-info
