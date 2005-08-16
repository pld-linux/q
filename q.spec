Summary:	Q eQuational Programming System
Summary(pl):	System programowania r�wnaniowego Q
Name:		q
Version:	6.0
Release:	1
License:	GPL
Group:		Development/Languages
Source0:	http://dl.sourceforge.net/q-lang/%{name}-%{version}.tar.gz
# Source0-md5:	bbf875950eed0aa0c8df1a657d74f273
URL:		http://q-lang.sourceforge.net/
BuildRequires:	gmp-devel
BuildRequires:	ncurses-devel
BuildRequires:	readline-devel
BuildRequires:	tk-devel
Requires(post,postun):	/sbin/ldconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Q is an equational programming language.

%description -l pl
Q jest j�zykiem programowania r�wnaniowego. Oznacza to, �e programy w
nim napisane sk�adaj� si� z r�wna� opisuj�cych funkcje.

%package tk
Summary:	Tk bindings for Q langauge
Summary(pl):	Wi�zania Tk dla j�zyka Q
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}

%description tk
Tk bindings for Q langauge.

%description tk -l pl
Wi�zania Tk dla j�zyka Q.

%package octave
Summary:	Octave bindings for Q langauge
Summary(pl):	Wi�zania do Octave dla j�zyka Q
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}
Requires:	octave

%description octave
Octave bindings for Q langauge.

%description octave -l pl
Wi�zania do Octave dla j�zyka Q.

%package static
Summary:	Static library for Q langauge
Summary(pl):	Statyczna biblioteka j�zyka Q
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}

%description static
Static library for Q langaug

%description static -l pl
Statyczna biblioteka j�zyka Q

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

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1
/sbin/ldconfig

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1
/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README ChangeLog NEWS AUTHORS etc/qinitrc etc/qexitrc etc/q-mode.el
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*.so.*.*.*
%{_libdir}/*.la
%dir %{_libdir}/q
%attr(755,root,root) %{_libdir}/q/clib.so
%{_libdir}/q/clib.la
%{_includedir}/*.h
%dir %{_datadir}/q
%{_datadir}/q/lib
%{_mandir}/man1/*
%{_infodir}/*info*
%{_examplesdir}/%{name}-%{version}

%files static
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/q/tk.so
%{_libdir}/*.a
%{_libdir}/q/clib.a

%files tk
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/q/tk.so
%{_libdir}/q/tk.la
%{_libdir}/q/tk.a
%{_datadir}/q/lib/tk.q

%files octave
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/q/octave.so
%{_libdir}/q/octave.la
%{_libdir}/q/octave.a
%{_datadir}/q/lib/octave.q
