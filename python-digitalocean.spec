%define module digitalocean

Name:		python-digitalocean
Version:	1.17.0
Release:	1
Summary:	Python API for DigitalOcean droplets and images
License:	LGPL-3.0-only
Group:		Development/Python
URL:		https://github.com/koalalorenzo/python-digitalocean
Source0:	https://files.pythonhosted.org/packages/source/p/python-digitalocean/python-digitalocean-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python
BuildRequires:	python%{pyver}dist(setuptools)

%description
Python client for the DigitalOcean API. Certbot's digitalocean
DNS authenticator uses it to create and remove TXT records.

%files
%doc README.md
%license LICENSE.txt
%{py_sitedir}/%{module}
%{py_sitedir}/python_%{module}-*.egg-info
