# TODO:
#warning: Installed (but unpackaged) file(s) found:
#    /etc/collectd.d/aggregation.conf
#    /etc/collectd.d/ceph.conf
#    /etc/collectd.d/cgroups.conf
#    /etc/collectd.d/drbd.conf
#    /etc/collectd.d/fhcount.conf
#    /etc/collectd.d/ipc.conf
#    /etc/collectd.d/java.conf
#    /etc/collectd.d/log_logstash.conf
#    /etc/collectd.d/lvm.conf
#    /etc/collectd.d/openldap.conf
#    /etc/collectd.d/pinba.conf
#    /etc/collectd.d/redis.conf
#    /etc/collectd.d/sigrok.conf
#    /etc/collectd.d/smart.conf
#    /etc/collectd.d/statsd.conf
#    /etc/collectd.d/tail_csv.conf
#    /etc/collectd.d/target_v5upgrade.conf
#    /etc/collectd.d/turbostat.conf
#    /etc/collectd.d/write_log.conf
#    /etc/collectd.d/write_redis.conf
#    /etc/collectd.d/write_riemann.conf
#    /etc/collectd.d/write_sensu.conf
#    /etc/collectd.d/write_tsdb.conf
#    /etc/collectd.d/zfs_arc.conf
#    /etc/collectd.d/zookeeper.conf
#    /usr/bin/collectd-tg
#    /usr/lib64/collectd/aggregation.so
#    /usr/lib64/collectd/ceph.so
#    /usr/lib64/collectd/cgroups.so
#    /usr/lib64/collectd/drbd.so
#    /usr/lib64/collectd/fhcount.so
#    /usr/lib64/collectd/ipc.so
#    /usr/lib64/collectd/java.so
#    /usr/lib64/collectd/log_logstash.so
#    /usr/lib64/collectd/lvm.so
#    /usr/lib64/collectd/openldap.so
#    /usr/lib64/collectd/pinba.so
#    /usr/lib64/collectd/redis.so
#    /usr/lib64/collectd/sigrok.so
#    /usr/lib64/collectd/smart.so
#    /usr/lib64/collectd/statsd.so
#    /usr/lib64/collectd/tail_csv.so
#    /usr/lib64/collectd/turbostat.so
#    /usr/lib64/collectd/write_log.so
#    /usr/lib64/collectd/write_redis.so
#    /usr/lib64/collectd/write_riemann.so
#    /usr/lib64/collectd/write_sensu.so
#    /usr/lib64/collectd/write_tsdb.so
#    /usr/lib64/collectd/zfs_arc.so
#    /usr/lib64/collectd/zookeeper.so
#    /usr/share/collectd/collection3/README
#    /usr/share/collectd/collection3/bin/.htaccess
#    /usr/share/collectd/collection3/test.px
#    /usr/share/collectd/java/collectd-api.jar
#    /usr/share/collectd/java/generic-jmx.jar
#    /usr/share/man/man1/collectd-tg.1.gz
#
# - package contrib scripts as %doc
# - perl modules with Collectd classes package to separate package
# - Bundled libraries - check if its not changed ones and if it can be
#   mainstream library:
# liboconfig  . . . . . yes (shipped version)
# - Libraries not found by configure:
#   libcredis . . . . . . no (credis.h not found) (http://code.google.com/p/credis/)
#   libganglia  . . . . . no (gm_protocol.h not found) (http://ganglia.info/)
#   libiokit  . . . . . . no (Darwin only)
#   libjvm  . . . . . . . no (javac not found)
#   libkstat  . . . . . . no (Solaris only)
#   libkvm  . . . . . . . no (BSD only)
#   libnetapp . . . . . . no (netapp_api.h not found) (properitary)
#   libperfstat . . . . . no (AIX only)
#   librabbitmq . . . . . no (amqp.h not found) (http://hg.rabbitmq.com/rabbitmq-c/)
#   librouteros . . . . . no ('routeros_api.h' not found) (http://verplant.org/librouteros/)
#   libtokyotyrant  . . . no (tcrdb.h not found) (http://1978th.net/tokyotyrant/)
#   libyajl . . . . . . . no (yajl/yajl_parse.h not found)
#   protobuf-c  . . . . . no
#   oracle  . . . . . . . no (ORACLE_HOME is not set)
# - Disabled modules (build most of them an package):
#   amqp    . . . . . . . no
#   apple_sensors . . . . no             (Darwin only)
#   gmond . . . . . . . . no
#   ipvs  . . . . . . . . no             (ip_vs.h not found - llh to be fixed)
#   java  . . . . . . . . no
#   lpar... . . . . . . . no
#   multimeter  . . . . . no             ?
#   netapp  . . . . . . . no
#   onewire . . . . . . . no             (needs libowfs)
#   oracle  . . . . . . . no
#   pinba . . . . . . . . no
#   redis . . . . . . . . no
#   routeros  . . . . . . no
#   tape  . . . . . . . . no             ?
#   tokyotyrant . . . . . no
#   write_redis . . . . . no
#   zfs_arc . . . . . . . no
# - logrotate file for logfile plugin
# - %desc -l pl for plugins
# - package SpamAssassin plugin from contrib

# Conditional build:
%bcond_without	curl		# apache, ascent, bind, curl and nginx plugins
%bcond_without	dns		# DNS plugin
%bcond_without	ipmi		# IPMI plugin
%bcond_without	iptables	# iptables plugin
%bcond_with	java
%bcond_without	libesmtp	# notify_email plugin
%bcond_without	libvirt		# libvirt plugin
%bcond_without	modbus	# modbus plugin
%bcond_with	multimeter	# multimeter plugin
%bcond_without	mysql		# MySQL plugin
%bcond_without	netlink		# netlink plugin
%bcond_without	notify		# notify_desktop plugin
%bcond_without	ping		# ping plugin
%bcond_without	pgsql		# PostgreSQL plugin
%bcond_without	rrd		# rrdtool and rrdcached plugins
%bcond_without	sensors		# sensors plugin
%bcond_without	snmp		# SNMP plugin
%bcond_without	ups		# nut plugin
%bcond_without	varnish		# varnish plugin
%bcond_without	xml		# ascent, bind and libvirt plugins
%bcond_without	xmms		# XMMS plugin

Summary:	Collects system information in RRD files
Summary(pl.UTF-8):	Zbieranie informacji o systemie w plikach RRD
Name:		collectd
Version:	5.5.0
Release:	7
License:	GPL v2
Group:		Daemons
Source0:	http://collectd.org/files/%{name}-%{version}.tar.bz2
# Source0-md5:	c39305ef5514b44238b0d31f77e29e6a
Source1:	%{name}.conf
Source2:	%{name}.init
Source3:	%{name}-http.conf
Source4:	%{name}-lighttpd.conf
Source5:	%{name}-apache.conf
Source10:	%{name}-df.conf
Source11:	%{name}-rrdtool.conf
Patch0:		%{name}-collection.patch
Patch1:		compile.patch
Patch2:		noquote.patch

Patch5:		no-Werror.patch
Patch6:		%{name}-modbus.patch
URL:		http://collectd.org/
%{?with_ipmi:BuildRequires:	OpenIPMI-devel >= 2.0.14-3}
BuildRequires:	autoconf
BuildRequires:	automake
%{?with_curl:BuildRequires:	curl-devel}
%{?with_iptables:BuildRequires:	iptables-devel >= 1.4.1.1-4}
BuildRequires:	libdbi-devel
%{?with_libesmtp:BuildRequires:	libesmtp-devel}
BuildRequires:	libltdl-devel
BuildRequires:	libmemcached-devel
%{?with_modbus:BuildRequires:	libmodbus-devel}
%{?with_netlink:BuildRequires:	libmnl-devel}
%{?with_libvirt:BuildRequires:	libnl1-devel}
%{?with_notify:BuildRequires:	libnotify-devel}
%{?with_ping:BuildRequires:	liboping-devel}
%{?with_dns:BuildRequires:	libpcap-devel}
BuildRequires:	libstatgrab-devel >= 0.12
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
%{?with_libvirt:BuildRequires:	libvirt-devel}
%{?with_xml:BuildRequires:	libxml2-devel}
%{?with_sensors:BuildRequires:	lm_sensors-devel}
%{?with_mysql:BuildRequires:	mysql-devel}
BuildRequires:	ncurses-devel
%{?with_snmp:BuildRequires:	net-snmp-devel}
%{?with_libvirt:BuildRequires:	numactl-devel}
%{?with_ups:BuildRequires:	nut-devel}
BuildRequires:	perl-devel
BuildRequires:	pkgconfig
%{?with_pgsql:BuildRequires:	postgresql-devel}
BuildRequires:	python-devel
BuildRequires:	python-modules
BuildRequires:	rpmbuild(macros) >= 1.268
%{?with_rrd:BuildRequires:	rrdtool-devel}
%{?with_varnish:BuildRequires:		varnish-devel}
BuildRequires:	which
#BuildRequires:	xfsprogs-devel
%{?with_xmms:BuildRequires:	xmms-devel}
BuildRequires:	yajl-devel
Requires(post,preun):	/sbin/chkconfig
Requires:	%{name}-libs = %{version}-%{release}
Requires:	rc-scripts
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_pkglibdir	%{_sharedstatedir}/%{name}
%define		_webapps	/etc/webapps
%define		_webapp		%{name}
%define		_webappdir	%{_webapps}/%{_webapp}
%define		_appdir		%{_datadir}/%{_webapp}

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

%package libs
Summary:	%{name} libraries
Summary(pl.UTF-8):	Biblioteki %{name}
Group:		Libraries

%description libs
%{name} libraries.

%description libs -l pl.UTF-8
Biblioteki %{name}.

%package devel
Summary:	Header files for %{name} libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek %{name}
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files for %{name} libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek %{name}.

%package static
Summary:	Static files for %{name} libraries
Summary(pl.UTF-8):	Pliki statyczne bibliotek %{name}
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description static
Static files for %{name} libraries.

%description static -l pl.UTF-8
Pliki statyczne bibliotek %{name}.

%package apache
Summary:	apache-plugin for collectd
Summary(pl.UTF-8):	Wtyczka apache dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description apache
This plugin collect data provided by Apache's `mod_status'.

%description apache -l pl.UTF-8
Wtyczka collectd zbierająca informacje udostępniane przez moduł
'mod_status' Apacha.

%package apcups
Summary:	APC UPS plugin for collectd
Summary(pl.UTF-8):	Wtyczka APC UPS dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description apcups
The APC UPS plugin connects to an instance of Apcupsd to read various
statistics about a connected uninterruptible power supply (UPS), such
as voltage, load, etc.

%package ascent
Summary:	ascent-plugin for collectd
Summary(pl.UTF-8):	Wtyczka ascent dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description ascent
The Ascent plugin reads and parses the statistics page of Ascent, a
free and open-source server software for the game World of Warcraft by
Blizzard Entertainment.

%package battery
Summary:	battery plugin for collectd
Summary(pl.UTF-8):	Wtyczka battery dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description battery
This plugin collects the battery's charge, the drawn current and the
battery's voltage.

%package bind
Summary:	bind plugin for collectd
Summary(pl.UTF-8):	Wtyczka bind dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description bind
Starting with BIND 9.5.0, the most widely used DNS server software
provides extensive statistics about queries, responses and lots of
other information. The bind plugin retrieves this information that's
encoded in XML and provided via HTTP and submits the values to
collectd.

%package collection
Summary:	Web script for collectd
Summary(pl.UTF-8):	Web script for collectd
Group:		Applications/WWW
Requires:	%{name} = %{version}-%{release}
Requires:	perl(CGI)
Requires:	perl(Data::Dumper)
Requires:	perl(HTML::Entities)
Requires:	perl(RRDs)
Requires:	perl(URI::Escape)
Requires:	webserver(cgi)
Suggests:	fonts-TTF-DejaVu
Conflicts:	apache-base < 2.4.0-1

%description collection
Web script for collectd.

%package collection3
Summary:	Web script for collectd
Summary(pl.UTF-8):	Web script for collectd
Group:		Applications/WWW
Requires:	%{name} = %{version}-%{release}
Requires:	perl(Config::General)
Requires:	perl(HTML::Entities)
Requires:	perl(RRDs)
Requires:	perl(Regexp::Common)
Requires:	perl-Collectd = %{version}-%{release}
Requires:	webserver(cgi)
Suggests:	fonts-TTF-DejaVu
Conflicts:	apache-base < 2.4.0-1

%description collection3
Web script for collectd.

%package contextswitch
Summary:	contextswitch-plugin for collectd
Summary(pl.UTF-8):	Wtyczka contextswitch dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description contextswitch
The ContextSwitch plugin collects the number of context switches done
by the operating system.

%package conntrack
Summary:	conntrack-plugin for collectd
Summary(pl.UTF-8):	Wtyczka conntrack dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description conntrack
The conntrack-plugin collects the connection tracking table size.

%package cpu
Summary:	cpu-plugin for collectd
Summary(pl.UTF-8):	Wtyczka cpu dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description cpu
The cpu-plugin collects the amount of time spent by the CPU in various
states, most notably executing user code, executing system code,
waiting for IO operations and being idle.

%package cpufreq
Summary:	cpufreq-plugin for collectd
Summary(pl.UTF-8):	Wtyczka cpufreq dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description cpufreq
Collects the current CPU's frequency, mostly for mobile computers.

%package csv
Summary:	CSV output plugin for collectd
Summary(pl.UTF-8):	Wtyczka wyjściowa CSV dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description csv
CSV output plugin for collectd.

%package curl
Summary:	cURL output plugin for collectd
Summary(pl.UTF-8):	Wtyczka wyjściowa cURL dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description curl
The curl plugin uses the libcurl to read web pages and the match
infrastructure (the same code used by the tail plugin) to use regular
expressions with the received data.

%package curl_json
Summary:	cURL JSON plugin for collectd
Summary(pl.UTF-8):	Wtyczka cURL JSON dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description curl_json
The cURL-JSON plugin queries JavaScript Object Notation (JSON) data
using the cURL library and parses it according to the user's
configuration using Yet Another JSON Library (YAJL). This can be used
to query statistics information from a CouchDB instance, for example.

%package dbi
Summary:	dbi plugin for collectd
Summary(pl.UTF-8):	Wtyczka dbi dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description dbi
This plugin uses the dbi library to connect to various databases,
execute SQL statements and read back the results. dbi is an acronym
for "database interface" in case you were wondering about the name.
You can configure how each column is to be interpreted and the plugin
will generate one or more data sets from each row returned according
to these rules.

%package df
Summary:	df-plugin for collectd
Summary(pl.UTF-8):	Wtyczka df dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description df
The df-plugin collects file system usage information, i. e. basically
how much space on a mounted partition is used and how much is
available. It's named after and very similar to the df(1) UNIX command
that's been around forever.

%package disk
Summary:	disk-plugin for collectd
Summary(pl.UTF-8):	Wtyczka disk dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description disk
This plugin collects performance statistics of harddisks and, where
supported, partitions.

%package dns
Summary:	dns-plugin for collectd
Summary(pl.UTF-8):	Wtyczka dns dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}
Requires:	perl-rrdtool

%description dns
This plugin has a similar functionality to dnstop: It uses libpcap to
get a copy of all traffic from/to port UDP/53 (that's the DNS port),
interprets the packets and collects statistics of your DNS traffic.

%package email
Summary:	email-plugin for collectd
Summary(pl.UTF-8):	Wtyczka email dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description email
The email plugin opens an UNIX-socket over which one can submit email
statistics, such as the number of ``ham'', ``spam'', ``virus'', etc.
mails received/handled, spam scores and matched spam checks.

This plugin is intended to be used with the the
Mail::SpamAssassin::Plugin::Collectd manpage SpamAssassin-plugin which
is included in contrib/, but is of course not limited to that use.

%package entropy
Summary:	entropy-plugin for collectd
Summary(pl.UTF-8):	Wtyczka entropy dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description entropy
The Entropy plugin collects the available entropy on a system. Entropy
is important to generate random numbers, which are used for
encryption, authorization and similar tasks.

%package ethstat
Summary:	ethstat-plugin for collectd
Summary(pl.UTF-8):	Wyczka ethstat dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description ethstat
The ethstat plugin reads performance statistics directly from ethernet
cards

%package exec
Summary:	exec-plugin for collectd
Summary(pl.UTF-8):	Wtyczka exec dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description exec
The exec plugin forks of an executable either to receive values or to
dispatch notifications to the outside world.

%package filecount
Summary:	filecount-plugin for collectd
Summary(pl.UTF-8):	Wtyczka filecount dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description filecount
The filecount-plugin does something very simple: Count the number of
files in a directory and all its subdirectories. This can be used for
a variety of statistics, for example the queue length of an MTA, the
number of PHP sessions of a web server or simply the number of files
in your home directory.

%package fscache
Summary:	fscache-plugin for collectd
Summary(pl.UTF-8):	Wtyczka fscache dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description fscache
The fscache-plugin collects statistics about Linux file-system based
caching framework.

%package hddtemp
Summary:	hddtemp-plugin for collectd
Summary(pl.UTF-8):	Wtyczka hddtemp dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}
Suggests:	hddtemp-hddtempd

%description hddtemp
Temperature of harddisks. The temperatures are provided via S.M.A.R.T.
and queried by the external hddtemp-daemon.

%package interface
Summary:	interface-plugin for collectd
Summary(pl.UTF-8):	Wtyczka interface dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description interface
The interface-plugin collects information about the traffic (octets),
packets and errors of interfaces.

%package iptables
Summary:	iptables-plugin for collectd
Summary(pl.UTF-8):	Wtyczka iptables dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description iptables
With this plugin you can gather statistics from your ip_tables based
packetfilter (aka. firewall). It can collect the byte- and
packet-counters of selected rules and submit them to collectd. You can
select rules that should be collected wither by its position (e.g.
"the fourth rule in the INPUT queue in the filter table") or by its
comment (using the COMMENT match). This means that depending on your
firewall layout you can collect certain services (such as the amount
of web-traffic), source or destination hosts or networks, dropped
packets and much more.

%package ipmi
Summary:	ipmi-plugin for collectd
Summary(pl.UTF-8):	Wtyczka ipmi dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description ipmi
The IPMI plugin uses the OpenIPMI library to read hardware sensors
from servers using the Intelligent Platform Management Interface
(IPMI). IPMI is very common with server hardware but usually not
available in consumer hardware.

%package irq
Summary:	IRQs-plugin for collectd
Summary(pl.UTF-8):	Wtyczka IRQs dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description irq
The IRQ plugin collects the number of times each interrupt has been
handled by the operating system.

%package libvirt
Summary:	libvirt-plugin for collectd
Summary(pl.UTF-8):	Wtyczka libvirt dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description libvirt
The libvirt plugin uses the virtualization API libvirt, created by
RedHat's Emerging Technology group, to gather statistics about
virtualized guests on a system. This way, you can collect CPU, network
interface and block device usage for each guest without installing
collectd on the guest systems. Because the statistics are received
from the hypervisor directly, this works not only with
para-virtualized hosts, but with hardware virtualized machines, too.

%package load
Summary:	load-plugin for collectd
Summary(pl.UTF-8):	Wtyczka load dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description load
Collects the system load. These numbers give a rough overview over the
utilization of a machine, though their meaning is mostly overrated.

%package logfile
Summary:	logfile-plugin for collectd
Summary(pl.UTF-8):	Wtyczka logfile dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description logfile
The LogFile plugin receives log messages from the daemon and writes
them to a text file.

%package madwifi
Summary:	madwifi plugin for collectd
Summary(pl.UTF-8):	Wtyczka madwifi dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description madwifi
The MadWifi plugin collects information about Atheros wireless LAN
chipsets from the MadWifi driver. It uses the /sys filesystem to
identify cards handled by this driver automatically but can be
configured manually, too. Because very many statistics are available,
an advanced selection mechanism is provided.

%package match_empty_counter
Summary:	match_empty_counter plugin for collectd
Summary(pl.UTF-8):	Wtyczka match_empty_counter dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description match_empty_counter
Empty Counter match matches value lists, where at least one data
source is of type COUNTER and the counter value of all counter data
sources is zero.

%package match_hashed
Summary:	match_hashed plugin for collectd
Summary(pl.UTF-8):	Wtyczka match_hashed dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description match_hashed
match_hashed plugin for collectd - match for simple load balancing and
redundant storage.

%package match_regex
Summary:	match_regex plugin for collectd
Summary(pl.UTF-8):	Wtyczka match_regex dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description match_regex
match_regex plugin for collectd.

%package match_timediff
Summary:	match_timediff plugin for collectd
Summary(pl.UTF-8):	Wtyczka match_timediff dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description match_timediff
match_timediff plugin for collectd.

%package match_value
Summary:	match_value plugin for collectd
Summary(pl.UTF-8):	Wtyczka match_value dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description match_value
match_value plugin for collectd.

%package mbmon
Summary:	mbmon plugin for collectd
Summary(pl.UTF-8):	Wtyczka mbmon dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description mbmon
The mbmon plugin uses mbmon to retrieve temperature, voltage, etc.

%package md
Summary:	md plugin for collectd
Summary(pl.UTF-8):	Wtyczka md dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description md
The md plugin reports the number of disks in various states in Linux
software RAID devices.

%package memcachec
Summary:	memcachec-plugin for collectd
Summary(pl.UTF-8):	Wtyczka memcachec dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description memcachec
The memcachec plugin connects to a memcached server, queries one or
more given pages and parses the returned data according to user
specification. The matches used are similar to the matches used in the
cURL and Tail plugins.

%package memcached
Summary:	memcached-plugin for collectd
Summary(pl.UTF-8):	Wtyczka memcached dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description memcached
The memcached plugin connects to a memcached daemon and collects the
number of connections and requests handled by the daemon, the CPU
resources consumed, number of items cached, number of threads, and
bytes sent and received.

%package memory
Summary:	memory-plugin for collectd
Summary(pl.UTF-8):	Wtyczka memory dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description memory
Collects physical memory utilization for collectd.

%package modbus
Summary:	modbus-plugin for collectd
Summary(pl.UTF-8):	Wtyczka modbus dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description modbus
The Modbus plugin connects to a Modbus "slave" via Modbus/TCP and
reads register values. It supports reading single registers (unsigned
16 bit values), large integer values (unsigned 32 bit values) and
floating point values (two registers interpreted as IEEE floats in big
endian notation).

%package multimeter
Summary:	multimeter-plugin for collectd
Summary(pl.UTF-8):	Wtyczka multimeter dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description multimeter
The Multimeter plugin reads a value (usually a voltage or current)
from a multimeter connected to a serial bus. The plugin tries
/dev/ttyS0-9 in order to find a multimeter – no configuration is
possible.

The multimeter used for development was a Metex M-4650CR.

%package mysql
Summary:	mysql-plugin for collectd
Summary(pl.UTF-8):	Moduł mysql dla collectd.
Group:		Daemons
Requires:	%{name} = %{version}-%{release}
Requires:	mysql-client

%description mysql
MySQL querying plugin. This plugins provides data of issued commands,
called handlers and database traffic.

%description mysql -l pl.UTF-8
Moduł odpytujący MySQL. Wtyczka udostępnia dane o wydawanych
poleceniach, wywoływanych procedurach obsługi i ruchu bazodanowym.

%package netlink
Summary:	netlink-plugin for collectd
Summary(pl.UTF-8):	Wtyczka netlink dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description netlink
This plugin will open a netlink socket to the Linux kernel and use it
to get statistics for interfaces, qdiscs, classes, and, if you can
make use of it, filters. Since in most setups many of the statistics
this plugin can collect aren't of interest, you can select which
information to gather using the configuration.

%package network
Summary:	network-plugin for collectd
Summary(pl.UTF-8):	Wtyczka network dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description network
The Network plugin can send values to other instances and receive
values from other %{name} instances.

%package nfs
Summary:	NFS-plugin for collectd
Summary(pl.UTF-8):	Wtyczka NFS dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description nfs
The nfs plugin counts the number of procedure calls of the different
NFS procedures.

%package nginx
Summary:	nginx-plugin for collectd
Summary(pl.UTF-8):	Wtyczka nginx dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description nginx
This plugin collects the number of connections and requests handled by
the nginx daemon, a HTTP and mail server/proxy. It queries the page
provided by the ngx_http_stub_status_module module, which isn't
compiled by default.

%package notify_desktop
Summary:	notify_desktop for collectd
Summary(pl.UTF-8):	Wtyczka notify_desktop dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}
Requires:	dbus(org.freedesktop.Notifications)

%description notify_desktop
This plugin sends a desktop notification to a notification daemon, as
defined in the Desktop Notification Specification.

%package notify_email
Summary:	notify_email-plugin for collectd
Summary(pl.UTF-8):	Wtyczka notify_email dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description notify_email
The Notify Email plugin uses libESMTP to send notifications to a
configured email address(es).

%package ntpd
Summary:	ntpd-plugin for collectd
Summary(pl.UTF-8):	Wtyczka ntpd dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description ntpd
The NTPd plugin queries an NTP server (usually the local one, where
statistics access is allowed) and extracts :
- "local" clock parameters: time offset, error and offset loop,
- parameters for each NTP server used to sync time: offset,
  dispersion, delay.

%package numa
Summary:	numa-plugin for collectd
Summary(pl.UTF-8):	Wtyczka numa dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description numa
The numa plugin reports statistics of the Non-Uniform Memory Access
(NUMA) subsystem of Linux.

%package nut
Summary:	nut-plugin for collectd
Summary(pl.UTF-8):	Wtyczka nut dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description nut
UPS statistics using the Network UPS Tools. These statistics include
basically everything NUT will give us, including voltages, currents,
power, frequencies, load, and temperatures.

%package olsrd
Summary:	olsrd plugin for collectd
Summary(pl.UTF-8):	Wtyczka olsrd dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description olsrd
The olsrd plugin reads information about meshed networks from the
txtinfo plugin of the Optimized Link State Routing daemon (olsrd).

%package openvpn
Summary:	openvpn plugin for collectd
Summary(pl.UTF-8):	Wtyczka openvpn dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}
Requires:	openvpn

%description openvpn
The OpenVPN plugin reads a status file maintained by OpenVPN and
gathers traffic statistics about connected clients.

%package perl
Summary:	perl plugin for collectd
Summary(pl.UTF-8):	Wtyczka perl dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}
Requires:	perl-Collectd = %{version}-%{release}

%description perl
The Perl plugin embeds a Perl interpreter into collectd and exposes
the application programming interface (API) to Perl-scripts. This
allows to write own plugins in the popular scripting language, which
are then loaded and executed by the daemon without the need to start a
new process and interpreter every few seconds. Perl-modules written
for the Perl plugin are therefore more powerful and efficient than
scripts executed by the Exec plugin.

%package ping
Summary:	ping-plugin for collectd
Summary(pl.UTF-8):	Wtyczka ping dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}
Requires:	liboping >= 1.1.2

%description ping
The network latency is measured as a roundtrip time. An
ICMP-echo-request (aka. "ping")is sent to a host and the time needed
for his echo-reply (aka. "pong") to arrive is measured. If a reply is
not received within one second the plugin will no longer expect a
reply and return. This may happen in several circumstances, e. g. the
packet is lost, the host is down, a router has dismissed the packet,
etc.

%package postgresql
Summary:	mysql-plugin for collectd
Summary(pl.UTF-8):	Moduł postgresql dla collectd.
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description postgresql
The postgresql plugin queries statistics from PostgreSQL databases. It
keeps a persistent connection to all configured databases and tries to
reconnect if the connection has been interrupted.

%package powerdns
Summary:	powerdns-plugin for collectd
Summary(pl.UTF-8):	Wtyczka powerdns dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description powerdns
The powerdns plugin queries statistics from an authoritative PowerDNS
nameserver and/or a PowerDNS recursor. Since both offer a wide variety
of values, many of which are probably meaningless to most users, but
may be useful for some.

%package processes
Summary:	processes-plugin for collectd
Summary(pl.UTF-8):	Wtyczka processes dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description processes
This plugin collects the number of processes, grouped by their state
(e.g. running, sleeping, zombies, etc.). In addition to that, it can
select detailed statistics about selected processes, grouped by name.

%package protocols
Summary:	protocols-plugin for collectd
Summary(pl.UTF-8):	Wtyczka protocols dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description protocols
The protocols-plugin provides information about network protocols,
such as IP, TCP and UDP.

%package python
Summary:	python-plugin for collectd
Summary(pl.UTF-8):	Wtyczka python dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description python
The Python plugin embeds a Python interpreter into collectd and
exposes the application programming interface (API) to Python-scripts.
This allows to write own plugins in the popular scripting language,
which are then loaded and executed by the daemon without the need to
start a new process and interpreter every few seconds. Python-modules
written for the Python plugin are therefore more powerful and
efficient than scripts executed by the Exec plugin.

%package rrdcached
Summary:	rrdcached-plugin for collectd
Summary(pl.UTF-8):	Wtyczka rrdcached dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description rrdcached
The rrdcached plugin uses the RRDtool accelerator daemon, rrdcached,
to store values to RRD files in an efficient manner. The combination
of the rrdcached plugin and the rrdcached daemon is very similar to
the way the rrdtool plugin works.

%package rrdtool
Summary:	rrdtool-plugin for collectd
Summary(pl.UTF-8):	Wtyczka rrdtool dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}
Requires:	rrdtool

%description rrdtool
The RRDtool plugin writes values to RRD-files using librrd.

%package sensors
Summary:	sensors-plugin for collectd
Summary(pl.UTF-8):	Wtyczka sensors dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description sensors
This plugin uses lm-sensors to read hardware sensors. You will need to
configure lm-sensors before this plugin will collect any usefull and
correct data.

%package serial
Summary:	serial-plugin for collectd
Summary(pl.UTF-8):	Wtyczka serial dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description serial
The Serial plugin collects the traffic on serial interfaces.

%package snmp
Summary:	snmp-plugin for collectd
Summary(pl.UTF-8):	Wtyczka snmp dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description snmp
The snmp plugin queries other hosts using SNMP, the Simple Network
Management Protocol, and translates the value it receives to
collectd's internal format and dispatches them. Depending on the write
plugins you have loaded they may be written to disk or submitted to
another instance or whatever you configured.

%package swap
Summary:	swap-plugin for collectd
Summary(pl.UTF-8):	Wtyczka swap dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description swap
The Swap plugin collects the amount of memory currently written onto
hard disk or whatever the system calls “swap”.

%package syslog
Summary:	syslog-plugin for collectd
Summary(pl.UTF-8):	Wtyczka syslog dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description syslog
The SysLog plugin receives log messages from the daemon and dispatches
them to syslog(3).

%package table
Summary:	table-plugin for collectd
Summary(pl.UTF-8):	Wtyczka table dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description table
The table-plugin provides parsing for table-like structured files,
such as many files beneath /proc.

%package target_notification
Summary:	target_notification-plugin for collectd
Summary(pl.UTF-8):	Wtyczka target_notification dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description target_notification
target_notification plugin for collectd.

%package target_replace
Summary:	target_replace-plugin for collectd
Summary(pl.UTF-8):	Wtyczka target_replace dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description target_replace
target_replace plugin for collectd.

%package target_scale
Summary:	target_scale-plugin for collectd
Summary(pl.UTF-8):	Wtyczka target_scale dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description target_scale
Target to scale (multiply) values by an arbitrary value.

%package target_set
Summary:	target_set-plugin for collectd
Summary(pl.UTF-8):	Wtyczka target_set dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description target_set
target_set plugin for collectd.

%package target_v5upgrade
Summary:	target_v5upgrade-plugin for collectd
Summary(pl.UTF-8):	Wtyczka target_v5upgrade dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description target_v5upgrade
The v5 upgrade target can be used to upgrade version 4 data to a
changed version 5 layout.

%package tail
Summary:	tail-plugin for collectd
Summary(pl.UTF-8):	Wtyczka tail dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description tail
The tail-plugin can be used to "tail" logfiles, i.e. follow them as
tail -F does. Each line is given to one or more "matches" which test
if the line is relevant for any statistics using a regular expression.

%package tcpconns
Summary:	tcpconns-plugin for collectd
Summary(pl.UTF-8):	Wtyczka tcpconns dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description tcpconns
The tcpconns-plugin counts the number of TCP connections to or from a
specified port. Typically the connectioins where you specify the local
port are incoming connections while the connections where you specify
the remote port are outgoing connections.

%package teamspeak2
Summary:	teamspeak2-plugin for collectd
Summary(pl.UTF-8):	Wtyczka teamspeak2 dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description teamspeak2
The teamspeak2 plugin connects to the query port of a teamspeak2
server and polls interesting global and virtual server data. The
plugin can query only one physical server but unlimited virtual
servers.

%package ted
Summary:	ted-plugin for collectd
Summary(pl.UTF-8):	Wtyczka ted dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description ted
The TED-plugin reads power consumption measurements from “The Energy
Detective” (TED).

%package thermal
Summary:	thermal-plugin for collectd
Summary(pl.UTF-8):	Wtyczka thermal dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description thermal
The thermal plugin reads ACPI thermal zone information from the sysfs
or procfs file system, i. e. mostly system temperature information.

%package threshold
Summary:	threshold-plugin for collectd
Summary(pl.UTF-8):	Wtyczka threshold dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description threshold
threshold-plugin for collectd.

%package unixsock
Summary:	unixsock-plugin for collectd
Summary(pl.UTF-8):	Wtyczka unixsock dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description unixsock
The unixsock plugin opens an UNIX-socket over which one can interact
with the daemon. This can be used to use the values collected by
collectd in other applications, such as monitoring, or submit
externally collected values to collectd.

%package uptime
Summary:	uptime-plugin for collectd
Summary(pl.UTF-8):	Wtyczka uptime dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description uptime
The uptime-plugin can collect the server's uptime.

%package users
Summary:	users-plugin for collectd
Summary(pl.UTF-8):	Wtyczka users dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description users
Number of users currently logged in.

%package uuid
Summary:	uuid-plugin for collectd
Summary(pl.UTF-8):	Wtyczka uuid dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description uuid
This plugin, if loaded, causes the Hostname to be taken from the
machine's UUID. The UUID is a universally unique designation for the
machine, usually taken from the machine's BIOS. This is most useful if
the machine is running in a virtual environment such as Xen, in which
case the UUID is preserved across shutdowns and migration.

%package varnish
Summary:	varnish-plugin for collectd
Summary(pl.UTF-8):	Wtyczka varnish dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description varnish
The Varnish plugin collects information about Varnish, an HTTP
accelerator.

%package vmem
Summary:	vmem-plugin for collectd
Summary(pl.UTF-8):	Wtyczka vmem dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description vmem
The vmem plugin collects information about the usage of virtual
memory. Since the statistics provided by the Linux kernel are very
detailed, they are collected very detailed.

%package vserver
Summary:	vserver-plugin for collectd
Summary(pl.UTF-8):	Wtyczka vserver dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description vserver
Collects information about the virtual servers running on a system,
using Linux-Vserver.

%package write_graphite
Summary:	write_graphite-plugin for collectd
Summary(pl.UTF-8):	wtyczka write_graphite dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description write_graphite
The Write Graphite plugin stores values in Carbon, the storage layer
of Graphite. The plugin aims to be very efficient. It keeps the TCP
connection to Carbon open in order to minimize the connection
handshake overhead. It buffers the data in a buffer to send many lines
at once, rather than generating lots of small network packets. The
size of this buffer (1428 bytes) is dimensioned so that the buffer as
well as the TCP and IP header fit into one Ethernet frame and can
(hopefully) be delivered without fragmentation.

%package write_http
Summary:	write_http-plugin for collectd
Summary(pl.UTF-8):	Wtyczka write_http dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description write_http
The Write HTTP plugin sends the values collected by collectd to a
web-server using HTTP POST requests. The data is formatted as PUTVAL
commands.

%package wireless
Summary:	wireless-plugin for collectd
Summary(pl.UTF-8):	Wtyczka wireless dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description wireless
The Wireless plugin collects signal quality, signal power and
signal-to-noise ratio for wireless LAN cards.

%package xmms
Summary:	xmms-plugin for collectd
Summary(pl.UTF-8):	Wtyczka xmms dla collectd
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description xmms
The XMMS plugin is a plugin for the XMMS music player. It graphs the
bit-rate and sampling rate as you play songs. Not really useful, just
something that got written because we can.

%package -n perl-Collectd
Summary:	Perl files from Collectd package
Group:		Daemons

%description -n perl-Collectd
Perl files from Collectd package

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%patch5 -p1
#%patch6 -p1

%build
%{__libtoolize} --ltdl
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}

%configure \
	CPPFLAGS="-Wno-unused-but-set-variable" \
	c_cv_have_libperl=yes \
	--with-libiptc=/usr \
	--with-libstatgrab=/usr \
	--with-lm-sensors=/usr \
	--with-libmysql=/usr \
	--enable-perl \
	%{__enable_disable dns} \
	%{__enable_disable ipmi} \
	%{__enable_disable iptables} \
	%{__with_without java} \
	%{__enable_disable multimeter} \
	%{__enable_disable mysql} \
	%{__enable_disable netlink} \
	%{__enable_disable notify notify_desktop} \
	%{__enable_disable libesmtp notify_email} \
	%{__enable_disable modbus } \
	%{__enable_disable libvirt} \
	%{__enable_disable ups nut} \
	%{__enable_disable ping} \
	%{__enable_disable pgsql postgresql} \
	%{__enable_disable rrd rrdtool} \
	%{__enable_disable sensors} \
	%{__enable_disable snmp} \
	%{__enable_disable xmms} \
	%{__enable_disable varnish} \
	%{__enable_disable curl} \
	%{__enable_disable curl apache} \
	%{__enable_disable curl ngix} \
	%{__enable_disable curl ascent} \
	%{__disable curl ascent} \
	%{__disable curl bind} \
	%{__disable xml ascent} \
	%{__disable xml bind} \
	--disable-ipvs


%{__make} -j1 LDFLAGS="%{rpmldflags} -lstatgrab" \
	BUILD_WITH_OPENIPMI_CFLAGS="-I/usr/include" \
	BUILD_WITH_OPENIPMI_LIBS="-L%{_libdir} -lOpenIPMIutils -lOpenIPMIpthread"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_var}/{log/,lib/%{name}},/etc/{rc.d/init.d/,collectd.d}} \
	$RPM_BUILD_ROOT{%{_appdir}/cgi-bin,%{_webappdir},%{_pkglibdir},%{perl_vendorlib}/,%{_mandir}/man3}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

touch $RPM_BUILD_ROOT%{_var}/log/collectd.log
install %{SOURCE2} $RPM_BUILD_ROOT/etc/rc.d/init.d/%{name}

# Web frontend:
install contrib/collection.conf $RPM_BUILD_ROOT%{_webappdir}
install contrib/collection.cgi $RPM_BUILD_ROOT%{_appdir}/cgi-bin
install %{SOURCE5} $RPM_BUILD_ROOT%{_webappdir}/apache.conf
install %{SOURCE3} $RPM_BUILD_ROOT%{_webappdir}/httpd.conf
install %{SOURCE4} $RPM_BUILD_ROOT%{_webappdir}/lighttpd.conf

cp -R contrib/collection3 $RPM_BUILD_ROOT%{_appdir}
mv $RPM_BUILD_ROOT%{_appdir}/collection3/etc/collection.conf $RPM_BUILD_ROOT%{_webappdir}/collection3.conf
ln -sf %{_webappdir}/collection3.conf $RPM_BUILD_ROOT%{_appdir}/collection3/etc/collection.conf
sed -i -e 's@#DataDir "/var/lib/collectd/rrd"@DataDir "%{_var}/lib/%{name}"@' $RPM_BUILD_ROOT%{_webappdir}/collection3.conf

### Configs instalation ###
for i in `egrep "^(#|)LoadPlugin" src/collectd.conf |awk '{print $NF}' ` ; do
	egrep "LoadPlugin $i$" src/collectd.conf | %{__sed} -e "s/^#//" > $RPM_BUILD_ROOT%{_sysconfdir}/collectd.d/$i.conf
	grep -v LoadPlugin src/collectd.conf |%{__sed} -e '/./{H;$!d;}' -e "x;/ $i>/!d;" >> $RPM_BUILD_ROOT%{_sysconfdir}/collectd.d/$i.conf
done

# Example config in sources: src/collectd.conf
install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/collectd.conf

# Overwrite only files which we want to change:
install %{SOURCE10} $RPM_BUILD_ROOT%{_sysconfdir}/collectd.d/df.conf
install %{SOURCE11} $RPM_BUILD_ROOT%{_sysconfdir}/collectd.d/rrdtool.conf

mv $RPM_BUILD_ROOT%{_datadir}/perl5/Collectd* $RPM_BUILD_ROOT%{perl_vendorlib}/
mv $RPM_BUILD_ROOT/usr/man/man3/Collectd::Unixsock.3pm $RPM_BUILD_ROOT%{_mandir}/man3/

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

%post   libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

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
%module_scripts bind
%module_scripts contextswitch
%module_scripts conntrack
%module_scripts cpu
%module_scripts cpufreq
%module_scripts csv
%module_scripts curl
%module_scripts curl_json
%module_scripts dbi
%module_scripts df
%module_scripts disk
%module_scripts dns
%module_scripts email
%module_scripts entropy
%module_scripts ethstat
%module_scripts exec
%module_scripts filecount
%module_scripts fscache
%module_scripts hddtemp
%module_scripts interface
%module_scripts ipmi
%module_scripts iptables
%module_scripts irq
%module_scripts libvirt
%module_scripts load
%module_scripts logfile
%module_scripts madwifi
%module_scripts match_empty_counter
%module_scripts match_hashed
%module_scripts match_regex
%module_scripts match_timediff
%module_scripts match_value
%module_scripts mbmon
%module_scripts md
%module_scripts memcachec
%module_scripts memcached
%module_scripts memory
%module_scripts multimeter
%module_scripts mysql
%module_scripts netlink
%module_scripts network
%module_scripts nfs
%module_scripts nginx
%module_scripts notify_desktop
%module_scripts notify_email
%module_scripts ntpd
%module_scripts numa
%module_scripts nut
%module_scripts olsrd
%module_scripts openvpn
%module_scripts perl
%module_scripts ping
%module_scripts postgresql
%module_scripts powerdns
%module_scripts processes
%module_scripts protocols
%module_scripts python
%module_scripts rrdcached
%module_scripts rrdtool
%module_scripts sensors
%module_scripts serial
%module_scripts snmp
%module_scripts swap
%module_scripts syslog
%module_scripts table
%module_scripts tail
%module_scripts target_notification
%module_scripts target_replace
%module_scripts target_scale
%module_scripts target_set
%module_scripts target_v5upgrade
%module_scripts tcpconns
%module_scripts teamspeak2
%module_scripts ted
%module_scripts thermal
%module_scripts threshold
%module_scripts unixsock
%module_scripts uptime
%module_scripts users
%module_scripts uuid
%module_scripts varnish
%module_scripts vmem
%module_scripts vserver
%module_scripts write_graphite
%module_scripts write_http
%module_scripts wireless
%module_scripts xmms

%triggerin collection -- apache1 < 1.3.37-3, apache1-base
%webapp_register apache %{_webapp}

%triggerun collection -- apache1 < 1.3.37-3, apache1-base
%webapp_unregister apache %{_webapp}

%triggerin collection -- apache-base
%webapp_register httpd %{_webapp}

%triggerun collection -- apache-base
%webapp_unregister httpd %{_webapp}

%triggerin collection -- lighttpd
%webapp_register lighttpd %{_webapp}

%triggerun collection -- lighttpd
%webapp_unregister lighttpd %{_webapp}

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO contrib
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.conf
%dir %{_sysconfdir}/%{name}.d
%dir %{_webappdir}
%attr(755,root,root) %{_sbindir}/collectd
%attr(755,root,root) %{_sbindir}/collectdmon
%attr(755,root,root) %{_bindir}/collectdctl
%attr(755,root,root) %{_bindir}/collectd-nagios
%dir %{_libdir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/types.db
%attr(754,root,root) /etc/rc.d/init.d/%{name}
%{_mandir}/man1/collectd.1*
%{_mandir}/man1/collectd-nagios.1*
%{_mandir}/man1/collectdctl.1*
%{_mandir}/man1/collectdmon.1*
%{_mandir}/man5/collectd.conf.5*
%{_mandir}/man5/collectd-java.5*
%{_mandir}/man5/types.db.5*
%dir %{_var}/lib/%{name}

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcollectdclient.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcollectdclient.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcollectdclient.so
%{_libdir}/libcollectdclient.la
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h
%{_pkgconfigdir}/libcollectdclient.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libcollectdclient.a
%{_libdir}/%{name}/*.a

%files collection
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_webappdir}/collection.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_webappdir}/apache.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_webappdir}/httpd.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_webappdir}/lighttpd.conf
%dir %{_appdir}
%dir %{_appdir}/cgi-bin
%attr(755,root,root) %{_appdir}/cgi-bin/collection.cgi

%files collection3
%defattr(644,root,root,755)
%doc contrib/collection3/README
%config(noreplace) %verify(not md5 mtime size) %{_webappdir}/collection3.conf
%dir %{_appdir}/collection3
%dir %{_appdir}/collection3/bin
%attr(755,root,root) %{_appdir}/collection3/bin/*.cgi
%{_appdir}/collection3/etc
%{_appdir}/collection3/lib
%{_appdir}/collection3/share

########## PLUGINS:
%if %{with xml}
%if %{with curl}
%files apache
%defattr(640,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/apache.conf
%attr(755,root,root) %{_libdir}/%{name}/apache.so
%endif
%endif

%files apcups
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/apcups.conf
%attr(755,root,root) %{_libdir}/%{name}/apcups.so

%if %{with curl}
%files ascent
%defattr(640,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/ascent.conf
%attr(755,root,root) %{_libdir}/%{name}/ascent.so
%endif

%files battery
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/battery.conf
%attr(755,root,root) %{_libdir}/%{name}/battery.so

%if %{with xml}
%if %{with curl}
%files bind
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/bind.conf
%attr(755,root,root) %{_libdir}/%{name}/bind.so
%endif
%endif

%files contextswitch
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/contextswitch.conf
%attr(755,root,root) %{_libdir}/%{name}/contextswitch.so

%files conntrack
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/conntrack.conf
%attr(755,root,root) %{_libdir}/%{name}/conntrack.so

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

%if %{with curl}
%files curl
%defattr(640,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/curl.conf
%attr(755,root,root) %{_libdir}/%{name}/curl.so
%if %{with xml}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/curl_xml.conf
%attr(755,root,root) %{_libdir}/%{name}/curl_xml.so
%endif

%files curl_json
%defattr(640,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/curl_json.conf
%attr(755,root,root) %{_libdir}/%{name}/curl_json.so
%endif

%files dbi
%defattr(640,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/dbi.conf
%attr(755,root,root) %{_libdir}/%{name}/dbi.so

%files df
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/df.conf
%attr(755,root,root) %{_libdir}/%{name}/df.so

%files disk
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/disk.conf
%attr(755,root,root) %{_libdir}/%{name}/disk.so

%if %{with dns}
%files dns
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/dns.conf
%attr(755,root,root) %{_libdir}/%{name}/dns.so
%endif

%files email
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/email.conf
%attr(755,root,root) %{_libdir}/%{name}/email.so
%{_mandir}/man5/collectd-email.5*

%files entropy
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/entropy.conf
%attr(755,root,root) %{_libdir}/%{name}/entropy.so

%files ethstat
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/ethstat.conf
%attr(755,root,root) %{_libdir}/%{name}/ethstat.so

%files exec
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/exec.conf
%attr(755,root,root) %{_libdir}/%{name}/exec.so
%{_mandir}/man5/collectd-exec.5*

%files filecount
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/filecount.conf
%attr(755,root,root) %{_libdir}/%{name}/filecount.so

%files fscache
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/fscache.conf
%attr(755,root,root) %{_libdir}/%{name}/fscache.so

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

%if %{with libvirt}
%files libvirt
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/virt.conf
%attr(755,root,root) %{_libdir}/%{name}/virt.so
%endif

%files load
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/load.conf
%attr(755,root,root) %{_libdir}/%{name}/load.so

%files logfile
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/logfile.conf
%attr(755,root,root) %{_libdir}/%{name}/logfile.so
%{_var}/log/collectd.log

%files madwifi
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/madwifi.conf
%attr(755,root,root) %{_libdir}/%{name}/madwifi.so

%files match_empty_counter
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/match_empty_counter.conf
%attr(755,root,root) %{_libdir}/%{name}/match_empty_counter.so

%files match_hashed
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/match_hashed.conf
%attr(755,root,root) %{_libdir}/%{name}/match_hashed.so

%files match_regex
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/match_regex.conf
%attr(755,root,root) %{_libdir}/%{name}/match_regex.so

%files match_timediff
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/match_timediff.so
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/match_timediff.conf

%files match_value
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/match_value.conf
%attr(755,root,root) %{_libdir}/%{name}/match_value.so

%files mbmon
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/mbmon.conf
%attr(755,root,root) %{_libdir}/%{name}/mbmon.so

%files md
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/md.conf
%attr(755,root,root) %{_libdir}/%{name}/md.so

%files memcachec
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/memcachec.conf
%attr(755,root,root) %{_libdir}/%{name}/memcachec.so

%files memcached
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/memcached.conf
%attr(755,root,root) %{_libdir}/%{name}/memcached.so

%files memory
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/memory.conf
%attr(755,root,root) %{_libdir}/%{name}/memory.so

%if %{with modbus}
%files modbus
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/modbus.conf
%attr(755,root,root) %{_libdir}/%{name}/modbus.so
%endif

%if %{with multimeter}
%files multimeter
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/multimeter.conf
%attr(755,root,root) %{_libdir}/%{name}/multimeter.so
%endif

%if %{with mysql}
%files mysql
%defattr(640,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/mysql.conf
%attr(755,root,root) %{_libdir}/%{name}/mysql.so
%endif

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

%if %{with curl}
%files nginx
%defattr(640,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/nginx.conf
%attr(755,root,root) %{_libdir}/%{name}/nginx.so
%endif

%if %{with notify}
%files notify_desktop
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/notify_desktop.conf
%attr(755,root,root) %{_libdir}/%{name}/notify_desktop.so
%endif

%if %{with libesmtp}
%files notify_email
%defattr(640,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/notify_email.conf
%attr(755,root,root) %{_libdir}/%{name}/notify_email.so
%endif

%files ntpd
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/ntpd.conf
%attr(755,root,root) %{_libdir}/%{name}/ntpd.so

%files numa
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/numa.conf
%attr(755,root,root) %{_libdir}/%{name}/numa.so

%if %{with ups}
%files nut
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/nut.conf
%attr(755,root,root) %{_libdir}/%{name}/nut.so
%endif

%files olsrd
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/olsrd.conf
%attr(755,root,root) %{_libdir}/%{name}/olsrd.so

%files openvpn
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/openvpn.conf
%attr(755,root,root) %{_libdir}/%{name}/openvpn.so

%files perl
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/perl.conf
%attr(755,root,root) %{_libdir}/%{name}/perl.so
%{_mandir}/man5/collectd-perl.5*

%if %{with ping}
%files ping
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/ping.conf
%attr(755,root,root) %{_libdir}/%{name}/ping.so
%endif

%if %{with pgsql}
%files postgresql
%defattr(640,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/postgresql.conf
%attr(755,root,root) %{_libdir}/%{name}/postgresql.so
%{_datadir}/%{name}/postgresql_default.conf
%endif

%files powerdns
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/powerdns.conf
%attr(755,root,root) %{_libdir}/%{name}/powerdns.so

%files processes
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/processes.conf
%attr(755,root,root) %{_libdir}/%{name}/processes.so

%files protocols
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/protocols.conf
%attr(755,root,root) %{_libdir}/%{name}/protocols.so

%files python
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/python.conf
%attr(755,root,root) %{_libdir}/%{name}/python.so
%{_mandir}/man5/collectd-python.5*

%if %{with rrd}
%files rrdcached
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/rrdcached.conf
%attr(755,root,root) %{_libdir}/%{name}/rrdcached.so

%files rrdtool
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/rrdtool.conf
%attr(755,root,root) %{_libdir}/%{name}/rrdtool.so
%endif

%if %{with sensors}
%files sensors
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/sensors.conf
%attr(755,root,root) %{_libdir}/%{name}/sensors.so
%endif

%files serial
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/serial.conf
%attr(755,root,root) %{_libdir}/%{name}/serial.so

%if %{with snmp}
%files snmp
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/snmp.conf
%attr(755,root,root) %{_libdir}/%{name}/snmp.so
%{_mandir}/man5/collectd-snmp.5*
%endif

%files swap
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/swap.conf
%attr(755,root,root) %{_libdir}/%{name}/swap.so

%files syslog
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/syslog.conf
%attr(755,root,root) %{_libdir}/%{name}/syslog.so

%files table
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/table.conf
%attr(755,root,root) %{_libdir}/%{name}/table.so

%files tail
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/tail.conf
%attr(755,root,root) %{_libdir}/%{name}/tail.so

%files target_notification
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/target_notification.conf
%attr(755,root,root) %{_libdir}/%{name}/target_notification.so

%files target_replace
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/target_replace.conf
%attr(755,root,root) %{_libdir}/%{name}/target_replace.so

%files target_scale
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/target_scale.conf
%attr(755,root,root) %{_libdir}/%{name}/target_scale.so

%files target_set
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/target_set.conf
%attr(755,root,root) %{_libdir}/%{name}/target_set.so

%files target_v5upgrade
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/target_v5upgrade.so

%files tcpconns
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/tcpconns.conf
%attr(755,root,root) %{_libdir}/%{name}/tcpconns.so

%files teamspeak2
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/teamspeak2.conf
%attr(755,root,root) %{_libdir}/%{name}/teamspeak2.so

%files ted
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/ted.conf
%attr(755,root,root) %{_libdir}/%{name}/ted.so

%files thermal
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/thermal.conf
%attr(755,root,root) %{_libdir}/%{name}/thermal.so

%files threshold
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/threshold.conf
%attr(755,root,root) %{_libdir}/%{name}/threshold.so
%{_mandir}/man5/collectd-threshold.5*

%files unixsock
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/unixsock.conf
%attr(755,root,root) %{_libdir}/%{name}/unixsock.so
%{_mandir}/man5/collectd-unixsock.5*

%files uptime
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/uptime.conf
%attr(755,root,root) %{_libdir}/%{name}/uptime.so

%files users
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/users.conf
%attr(755,root,root) %{_libdir}/%{name}/users.so

%files uuid
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/uuid.conf
%attr(755,root,root) %{_libdir}/%{name}/uuid.so

%if %{with varnish}
%files varnish
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/varnish.conf
%attr(755,root,root) %{_libdir}/%{name}/varnish.so
%endif

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

%files write_graphite
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/write_graphite.conf
%attr(755,root,root) %{_libdir}/%{name}/write_graphite.so

%files write_http
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/write_http.conf
%attr(755,root,root) %{_libdir}/%{name}/write_http.so

%if %{with xmms}
%files xmms
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.d/xmms.conf
%attr(755,root,root) %{_libdir}/%{name}/xmms.so
%endif

%files -n perl-Collectd
%defattr(644,root,root,755)
%{perl_vendorlib}/Collectd.pm
%{perl_vendorlib}/Collectd
%{_mandir}/man3/*.3*
