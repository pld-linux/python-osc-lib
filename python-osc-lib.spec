#
# Conditional build:
%bcond_with	doc	# do build doc (missing deps)
%bcond_with	tests	# do perform "make test" (missing deps)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	OpenStackClient Library
Name:		python-osc-lib
Version:	1.7.0
Release:	6
License:	Apache
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/o/osc-lib/osc-lib-%{version}.tar.gz
# Source0-md5:	8bae654318c8c82d341f7228cfa3ec2d
URL:		https://pypi.python.org/pypi/osc-lib
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
%endif
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenStackClient (aka OSC) is a command-line client for OpenStack.
osc-lib is a package of common support modules for writing OSC
plugins.

%package -n python3-osc-lib
Summary:	OpenStackClient Library
Group:		Libraries/Python
Requires:	python3-modules

%description -n python3-osc-lib
OpenStackClient (aka OSC) is a command-line client for OpenStack.
osc-lib is a package of common support modules for writing OSC
plugins.

%package apidocs
Summary:	API documentation for Python osc-lib module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona osc-lib
Group:		Documentation

%description apidocs
API documentation for Pythona osc-lib module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona osc-lib.

%prep
%setup -q -n osc-lib-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%if %{with doc}
cd doc
%{__make} -j1 html
rm -rf _build/html/_sources
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.rst
%{py_sitescriptdir}/osc_lib
%{py_sitescriptdir}/osc_lib-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-osc-lib
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.rst
%{py3_sitescriptdir}/osc_lib
%{py3_sitescriptdir}/osc_lib-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc doc/_build/html/*
%endif
