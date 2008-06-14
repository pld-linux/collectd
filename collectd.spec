# TODO:
# - lm_sensors subpackage
# - initscripts for local/client/server mode (subpackage ?)
# - package contrib scripts as %doc
# - put every plugin into subpackages
# - Current plugins status:
#    apache  . . . . . . yes
#    apcups  . . . . . . yes
#    apple_sensors . . . no
#    ascent  . . . . . . yes
#    battery . . . . . . yes
#    cpu . . . . . . . . yes
#    cpufreq . . . . . . yes
#    csv . . . . . . . . yes
#    df  . . . . . . . . yes
#    disk  . . . . . . . yes
#    dns . . . . . . . . yes
#    email . . . . . . . yes
#    entropy . . . . . . yes
#    exec  . . . . . . . yes
#    hddtemp . . . . . . yes
#    interface . . . . . yes
#    iptables  . . . . . yes
#    ipmi  . . . . . . . no
#    ipvs  . . . . . . . no (ip_vs.h not found)
#    irq . . . . . . . . yes
#    libvirt . . . . . . no
#    load  . . . . . . . yes
#    logfile . . . . . . yes
#    mbmon . . . . . . . yes
#    memcached . . . . . yes
#    memory  . . . . . . yes
#    multimeter  . . . . yes
#    mysql . . . . . . . yes
#    netlink . . . . . . yes
#    network . . . . . . yes
#    nfs . . . . . . . . yes
#    nginx . . . . . . . yes
#    ntpd  . . . . . . . yes
#    nut . . . . . . . . no
#    perl  . . . . . . . no (needs libperl)
#    ping  . . . . . . . yes
#    powerdns  . . . . . yes
#    processes . . . . . yes
#    rrdtool . . . . . . yes
#    sensors . . . . . . yes
#    serial  . . . . . . yes
#    snmp  . . . . . . . yes
#    swap  . . . . . . . yes
#    syslog  . . . . . . yes
#    tail  . . . . . . . yes
#    tape  . . . . . . . no
#    tcpconns  . . . . . yes
#    teamspeak2  . . . . yes
#    unixsock  . . . . . yes
#    users . . . . . . . yes
#    uuid  . . . . . . . yes
#    vmem  . . . . . . . yes
#    vserver . . . . . . yes
#    wireless  . . . . . yes
#    xmms  . . . . . . . yes
%bcond_without	dns
%bcond_without	iptables
%bcond_without	netlink

#http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=358637
%ifarch %{x8664}
%undefine with_iptables
%undefine with_netlink
%endif
Summary:	Collects system information in RRD files
Summary(pl.UTF-8):	Zbieranie informacji o systemie w plikach RRD
Name:		collectd
Version:	4.4.0
Release:	0.6
License:	GPL v2
Group:		Daemons
Source0:	http://collectd.org/files/%{name}-%{version}.tar.gz
# Source0-md5:	a677ddcad97fdb3cdd09efac4842b11d
Source1:	%{name}.conf
Source2:	%{name}.init
Source3:	%{name}-http.conf
URL:		http://collectd.org/
BuildRequires:	OpenIPMI-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	curl-devel
BuildRequires:	iptables-devel
BuildRequires:	libnetlink-devel
BuildRequires:	liboping-devel
BuildRequires:	libpcap-devel
BuildRequires:	libstatgrab-devel >= 0.12
BuildRequires:	libtool
BuildRequires:	lm_sensors-devel
BuildRequires:	mysql-devel
BuildRequires:	perl-devel
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	rrdtool-devel
BuildRequires:	net-snmp-devel
BuildRequires:	xmms-devel
Requires(post,preun):	/sbin/chkconfig
Requires:	rc-scripts
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _pkglibdir      /var/lib/%{name}
%define         _webapps        /etc/webapps 
%define         _webapp         %{name}
%define         _webappdir      %{_webapps}/%{_webapp}
%define         _appdir         %{_datadir}/%{_webapp}

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

%package ascent
Summary:	ascent-plugin for collectd
Summary(pl_PL.UTF-8):	Wtyczka ascent dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description ascent
ascent plugin for collectd.

%package apache
Summary:	apache-plugin for collectd
Summary(pl_PL.UTF-8):	Wtyczka apache dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description apache
This plugin collectd data provided by Apache's `mod_status'.

%description apache -l pl.UTF-8
Wtyczka collectd zbierająca informacje udostępniane przez moduł
'mod_status' Apacha.

%package collection
Summary:	Web script for collectiond
Summary(pl_PL.UTF-8):	Web script for collectiond
Group:		Applications/WWW
Requires:	%{name} = %{version}-%{release}

%description collection
Web script for collectiond

%package dns
Summary:	dns-plugin for collectd
Summary(pl_PL.UTF-8):	Wtyczka dns dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}
Requires:	perl-rrdtool

%description dns
dns plugin for collectd.

%package hddtemp
Summary:	hddtemp-plugin for collectd
Summary(pl_PL.UTF-8):	Wtyczka hddtemp dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description hddtemp
hddtemp plugin for collectd.

%package mysql
Summary:	mysql-plugin for collectd
Summary(pl_PL.UTF-8):	Moduł mysql dla collectd.
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description mysql
MySQL querying plugin. This plugins provides data of issued commands,
called handlers and database traffic.

%description mysql -l pl.UTF-8
Moduł odpytujący MySQL. Wtyczka udostępnia dane o wydawanych
poleceniach, wywoływanych procedurach obsługi i ruchu bazodanowym.

%package nginx
Summary:	nginx-plugin for collectd
Summary(pl_PL.UTF-8):	Wtyczka nginx dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description nginx
nginx plugin for collectd.

%package ping
Summary:	ping-plugin for collectd
Summary(pl_PL.UTF-8):	Wtyczka ping dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description ping
ping plugin for collectd.

%package powerdns
Summary:	powerdns-plugin for collectd
Summary(pl_PL.UTF-8):	Wtyczka powerdns dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description powerdns
powerdns plugin for collectd.

%package rrdtool
Summary:	rrdtool-plugin for collectd
Summary(pl_PL.UTF-8):	Wtyczka rrdtool dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}
Requires:	rrdtool

%description rrdtool
RRDTOOL plugin for collectd.

%package sensors
Summary:	sensors-plugin for collectd
Summary(pl_PL.UTF-8):	Wtyczka sensors dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description sensors
This plugin collectd data provided by hardware sensors.

%package snmp
Summary:	snmp-plugin for collectd
Summary(pl_PL.UTF-8):	Wtyczka snmp dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description snmp
snmp plugin for collectd.

%package uuid
Summary:	uuid-plugin for collectd
Summary(pl_PL.UTF-8):	Wtyczka uuid dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description uuid
This plugin collectd UUID data.

%package xmms
Summary:	xmms-plugin for collectd
Summary(pl_PL.UTF-8):	Wtyczka xmms dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}
Requires:	xmms-libs

%description xmms
This plugin collectd data provided by XMMS.

%prep
%setup -q

cat >> collection.conf <<'EOF'
datadir: "/var/lib/collectd/"
libdir: "/usr/lib/collectd/"
EOF

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
	--%{?with_dns:en}%{?!with_dns:dis}able-dns \
	--%{?with_iptables:en}%{?!with_iptables:dis}able-iptables \
	--%{?with_netlink:en}%{?!with_netlink:dis}able-netlink


%{__make} LDFLAGS="%{rpmldflags} -lstatgrab"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_var}/{log/,lib/%{name}},/etc/rc.d/init.d/} \
	$RPM_BUILD_ROOT{%{_appdir}/cgi-bin,%{_webappdir},%{_pkglibdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

#install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/collectd.conf
touch $RPM_BUILD_ROOT%{_var}/log/collectd.log
install src/collectd.conf $RPM_BUILD_ROOT%{_sysconfdir}/collectd.conf
install %{SOURCE2} $RPM_BUILD_ROOT/etc/rc.d/init.d/%{name}

# Web frontend:
install contrib/collection.conf $RPM_BUILD_ROOT%{_webappdir}
install contrib/collection.cgi $RPM_BUILD_ROOT%{_appdir}/cgi-bin
install %{SOURCE3} $RPM_BUILD_ROOT%{_webappdir}/apache.conf
install %{SOURCE3} $RPM_BUILD_ROOT%{_webappdir}/httpd.conf

# Cleanups:
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

%triggerin collection -- apache1 < 1.3.37-3, apache1-base
%webapp_register apache %{_webapp}

%triggerun collection -- apache1 < 1.3.37-3, apache1-base
%webapp_unregister apache %{_webapp}

%triggerin collection -- apache < 2.2.0, apache-base
%webapp_register httpd %{_webapp}

%triggerun collection -- apache < 2.2.0, apache-base
%webapp_unregister httpd %{_webapp}

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO contrib

%attr(755,root,root) %{_sbindir}/collectd
%attr(755,root,root) %{_sbindir}/collectdmon
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
%attr(755,root,root) %{_libdir}/%{name}/email.so
%attr(755,root,root) %{_libdir}/%{name}/entropy.so
%attr(755,root,root) %{_libdir}/%{name}/exec.so
%attr(755,root,root) %{_libdir}/%{name}/interface.so
%if %{with iptables}
%attr(755,root,root) %{_libdir}/%{name}/iptables.so
%endif
%attr(755,root,root) %{_libdir}/%{name}/irq.so
%attr(755,root,root) %{_libdir}/%{name}/load.so
%attr(755,root,root) %{_libdir}/%{name}/logfile.so
%attr(755,root,root) %{_libdir}/%{name}/mbmon.so
%attr(755,root,root) %{_libdir}/%{name}/memcached.so
%attr(755,root,root) %{_libdir}/%{name}/memory.so
%attr(755,root,root) %{_libdir}/%{name}/multimeter.so
%if %{with netlink}
%attr(755,root,root) %{_libdir}/%{name}/netlink.so
%endif
%attr(755,root,root) %{_libdir}/%{name}/network.so
%attr(755,root,root) %{_libdir}/%{name}/nfs.so
%attr(755,root,root) %{_libdir}/%{name}/ntpd.so
#%attr(755,root,root) %{_libdir}/%{name}/perl.so
%attr(755,root,root) %{_libdir}/%{name}/processes.so
%attr(755,root,root) %{_libdir}/%{name}/serial.so
%attr(755,root,root) %{_libdir}/%{name}/swap.so
%attr(755,root,root) %{_libdir}/%{name}/syslog.so
%attr(755,root,root) %{_libdir}/%{name}/tail.so
#%attr(755,root,root) %{_libdir}/%{name}/tape.so
%attr(755,root,root) %{_libdir}/%{name}/teamspeak2.so
%attr(755,root,root) %{_libdir}/%{name}/tcpconns.so
#%attr(755,root,root) %{_libdir}/%{name}/traffic.so
%attr(755,root,root) %{_libdir}/%{name}/unixsock.so
%attr(755,root,root) %{_libdir}/%{name}/users.so
%attr(755,root,root) %{_libdir}/%{name}/vmem.so
%attr(755,root,root) %{_libdir}/%{name}/vserver.so
%attr(755,root,root) %{_libdir}/%{name}/wireless.so
%{_libdir}/%{name}/types.db

%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.conf

%attr(754,root,root) /etc/rc.d/init.d/%{name}

%{_mandir}/man1/collectd.1*
%{_mandir}/man1/collectd-nagios.1*
%{_mandir}/man5/collectd.conf.5*
%{_mandir}/man5/collectd-email.5*
%{_mandir}/man5/collectd-exec.5*
%{_mandir}/man5/collectd-perl.5*
%{_mandir}/man5/collectd-snmp.5*
%{_mandir}/man5/collectd-unixsock.5*
%{_mandir}/man1/collectdmon.1*
%{_mandir}/man5/types.db.5*
%{_var}/log/collectd.log
%dir %{_var}/lib/%{name}

########## PLUGINS:
%files ascent
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/ascent.so

%files apache
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/apache.so

%files collection
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_webappdir}/collection.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_webappdir}/apache.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_webappdir}/httpd.conf
%attr(755,root,root) %{_appdir}/cgi-bin/collection.cgi

%files dns
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/dns.so

%files hddtemp
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/hddtemp.so

%files mysql
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/mysql.so

%files nginx
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/nginx.so

%files ping
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/ping.so

%files powerdns
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/powerdns.so

%files rrdtool
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/rrdtool.so

%files sensors
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/sensors.so

%files snmp
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/snmp.so

%files uuid
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/uuid.so

%files xmms
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/xmms.so
