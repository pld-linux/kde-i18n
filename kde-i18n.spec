%define		REV	20000330
Summary:	K Desktop Environment - International Support
Summary(pl):	KDE - Wsparcie dla t³umaczeñ miêdzynarodowych.
Name:		kde-i18n
Version:	2.0pre_%{_REV}
Release:	1
Copyright:	GPL/LGPL
Group:		X11/KDE
Group(pl):	X11/KDE
Source0:	ftp://ftp.kde.org/pub/kde/snapshots/current/%{name}-%{REV}.tar.bz2
#Patch0:		
#BuildRequires:	
#Requires:	
Buildroot:	/tmp/%{name}-%{version}-root-%(id -u -n)

%define	_prefix	/usr/X11R6

%description

%description -l pl


%prep
%setup -q -n %{name}

#%patch

%build
KDEDIR=%{_prefix};			export KDEDIR
CFLAGS="$RPM_OPT_FLAGS -Wall";		export CFLAGS
CXXFLAGS="$RPM_OPT_FLAGS -Wall";	export CXXFLAGS
LDFLAGS="-s"
%configure --prefix=%{_prefix}
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT%{_prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc
%attr(,,)
