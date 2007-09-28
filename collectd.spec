# TODO:
# - lm_sensors subpackage
# - perl subpackage
# - hddtemp subpackage
# - initscripts for local/client/server mode (subpackage ?)
# - collection CGI script
# - package contrib scripts as %doc
Summary:	Collects system information in RRD files
Summary(pl.UTF-8):	Zbieranie informacji o systemie w plikach RRD
Name:		collectd
Version:	4.1.2
Release:	0.1
License:	GPL v2
Group:		Daemons
Source0:	http://collectd.org/files/%{name}-%{version}.tar.gz
# Source0-md5:	40458dabe8ec5df87323c1862a03cb94
Source1:	%{name}.conf
#Patch0:		%{name}-include.patch
URL:		http://collectd.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	curl-devel
BuildRequires:	libstatgrab-devel >= 0.12
BuildRequires:	libpcap-devel
BuildRequires:	libtool
BuildRequires:	mysql-devel
BuildRequires:	perl-devel
BuildRequires:	rpmbuild(macros) >= 1.228
BuildRequires:	rrdtool-devel
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

%description -l pl.UTF-8
collectd to mały demon zbierający co 10 sekund informacje o systemie i
zapisujący wyniki do pliku RRD.

W odróżnieniu od innych podobnych programów collectd nie jest
skryptem, lecz jest napisany w czystym C z myślą o wydajności i
przenośności. Jako demon pozostaje w pamięci, więc nie ma potrzeby
urychamiania ciężkiego interpretera za każdym razem, kiedy powinny być
zapisane nowe wartości. Dzięki temu collect może mieć rozdzielczość 10
sekund i nie obciążać zbytnio systemu.

%package apache
Summary:	apache-plugin for collectd.
Summary(pl_PL.UTF-8):	moduł apache dla collectd.
Group:		Daemons
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description apache
This plugin collectd data provided by Apache's `mod_status'.

%description apache -l pl.UTF-8
Plugin collectd zbierający informacje udostępniane przez moduł 'mod_status' Apacha.

%package mysql
Summary:	mysql-plugin for collectd.
Summary(pl_PL.UTF-8):	moduł mysql-plugin do collectd.
Group:		Daemons
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description mysql
MySQL  querying  plugin.  This plugins  provides data of  issued commands,
called handlers and database traffic.

%description mysql -l pl.UTF-8
Moduł odpytujący MySQL. Wtyczka udostępnia dane z mysqla.

%prep
%setup -q
#%patch -p1

%build
if [ -f version-gen.sh ]; then
	echo zaktualizuj speca baranie
else
	echo "head -1 ChangeLog  |cut -f 3 -d ' ' |tr -d '\n' " > version-gen.sh
	chmod a+rx version-gen.sh
fi
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
%attr(755,root,root) %{_bindir}/collectd-nagios
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/apcups.so
#%attr(755,root,root) %{_libdir}/%{name}/apple_sensors.so
%attr(755,root,root) %{_libdir}/%{name}/battery.so
%attr(755,root,root) %{_libdir}/%{name}/cpufreq.so
%attr(755,root,root) %{_libdir}/%{name}/cpu.so
%attr(755,root,root) %{_libdir}/%{name}/csv.so
%attr(755,root,root) %{_libdir}/%{name}/df.so
%attr(755,root,root) %{_libdir}/%{name}/disk.so
%attr(755,root,root) %{_libdir}/%{name}/dns.so
%attr(755,root,root) %{_libdir}/%{name}/email.so
%attr(755,root,root) %{_libdir}/%{name}/entropy.so
%attr(755,root,root) %{_libdir}/%{name}/exec.so
%attr(755,root,root) %{_libdir}/%{name}/hddtemp.so
%attr(755,root,root) %{_libdir}/%{name}/interface.so
%attr(755,root,root) %{_libdir}/%{name}/irq.so
%attr(755,root,root) %{_libdir}/%{name}/load.so
%attr(755,root,root) %{_libdir}/%{name}/logfile.so
%attr(755,root,root) %{_libdir}/%{name}/mbmon.so
%attr(755,root,root) %{_libdir}/%{name}/memory.so
%attr(755,root,root) %{_libdir}/%{name}/multimeter.so
%attr(755,root,root) %{_libdir}/%{name}/network.so
%attr(755,root,root) %{_libdir}/%{name}/nfs.so
%attr(755,root,root) %{_libdir}/%{name}/ntpd.so
%attr(755,root,root) %{_libdir}/%{name}/perl.so
%attr(755,root,root) %{_libdir}/%{name}/ping.so
%attr(755,root,root) %{_libdir}/%{name}/processes.so
%attr(755,root,root) %{_libdir}/%{name}/rrdtool.so
#%attr(755,root,root) %{_libdir}/%{name}/sensors.so
%attr(755,root,root) %{_libdir}/%{name}/serial.so
%attr(755,root,root) %{_libdir}/%{name}/syslog.so
%attr(755,root,root) %{_libdir}/%{name}/swap.so
%{_libdir}/%{name}/types.db
#%attr(755,root,root) %{_libdir}/%{name}/tape.so
#%attr(755,root,root) %{_libdir}/%{name}/traffic.so
%attr(755,root,root) %{_libdir}/%{name}/users.so
%attr(755,root,root) %{_libdir}/%{name}/unixsock.so
%attr(755,root,root) %{_libdir}/%{name}/vserver.so
%attr(755,root,root) %{_libdir}/%{name}/wireless.so

%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.conf

#%attr(754,root,root) /etc/rc.d/init.d/%{name}
#%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/%{name}

%{_mandir}/man1/collectd.1*
%{_mandir}/man1/collectd-nagios.1*
%{_mandir}/man5/collectd.conf.5*
%{_mandir}/man5/collectd-email.5*
%{_mandir}/man5/collectd-exec.5*
%{_mandir}/man5/collectd-perl.5*
%{_mandir}/man5/collectd-snmp.5*
%{_mandir}/man5/collectd-unixsock.5*

%files apache
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/apache.so

%files mysql
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/mysql.so
