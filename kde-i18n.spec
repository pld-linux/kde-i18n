Summary:	K Desktop Environment - International Support
Summary(pl):	KDE - Wsparcie dla tłumaczeń międzynarodowych
Name:		kde-i18n
Version:	3.0
Release:	1
License:	GPL/LGPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/stable/3.0/src/%{name}-%{version}.tar.bz2
BuildRequires:	libxml2 >= 2.4.2
# It creates symlinks to some not-translated files.
BuildRequires:	kdelibs = %{version}
BuildRequires:	kdelibs-devel
BuildRequires:	libxml2-progs
BuildRequires:	gettext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
K Desktop Environment - International Support.

%description -l pl
KDE - Wsparcie dla tłumaczeń międzynarodowych.

%package Affrikaans
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Affrikaans
K Desktop Environment - International Support.

%package Azerbaijani
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Azerbaijani
K Desktop Environment - International Support.

%package Bulgarian
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Bulgarian
K Desktop Environment - International Support.

%package Breton
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Breton
K Desktop Environment - International Support.

%package Catalan
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Catalan
K Desktop Environment - International Support.

%package Czech
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Czech
K Desktop Environment - International Support.

%package Cymraeg
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Cymraeg
K Desktop Environment - International Support.

%package Danish
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Danish
K Desktop Environment - International Support.

%package German
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description German
K Desktop Environment - International Support.

%package Greek
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Greek
K Desktop Environment - International Support.

%package English
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description English
K Desktop Environment - International Support.

%package English_UK
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description English_UK
K Desktop Environment - International Support.

%package Esperanto
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Esperanto
K Desktop Environment - International Support.

%package Spanish
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Spanish
K Desktop Environment - International Support.

%package Estonian
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Estonian
K Desktop Environment - International Support.

%package Basque
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Basque
K Desktop Environment - International Support.

%package Finnish
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Finnish
K Desktop Environment - International Support.

%package French
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description French
K Desktop Environment - International Support.

%package Irish
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Irish
K Desktop Environment - International Support.

%package Galician
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Galician
K Desktop Environment - International Support.

%package Hebrew
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Hebrew
K Desktop Environment - International Support.

%package Croatian
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Croatian
K Desktop Environment - International Support.

%package Hungarian
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Hungarian
K Desktop Environment - International Support.

%package Icelandic
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Icelandic
K Desktop Environment - International Support.

%package Italian
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Italian
K Desktop Environment - International Support.

%package Japanese
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Japanese
K Desktop Environment - International Support.

%package Korean
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Korean
K Desktop Environment - International Support.

%package Lithuanian
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Lithuanian
K Desktop Environment - International Support.

%package Latvian
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Latvian
K Desktop Environment - International Support.

%package Maltese
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Maltese
K Desktop Environment - International Support.

%package Maori
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Maori
K Desktop Environment - International Support.

%package Macedonian
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Macedonian
K Desktop Environment - International Support.

%package Dutch
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Dutch
K Desktop Environment - International Support.

%package Norwegian_Bokmaal
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Norwegian_Bokmaal
K Desktop Environment - International Support.

%package Norwegian_Nynorsk
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Norwegian_Nynorsk
K Desktop Environment - International Support.

%package Gascon_occitan
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Gascon_occitan
K Desktop Environment - International Support.

%package Polish
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Polish
K Desktop Environment - International Support.

%package Portugnese
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Portugnese
K Desktop Environment - International Support.

%package Brazil_Portugnese
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Brazil_Portugnese
K Desktop Environment - International Support.

%package Romanian
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Romanian
K Desktop Environment - International Support.

%package Russian
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Russian
K Desktop Environment - International Support.

%package Slovak
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Slovak
K Desktop Environment - International Support.

%package Slovenian
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Slovenian
K Desktop Environment - International Support.

%package Serbian
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Serbian
K Desktop Environment - International Support.

%package Swedish
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Swedish
K Desktop Environment - International Support.

%package Tamil
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Tamil
K Desktop Environment - International Support.

%package Thai
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Thai
K Desktop Environment - International Support.

%package Turkish
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Turkish
K Desktop Environment - International Support.

%package Ukrainian
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Ukrainian
K Desktop Environment - International Support.

%package Walloon
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Walloon
K Desktop Environment - International Support.

%package Xhosa
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Xhosa
K Desktop Environment - International Support.

%package Simplified_Chinese
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Simplified_Chinese
K Desktop Environment - International Support.

%package Chinese
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Chinese
K Desktop Environment - International Support.

%prep
%setup -q

%build
%define         _sharedir       %{_datadir}
%define         _htmldir        /usr/share/doc/kde/HTML

kde_htmldir="%{_htmldir}"; export kde_htmldir

LDFLAGS="%{rpmldflags}"
#$%{__make} -f Makefile.cvs
%configure
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
%files -f Azerbaijani.lang Azerbaijani
%files -f Bulgarian.lang Bulgarian
%files -f Breton.lang Breton
%files -f Catalan.lang Catalan
%files -f Czech.lang Czech
%files -f Cymraeg.lang Cymraeg
%files -f Danish.lang Danish
%files -f German.lang German
%files -f Greek.lang Greek
%files -f English.lang English
%files -f English_UK.lang English_UK
%files -f Esperanto.lang Esperanto
%files -f Spanish.lang Spanish
%files -f Estonian.lang Estonian
%files -f Basque.lang Basque
%files -f Finnish.lang Finnish
%files -f French.lang French
%files -f Irish.lang Irish
%files -f Galician.lang Galician
%files -f Hebrew.lang Hebrew
%files -f Croatian.lang Croatian
%files -f Hungarian.lang Hungarian
%files -f Icelandic.lang Icelandic
%files -f Italian.lang Italian
%files -f Japanese.lang Japanese
%files -f Korean.lang Korean
%files -f Lithuanian.lang Lithuanian
%files -f Latvian.lang Latvian
%files -f Maltese.lang Maltese
%files -f Maori.lang Maori
%files -f Macedonian.lang Macedonian
%files -f Dutch.lang Dutch
%files -f Norwegian_Bokmaal.lang Norwegian_Bokmaal
%files -f Norwegian_Nynorsk.lang Norwegian_Nynorsk
%files -f Gascon_occitan.lang Gascon_occitan
%files -f Polish.lang Polish
%files -f Portugnese.lang Portugnese
%files -f Brazil_Portugnese.lang Brazil_Portugnese
%files -f Romanian.lang Romanian
%files -f Russian.lang Russian
%files -f Slovak.lang Slovak
%files -f Slovenian.lang Slovenian
%files -f Serbian.lang Serbian
%files -f Swedish.lang Swedish
%files -f Tamil.lang Tamil
%files -f Thai.lang Thai
%files -f Turkish.lang Turkish
%files -f Ukrainian.lang Ukrainian
%files -f Walloon.lang Walloon
%files -f Xhosa.lang Xhosa
%files -f Simplified_Chinese.lang Simplified_Chinese
%files -f Chinese.lang Chinese
