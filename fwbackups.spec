Summary:	Feature-rich user backup program
Name:		fwbackups
Version:	1.43.4
Release:	4
Group:		Archiving/Backup
License:	GPLv2+
URL:		http://www.diffingo.com/oss/fwbackups/
Source0:	http://www.diffingo.com/downloads/fwbackups/%{name}-%{version}%{?pre:%{pre}}.tar.bz2
Source1:	fwbackups-po.tar.gz
Patch0:		fwbackups-desktop.patch
Patch1:		fwbackups-glade.patch
Patch2:		fwbackups-runapp.patch
BuildArch:	noarch
BuildRequires:	imagemagick
BuildRequires:	intltool
BuildRequires:	xsltproc
BuildRequires:	python-devel
Requires:	pygtk2.0
Requires:	pygtk2.0-libglade
Requires:	python-pycrypto
Requires:	python-paramiko
Requires:	python-notify
Requires:	tar
Requires:	rsync

%description
fwbackups is a feature-rich user backup program that allows you to
backup your documents anytime, anywhere.

It offers a simple but powerful interface that permits you to perform
backups with ease, supporting scheduled backups and backing up to
remote computers.

%prep
%setup -q -n %{name}-%{version}%{?pre:%{pre}} -a1
%apply_patches

%build
%configure
%make

%install
%makeinstall_std

# icon theme spec
install -d -m755 %{buildroot}%{_iconsdir}/hicolor/{scalable,48x48,32x32,16x16}/apps
mv %{buildroot}%{_datadir}/pixmaps/%{name}.svg %{buildroot}%{_iconsdir}/hicolor/scalable/apps/
for i in 16x16 32x32 48x48; do
	convert %{buildroot}%{_iconsdir}/hicolor/scalable/apps/%{name}.svg -resize ${i} %{buildroot}%{_iconsdir}/hicolor/${i}/apps/%{name}.png
done

%find_lang %{name} 

%files
%doc AUTHORS ChangeLog README TODO
%{_bindir}/%{name}
%{_bindir}/%{name}-*
%{_datadir}/%{name}
%{_datadir}/applications/fwbackups.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.*
%{python_sitelib}/%{name}
%{_localedir}/*
