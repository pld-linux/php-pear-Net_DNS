%include	/usr/lib/rpm/macros.php
%define         _class          Net
%define         _subclass       DNS
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - Resolver library to communicate with a DNS server
Summary(pl):	%{_pearname} - Biblioteka resolvera u¿ywana do komunikacji z serwerem DNS
Name:		php-pear-%{_pearname}
Version:	1.00b1
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A resolver library used to communicate with a name server to perform
DNS queries, zone transfers, dynamic DNS updates, etc. Creates an
object hierarchy from a DNS server's response, which allows you to
view all of the information given by the DNS server. It bypasses the
system's resolver library and communicates directly with the server.

This class has in PEAR status: %{_status}.

%description -l pl
Biblioteka resolvera jest u¿ywana w komunikacji z serwerami nazw do
przygotowania zapytañ DNS, transferów stref, aktualizacji dynamicznego
DNS, itd. Tworzy hierarchiê obiektów z odpowiedzi serwera DNS, która
pozwala zobaczyæ wszystkie informacje dawane przez server DNS. To
omija systemowy resolver i komunikuje siê bezpo¶rednio z serwerem.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/RR

install %{_pearname}-%{version}/*.php	$RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_pearname}-%{version}/%{_subclass}/*.php	$RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}
install %{_pearname}-%{version}/%{_subclass}/RR/*.php	$RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/RR

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{php_pear_dir}/%{_class}/%{_subclass}
%dir %{php_pear_dir}/%{_class}/%{_subclass}/RR
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/RR/*.php
