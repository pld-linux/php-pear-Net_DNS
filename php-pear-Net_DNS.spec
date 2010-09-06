# NOTE
# - mhash used only in RR/TSIG, so we mark it optional
#
%include	/usr/lib/rpm/macros.php
%define		_class		Net
%define		_subclass	DNS
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - resolver library to communicate with a DNS server
Summary(pl.UTF-8):	%{_pearname} - biblioteka resolvera używana do komunikacji z serwerem DNS
Name:		php-pear-%{_pearname}
Version:	1.0.5
Release:	2
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	16f9533b49c581e55b5be7512e5733c1
Patch0:		%{name}-missing-vars.patch
URL:		http://pear.php.net/package/Net_DNS/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-common >= 3:4.2
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A resolver library used to communicate with a name server to perform
DNS queries, zone transfers, dynamic DNS updates, etc. Creates an
object hierarchy from a DNS server's response, which allows you to
view all of the information given by the DNS server. It bypasses the
system's resolver library and communicates directly with the server.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Biblioteka resolvera jest używana w komunikacji z serwerami nazw do
przygotowania zapytań DNS, transferów stref, aktualizacji dynamicznego
DNS, itd. Tworzy hierarchię obiektów z odpowiedzi serwera DNS, która
pozwala zobaczyć wszystkie informacje dawane przez serwer DNS. To
omija systemowy resolver i komunikuje się bezpośrednio z serwerem.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup
echo '%{name} can optionally use PHP extension "mhash"' >> install.log

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%patch0 -p1

# don't care for tests
rm -rf $RPM_BUILD_ROOT%{php_pear_dir}/tests/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
