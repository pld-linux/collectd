# TODO:
# - package contrib scripts as %doc
# - perl modules with Collectd classes package to separate package
# - Disabled modules:
#    apple_sensors . . . no		(obvious)
#    ipvs  . . . . . . . no		(ip_vs.h not found - llh to be fixed)
#    libvirt . . . . . . no		(requires library)
#    multimeter  . . . . no		?
#    onewire . . . . . . no		(needs libowfs)
#    perl  . . . . . . . no		(needs libperl)
#    tape  . . . . . . . no		?
#
# Conditional build:
%bcond_without	dns		# ???
%bcond_without	ipmi		# ipmi plugin package
%bcond_without	iptables	# iptables plugin
%bcond_with	multimeter	# multimeter plugin
%bcond_without	netlink		# netlink plugin
#
#http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=358637
%ifarch %{x8664}
%undefine with_iptables
%undefine with_netlink
%endif
Summary:	Collects system information in RRD files
Summary(pl.UTF-8):	Zbieranie informacji o systemie w plikach RRD
Name:		collectd
Version:	4.5.1
Release:	1.5
License:	GPL v2
Group:		Daemons
Source0:	http://collectd.org/files/%{name}-%{version}.tar.gz
# Source0-md5:	ab900d15662859b8793abf99eda15c29
Source1:	%{name}.conf
Source2:	%{name}.init
Source3:	%{name}-http.conf
Source10:	%{name}-ascent.conf
Source11:	%{name}-apache.conf
Source12:	%{name}-dns.conf
Source13:	%{name}-hddtemp.conf
Source14:	%{name}-ipmi.conf
Source15:	%{name}-mysql.conf
Source16:	%{name}-nginx.conf
Source17:	%{name}-notify_desktop.conf
Source18:	%{name}-notify_email.conf
Source19:	%{name}-nut.conf
Source20:	%{name}-ping.conf
Source21:	%{name}-postgresql.conf
Source22:	%{name}-powerdns.conf
Source23:	%{name}-rrdtool.conf
Source24:	%{name}-sensors.conf
Source25:	%{name}-snmp.conf
Source26:	%{name}-uuid.conf
Source27:	%{name}-xmms.conf
Source28:	%{name}-tcpconns.conf
Source29:	%{name}-teamspeak2.conf
Source30:	%{name}-thermal.conf
Source31:	%{name}-unixsock.conf
Source32:	%{name}-users.conf
Source33:	%{name}-vmem.conf
Source34:	%{name}-vserver.conf
Source35:	%{name}-wireless.conf
Source36:	%{name}-apcups.conf
Source37:	%{name}-battery.conf
Source38:	%{name}-cpufreq.conf
Source39:	%{name}-cpu.conf
Source40:	%{name}-csv.conf
Source41:	%{name}-df.conf
Source42:	%{name}-disk.conf
Source43:	%{name}-email.conf
Source44:	%{name}-entropy.conf
Source45:	%{name}-exec.conf
Source46:	%{name}-filecount.conf
Source47:	%{name}-interface.conf
Source48:	%{name}-iptables.conf
Source49:	%{name}-irq.conf
Source51:	%{name}-load.conf
Source52:	%{name}-logfile.conf
Source53:	%{name}-mbmon.conf
Source54:	%{name}-memcached.conf
Source55:	%{name}-memory.conf
Source56:	%{name}-multimeter.conf
Source57:	%{name}-netlink.conf
Source58:	%{name}-network.conf
Source59:	%{name}-nfs.conf
Source60:	%{name}-ntpd.conf
Source61:	%{name}-processes.conf
Source62:	%{name}-serial.conf
Source63:	%{name}-swap.conf
Source64:	%{name}-syslog.conf
Source65:	%{name}-tail.conf
URL:		http://collectd.org/
%{?with_ipmi:BuildRequires:	OpenIPMI-devel >= 2.0.14-3}
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	curl-devel
%{?with_iptables:BuildRequires:	iptables-devel >= 1.4.1.1-4}
BuildRequires:	libesmtp-devel
BuildRequires:	libnetlink-devel
BuildRequires:	libnotify-devel
BuildRequires:	liboping-devel
BuildRequires:	libpcap-devel
BuildRequires:	libstatgrab-devel >= 0.12
BuildRequires:	libtool
BuildRequires:	lm_sensors-devel
BuildRequires:	mysql-devel
BuildRequires:	nut-devel
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

%package apcups
Summary:	APC UPS plugin for collectd
Summary(pl_PL.UTF-8):	Wtyczka APC UPS dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description apcups
APC UPS plugin for collectd.

%package ascent
Summary:	ascent-plugin for collectd
Summary(pl_PL.UTF-8):	Wtyczka ascent dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description ascent
ascent plugin for collectd.

%package battery
Summary:	battery plugin for collectd
Summary(pl_PL.UTF-8):	Wtyczka battery dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description battery
This plugin collects the battery's charge, the drawn current and the
battery's voltage.

%package collection
Summary:	Web script for collectiond
Summary(pl_PL.UTF-8):	Web script for collectiond
Group:		Applications/WWW
Requires:	%{name} = %{version}-%{release}

%description collection
Web script for collectiond

%package cpu
Summary:	cpu-plugin for collectd
Summary(pl_PL.UTF-8):	Wtyczka cpu dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description cpu
The cpu-plugin collects the amount of time spent by the CPU in various states,
most notably executing user code, executing system code, waiting for IO
operations and being idle.

%package cpufreq
Summary:	cpufreq-plugin for collectd
Summary(pl_PL.UTF-8):	Wtyczka cpufreq dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description cpufreq
Collects the current CPU's frequency, mostly for mobile computers.

%package csv
Summary:	CSV output plugin for collectd
Summary(pl_PL.UTF-8):	Wtyczka wyjściowa CSV dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description csv
CSV output plugin for collectd.

%package df
Summary:	df-plugin for collectd
Summary(pl_PL.UTF-8):	Wtyczka df dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description df
The df-plugin collects file system usage information, i. e. basically how
much space on a mounted partition is used and how much is available. It's
named after and very similar to the df(1) UNIX command that's been around
forever.

%package disk
Summary:	disk-plugin for collectd
Summary(pl_PL.UTF-8):	Wtyczka disk dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description disk
This plugin collects performance statistics of harddisks and, where
supported, partitions.

%package dns
Summary:	dns-plugin for collectd
Summary(pl_PL.UTF-8):	Wtyczka dns dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}
Requires:	perl-rrdtool

%description dns
This plugin has a similar functionality to dnstop: It uses libpcap to get
a copy of all traffic from/to port UDP/53 (that's the DNS port), interprets
the packets and collects statistics of your DNS traffic.

%package email
Summary:	email-plugin for collectd
Summary(pl_PL.UTF-8):	Wtyczka email dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description email
The email plugin opens an UNIX-socket over which one can submit email
statistics, such as the number of ``ham'', ``spam'', ``virus'', etc. mails
received/handled, spam scores and matched spam checks.

This plugin is intended to be used with the the
Mail::SpamAssassin::Plugin::Collectd manpage SpamAssassin-plugin which is
included in contrib/, but is of course not limited to that use.

%package entropy
Summary:	entropy-plugin for collectd
Summary(pl_PL.UTF-8):	Wtyczka entropy dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description entropy
entropy plugin for collectd.

%package exec
Summary:	exec-plugin for collectd
Summary(pl_PL.UTF-8):	Wtyczka exec dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description exec
The exec plugin forks of an executable either to receive values or to
dispatch notifications to the outside world.

%package filecount
Summary:	filecount-plugin for collectd
Summary(pl_PL.UTF-8):	Wtyczka filecount dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description filecount
The filecount-plugin does something very simple: Count the number of files
in a directory and all its subdirectories. This can be used for a variety of
statistics, for example the queue length of an MTA, the number of PHP
sessions of a web server or simply the number of files in your home
directory.

%package hddtemp
Summary:	hddtemp-plugin for collectd
Summary(pl_PL.UTF-8):	Wtyczka hddtemp dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description hddtemp
Temperature of harddisks. The temperatures are provided via S.M.A.R.T. and
queried by the external hddtemp-daemon.

%package interface
Summary:	interface-plugin for collectd
Summary(pl_PL.UTF-8):	Wtyczka interface dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description interface
The interface-plugin collects information about the traffic (octets), packets
and errors of interfaces.

%package iptables
Summary:	iptables-plugin for collectd
Summary(pl_PL.UTF-8):	Wtyczka iptables dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description iptables
With this plugin you can gather statistics from your ip_tables based
packetfilter (aka. firewall). It can collect the byte- and packet-counters
of selected rules and submit them to collectd. You can select rules that
should be collected wither by its position (e.g. "the fourth rule in the
INPUT queue in the filter table") or by its comment (using the COMMENT
match). This means that depending on your firewall layout you can collect
certain services (such as the amount of web-traffic), source or destination
hosts or networks, dropped packets and much more.

%package ipmi
Summary:	ipmi-plugin for collectd
Summary(pl_PL.UTF-8):	Wtyczka ipmi dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description ipmi
ipmi plugin for collectd.

%description ipmi -l pl.UTF-8
Wtyczka ipmi dla collectd.

%package irq
Summary:	IRQs-plugin for collectd
Summary(pl_PL.UTF-8):	Wtyczka IRQs dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description irq
IRQs plugin for collectd.

%package load
Summary:	load-plugin for collectd
Summary(pl_PL.UTF-8):	Wtyczka load dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description load
Collects the system load. These numbers give a rough overview over the
utilization of a machine, though their meaning is mostly overrated.

%package logfile
Summary:	logfile-plugin for collectd
Summary(pl_PL.UTF-8):	Wtyczka logfile dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description logfile
Logfile plugin for collectd.

%module_scripts mbmon
%package mbmon
Summary:	mbmon-plugin for collectd
Summary(pl_PL.UTF-8):	Wtyczka mbmon dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description mbmon
The mbmon plugin uses mbmon to retrieve temperature, voltage, etc.

%package memcached
Summary:	memcached-plugin for collectd
Summary(pl_PL.UTF-8):	Wtyczka memcached dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description memcached
The memcached plugin connects to a memcached daemon and collects the number
of connections and requests handled by the daemon, the CPU resources consumed,
number of items cached, number of threads, and bytes sent and received.

%package memory
Summary:	memory-plugin for collectd
Summary(pl_PL.UTF-8):	Wtyczka memory dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description memory
Collects physical memory utilization for collectd.

%package multimeter
Summary:	multimeter-plugin for collectd
Summary(pl_PL.UTF-8):	Wtyczka multimeter dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description multimeter
Multimeter plugin for collectd.

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

%package netlink
Summary:	netlink-plugin for collectd
Summary(pl_PL.UTF-8):	Wtyczka netlink dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description netlink
This plugin will open a netlink socket to the Linux kernel and use it to get
statistics for interfaces, qdiscs, classes, and, if you can make use of it,
filters. Since in most setups many of the statistics this plugin can collect
aren't of interest, you can select which information to gather using the
configuration.

%package network
Summary:	network-plugin for collectd
Summary(pl_PL.UTF-8):	Wtyczka network dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description network
nginx plugin for collectd.

%package nfs
Summary:	NFS-plugin for collectd
Summary(pl_PL.UTF-8):	Wtyczka NFS dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description nfs
The nfs plugin counts the number of procedure calls of the different NFS
procedures.

%package nginx
Summary:	nginx-plugin for collectd
Summary(pl_PL.UTF-8):	Wtyczka nginx dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description nginx
This plugin collects the number of connections and requests handled by the
nginx daemon, a HTTP and mail server/proxy. It queries the page provided by
the ngx_http_stub_status_module module, which isn't compiled by default.

%package notify_desktop
Summary:	notify_desktop for collectd
Summary(pl_PL.UTF-8):	Wtyczka notify_desktop dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description notify_desktop
This plugin sends a desktop notification to a notification daemon, as
defined in the Desktop Notification Specification. To actually display the
notifications, notification-daemon is required and collectd has to be able
to access the X server.

%package notify_email
Summary:	notify_email-plugin for collectd
Summary(pl_PL.UTF-8):	Wtyczka notify_email dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description notify_email
notify_email plugin for collectd.

%package ntpd
Summary:	ntpd-plugin for collectd
Summary(pl_PL.UTF-8):	Wtyczka ntpd dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description ntpd
NTPd plugin for collectd.

%package nut
Summary:	nut-plugin for collectd
Summary(pl_PL.UTF-8):	Wtyczka nut dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description nut
UPS statistics using the Network UPS Tools. These statistics include
basically everything NUT will give us, including voltages, currents, power,
frequencies, load, and temperatures.

%package ping
Summary:	ping-plugin for collectd
Summary(pl_PL.UTF-8):	Wtyczka ping dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description ping
The network latency is measured as a roundtrip time. An ICMP-echo-request
(aka. "ping")is sent to a host and the time needed for his echo-reply (aka.
"pong") to arrive is measured. If a reply is not received within one second
the plugin will no longer expect a reply and return. This may happen in
several circumstances, e. g. the packet is lost, the host is down, a router
has dismissed the packet, etc.

%package postgresql
Summary:	mysql-plugin for collectd
Summary(pl_PL.UTF-8):	Moduł postgresql dla collectd.
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description postgresql
The postgresql plugin queries statistics from PostgreSQL databases. It keeps
a persistent connection to all configured databases and tries to reconnect
if the connection has been interrupted.

%package powerdns
Summary:	powerdns-plugin for collectd
Summary(pl_PL.UTF-8):	Wtyczka powerdns dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description powerdns
The powerdns plugin queries statistics from an authoritative PowerDNS
nameserver and/or a PowerDNS recursor. Since both offer a wide variety of
values, many of which are probably meaningless to most users, but may be
useful for some.

%package processes
Summary:	processes-plugin for collectd
Summary(pl_PL.UTF-8):	Wtyczka processes dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description processes
This plugin collects the number of processes, grouped by their state (e.g.
running, sleeping, zombies, etc.). In addition to that, it can select
detailed statistics about selected processes, grouped by name.

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
This plugin uses lm-sensors to read hardware sensors. You will need to
configure lm-sensors before this plugin will collect any usefull and correct
data.

%module_scripts serial
%package serial
Summary:	serial-plugin for collectd
Summary(pl_PL.UTF-8):	Wtyczka serial dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description serial
Serial plugin for collectd.

%package snmp
Summary:	snmp-plugin for collectd
Summary(pl_PL.UTF-8):	Wtyczka snmp dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description snmp
The snmp plugin queries other hosts using SNMP, the Simple Network
Management Protocol, and translates the value it receives to collectd's
internal format and dispatches them. Depending on the write plugins you have
loaded they may be written to disk or submitted to another instance or
whatever you configured.

%package swap
Summary:	swap-plugin for collectd
Summary(pl_PL.UTF-8):	Wtyczka swap dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description swap
Swap space plugin for collectd.

%package syslog
Summary:	syslog-plugin for collectd
Summary(pl_PL.UTF-8):	Wtyczka syslog dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description syslog
Syslog plugin for collectd.

%package tail
Summary:	tail-plugin for collectd
Summary(pl_PL.UTF-8):	Wtyczka tail dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description tail
The tail-plugin can be used to "tail" logfiles, i.e. follow them as tail -F
does. Each line is given to one or more "matches" which test if the line is
relevant for any statistics using a regular expression.

%package tcpconns
Summary:	tcpconns-plugin for collectd
Summary(pl_PL.UTF-8):	Wtyczka tcpconns dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description tcpconns
The tcpconns-plugin counts the number of TCP connections to or from a
specified port. Typically the connectioins where you specify the local port
are incoming connections while the connections where you specify the remote
port are outgoing connections.

%package teamspeak2
Summary:	teamspeak2-plugin for collectd
Summary(pl_PL.UTF-8):	Wtyczka teamspeak2 dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description teamspeak2
The teamspeak2 plugin connects to the query port of a teamspeak2 server and
polls interesting global and virtual server data. The plugin can query only
one physical server but unlimited virtual servers.

%package thermal
Summary:	thermal-plugin for collectd
Summary(pl_PL.UTF-8):	Wtyczka thermal dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description thermal
Thermal plugin for collectd.

%package unixsock
Summary:	unixsock-plugin for collectd
Summary(pl_PL.UTF-8):	Wtyczka unixsock dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description unixsock
The unixsock plugin opens an UNIX-socket over which one can interact with
the daemon. This can be used to use the values collected by collectd in
other applications, such as monitoring, or submit externally collected
values to collectd.

%package users
Summary:	users-plugin for collectd
Summary(pl_PL.UTF-8):	Wtyczka users dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description users
Number of users currently logged in.

%package uuid
Summary:	uuid-plugin for collectd
Summary(pl_PL.UTF-8):	Wtyczka uuid dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description uuid
This plugin, if loaded, causes the Hostname to be taken from the machine's
UUID. The UUID is a universally unique designation for the machine, usually
taken from the machine's BIOS. This is most useful if the machine is
running in a virtual environment such as Xen, in which case the UUID is
preserved across shutdowns and migration.

%package vmem
Summary:	vmem-plugin for collectd
Summary(pl_PL.UTF-8):	Wtyczka vmem dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description vmem
The vmem plugin collects information about the usage of virtual memory.
Since the statistics provided by the Linux kernel are very detailed, they
are collected very detailed.

%package vserver
Summary:	vserver-plugin for collectd
Summary(pl_PL.UTF-8):	Wtyczka vserver dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description vserver
Collects information about the virtual servers running on a system, using
Linux-Vserver.

%package wireless
Summary:	wireless-plugin for collectd
Summary(pl_PL.UTF-8):	Wtyczka wireless dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description wireless
Wireless plugin for collectd.

%package xmms
Summary:	xmms-plugin for collectd
Summary(pl_PL.UTF-8):	Wtyczka xmms dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

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
	--%{?with_ipmi:en}%{!?with_ipmi:dis}able-ipmi \
	--%{?with_multimeter:en}%{!?with_multimeter:dis}able-multimeter \
	--%{?with_dns:en}%{!?with_dns:dis}able-dns \
	--%{?with_iptables:en}%{!?with_iptables:dis}able-iptables \
	--%{?with_netlink:en}%{!?with_netlink:dis}able-netlink \
	--disable-ipvs \
	--disable-libvirt \
	--disable-perl


%{__make} LDFLAGS="%{rpmldflags} -lstatgrab" \
	BUILD_WITH_OPENIPMI_CFLAGS="-I/usr/include" \
	BUILD_WITH_OPENIPMI_LIBS="-L/usr/lib64 -lOpenIPMIutils -lOpenIPMIpthread"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_var}/{log/,lib/%{name}},/etc/{rc.d/init.d/,collectd.d}} \
	$RPM_BUILD_ROOT{%{_appdir}/cgi-bin,%{_webappdir},%{_pkglibdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

touch $RPM_BUILD_ROOT%{_var}/log/collectd.log
install %{SOURCE2} $RPM_BUILD_ROOT/etc/rc.d/init.d/%{name}

# Web frontend:
install contrib/collection.conf $RPM_BUILD_ROOT%{_webappdir}
install contrib/collection.cgi $RPM_BUILD_ROOT%{_appdir}/cgi-bin
install %{SOURCE3} $RPM_BUILD_ROOT%{_webappdir}/apache.conf
install %{SOURCE3} $RPM_BUILD_ROOT%{_webappdir}/httpd.conf

### Configs instalation ###
# Example config in sources: src/collectd.conf
install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/collectd.conf
install %{SOURCE10} $RPM_BUILD_ROOT%{_sysconfdir}/collectd.d/ascent.conf
install %{SOURCE11} $RPM_BUILD_ROOT%{_sysconfdir}/collectd.d/apache.conf
%{?with_dns:install %{SOURCE12} $RPM_BUILD_ROOT%{_sysconfdir}/collectd.d/dns.conf}
install %{SOURCE13} $RPM_BUILD_ROOT%{_sysconfdir}/collectd.d/hddtemp.conf
%{?with_ipmi:install %{SOURCE14} $RPM_BUILD_ROOT%{_sysconfdir}/collectd.d/ipmi.conf}
install %{SOURCE15} $RPM_BUILD_ROOT%{_sysconfdir}/collectd.d/mysql.conf
install %{SOURCE16} $RPM_BUILD_ROOT%{_sysconfdir}/collectd.d/nginx.conf
install %{SOURCE17} $RPM_BUILD_ROOT%{_sysconfdir}/collectd.d/notify_desktop.conf
install %{SOURCE18} $RPM_BUILD_ROOT%{_sysconfdir}/collectd.d/notify_email.conf
install %{SOURCE19} $RPM_BUILD_ROOT%{_sysconfdir}/collectd.d/nut.conf
install %{SOURCE20} $RPM_BUILD_ROOT%{_sysconfdir}/collectd.d/ping.conf
install %{SOURCE21} $RPM_BUILD_ROOT%{_sysconfdir}/collectd.d/postgresql.conf
install %{SOURCE22} $RPM_BUILD_ROOT%{_sysconfdir}/collectd.d/powerdns.conf
install %{SOURCE23} $RPM_BUILD_ROOT%{_sysconfdir}/collectd.d/rrdtool.conf
install %{SOURCE24} $RPM_BUILD_ROOT%{_sysconfdir}/collectd.d/sensors.conf
install %{SOURCE25} $RPM_BUILD_ROOT%{_sysconfdir}/collectd.d/snmp.conf
install %{SOURCE26} $RPM_BUILD_ROOT%{_sysconfdir}/collectd.d/uuid.conf
install %{SOURCE27} $RPM_BUILD_ROOT%{_sysconfdir}/collectd.d/xmms.conf
install %{SOURCE28} $RPM_BUILD_ROOT%{_sysconfdir}/collectd.d/tcpconns.conf
install %{SOURCE29} $RPM_BUILD_ROOT%{_sysconfdir}/collectd.d/teamspeak2.conf
install %{SOURCE30} $RPM_BUILD_ROOT%{_sysconfdir}/collectd.d/thermal.conf
install %{SOURCE31} $RPM_BUILD_ROOT%{_sysconfdir}/collectd.d/unixsock.conf
install %{SOURCE32} $RPM_BUILD_ROOT%{_sysconfdir}/collectd.d/users.conf
install %{SOURCE33} $RPM_BUILD_ROOT%{_sysconfdir}/collectd.d/vmem.conf
install %{SOURCE34} $RPM_BUILD_ROOT%{_sysconfdir}/collectd.d/vserver.conf
install %{SOURCE35} $RPM_BUILD_ROOT%{_sysconfdir}/collectd.d/wireless.conf
install %{SOURCE36} $RPM_BUILD_ROOT%{_sysconfdir}/collectd.d/apcups.conf
install %{SOURCE37} $RPM_BUILD_ROOT%{_sysconfdir}/collectd.d/battery.conf
install %{SOURCE38} $RPM_BUILD_ROOT%{_sysconfdir}/collectd.d/cpufreq.conf
install %{SOURCE39} $RPM_BUILD_ROOT%{_sysconfdir}/collectd.d/cpu.conf
install %{SOURCE40} $RPM_BUILD_ROOT%{_sysconfdir}/collectd.d/csv.conf
install %{SOURCE41} $RPM_BUILD_ROOT%{_sysconfdir}/collectd.d/df.conf
install %{SOURCE42} $RPM_BUILD_ROOT%{_sysconfdir}/collectd.d/disk.conf
install %{SOURCE43} $RPM_BUILD_ROOT%{_sysconfdir}/collectd.d/email.conf
install %{SOURCE44} $RPM_BUILD_ROOT%{_sysconfdir}/collectd.d/entropy.conf
install %{SOURCE45} $RPM_BUILD_ROOT%{_sysconfdir}/collectd.d/exec.conf
install %{SOURCE46} $RPM_BUILD_ROOT%{_sysconfdir}/collectd.d/filecount.conf
install %{SOURCE47} $RPM_BUILD_ROOT%{_sysconfdir}/collectd.d/interface.conf
%{?with_iptables:install %{SOURCE48} $RPM_BUILD_ROOT%{_sysconfdir}/collectd.d/iptables.conf}
install %{SOURCE49} $RPM_BUILD_ROOT%{_sysconfdir}/collectd.d/irq.conf
install %{SOURCE51} $RPM_BUILD_ROOT%{_sysconfdir}/collectd.d/load.conf
install %{SOURCE52} $RPM_BUILD_ROOT%{_sysconfdir}/collectd.d/logfile.conf
install %{SOURCE53} $RPM_BUILD_ROOT%{_sysconfdir}/collectd.d/mbmon.conf
install %{SOURCE54} $RPM_BUILD_ROOT%{_sysconfdir}/collectd.d/memcached.conf
install %{SOURCE55} $RPM_BUILD_ROOT%{_sysconfdir}/collectd.d/memory.conf
%{?with_multimeter:install %{SOURCE56} $RPM_BUILD_ROOT%{_sysconfdir}/collectd.d/multimeter.conf}
%{?with_netlink:install %{SOURCE57} $RPM_BUILD_ROOT%{_sysconfdir}/collectd.d/netlink.conf}
install %{SOURCE58} $RPM_BUILD_ROOT%{_sysconfdir}/collectd.d/network.conf
install %{SOURCE59} $RPM_BUILD_ROOT%{_sysconfdir}/collectd.d/nfs.conf
install %{SOURCE60} $RPM_BUILD_ROOT%{_sysconfdir}/collectd.d/ntpd.conf
install %{SOURCE61} $RPM_BUILD_ROOT%{_sysconfdir}/collectd.d/processes.conf
install %{SOURCE62} $RPM_BUILD_ROOT%{_sysconfdir}/collectd.d/serial.conf
install %{SOURCE63} $RPM_BUILD_ROOT%{_sysconfdir}/collectd.d/swap.conf
install %{SOURCE64} $RPM_BUILD_ROOT%{_sysconfdir}/collectd.d/syslog.conf
install %{SOURCE65} $RPM_BUILD_ROOT%{_sysconfdir}/collectd.d/tail.conf

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

%define module_scripts() \
%post %1 \
%service %{name} restart \
\
%postun %1 \
%service %{name} restart

%module_scripts apache
%module_scripts apcups
%module_scripts ascent
%module_scripts battery
%module_scripts cpufreq
%module_scripts cpu
%module_scripts csv
%module_scripts df
%module_scripts disk
%{?with_dns:%module_scripts dns}
%module_scripts email
%module_scripts entropy
%module_scripts exec
%module_scripts filecount
%module_scripts hddtemp
%module_scripts interface
%{?with_ipmi:%module_scripts ipmi}
%{?with_iptables:%module_scripts iptables}
%module_scripts irq
%module_scripts load
%module_scripts logfile
%module_scripts mbmon
%module_scripts memcached
%module_scripts memory
%{?with_multimeter:%module_scripts multimeter}
%module_scripts mysql
%{?with_netlink:%module_scripts netlink}
%module_scripts network
%module_scripts nfs
%module_scripts nginx
%module_scripts notify_desktop
%module_scripts notify_email
%module_scripts ntpd
%module_scripts nut
%module_scripts ping
%module_scripts postgresql
%module_scripts powerdns
%module_scripts processes
%module_scripts rrdtool
%module_scripts sensors
%module_scripts serial
%module_scripts snmp
%module_scripts swap
%module_scripts syslog
%module_scripts tail
%module_scripts tcpconns
%module_scripts teamspeak2
%module_scripts thermal
%module_scripts unixsock
%module_scripts users
%module_scripts uuid
%module_scripts vmem
%module_scripts vserver
%module_scripts wireless
%module_scripts xmms

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
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.conf
%dir %{_sysconfdir}/%{name}.d
%attr(755,root,root) %{_sbindir}/collectd
%attr(755,root,root) %{_sbindir}/collectdmon
%attr(755,root,root) %{_bindir}/collectd-nagios
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/types.db
%attr(754,root,root) /etc/rc.d/init.d/%{name}
%{_mandir}/man1/collectd.1*
%{_mandir}/man1/collectd-nagios.1*
%{_mandir}/man5/collectd.conf.5*
%{_mandir}/man5/collectd-perl.5*
%{_mandir}/man1/collectdmon.1*
%{_mandir}/man5/types.db.5*
%{_var}/log/collectd.log
%dir %{_var}/lib/%{name}

%files collection
%defattr(644,root,root,755)
%dir %{_webappdir}
%config(noreplace) %verify(not md5 mtime size) %{_webappdir}/collection.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_webappdir}/apache.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_webappdir}/httpd.conf
%dir %{_appdir}
%dir %{_appdir}/cgi-bin
%attr(755,root,root) %{_appdir}/cgi-bin/collection.cgi

########## PLUGINS:
%files apcups
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/apcups.conf
%attr(755,root,root) %{_libdir}/%{name}/apcups.so

%files ascent
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/ascent.conf
%attr(755,root,root) %{_libdir}/%{name}/ascent.so

%files apache
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/apache.conf
%attr(755,root,root) %{_libdir}/%{name}/apache.so

%files battery
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/battery.conf
%attr(755,root,root) %{_libdir}/%{name}/battery.so

%files cpu
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/cpu.conf
%attr(755,root,root) %{_libdir}/%{name}/cpu.so

%files cpufreq
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/cpufreq.conf
%attr(755,root,root) %{_libdir}/%{name}/cpufreq.so

%files csv
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/csv.conf
%attr(755,root,root) %{_libdir}/%{name}/csv.so

%files df
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/df.conf
%attr(755,root,root) %{_libdir}/%{name}/df.so

%files disk
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/disk.conf
%attr(755,root,root) %{_libdir}/%{name}/disk.so

%files dns
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/dns.conf
%attr(755,root,root) %{_libdir}/%{name}/dns.so

%files email
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/email.conf
%attr(755,root,root) %{_libdir}/%{name}/email.so
%{_mandir}/man5/collectd-email.5*

%files entropy
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/entropy.conf
%attr(755,root,root) %{_libdir}/%{name}/entropy.so

%files exec
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/exec.conf
%attr(755,root,root) %{_libdir}/%{name}/exec.so
%{_mandir}/man5/collectd-exec.5*

%files filecount
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/filecount.conf
%attr(755,root,root) %{_libdir}/%{name}/filecount.so

%files hddtemp
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/hddtemp.conf
%attr(755,root,root) %{_libdir}/%{name}/hddtemp.so

%files interface
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/interface.conf
%attr(755,root,root) %{_libdir}/%{name}/interface.so

%if %{with ipmi}
%files ipmi
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/ipmi.conf
%attr(755,root,root) %{_libdir}/%{name}/ipmi.so
%endif

%if %{with iptables}
%files iptables
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/iptables.conf
%attr(755,root,root) %{_libdir}/%{name}/iptables.so
%endif

%files irq
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/irq.conf
%attr(755,root,root) %{_libdir}/%{name}/irq.so

%files load
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/load.conf
%attr(755,root,root) %{_libdir}/%{name}/load.so

%files logfile
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/logfile.conf
%attr(755,root,root) %{_libdir}/%{name}/logfile.so

%files mbmon
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/mbmon.conf
%attr(755,root,root) %{_libdir}/%{name}/mbmon.so

%files memcached
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/memcached.conf
%attr(755,root,root) %{_libdir}/%{name}/memcached.so

%files memory
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/memory.conf
%attr(755,root,root) %{_libdir}/%{name}/memory.so

%if %{with multimeter}
%files multimeter
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/multimeter.conf
%attr(755,root,root) %{_libdir}/%{name}/multimeter.so
%endif

%files mysql
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/mysql.conf
%attr(755,root,root) %{_libdir}/%{name}/mysql.so

%if %{with netlink}
%files netlink
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/netlink.conf
%attr(755,root,root) %{_libdir}/%{name}/netlink.so
%endif

%files network
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/network.conf
%attr(755,root,root) %{_libdir}/%{name}/network.so

%files nfs
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/nfs.conf
%attr(755,root,root) %{_libdir}/%{name}/nfs.so

%files nginx
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/nginx.conf
%attr(755,root,root) %{_libdir}/%{name}/nginx.so

%files notify_desktop
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/notify_desktop.conf
%attr(755,root,root) %{_libdir}/%{name}/notify_desktop.so

%files notify_email
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/notify_email.conf
%attr(755,root,root) %{_libdir}/%{name}/notify_email.so

%files ntpd
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/ntpd.conf
%attr(755,root,root) %{_libdir}/%{name}/ntpd.so

%files nut
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/nut.conf
%attr(755,root,root) %{_libdir}/%{name}/nut.so

%files ping
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/ping.conf
%attr(755,root,root) %{_libdir}/%{name}/ping.so

%files postgresql
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/postgresql.conf
%attr(755,root,root) %{_libdir}/%{name}/postgresql.so

%files powerdns
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/powerdns.conf
%attr(755,root,root) %{_libdir}/%{name}/powerdns.so

%files processes
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/processes.conf
%attr(755,root,root) %{_libdir}/%{name}/processes.so

%files rrdtool
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/rrdtool.conf
%attr(755,root,root) %{_libdir}/%{name}/rrdtool.so

%files sensors
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/sensors.conf
%attr(755,root,root) %{_libdir}/%{name}/sensors.so

%files serial
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/serial.conf
%attr(755,root,root) %{_libdir}/%{name}/serial.so

%files snmp
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/snmp.conf
%attr(755,root,root) %{_libdir}/%{name}/snmp.so
%{_mandir}/man5/collectd-snmp.5*

%files swap
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/swap.conf
%attr(755,root,root) %{_libdir}/%{name}/swap.so

%files syslog
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/syslog.conf
%attr(755,root,root) %{_libdir}/%{name}/syslog.so

%files tail
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/tail.conf
%attr(755,root,root) %{_libdir}/%{name}/tail.so

%files tcpconns
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/tcpconns.conf
%attr(755,root,root) %{_libdir}/%{name}/tcpconns.so

%files teamspeak2
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/teamspeak2.conf
%attr(755,root,root) %{_libdir}/%{name}/teamspeak2.so

%files thermal
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/thermal.conf
%attr(755,root,root) %{_libdir}/%{name}/thermal.so

%files unixsock
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/unixsock.conf
%attr(755,root,root) %{_libdir}/%{name}/unixsock.so
%{_mandir}/man5/collectd-unixsock.5*

%files users
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/users.conf
%attr(755,root,root) %{_libdir}/%{name}/users.so

%files uuid
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/uuid.conf
%attr(755,root,root) %{_libdir}/%{name}/uuid.so

%files vmem
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/vmem.conf
%attr(755,root,root) %{_libdir}/%{name}/vmem.so

%files vserver
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/vserver.conf
%attr(755,root,root) %{_libdir}/%{name}/vserver.so

%files wireless
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/wireless.conf
%attr(755,root,root) %{_libdir}/%{name}/wireless.so

%files xmms
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/xmms.conf
%attr(755,root,root) %{_libdir}/%{name}/xmms.so
