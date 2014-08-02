Summary:	UID wrapper library
Summary(pl.UTF-8):	Biblioteka obudowująca UID
Name:		uid_wrapper
Version:	1.0.2
Release:	1
License:	GPL v3+
Group:		Libraries
Source0:	http://www.samba.org/ftp/cwrap/%{name}-%{version}.tar.gz
# Source0-md5:	8fb6b12fa2f0dd918f2d5ad90e60014f
URL:		http://cwrap.org/uid_wrapper.html
BuildRequires:	cmake >= 2.8.0
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Privilege separation - some projects like a file server need privilege
separation to be able to switch to the connnection user and do file
operations. uid_wrapper convincingly lies to the application letting
it believe it is operating as root and even switching between uids and
gids as needed.

%description -l pl.UTF-8
Rozdzielenie uprawnień - niektóre projekty, takie jak serwer plików,
wymagają rozdzielenia uprawnień, aby przełączać się na użytkownika
połączenia i wykonywać operacje na plikach. uid_wrapper dla wygody
okłamuje aplikację, pozwalając jej wierzyć, że działa jako root, nawet
gdy wymagane jest przełączanie między różnymi uidami i gidami.

%prep
%setup -q

%build
install -d build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README TODO
%attr(755,root,root) %{_libdir}/libuid_wrapper.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libuid_wrapper.so.0
%attr(755,root,root) %{_libdir}/libuid_wrapper.so
%{_pkgconfigdir}/uid_wrapper.pc
%{_libdir}/cmake/uid_wrapper
%{_mandir}/man1/uid_wrapper.1*
