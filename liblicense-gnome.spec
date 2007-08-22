Name: liblicense-gnome
Version: 0.4
Release: 1
License: LGPL
Summary: liblicense Gnome Integration
Group: Development/Libraries
Source: liblicense-gnome-%{version}.tar.bz2
BuildRequires: nautilus-python >= 0.4.3
BuildRequires: gnome-common
BuildRequires: pygtk2-devel
BuildRequires: nautilus-python-devel >= 0.4.3
Requires: pygtk2
Requires: liblicense >= 0.4
Requires: nautilus-python >= 0.4.3
Url: http://www.creativecommons.org/project/Liblicense

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
The liblicense-gnome package contains the GTK and Gnome tools for liblicense.

%prep
%setup -n liblicense-gnome-0.4
./configure --prefix=/usr

%build
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYING
/usr/bin
/usr/lib
/usr/share

%changelog
* Wed Aug 22 2007 Scott Shawcroft <scott.shawcroft@gmail.com> - 0.4-1
- initial liblicense-gnome rpm
