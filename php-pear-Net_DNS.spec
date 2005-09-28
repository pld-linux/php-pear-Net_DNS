%include	/usr/lib/rpm/macros.php
%define		_class		Net
%define		_subclass	DNS
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - resolver library to communicate with a DNS server
Summary(pl):	%{_pearname} - biblioteka resolvera u¿ywana do komunikacji z serwerem DNS
Name:		php-pear-%{_pearname}
Version:	1.0.0
%define		_suf b3
%define		_rel 1.1
Release:	0.%{_suf}.%{_rel}
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}%{_suf}.tgz
# Source0-md5:	989985f8487a8c32c054cdd7ac539f93
URL:		http://pear.php.net/package/Net_DNS/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
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

%description -l pl
Biblioteka resolvera jest u¿ywana w komunikacji z serwerami nazw do
przygotowania zapytañ DNS, transferów stref, aktualizacji dynamicznego
DNS, itd. Tworzy hierarchiê obiektów z odpowiedzi serwera DNS, która
pozwala zobaczyæ wszystkie informacje dawane przez serwer DNS. To
omija systemowy resolver i komunikuje siê bezpo¶rednio z serwerem.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
