Name:		python-pyrfc3339
Version:	2.1.1
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/p/pyrfc3339/pyRFC3339-%{version}.tar.gz
Summary:	Generate and parse RFC 3339 timestamps
URL:		https://pypi.org/project/pyrfc3339/
License:	MIT
Group:		Development/Python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildRequires:	python%{pyver}dist(wheel)
BuildArch:	noarch

%description
Generate and parse RFC 3339 timestamps

%prep
%autosetup -p1 -n pyrfc3339-%{version}

%build
export SETUPTOOLS_SCM_PRETEND_VERSION="%{version}"
%py_build

%install
%py_install

%files
%{py_sitedir}/pyrfc3339
%{py_sitedir}/pyrfc3339-%{version}.dist-info
