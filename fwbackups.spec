#NOTE: this package is obsolete becaute it requires python2

Summary:	Feature-rich user backup program
Name:		fwbackups
Version:	1.43.7
Release:	1
Group:		Archiving/Backup
License:	GPLv2+
URL:		https://www.diffingo.com/oss/fwbackups/
Source0:	http://www.diffingo.com/downloads/fwbackups/%{name}-%{version}%{?pre:%{pre}}.tar.bz2
Source1:	fwbackups-po.tar.gz
BuildArch:	noarch
BuildRequires:	imagemagick
BuildRequires:	intltool
BuildRequires:	xsltproc
BuildRequires:	desktop-file-utils
BuildRequires:	python2-devel
Requires:	pygtk2.0
Requires:	pygtk2.0-libglade
Requires:	python2-pycrypto
Requires:	python2-paramiko
Requires:	python2-notify
Requires:	tar
Requires:	rsync

%description
fwbackups is a feature-rich user backup program that allows you to
backup your documents anytime, anywhere.

It offers a simple but powerful interface that permits you to perform
backups with ease, supporting scheduled backups and backing up to
remote computers.

%prep
%autosetup -p1 -n %{name}-%{version}%{?pre:%{pre}} -a1
sed -i 's/\bpython\b/python2/' bin/*

%build
export PYTHON=python2
%configure
%make_build

%install
%make_install

desktop-file-edit --add-category=Archiving --add-category=Utility %{buildroot}%{_datadir}/applications/fwbackups.desktop

%find_lang %{name} 

%files
%doc AUTHORS ChangeLog README TODO
%{_bindir}/%{name}
%{_bindir}/%{name}-*
%{_datadir}/%{name}
%{_datadir}/applications/fwbackups.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.*
%{python2_sitelib}/%{name}
%{_localedir}/*
