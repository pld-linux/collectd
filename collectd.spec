# TODO:
# - mysql subpackage
# - lm_sensors subpackage
# - hddtemp subpackage
# - initscripts for local/network mode (subpackage ?)
# - initscripts for server mode (subpackage ?)
# - collection CGI script
# - package contrib scripts as %doc
Summary:	Collects system information in RRD files
Summary(pl):	Zbieranie informacji o systemie w plikach RRD
Name:		collectd
Version:	3.10.1
Release:	0.1
License:	GPL v2
Group:		Daemons
Source0:	http://collectd.org/files/%{name}-%{version}.tar.gz
# Source0-md5:	0a355891f319855e1d242e6c57f7ed4f
Source1:	%{name}.conf
URL:		http://collectd.org/
BuildRequires:	autoconf
BuildRequires:	automake
#BuildRequires:	intltool
BuildRequires:	libstatgrab-devel >= 0.12
BuildRequires:	libtool
BuildRequires:	rpmbuild(macros) >= 1.228
Requires(post,preun):	/sbin/chkconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
collectd is a small daemon which collects system information every 10
seconds and writes the results in an RRD-file.

In contrast to most similar software, collectd is not a script but
written in plain C for performance and portability. As a daemon it
stays in memory, so there is no need to start up a heavy interpreter
every time new values should be logged. This allows collectd to have a
10 second resolution while being nice to the system.

%description -l pl
collectd to ma³y demon zbieraj±cy co 10 sekund informacje o systemie i
zapisuj±cy wyniki do pliku RRD.

W odró¿nieniu od innych podobnych programów collectd nie jest
skryptem, lecz jest napisany w czystym C z my¶l± o wydajno¶ci i
przeno¶no¶ci. Jako demon pozostaje w pamiêci, wiêc nie ma potrzeby
urychamiania ciê¿kiego interpretera za ka¿dym razem, kiedy powinny byæ
zapisane nowe warto¶ci. Dziêki temu collect mo¿e mieæ rozdzielczo¶æ 10
sekund i nie obci±¿aæ zbytnio systemu.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-libstatgrab=/usr \
	--with-lm-sensors=/usr \
	--with-libmysql=/usr \
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/collectd.conf

rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add %{name}
%service %{name} restart

%preun
if [ "$1" = "0" ]; then
	%service -q %{name} stop
	/sbin/chkconfig --del %{name}
fi

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO

%attr(755,root,root) %{_sbindir}/collectd
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/apache.so
%attr(755,root,root) %{_libdir}/%{name}/apcups.so
%attr(755,root,root) %{_libdir}/%{name}/apple_sensors.so
%attr(755,root,root) %{_libdir}/%{name}/battery.so
%attr(755,root,root) %{_libdir}/%{name}/cpufreq.so
%attr(755,root,root) %{_libdir}/%{name}/cpu.so
%attr(755,root,root) %{_libdir}/%{name}/df.so
%attr(755,root,root) %{_libdir}/%{name}/disk.so
%attr(755,root,root) %{_libdir}/%{name}/hddtemp.so
%attr(755,root,root) %{_libdir}/%{name}/load.so
%attr(755,root,root) %{_libdir}/%{name}/memory.so
%attr(755,root,root) %{_libdir}/%{name}/mysql.so
%attr(755,root,root) %{_libdir}/%{name}/nfs.so
%attr(755,root,root) %{_libdir}/%{name}/ntpd.so
%attr(755,root,root) %{_libdir}/%{name}/ping.so
%attr(755,root,root) %{_libdir}/%{name}/processes.so
%attr(755,root,root) %{_libdir}/%{name}/sensors.so
%attr(755,root,root) %{_libdir}/%{name}/serial.so
%attr(755,root,root) %{_libdir}/%{name}/swap.so
%attr(755,root,root) %{_libdir}/%{name}/tape.so
%attr(755,root,root) %{_libdir}/%{name}/traffic.so
%attr(755,root,root) %{_libdir}/%{name}/users.so
%attr(755,root,root) %{_libdir}/%{name}/vserver.so
%attr(755,root,root) %{_libdir}/%{name}/wireless.so

%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.conf

#%attr(754,root,root) /etc/rc.d/init.d/%{name}
#%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/%{name}

%{_mandir}/man1/collectd.1*
%{_mandir}/man5/collectd.conf.5*
