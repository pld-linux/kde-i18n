Summary:	K Desktop Environment - International Support
Summary(pl):	KDE - Wsparcie dla t³umaczeñ miêdzynarodowych
Name:		kde-i18n
Version:	2.2.2
Release:	3
License:	GPL/LGPL
Group:		X11/Applications
Group(cs):	X11/Aplikace
Group(da):	X11/Programmer
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(fr):	X11/Applications
Group(id):	X11/Aplikasi
Group(is):	X11/Forrit
Group(it):	X11/Applicazioni
Group(ja):	X11/¥¢¥×¥ê¥±¡¼¥·¥ç¥ó
Group(no):	X11/Applikasjoner
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplicações
Group(pt):	X11/Aplicações
Group(ru):	X11/ðÒÉÌÏÖÅÎÉÑ
Group(sl):	X11/Programi
Group(sv):	X11/Tillämpningar
Group(uk):	X11/ðÒÉËÌÁÄÎ¦ ðÒÏÇÒÁÍÉ
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.bz2
# this is workaround - I don't know Chinese :)
Source1:	ppdtranslations.gmo
Patch0:		%{name}-ugly.patch
BuildRequires:	libxml2 >= 2.4.2
# It creates symlinks to some not-translated files.
BuildRequires:	kdelibs
BuildRequires:	kdelibs-devel
BuildRequires:	libxml2-progs
BuildRequires:	gettext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
K Desktop Environment - International Support.

%description -l pl
KDE - Wsparcie dla t³umaczeñ miêdzynarodowych.

%package Affrikaans
Summary:	K Desktop Environment - International Support
Group:		X11/Applications
Group(cs):	X11/Aplikace
Group(da):	X11/Programmer
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(fr):	X11/Applications
Group(id):	X11/Aplikasi
Group(is):	X11/Forrit
Group(it):	X11/Applicazioni
Group(ja):	X11/¥¢¥×¥ê¥±¡¼¥·¥ç¥ó
Group(no):	X11/Applikasjoner
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplicações
Group(pt):	X11/Aplicações
Group(ru):	X11/ðÒÉÌÏÖÅÎÉÑ
Group(sl):	X11/Programi
Group(sv):	X11/Tillämpningar
Group(uk):	X11/ðÒÉËÌÁÄÎ¦ ðÒÏÇÒÁÍÉ

%description Affrikaans
K Desktop Environment - International Support.

%package Azerbaijani
Summary:	K Desktop Environment - International Support
Group:		X11/Applications
Group(cs):	X11/Aplikace
Group(da):	X11/Programmer
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(fr):	X11/Applications
Group(id):	X11/Aplikasi
Group(is):	X11/Forrit
Group(it):	X11/Applicazioni
Group(ja):	X11/¥¢¥×¥ê¥±¡¼¥·¥ç¥ó
Group(no):	X11/Applikasjoner
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplicações
Group(pt):	X11/Aplicações
Group(ru):	X11/ðÒÉÌÏÖÅÎÉÑ
Group(sl):	X11/Programi
Group(sv):	X11/Tillämpningar
Group(uk):	X11/ðÒÉËÌÁÄÎ¦ ðÒÏÇÒÁÍÉ

%description Azerbaijani
K Desktop Environment - International Support.

%package Bulgarian
Summary:	K Desktop Environment - International Support
Group:		X11/Applications
Group(cs):	X11/Aplikace
Group(da):	X11/Programmer
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(fr):	X11/Applications
Group(id):	X11/Aplikasi
Group(is):	X11/Forrit
Group(it):	X11/Applicazioni
Group(ja):	X11/¥¢¥×¥ê¥±¡¼¥·¥ç¥ó
Group(no):	X11/Applikasjoner
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplicações
Group(pt):	X11/Aplicações
Group(ru):	X11/ðÒÉÌÏÖÅÎÉÑ
Group(sl):	X11/Programi
Group(sv):	X11/Tillämpningar
Group(uk):	X11/ðÒÉËÌÁÄÎ¦ ðÒÏÇÒÁÍÉ

%description Bulgarian
K Desktop Environment - International Support.

%package Breton
Summary:	K Desktop Environment - International Support
Group:		X11/Applications
Group(cs):	X11/Aplikace
Group(da):	X11/Programmer
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(fr):	X11/Applications
Group(id):	X11/Aplikasi
Group(is):	X11/Forrit
Group(it):	X11/Applicazioni
Group(ja):	X11/¥¢¥×¥ê¥±¡¼¥·¥ç¥ó
Group(no):	X11/Applikasjoner
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplicações
Group(pt):	X11/Aplicações
Group(ru):	X11/ðÒÉÌÏÖÅÎÉÑ
Group(sl):	X11/Programi
Group(sv):	X11/Tillämpningar
Group(uk):	X11/ðÒÉËÌÁÄÎ¦ ðÒÏÇÒÁÍÉ

%description Breton
K Desktop Environment - International Support.

%package Catalan
Summary:	K Desktop Environment - International Support
Group:		X11/Applications
Group(cs):	X11/Aplikace
Group(da):	X11/Programmer
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(fr):	X11/Applications
Group(id):	X11/Aplikasi
Group(is):	X11/Forrit
Group(it):	X11/Applicazioni
Group(ja):	X11/¥¢¥×¥ê¥±¡¼¥·¥ç¥ó
Group(no):	X11/Applikasjoner
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplicações
Group(pt):	X11/Aplicações
Group(ru):	X11/ðÒÉÌÏÖÅÎÉÑ
Group(sl):	X11/Programi
Group(sv):	X11/Tillämpningar
Group(uk):	X11/ðÒÉËÌÁÄÎ¦ ðÒÏÇÒÁÍÉ

%description Catalan
K Desktop Environment - International Support.

%package Czech
Summary:	K Desktop Environment - International Support
Group:		X11/Applications
Group(cs):	X11/Aplikace
Group(da):	X11/Programmer
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(fr):	X11/Applications
Group(id):	X11/Aplikasi
Group(is):	X11/Forrit
Group(it):	X11/Applicazioni
Group(ja):	X11/¥¢¥×¥ê¥±¡¼¥·¥ç¥ó
Group(no):	X11/Applikasjoner
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplicações
Group(pt):	X11/Aplicações
Group(ru):	X11/ðÒÉÌÏÖÅÎÉÑ
Group(sl):	X11/Programi
Group(sv):	X11/Tillämpningar
Group(uk):	X11/ðÒÉËÌÁÄÎ¦ ðÒÏÇÒÁÍÉ

%description Czech
K Desktop Environment - International Support.

%package Cymraeg
Summary:	K Desktop Environment - International Support
Group:		X11/Applications
Group(cs):	X11/Aplikace
Group(da):	X11/Programmer
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(fr):	X11/Applications
Group(id):	X11/Aplikasi
Group(is):	X11/Forrit
Group(it):	X11/Applicazioni
Group(ja):	X11/¥¢¥×¥ê¥±¡¼¥·¥ç¥ó
Group(no):	X11/Applikasjoner
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplicações
Group(pt):	X11/Aplicações
Group(ru):	X11/ðÒÉÌÏÖÅÎÉÑ
Group(sl):	X11/Programi
Group(sv):	X11/Tillämpningar
Group(uk):	X11/ðÒÉËÌÁÄÎ¦ ðÒÏÇÒÁÍÉ

%description Cymraeg
K Desktop Environment - International Support.

%package Danish
Summary:	K Desktop Environment - International Support
Group:		X11/Applications
Group(cs):	X11/Aplikace
Group(da):	X11/Programmer
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(fr):	X11/Applications
Group(id):	X11/Aplikasi
Group(is):	X11/Forrit
Group(it):	X11/Applicazioni
Group(ja):	X11/¥¢¥×¥ê¥±¡¼¥·¥ç¥ó
Group(no):	X11/Applikasjoner
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplicações
Group(pt):	X11/Aplicações
Group(ru):	X11/ðÒÉÌÏÖÅÎÉÑ
Group(sl):	X11/Programi
Group(sv):	X11/Tillämpningar
Group(uk):	X11/ðÒÉËÌÁÄÎ¦ ðÒÏÇÒÁÍÉ

%description Danish
K Desktop Environment - International Support.

%package German
Summary:	K Desktop Environment - International Support
Group:		X11/Applications
Group(cs):	X11/Aplikace
Group(da):	X11/Programmer
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(fr):	X11/Applications
Group(id):	X11/Aplikasi
Group(is):	X11/Forrit
Group(it):	X11/Applicazioni
Group(ja):	X11/¥¢¥×¥ê¥±¡¼¥·¥ç¥ó
Group(no):	X11/Applikasjoner
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplicações
Group(pt):	X11/Aplicações
Group(ru):	X11/ðÒÉÌÏÖÅÎÉÑ
Group(sl):	X11/Programi
Group(sv):	X11/Tillämpningar
Group(uk):	X11/ðÒÉËÌÁÄÎ¦ ðÒÏÇÒÁÍÉ

%description German
K Desktop Environment - International Support.

%package Greek
Summary:	K Desktop Environment - International Support
Group:		X11/Applications
Group(cs):	X11/Aplikace
Group(da):	X11/Programmer
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(fr):	X11/Applications
Group(id):	X11/Aplikasi
Group(is):	X11/Forrit
Group(it):	X11/Applicazioni
Group(ja):	X11/¥¢¥×¥ê¥±¡¼¥·¥ç¥ó
Group(no):	X11/Applikasjoner
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplicações
Group(pt):	X11/Aplicações
Group(ru):	X11/ðÒÉÌÏÖÅÎÉÑ
Group(sl):	X11/Programi
Group(sv):	X11/Tillämpningar
Group(uk):	X11/ðÒÉËÌÁÄÎ¦ ðÒÏÇÒÁÍÉ

%description Greek
K Desktop Environment - International Support.

%package English
Summary:	K Desktop Environment - International Support
Group:		X11/Applications
Group(cs):	X11/Aplikace
Group(da):	X11/Programmer
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(fr):	X11/Applications
Group(id):	X11/Aplikasi
Group(is):	X11/Forrit
Group(it):	X11/Applicazioni
Group(ja):	X11/¥¢¥×¥ê¥±¡¼¥·¥ç¥ó
Group(no):	X11/Applikasjoner
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplicações
Group(pt):	X11/Aplicações
Group(ru):	X11/ðÒÉÌÏÖÅÎÉÑ
Group(sl):	X11/Programi
Group(sv):	X11/Tillämpningar
Group(uk):	X11/ðÒÉËÌÁÄÎ¦ ðÒÏÇÒÁÍÉ

%description English
K Desktop Environment - International Support.

%package English_UK
Summary:	K Desktop Environment - International Support
Group:		X11/Applications
Group(cs):	X11/Aplikace
Group(da):	X11/Programmer
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(fr):	X11/Applications
Group(id):	X11/Aplikasi
Group(is):	X11/Forrit
Group(it):	X11/Applicazioni
Group(ja):	X11/¥¢¥×¥ê¥±¡¼¥·¥ç¥ó
Group(no):	X11/Applikasjoner
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplicações
Group(pt):	X11/Aplicações
Group(ru):	X11/ðÒÉÌÏÖÅÎÉÑ
Group(sl):	X11/Programi
Group(sv):	X11/Tillämpningar
Group(uk):	X11/ðÒÉËÌÁÄÎ¦ ðÒÏÇÒÁÍÉ

%description English_UK
K Desktop Environment - International Support.

%package Esperanto
Summary:	K Desktop Environment - International Support
Group:		X11/Applications
Group(cs):	X11/Aplikace
Group(da):	X11/Programmer
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(fr):	X11/Applications
Group(id):	X11/Aplikasi
Group(is):	X11/Forrit
Group(it):	X11/Applicazioni
Group(ja):	X11/¥¢¥×¥ê¥±¡¼¥·¥ç¥ó
Group(no):	X11/Applikasjoner
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplicações
Group(pt):	X11/Aplicações
Group(ru):	X11/ðÒÉÌÏÖÅÎÉÑ
Group(sl):	X11/Programi
Group(sv):	X11/Tillämpningar
Group(uk):	X11/ðÒÉËÌÁÄÎ¦ ðÒÏÇÒÁÍÉ

%description Esperanto
K Desktop Environment - International Support.

%package Spanish
Summary:	K Desktop Environment - International Support
Group:		X11/Applications
Group(cs):	X11/Aplikace
Group(da):	X11/Programmer
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(fr):	X11/Applications
Group(id):	X11/Aplikasi
Group(is):	X11/Forrit
Group(it):	X11/Applicazioni
Group(ja):	X11/¥¢¥×¥ê¥±¡¼¥·¥ç¥ó
Group(no):	X11/Applikasjoner
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplicações
Group(pt):	X11/Aplicações
Group(ru):	X11/ðÒÉÌÏÖÅÎÉÑ
Group(sl):	X11/Programi
Group(sv):	X11/Tillämpningar
Group(uk):	X11/ðÒÉËÌÁÄÎ¦ ðÒÏÇÒÁÍÉ

%description Spanish
K Desktop Environment - International Support.

%package Estonian
Summary:	K Desktop Environment - International Support
Group:		X11/Applications
Group(cs):	X11/Aplikace
Group(da):	X11/Programmer
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(fr):	X11/Applications
Group(id):	X11/Aplikasi
Group(is):	X11/Forrit
Group(it):	X11/Applicazioni
Group(ja):	X11/¥¢¥×¥ê¥±¡¼¥·¥ç¥ó
Group(no):	X11/Applikasjoner
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplicações
Group(pt):	X11/Aplicações
Group(ru):	X11/ðÒÉÌÏÖÅÎÉÑ
Group(sl):	X11/Programi
Group(sv):	X11/Tillämpningar
Group(uk):	X11/ðÒÉËÌÁÄÎ¦ ðÒÏÇÒÁÍÉ

%description Estonian
K Desktop Environment - International Support.

%package Basque
Summary:	K Desktop Environment - International Support
Group:		X11/Applications
Group(cs):	X11/Aplikace
Group(da):	X11/Programmer
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(fr):	X11/Applications
Group(id):	X11/Aplikasi
Group(is):	X11/Forrit
Group(it):	X11/Applicazioni
Group(ja):	X11/¥¢¥×¥ê¥±¡¼¥·¥ç¥ó
Group(no):	X11/Applikasjoner
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplicações
Group(pt):	X11/Aplicações
Group(ru):	X11/ðÒÉÌÏÖÅÎÉÑ
Group(sl):	X11/Programi
Group(sv):	X11/Tillämpningar
Group(uk):	X11/ðÒÉËÌÁÄÎ¦ ðÒÏÇÒÁÍÉ

%description Basque
K Desktop Environment - International Support.

%package Finnish
Summary:	K Desktop Environment - International Support
Group:		X11/Applications
Group(cs):	X11/Aplikace
Group(da):	X11/Programmer
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(fr):	X11/Applications
Group(id):	X11/Aplikasi
Group(is):	X11/Forrit
Group(it):	X11/Applicazioni
Group(ja):	X11/¥¢¥×¥ê¥±¡¼¥·¥ç¥ó
Group(no):	X11/Applikasjoner
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplicações
Group(pt):	X11/Aplicações
Group(ru):	X11/ðÒÉÌÏÖÅÎÉÑ
Group(sl):	X11/Programi
Group(sv):	X11/Tillämpningar
Group(uk):	X11/ðÒÉËÌÁÄÎ¦ ðÒÏÇÒÁÍÉ

%description Finnish
K Desktop Environment - International Support.

%package French
Summary:	K Desktop Environment - International Support
Group:		X11/Applications
Group(cs):	X11/Aplikace
Group(da):	X11/Programmer
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(fr):	X11/Applications
Group(id):	X11/Aplikasi
Group(is):	X11/Forrit
Group(it):	X11/Applicazioni
Group(ja):	X11/¥¢¥×¥ê¥±¡¼¥·¥ç¥ó
Group(no):	X11/Applikasjoner
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplicações
Group(pt):	X11/Aplicações
Group(ru):	X11/ðÒÉÌÏÖÅÎÉÑ
Group(sl):	X11/Programi
Group(sv):	X11/Tillämpningar
Group(uk):	X11/ðÒÉËÌÁÄÎ¦ ðÒÏÇÒÁÍÉ

%description French
K Desktop Environment - International Support.

%package Irish
Summary:	K Desktop Environment - International Support
Group:		X11/Applications
Group(cs):	X11/Aplikace
Group(da):	X11/Programmer
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(fr):	X11/Applications
Group(id):	X11/Aplikasi
Group(is):	X11/Forrit
Group(it):	X11/Applicazioni
Group(ja):	X11/¥¢¥×¥ê¥±¡¼¥·¥ç¥ó
Group(no):	X11/Applikasjoner
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplicações
Group(pt):	X11/Aplicações
Group(ru):	X11/ðÒÉÌÏÖÅÎÉÑ
Group(sl):	X11/Programi
Group(sv):	X11/Tillämpningar
Group(uk):	X11/ðÒÉËÌÁÄÎ¦ ðÒÏÇÒÁÍÉ

%description Irish
K Desktop Environment - International Support.

%package Galician
Summary:	K Desktop Environment - International Support
Group:		X11/Applications
Group(cs):	X11/Aplikace
Group(da):	X11/Programmer
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(fr):	X11/Applications
Group(id):	X11/Aplikasi
Group(is):	X11/Forrit
Group(it):	X11/Applicazioni
Group(ja):	X11/¥¢¥×¥ê¥±¡¼¥·¥ç¥ó
Group(no):	X11/Applikasjoner
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplicações
Group(pt):	X11/Aplicações
Group(ru):	X11/ðÒÉÌÏÖÅÎÉÑ
Group(sl):	X11/Programi
Group(sv):	X11/Tillämpningar
Group(uk):	X11/ðÒÉËÌÁÄÎ¦ ðÒÏÇÒÁÍÉ

%description Galician
K Desktop Environment - International Support.

%package Hebrew
Summary:	K Desktop Environment - International Support
Group:		X11/Applications
Group(cs):	X11/Aplikace
Group(da):	X11/Programmer
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(fr):	X11/Applications
Group(id):	X11/Aplikasi
Group(is):	X11/Forrit
Group(it):	X11/Applicazioni
Group(ja):	X11/¥¢¥×¥ê¥±¡¼¥·¥ç¥ó
Group(no):	X11/Applikasjoner
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplicações
Group(pt):	X11/Aplicações
Group(ru):	X11/ðÒÉÌÏÖÅÎÉÑ
Group(sl):	X11/Programi
Group(sv):	X11/Tillämpningar
Group(uk):	X11/ðÒÉËÌÁÄÎ¦ ðÒÏÇÒÁÍÉ

%description Hebrew
K Desktop Environment - International Support.

%package Croatian
Summary:	K Desktop Environment - International Support
Group:		X11/Applications
Group(cs):	X11/Aplikace
Group(da):	X11/Programmer
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(fr):	X11/Applications
Group(id):	X11/Aplikasi
Group(is):	X11/Forrit
Group(it):	X11/Applicazioni
Group(ja):	X11/¥¢¥×¥ê¥±¡¼¥·¥ç¥ó
Group(no):	X11/Applikasjoner
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplicações
Group(pt):	X11/Aplicações
Group(ru):	X11/ðÒÉÌÏÖÅÎÉÑ
Group(sl):	X11/Programi
Group(sv):	X11/Tillämpningar
Group(uk):	X11/ðÒÉËÌÁÄÎ¦ ðÒÏÇÒÁÍÉ

%description Croatian
K Desktop Environment - International Support.

%package Hungarian
Summary:	K Desktop Environment - International Support
Group:		X11/Applications
Group(cs):	X11/Aplikace
Group(da):	X11/Programmer
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(fr):	X11/Applications
Group(id):	X11/Aplikasi
Group(is):	X11/Forrit
Group(it):	X11/Applicazioni
Group(ja):	X11/¥¢¥×¥ê¥±¡¼¥·¥ç¥ó
Group(no):	X11/Applikasjoner
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplicações
Group(pt):	X11/Aplicações
Group(ru):	X11/ðÒÉÌÏÖÅÎÉÑ
Group(sl):	X11/Programi
Group(sv):	X11/Tillämpningar
Group(uk):	X11/ðÒÉËÌÁÄÎ¦ ðÒÏÇÒÁÍÉ

%description Hungarian
K Desktop Environment - International Support.

%package Icelandic
Summary:	K Desktop Environment - International Support
Group:		X11/Applications
Group(cs):	X11/Aplikace
Group(da):	X11/Programmer
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(fr):	X11/Applications
Group(id):	X11/Aplikasi
Group(is):	X11/Forrit
Group(it):	X11/Applicazioni
Group(ja):	X11/¥¢¥×¥ê¥±¡¼¥·¥ç¥ó
Group(no):	X11/Applikasjoner
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplicações
Group(pt):	X11/Aplicações
Group(ru):	X11/ðÒÉÌÏÖÅÎÉÑ
Group(sl):	X11/Programi
Group(sv):	X11/Tillämpningar
Group(uk):	X11/ðÒÉËÌÁÄÎ¦ ðÒÏÇÒÁÍÉ

%description Icelandic
K Desktop Environment - International Support.

%package Italian
Summary:	K Desktop Environment - International Support
Group:		X11/Applications
Group(cs):	X11/Aplikace
Group(da):	X11/Programmer
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(fr):	X11/Applications
Group(id):	X11/Aplikasi
Group(is):	X11/Forrit
Group(it):	X11/Applicazioni
Group(ja):	X11/¥¢¥×¥ê¥±¡¼¥·¥ç¥ó
Group(no):	X11/Applikasjoner
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplicações
Group(pt):	X11/Aplicações
Group(ru):	X11/ðÒÉÌÏÖÅÎÉÑ
Group(sl):	X11/Programi
Group(sv):	X11/Tillämpningar
Group(uk):	X11/ðÒÉËÌÁÄÎ¦ ðÒÏÇÒÁÍÉ

%description Italian
K Desktop Environment - International Support.

%package Japanese
Summary:	K Desktop Environment - International Support
Group:		X11/Applications
Group(cs):	X11/Aplikace
Group(da):	X11/Programmer
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(fr):	X11/Applications
Group(id):	X11/Aplikasi
Group(is):	X11/Forrit
Group(it):	X11/Applicazioni
Group(ja):	X11/¥¢¥×¥ê¥±¡¼¥·¥ç¥ó
Group(no):	X11/Applikasjoner
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplicações
Group(pt):	X11/Aplicações
Group(ru):	X11/ðÒÉÌÏÖÅÎÉÑ
Group(sl):	X11/Programi
Group(sv):	X11/Tillämpningar
Group(uk):	X11/ðÒÉËÌÁÄÎ¦ ðÒÏÇÒÁÍÉ

%description Japanese
K Desktop Environment - International Support.

%package Korean
Summary:	K Desktop Environment - International Support
Group:		X11/Applications
Group(cs):	X11/Aplikace
Group(da):	X11/Programmer
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(fr):	X11/Applications
Group(id):	X11/Aplikasi
Group(is):	X11/Forrit
Group(it):	X11/Applicazioni
Group(ja):	X11/¥¢¥×¥ê¥±¡¼¥·¥ç¥ó
Group(no):	X11/Applikasjoner
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplicações
Group(pt):	X11/Aplicações
Group(ru):	X11/ðÒÉÌÏÖÅÎÉÑ
Group(sl):	X11/Programi
Group(sv):	X11/Tillämpningar
Group(uk):	X11/ðÒÉËÌÁÄÎ¦ ðÒÏÇÒÁÍÉ

%description Korean
K Desktop Environment - International Support.

%package Lithuanian
Summary:	K Desktop Environment - International Support
Group:		X11/Applications
Group(cs):	X11/Aplikace
Group(da):	X11/Programmer
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(fr):	X11/Applications
Group(id):	X11/Aplikasi
Group(is):	X11/Forrit
Group(it):	X11/Applicazioni
Group(ja):	X11/¥¢¥×¥ê¥±¡¼¥·¥ç¥ó
Group(no):	X11/Applikasjoner
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplicações
Group(pt):	X11/Aplicações
Group(ru):	X11/ðÒÉÌÏÖÅÎÉÑ
Group(sl):	X11/Programi
Group(sv):	X11/Tillämpningar
Group(uk):	X11/ðÒÉËÌÁÄÎ¦ ðÒÏÇÒÁÍÉ

%description Lithuanian
K Desktop Environment - International Support.

%package Latvian
Summary:	K Desktop Environment - International Support
Group:		X11/Applications
Group(cs):	X11/Aplikace
Group(da):	X11/Programmer
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(fr):	X11/Applications
Group(id):	X11/Aplikasi
Group(is):	X11/Forrit
Group(it):	X11/Applicazioni
Group(ja):	X11/¥¢¥×¥ê¥±¡¼¥·¥ç¥ó
Group(no):	X11/Applikasjoner
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplicações
Group(pt):	X11/Aplicações
Group(ru):	X11/ðÒÉÌÏÖÅÎÉÑ
Group(sl):	X11/Programi
Group(sv):	X11/Tillämpningar
Group(uk):	X11/ðÒÉËÌÁÄÎ¦ ðÒÏÇÒÁÍÉ

%description Latvian
K Desktop Environment - International Support.

%package Maltese
Summary:	K Desktop Environment - International Support
Group:		X11/Applications
Group(cs):	X11/Aplikace
Group(da):	X11/Programmer
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(fr):	X11/Applications
Group(id):	X11/Aplikasi
Group(is):	X11/Forrit
Group(it):	X11/Applicazioni
Group(ja):	X11/¥¢¥×¥ê¥±¡¼¥·¥ç¥ó
Group(no):	X11/Applikasjoner
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplicações
Group(pt):	X11/Aplicações
Group(ru):	X11/ðÒÉÌÏÖÅÎÉÑ
Group(sl):	X11/Programi
Group(sv):	X11/Tillämpningar
Group(uk):	X11/ðÒÉËÌÁÄÎ¦ ðÒÏÇÒÁÍÉ

%description Maltese
K Desktop Environment - International Support.

%package Maori
Summary:	K Desktop Environment - International Support
Group:		X11/Applications
Group(cs):	X11/Aplikace
Group(da):	X11/Programmer
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(fr):	X11/Applications
Group(id):	X11/Aplikasi
Group(is):	X11/Forrit
Group(it):	X11/Applicazioni
Group(ja):	X11/¥¢¥×¥ê¥±¡¼¥·¥ç¥ó
Group(no):	X11/Applikasjoner
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplicações
Group(pt):	X11/Aplicações
Group(ru):	X11/ðÒÉÌÏÖÅÎÉÑ
Group(sl):	X11/Programi
Group(sv):	X11/Tillämpningar
Group(uk):	X11/ðÒÉËÌÁÄÎ¦ ðÒÏÇÒÁÍÉ

%description Maori
K Desktop Environment - International Support.

%package Macedonian
Summary:	K Desktop Environment - International Support
Group:		X11/Applications
Group(cs):	X11/Aplikace
Group(da):	X11/Programmer
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(fr):	X11/Applications
Group(id):	X11/Aplikasi
Group(is):	X11/Forrit
Group(it):	X11/Applicazioni
Group(ja):	X11/¥¢¥×¥ê¥±¡¼¥·¥ç¥ó
Group(no):	X11/Applikasjoner
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplicações
Group(pt):	X11/Aplicações
Group(ru):	X11/ðÒÉÌÏÖÅÎÉÑ
Group(sl):	X11/Programi
Group(sv):	X11/Tillämpningar
Group(uk):	X11/ðÒÉËÌÁÄÎ¦ ðÒÏÇÒÁÍÉ

%description Macedonian
K Desktop Environment - International Support.

%package Dutch
Summary:	K Desktop Environment - International Support
Group:		X11/Applications
Group(cs):	X11/Aplikace
Group(da):	X11/Programmer
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(fr):	X11/Applications
Group(id):	X11/Aplikasi
Group(is):	X11/Forrit
Group(it):	X11/Applicazioni
Group(ja):	X11/¥¢¥×¥ê¥±¡¼¥·¥ç¥ó
Group(no):	X11/Applikasjoner
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplicações
Group(pt):	X11/Aplicações
Group(ru):	X11/ðÒÉÌÏÖÅÎÉÑ
Group(sl):	X11/Programi
Group(sv):	X11/Tillämpningar
Group(uk):	X11/ðÒÉËÌÁÄÎ¦ ðÒÏÇÒÁÍÉ

%description Dutch
K Desktop Environment - International Support.

%package Norwegian_Bokmaal
Summary:	K Desktop Environment - International Support
Group:		X11/Applications
Group(cs):	X11/Aplikace
Group(da):	X11/Programmer
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(fr):	X11/Applications
Group(id):	X11/Aplikasi
Group(is):	X11/Forrit
Group(it):	X11/Applicazioni
Group(ja):	X11/¥¢¥×¥ê¥±¡¼¥·¥ç¥ó
Group(no):	X11/Applikasjoner
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplicações
Group(pt):	X11/Aplicações
Group(ru):	X11/ðÒÉÌÏÖÅÎÉÑ
Group(sl):	X11/Programi
Group(sv):	X11/Tillämpningar
Group(uk):	X11/ðÒÉËÌÁÄÎ¦ ðÒÏÇÒÁÍÉ

%description Norwegian_Bokmaal
K Desktop Environment - International Support.

%package Norwegian_Nynorsk
Summary:	K Desktop Environment - International Support
Group:		X11/Applications
Group(cs):	X11/Aplikace
Group(da):	X11/Programmer
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(fr):	X11/Applications
Group(id):	X11/Aplikasi
Group(is):	X11/Forrit
Group(it):	X11/Applicazioni
Group(ja):	X11/¥¢¥×¥ê¥±¡¼¥·¥ç¥ó
Group(no):	X11/Applikasjoner
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplicações
Group(pt):	X11/Aplicações
Group(ru):	X11/ðÒÉÌÏÖÅÎÉÑ
Group(sl):	X11/Programi
Group(sv):	X11/Tillämpningar
Group(uk):	X11/ðÒÉËÌÁÄÎ¦ ðÒÏÇÒÁÍÉ

%description Norwegian_Nynorsk
K Desktop Environment - International Support.

%package Gascon_occitan
Summary:	K Desktop Environment - International Support
Group:		X11/Applications
Group(cs):	X11/Aplikace
Group(da):	X11/Programmer
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(fr):	X11/Applications
Group(id):	X11/Aplikasi
Group(is):	X11/Forrit
Group(it):	X11/Applicazioni
Group(ja):	X11/¥¢¥×¥ê¥±¡¼¥·¥ç¥ó
Group(no):	X11/Applikasjoner
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplicações
Group(pt):	X11/Aplicações
Group(ru):	X11/ðÒÉÌÏÖÅÎÉÑ
Group(sl):	X11/Programi
Group(sv):	X11/Tillämpningar
Group(uk):	X11/ðÒÉËÌÁÄÎ¦ ðÒÏÇÒÁÍÉ

%description Gascon_occitan
K Desktop Environment - International Support.

%package Polish
Summary:	K Desktop Environment - International Support
Group:		X11/Applications
Group(cs):	X11/Aplikace
Group(da):	X11/Programmer
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(fr):	X11/Applications
Group(id):	X11/Aplikasi
Group(is):	X11/Forrit
Group(it):	X11/Applicazioni
Group(ja):	X11/¥¢¥×¥ê¥±¡¼¥·¥ç¥ó
Group(no):	X11/Applikasjoner
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplicações
Group(pt):	X11/Aplicações
Group(ru):	X11/ðÒÉÌÏÖÅÎÉÑ
Group(sl):	X11/Programi
Group(sv):	X11/Tillämpningar
Group(uk):	X11/ðÒÉËÌÁÄÎ¦ ðÒÏÇÒÁÍÉ

%description Polish
K Desktop Environment - International Support.

%package Portugnese
Summary:	K Desktop Environment - International Support
Group:		X11/Applications
Group(cs):	X11/Aplikace
Group(da):	X11/Programmer
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(fr):	X11/Applications
Group(id):	X11/Aplikasi
Group(is):	X11/Forrit
Group(it):	X11/Applicazioni
Group(ja):	X11/¥¢¥×¥ê¥±¡¼¥·¥ç¥ó
Group(no):	X11/Applikasjoner
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplicações
Group(pt):	X11/Aplicações
Group(ru):	X11/ðÒÉÌÏÖÅÎÉÑ
Group(sl):	X11/Programi
Group(sv):	X11/Tillämpningar
Group(uk):	X11/ðÒÉËÌÁÄÎ¦ ðÒÏÇÒÁÍÉ

%description Portugnese
K Desktop Environment - International Support.

%package Brazil_Portugnese
Summary:	K Desktop Environment - International Support
Group:		X11/Applications
Group(cs):	X11/Aplikace
Group(da):	X11/Programmer
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(fr):	X11/Applications
Group(id):	X11/Aplikasi
Group(is):	X11/Forrit
Group(it):	X11/Applicazioni
Group(ja):	X11/¥¢¥×¥ê¥±¡¼¥·¥ç¥ó
Group(no):	X11/Applikasjoner
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplicações
Group(pt):	X11/Aplicações
Group(ru):	X11/ðÒÉÌÏÖÅÎÉÑ
Group(sl):	X11/Programi
Group(sv):	X11/Tillämpningar
Group(uk):	X11/ðÒÉËÌÁÄÎ¦ ðÒÏÇÒÁÍÉ

%description Brazil_Portugnese
K Desktop Environment - International Support.

%package Romanian
Summary:	K Desktop Environment - International Support
Group:		X11/Applications
Group(cs):	X11/Aplikace
Group(da):	X11/Programmer
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(fr):	X11/Applications
Group(id):	X11/Aplikasi
Group(is):	X11/Forrit
Group(it):	X11/Applicazioni
Group(ja):	X11/¥¢¥×¥ê¥±¡¼¥·¥ç¥ó
Group(no):	X11/Applikasjoner
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplicações
Group(pt):	X11/Aplicações
Group(ru):	X11/ðÒÉÌÏÖÅÎÉÑ
Group(sl):	X11/Programi
Group(sv):	X11/Tillämpningar
Group(uk):	X11/ðÒÉËÌÁÄÎ¦ ðÒÏÇÒÁÍÉ

%description Romanian
K Desktop Environment - International Support.

%package Russian
Summary:	K Desktop Environment - International Support
Group:		X11/Applications
Group(cs):	X11/Aplikace
Group(da):	X11/Programmer
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(fr):	X11/Applications
Group(id):	X11/Aplikasi
Group(is):	X11/Forrit
Group(it):	X11/Applicazioni
Group(ja):	X11/¥¢¥×¥ê¥±¡¼¥·¥ç¥ó
Group(no):	X11/Applikasjoner
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplicações
Group(pt):	X11/Aplicações
Group(ru):	X11/ðÒÉÌÏÖÅÎÉÑ
Group(sl):	X11/Programi
Group(sv):	X11/Tillämpningar
Group(uk):	X11/ðÒÉËÌÁÄÎ¦ ðÒÏÇÒÁÍÉ

%description Russian
K Desktop Environment - International Support.

%package Slovak
Summary:	K Desktop Environment - International Support
Group:		X11/Applications
Group(cs):	X11/Aplikace
Group(da):	X11/Programmer
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(fr):	X11/Applications
Group(id):	X11/Aplikasi
Group(is):	X11/Forrit
Group(it):	X11/Applicazioni
Group(ja):	X11/¥¢¥×¥ê¥±¡¼¥·¥ç¥ó
Group(no):	X11/Applikasjoner
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplicações
Group(pt):	X11/Aplicações
Group(ru):	X11/ðÒÉÌÏÖÅÎÉÑ
Group(sl):	X11/Programi
Group(sv):	X11/Tillämpningar
Group(uk):	X11/ðÒÉËÌÁÄÎ¦ ðÒÏÇÒÁÍÉ

%description Slovak
K Desktop Environment - International Support.

%package Slovenian
Summary:	K Desktop Environment - International Support
Group:		X11/Applications
Group(cs):	X11/Aplikace
Group(da):	X11/Programmer
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(fr):	X11/Applications
Group(id):	X11/Aplikasi
Group(is):	X11/Forrit
Group(it):	X11/Applicazioni
Group(ja):	X11/¥¢¥×¥ê¥±¡¼¥·¥ç¥ó
Group(no):	X11/Applikasjoner
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplicações
Group(pt):	X11/Aplicações
Group(ru):	X11/ðÒÉÌÏÖÅÎÉÑ
Group(sl):	X11/Programi
Group(sv):	X11/Tillämpningar
Group(uk):	X11/ðÒÉËÌÁÄÎ¦ ðÒÏÇÒÁÍÉ

%description Slovenian
K Desktop Environment - International Support.

%package Serbian
Summary:	K Desktop Environment - International Support
Group:		X11/Applications
Group(cs):	X11/Aplikace
Group(da):	X11/Programmer
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(fr):	X11/Applications
Group(id):	X11/Aplikasi
Group(is):	X11/Forrit
Group(it):	X11/Applicazioni
Group(ja):	X11/¥¢¥×¥ê¥±¡¼¥·¥ç¥ó
Group(no):	X11/Applikasjoner
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplicações
Group(pt):	X11/Aplicações
Group(ru):	X11/ðÒÉÌÏÖÅÎÉÑ
Group(sl):	X11/Programi
Group(sv):	X11/Tillämpningar
Group(uk):	X11/ðÒÉËÌÁÄÎ¦ ðÒÏÇÒÁÍÉ

%description Serbian
K Desktop Environment - International Support.

%package Swedish
Summary:	K Desktop Environment - International Support
Group:		X11/Applications
Group(cs):	X11/Aplikace
Group(da):	X11/Programmer
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(fr):	X11/Applications
Group(id):	X11/Aplikasi
Group(is):	X11/Forrit
Group(it):	X11/Applicazioni
Group(ja):	X11/¥¢¥×¥ê¥±¡¼¥·¥ç¥ó
Group(no):	X11/Applikasjoner
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplicações
Group(pt):	X11/Aplicações
Group(ru):	X11/ðÒÉÌÏÖÅÎÉÑ
Group(sl):	X11/Programi
Group(sv):	X11/Tillämpningar
Group(uk):	X11/ðÒÉËÌÁÄÎ¦ ðÒÏÇÒÁÍÉ

%description Swedish
K Desktop Environment - International Support.

%package Tamil
Summary:	K Desktop Environment - International Support
Group:		X11/Applications
Group(cs):	X11/Aplikace
Group(da):	X11/Programmer
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(fr):	X11/Applications
Group(id):	X11/Aplikasi
Group(is):	X11/Forrit
Group(it):	X11/Applicazioni
Group(ja):	X11/¥¢¥×¥ê¥±¡¼¥·¥ç¥ó
Group(no):	X11/Applikasjoner
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplicações
Group(pt):	X11/Aplicações
Group(ru):	X11/ðÒÉÌÏÖÅÎÉÑ
Group(sl):	X11/Programi
Group(sv):	X11/Tillämpningar
Group(uk):	X11/ðÒÉËÌÁÄÎ¦ ðÒÏÇÒÁÍÉ

%description Tamil
K Desktop Environment - International Support.

%package Thai
Summary:	K Desktop Environment - International Support
Group:		X11/Applications
Group(cs):	X11/Aplikace
Group(da):	X11/Programmer
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(fr):	X11/Applications
Group(id):	X11/Aplikasi
Group(is):	X11/Forrit
Group(it):	X11/Applicazioni
Group(ja):	X11/¥¢¥×¥ê¥±¡¼¥·¥ç¥ó
Group(no):	X11/Applikasjoner
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplicações
Group(pt):	X11/Aplicações
Group(ru):	X11/ðÒÉÌÏÖÅÎÉÑ
Group(sl):	X11/Programi
Group(sv):	X11/Tillämpningar
Group(uk):	X11/ðÒÉËÌÁÄÎ¦ ðÒÏÇÒÁÍÉ

%description Thai
K Desktop Environment - International Support.

%package Turkish
Summary:	K Desktop Environment - International Support
Group:		X11/Applications
Group(cs):	X11/Aplikace
Group(da):	X11/Programmer
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(fr):	X11/Applications
Group(id):	X11/Aplikasi
Group(is):	X11/Forrit
Group(it):	X11/Applicazioni
Group(ja):	X11/¥¢¥×¥ê¥±¡¼¥·¥ç¥ó
Group(no):	X11/Applikasjoner
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplicações
Group(pt):	X11/Aplicações
Group(ru):	X11/ðÒÉÌÏÖÅÎÉÑ
Group(sl):	X11/Programi
Group(sv):	X11/Tillämpningar
Group(uk):	X11/ðÒÉËÌÁÄÎ¦ ðÒÏÇÒÁÍÉ

%description Turkish
K Desktop Environment - International Support.

%package Ukrainian
Summary:	K Desktop Environment - International Support
Group:		X11/Applications
Group(cs):	X11/Aplikace
Group(da):	X11/Programmer
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(fr):	X11/Applications
Group(id):	X11/Aplikasi
Group(is):	X11/Forrit
Group(it):	X11/Applicazioni
Group(ja):	X11/¥¢¥×¥ê¥±¡¼¥·¥ç¥ó
Group(no):	X11/Applikasjoner
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplicações
Group(pt):	X11/Aplicações
Group(ru):	X11/ðÒÉÌÏÖÅÎÉÑ
Group(sl):	X11/Programi
Group(sv):	X11/Tillämpningar
Group(uk):	X11/ðÒÉËÌÁÄÎ¦ ðÒÏÇÒÁÍÉ

%description Ukrainian
K Desktop Environment - International Support.

%package Walloon
Summary:	K Desktop Environment - International Support
Group:		X11/Applications
Group(cs):	X11/Aplikace
Group(da):	X11/Programmer
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(fr):	X11/Applications
Group(id):	X11/Aplikasi
Group(is):	X11/Forrit
Group(it):	X11/Applicazioni
Group(ja):	X11/¥¢¥×¥ê¥±¡¼¥·¥ç¥ó
Group(no):	X11/Applikasjoner
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplicações
Group(pt):	X11/Aplicações
Group(ru):	X11/ðÒÉÌÏÖÅÎÉÑ
Group(sl):	X11/Programi
Group(sv):	X11/Tillämpningar
Group(uk):	X11/ðÒÉËÌÁÄÎ¦ ðÒÏÇÒÁÍÉ

%description Walloon
K Desktop Environment - International Support.

%package Xhosa
Summary:	K Desktop Environment - International Support
Group:		X11/Applications
Group(cs):	X11/Aplikace
Group(da):	X11/Programmer
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(fr):	X11/Applications
Group(id):	X11/Aplikasi
Group(is):	X11/Forrit
Group(it):	X11/Applicazioni
Group(ja):	X11/¥¢¥×¥ê¥±¡¼¥·¥ç¥ó
Group(no):	X11/Applikasjoner
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplicações
Group(pt):	X11/Aplicações
Group(ru):	X11/ðÒÉÌÏÖÅÎÉÑ
Group(sl):	X11/Programi
Group(sv):	X11/Tillämpningar
Group(uk):	X11/ðÒÉËÌÁÄÎ¦ ðÒÏÇÒÁÍÉ

%description Xhosa
K Desktop Environment - International Support.

%package Simplified_Chinese
Summary:	K Desktop Environment - International Support
Group:		X11/Applications
Group(cs):	X11/Aplikace
Group(da):	X11/Programmer
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(fr):	X11/Applications
Group(id):	X11/Aplikasi
Group(is):	X11/Forrit
Group(it):	X11/Applicazioni
Group(ja):	X11/¥¢¥×¥ê¥±¡¼¥·¥ç¥ó
Group(no):	X11/Applikasjoner
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplicações
Group(pt):	X11/Aplicações
Group(ru):	X11/ðÒÉÌÏÖÅÎÉÑ
Group(sl):	X11/Programi
Group(sv):	X11/Tillämpningar
Group(uk):	X11/ðÒÉËÌÁÄÎ¦ ðÒÏÇÒÁÍÉ

%description Simplified_Chinese
K Desktop Environment - International Support.

%package Chinese
Summary:	K Desktop Environment - International Support
Group:		X11/Applications
Group(cs):	X11/Aplikace
Group(da):	X11/Programmer
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(fr):	X11/Applications
Group(id):	X11/Aplikasi
Group(is):	X11/Forrit
Group(it):	X11/Applicazioni
Group(ja):	X11/¥¢¥×¥ê¥±¡¼¥·¥ç¥ó
Group(no):	X11/Applikasjoner
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplicações
Group(pt):	X11/Aplicações
Group(ru):	X11/ðÒÉÌÏÖÅÎÉÑ
Group(sl):	X11/Programi
Group(sv):	X11/Tillämpningar
Group(uk):	X11/ðÒÉËÌÁÄÎ¦ ðÒÏÇÒÁÍÉ

%description Chinese
K Desktop Environment - International Support.

%prep
%setup -q
#%patch0 -p1

%build
%define         _sharedir       %{_datadir}
%define         _htmldir        /usr/share/doc/kde/HTML

kde_htmldir="%{_htmldir}"; export kde_htmldir

LDFLAGS="%{rpmldflags}"
#$%{__make} -f Makefile.cvs
cp -f %{SOURCE1} zh_CN.GB2312/messages
%configure2_13
%{__make} RPM_OPT_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
FindLang() {
#    $1 - short language name
#    $2 - long language name

    BUILDDIR=%(pwd)

    echo "%defattr(644,root,root,755)" > "$2.lang"

# share/doc/kde/HTML/(%%lang)
    if [ -d "$RPM_BUILD_ROOT/%{_htmldir}/$1" ]; then
	echo "%lang($1) %{_htmldir}/$1" >> "$2.lang"
    fi

# share/locale/(%%lang)
    if [ -d "$RPM_BUILD_ROOT/%{_datadir}/locale/$1" ]; then
	echo "%lang($1) %{_datadir}/locale/$1" >> "$2.lang"
    fi

# share/apps/amor/tips-(%%lang)
    if [ -f "$RPM_BUILD_ROOT/%{_datadir}/apps/amor/tips-$1" ]; then
	echo "%lang($1) %{_datadir}/apps/amor/tips-$1" >> "$2.lang"
    fi

# share/apps/ktuberling/sounds/(%%lang)
    if [ -d "$RPM_BUILD_ROOT/%{_datadir}/apps/ktuberling/sounds/$1" ]; then
	echo "%lang($1) %{_datadir}/apps/ktuberling/sounds/$1" >> "$2.lang"
    fi
}

rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install

FindLang af Affrikaans
FindLang az Azerbaijani
FindLang bg Bulgarian
FindLang br Breton
FindLang ca Catalan
FindLang cs Czech
FindLang cy Cymraeg
FindLang da Danish
FindLang de German
FindLang el Greek
FindLang en English
FindLang en_GB English_UK
FindLang eo Esperanto
FindLang es Spanish
FindLang et Estonian
FindLang eu Basque
FindLang fi Finnish
FindLang fr French
FindLang ga Irish
FindLang gl Galician
FindLang he Hebrew
FindLang hr Croatian
FindLang hu Hungarian
FindLang is Icelandic
FindLang it Italian
FindLang ja Japanese
FindLang ko Korean
FindLang lt Lithuanian
FindLang lv Latvian
FindLang mi Maori
FindLang mk Macedonian
FindLang mt Maltese
FindLang nl Dutch
FindLang no Norwegian_Bokmaal
# wrong: should be "nn" or "nn_NO" - not "no_NY"
FindLang no_NY Norwegian_Nynorsk
FindLang oc Gascon_occitan
FindLang pl Polish
FindLang pt Portugnese
FindLang pt_BR Brazil_Portugnese
FindLang ro Romanian
FindLang ru Russian
FindLang sk Slovak
FindLang sl Slovenian
FindLang sr Serbian
FindLang sv Swedish
FindLang ta Tamil
FindLang th Thai
FindLang tr Turkish
FindLang uk Ukrainian
FindLang xh Xhosa
FindLang wa Walloon
FindLang zh_CN.GB2312 Simplified_Chinese
FindLang zh_TW.Big5 Chinese

%clean
rm -rf $RPM_BUILD_ROOT

%files -f Affrikaans.lang Affrikaans
%defattr(644,root,root,755)
%files -f Azerbaijani.lang Azerbaijani
%defattr(644,root,root,755)
%files -f Bulgarian.lang Bulgarian
%defattr(644,root,root,755)
%files -f Breton.lang Breton
%defattr(644,root,root,755)
%files -f Catalan.lang Catalan
%defattr(644,root,root,755)
%files -f Czech.lang Czech
%defattr(644,root,root,755)
%files -f Cymraeg.lang Cymraeg
%defattr(644,root,root,755)
%files -f Danish.lang Danish
%defattr(644,root,root,755)
%files -f German.lang German
%defattr(644,root,root,755)
%files -f Greek.lang Greek
%defattr(644,root,root,755)
%files -f English.lang English
%defattr(644,root,root,755)
%files -f English_UK.lang English_UK
%defattr(644,root,root,755)
%files -f Esperanto.lang Esperanto
%defattr(644,root,root,755)
%files -f Spanish.lang Spanish
%defattr(644,root,root,755)
%files -f Estonian.lang Estonian
%defattr(644,root,root,755)
%files -f Basque.lang Basque
%defattr(644,root,root,755)
%files -f Finnish.lang Finnish
%defattr(644,root,root,755)
%files -f French.lang French
%defattr(644,root,root,755)
%files -f Irish.lang Irish
%defattr(644,root,root,755)
%files -f Galician.lang Galician
%defattr(644,root,root,755)
%files -f Hebrew.lang Hebrew
%defattr(644,root,root,755)
%files -f Croatian.lang Croatian
%defattr(644,root,root,755)
%files -f Hungarian.lang Hungarian
%defattr(644,root,root,755)
%files -f Icelandic.lang Icelandic
%defattr(644,root,root,755)
%files -f Italian.lang Italian
%defattr(644,root,root,755)
%files -f Japanese.lang Japanese
%defattr(644,root,root,755)
%files -f Korean.lang Korean
%defattr(644,root,root,755)
%files -f Lithuanian.lang Lithuanian
%defattr(644,root,root,755)
%files -f Latvian.lang Latvian
%defattr(644,root,root,755)
%files -f Maltese.lang Maltese
%defattr(644,root,root,755)
%files -f Maori.lang Maori
%defattr(644,root,root,755)
%files -f Macedonian.lang Macedonian
%defattr(644,root,root,755)
%files -f Dutch.lang Dutch
%defattr(644,root,root,755)
%files -f Norwegian_Bokmaal.lang Norwegian_Bokmaal
%defattr(644,root,root,755)
%files -f Norwegian_Nynorsk.lang Norwegian_Nynorsk
%defattr(644,root,root,755)
%files -f Gascon_occitan.lang Gascon_occitan
%defattr(644,root,root,755)
%files -f Polish.lang Polish
%defattr(644,root,root,755)
%files -f Portugnese.lang Portugnese
%defattr(644,root,root,755)
%files -f Brazil_Portugnese.lang Brazil_Portugnese
%defattr(644,root,root,755)
%files -f Romanian.lang Romanian
%defattr(644,root,root,755)
%files -f Russian.lang Russian
%defattr(644,root,root,755)
%files -f Slovak.lang Slovak
%defattr(644,root,root,755)
%files -f Slovenian.lang Slovenian
%defattr(644,root,root,755)
%files -f Serbian.lang Serbian
%defattr(644,root,root,755)
%files -f Swedish.lang Swedish
%defattr(644,root,root,755)
%files -f Tamil.lang Tamil
%defattr(644,root,root,755)
%files -f Thai.lang Thai
%defattr(644,root,root,755)
%files -f Turkish.lang Turkish
%defattr(644,root,root,755)
%files -f Ukrainian.lang Ukrainian
%defattr(644,root,root,755)
%files -f Walloon.lang Walloon
%defattr(644,root,root,755)
%files -f Xhosa.lang Xhosa
%defattr(644,root,root,755)
%files -f Simplified_Chinese.lang Simplified_Chinese
%defattr(644,root,root,755)
%files -f Chinese.lang Chinese
%defattr(644,root,root,755)
