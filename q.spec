Summary:	Q eQuational Programming System
Summary(pl):	System programowania równaniowego Q
Name:		q
Version:	3.3
Release:	1
License:	GPL
Group:		Development/Languages
Source0:	http://www.musikwissenschaft.uni-mainz.de/~ag/q/%{name}-%{version}.tar.gz
URL:		http://www.musikwissenschaft.uni-mainz.de/~ag/q/
BuildRequires:	ncurses-devel
BuildRequires:	readline-devel
BuildRequires:	gmp-devel
BuildRequires:	tk-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Q is an equational programming language.

%description -l pl
Q jest jêzykiem programowania równaniowego. Oznacza to, ¿e
programy w nim napisane sk³adaj± siê z równañ opisuj±cych
funkcje.

%package tk
Summary:	Tk bindings for Q langauge
Summary(pl):	Wi±zania Tk dla jêzyka Q
Group:		Development/Languages
Requires:	%{name} = %{version}

%description tk
Tk bindings for Q langauge.

%description tk -l pl
Wi±zania Tk dla jêzyka Q.

%package octave
Summary:	Octave bindings for Q langauge
Summary(pl):	Wi±zania do Octave dla jêzyka Q
Group:		Development/Languages
Requires:	%{name} = %{version}
Requires:	octave

%description octave
Octave bindings for Q langauge.

%description octave -l pl
Wi±zania do Octave dla jêzyka Q.

%package static
Summary:	Static library for Q langauge
Summary:	Statyczna biblioteka jêzyka Q
Group:		Development/Languages
Requires:	%{name} = %{version}

%description static
Static library for Q langaug

%description static -l pl
Statyczna biblioteka jêzyka Q

%prep
%setup -q

%build
%configure \
	--with-gpm \
	--with-rl \
	--with-tk \
	--with-pthread

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1
/sbin/ldconfig

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1
/sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog NEWS AUTHORS etc/qinitrc etc/qexitrc etc/q-mode.el
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*.so.*.*.*
%{_libdir}/*.la
%attr(755,root,root) %{_libdir}/q/clib.so
%{_libdir}/q/clib.la
%{_includedir}/*.h
%{_datadir}/q/lib
%{_mandir}/man1/*
%{_infodir}/*info*
%{_examplesdir}/%{name}-%{version}

%files static
%attr(755,root,root) %{_libdir}/q/tk.so
%{_libdir}/*.a
%{_libdir}/q/clib.a

%files tk
%attr(755,root,root) %{_libdir}/q/tk.so
%{_libdir}/q/tk.la
%{_libdir}/q/tk.a
%{_datadir}/q/lib/tk.q

%files octave
%attr(755,root,root) %{_libdir}/q/octave.so
%{_libdir}/q/octave.la
%{_libdir}/q/octave.a
%{_datadir}/q/lib/octave.q
