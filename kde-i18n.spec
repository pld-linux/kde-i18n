Summary:	K Desktop Environment - international support
Summary(pl):	KDE - wsparcie dla t³umaczeñ miêdzynarodowych
Name:		kde-i18n
Version:	2.2.2
Release:	9
License:	GPL/LGPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.bz2
# this is workaround - I don't know Chinese :)
Source1:	ppdtranslations.gmo
Patch0:		%{name}-ugly.patch
Patch1:		%{name}-nodoc.patch
Patch2:		%{name}-pl_lang_names.patch
Patch3:		%{name}-nn.patch
Patch4:		%{name}-zh.patch
BuildRequires:	libxml2 >= 2.4.2
# It creates symlinks to some not-translated files.
BuildRequires:	kdelibs = %{version}
BuildRequires:	kdelibs-devel
BuildRequires:	libxml2-progs
BuildRequires:	gettext-devel
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
K Desktop Environment - international support.

%description -l pl
KDE - wsparcie dla t³umaczeñ miêdzynarodowych.


%package Affrikaans
Summary:	K Desktop Environment - Affrikaans language support
Summary(pl):	KDE - wsparcie dla jêzyka afrykanerskiego
Group:		X11/Applications

%description Affrikaans
K Desktop Environment - Affrikaans language support.

%description Affrikaans -l pl
KDE - wsparcie dla jêzyka afrykanerskiego.


%package Azerbaijani
Summary:	K Desktop Environment - Azerbaijani language support
Summary(pl):	KDE - wsparcie dla jêzyka azerskiego
Group:		X11/Applications

%description Azerbaijani
K Desktop Environment - Azerbaijani language support.

%description Azerbaijani -l pl
KDE - wsparcie dla jêzyka azerskiego.


%package Bulgarian
Summary:	K Desktop Environment - Bulgarian language support
Summary(pl):	KDE - wsparcie dla jêzyka bu³garskiego
Group:		X11/Applications

%description Bulgarian
K Desktop Environment - Bulgarian language support.

%description Bulgarian -l pl
KDE - wsparcie dla jêzyka bu³garskiego.


#%package Breton
#Summary:	K Desktop Environment - International Support
#Group:		X11/Applications
#
#%description Breton
#K Desktop Environment - International Support.
#
#%package Catalan
#Summary:	K Desktop Environment - International Support
#Group:		X11/Applications
#
#%description Catalan
#K Desktop Environment - International Support.


%package Czech
Summary:	K Desktop Environment - Czech language support
Summary(pl):	KDE - wsparcie dla jêzyka czeskiego
Group:		X11/Applications

%description Czech
K Desktop Environment - Czech language support.

%description Czech -l pl
KDE - wsparcie dla jêzyka czeskiego.


#%package Cymraeg
#Summary:	K Desktop Environment - International Support
#Group:		X11/Applications
#
#%description Cymraeg
#K Desktop Environment - International Support.


%package Danish
Summary:	K Desktop Environment - Danish language support
Summary(pl):	KDE - wsparcie dla jêzyka duñskiego
Group:		X11/Applications

%description Danish
K Desktop Environment - Danish language support.

%description Danish -l pl
KDE - wsparcie dla jêzyka duñskiego.


%package German
Summary:	K Desktop Environment - German language support
Summary(pl):	KDE - wsparcie dla jêzyka niemieckiego
Group:		X11/Applications

%description German
K Desktop Environment - German language support.

%description German -l pl
KDE - wsparcie dla jêzyka niemieckiego.


%package Greek
Summary:	K Desktop Environment - Greek language support
Summary(pl):	KDE - wsparcie dla jêzyka greckiego
Group:		X11/Applications

%description Greek
K Desktop Environment - Greek language support.

%description Greek -l pl
KDE - wsparcie dla jêzyka greckiego.


#%package English
#Summary:	K Desktop Environment - International Support
#Group:		X11/Applications
#
#%description English
#K Desktop Environment - International Support.


%package English_UK
Summary:	K Desktop Environment - English (UK) language support
Summary(pl):	KDE - wsparcie dla jêzyka angielskiego (odmiany brytyjskiej)
Group:		X11/Applications

%description English_UK
K Desktop Environment - English (UK) language support.

%description English_UK -l pl
KDE - wsparcie dla jêzyka angielskiego (odmiany brytyjskiej).


%package Esperanto
Summary:	K Desktop Environment - Esperanto language support
Summary(pl):	KDE - wsparcie dla jêzyka esperanto
Group:		X11/Applications

%description Esperanto
K Desktop Environment - Esperanto language support.

%description Esperanto -l pl
KDE - wsparcie dla jêzyka esperanto.


%package Spanish
Summary:	K Desktop Environment - Spanish language support
Summary(pl):	KDE - wsparcie dla jêzyka hiszpañskiego
Group:		X11/Applications

%description Spanish
K Desktop Environment - Spanish language support.

%description Spanish -l pl
KDE - wsparcie dla jêzyka hiszpañskiego.


%package Estonian
Summary:	K Desktop Environment - Estonian language support
Summary(pl):	KDE - wsparcie dla jêzyka estoñskiego
Group:		X11/Applications

%description Estonian
K Desktop Environment - Estonian language support.

%description Estonian -l pl
KDE - wsparcie dla jêzyka estoñskiego.


#%package Basque
#Summary:	K Desktop Environment - International Support
#Group:		X11/Applications
#
#%description Basque
#K Desktop Environment - International Support.


%package Finnish
Summary:	K Desktop Environment - Finnish language support
Summary(pl):	KDE - wsparcie dla jêzyka fiñskiego
Group:		X11/Applications

%description Finnish
K Desktop Environment - Finnish language support.

%description Finnish -l pl
KDE - wsparcie dla jêzyka fiñskiego.


%package French
Summary:	K Desktop Environment - French language support
Summary(pl):	KDE - wsparcie dla jêzyka francuskiego
Group:		X11/Applications

%description French
K Desktop Environment - French language support.

%description French -l pl
KDE - wsparcie dla jêzyka francuskiego.


#%package Irish
#Summary:	K Desktop Environment - International Support
#Group:		X11/Applications
#
#%description Irish
#K Desktop Environment - International Support.
#
#%package Galician
#Summary:	K Desktop Environment - International Support
#Group:		X11/Applications
#
#%description Galician
#K Desktop Environment - International Support.


%package Hebrew
Summary:	K Desktop Environment - Hebrew language support
Summary(pl):	KDE - wsparcie dla jêzyka hebrajskiego
Group:		X11/Applications

%description Hebrew
K Desktop Environment - Hebrew language support.

%description Hebrew -l pl
KDE - wsparcie dla jêzyka hebrajskiego.


#%package Croatian
#Summary:	K Desktop Environment - International Support
#Group:		X11/Applications
#
#%description Croatian
#K Desktop Environment - International Support.


%package Hungarian
Summary:	K Desktop Environment - Hungarian language support
Summary(pl):	KDE - wsparcie dla jêzyka wêgierskiego
Group:		X11/Applications

%description Hungarian
K Desktop Environment - Hungarian language support.

%description Hungarian -l pl
KDE - wsparcie dla jêzyka wêgierskiego.


%package Icelandic
Summary:	K Desktop Environment - Icelandic language support
Summary(pl):	KDE - wsparcie dla jêzyka islandzkiego
Group:		X11/Applications

%description Icelandic
K Desktop Environment - Icelandic language support.

%description Icelandic -l pl
KDE - wsparcie dla jêzyka islandzkiego.


%package Italian
Summary:	K Desktop Environment - Italian language support
Summary(pl):	KDE - wsparcie dla jêzyka w³oskiego
Group:		X11/Applications

%description Italian
K Desktop Environment - Italian language support.

%description Italian -l pl
KDE - wsparcie dla jêzyka w³oskiego.


%package Japanese
Summary:	K Desktop Environment - Japanese language support
Summary(pl):	KDE - wsparcie dla jêzyka japoñskiego
Group:		X11/Applications

%description Japanese
K Desktop Environment - Japanese language support.

%description Japanese -l pl
KDE - wsparcie dla jêzyka japoñskiego.


%package Korean
Summary:	K Desktop Environment - Korean language support
Summary(pl):    KDE - wsparcie dla jêzyka koreañskiego
Group:		X11/Applications

%description Korean
K Desktop Environment - Korean language support.

%description Korean -l pl
KDE - wsparcie dla jêzyka koreañskiego.


%package Lithuanian
Summary:	K Desktop Environment - Lithuanian language support
Summary(pl):	KDE - wsparcie dla jêzyka litewskiego
Group:		X11/Applications

%description Lithuanian
K Desktop Environment - Lithuanian language support.

%description Lithuanian -l pl
KDE - Wsparcie dla jêzyka litewskiego.


%package Latvian
Summary:	K Desktop Environment - Latvian language support
Summary(pl):	KDE - wsparcie dla jêzyka ³otewskiego
Group:		X11/Applications

%description Latvian
K Desktop Environment - Latvian language support.

%description Latvian -l pl
KDE - wsparcie dla jêzyka ³otewskiego.


%package Maltese
Summary:	K Desktop Environment - Maltese language support
Summary(pl):	KDE - wsparcie dla jêzyka maltañskiego
Group:		X11/Applications

%description Maltese
K Desktop Environment - Maltese language support.

%description Maltese -l pl
KDE - wsparcie dla jêzyka maltañskiego.


#%package Maori
#Summary:	K Desktop Environment - International Support
#Group:		X11/Applications
#
#%description Maori
#K Desktop Environment - International Support.
#
#%package Macedonian
#Summary:	K Desktop Environment - International Support
#Group:		X11/Applications
#
#%description Macedonian
#K Desktop Environment - International Support.


%package Dutch
Summary:	K Desktop Environment - Dutch language support
Summary(pl):	KDE - wsparcie dla jêzyka holenderskiego
Group:		X11/Applications

%description Dutch
K Desktop Environment - Dutch language support.

%description Dutch -l pl
KDE - wsparcie dla jêzyka holenderskiego.


%package Norwegian_Bokmaal
Summary:	K Desktop Environment - Norwegian (Bokmaal) language support
Summary(pl):	KDE - wsparcie dla jêzyka norweskiego (odmiany bokmaal)
Provides:	%{name}-Norwegian
Group:		X11/Applications

%description Norwegian_Bokmaal
K Desktop Environment - Norwegian (Bokmaal) language support.

%description Norwegian_Bokmaal -l pl
KDE - wsparcie dla jêzyka norweskiego (odmiany bokmaal).


%package Norwegian_Nynorsk
Summary:	K Desktop Environment - Norwegian (Nynorsk) language support
Summary(pl):    KDE - wsparcie dla jêzyka norweskiego (odmiany nunorsk)
Group:		X11/Applications

%description Norwegian_Nynorsk
K Desktop Environment - Norwegian (Nynorsk) language support.

%description Norwegian_Nynorsk -l pl
KDE - wsparcie dla jêzyka norweskiego (odmiany nunorsk).


#%package Gascon_occitan
#Summary:	K Desktop Environment - International Support
#Group:		X11/Applications
#
#%description Gascon_occitan
#K Desktop Environment - International Support.


%package Polish
Summary:	K Desktop Environment - Polish language support
Summary(pl):	KDE - wsparcie dla jêzyka polskiego
Group:		X11/Applications

%description Polish
K Desktop Environment - Polish language support.

%description Polish -l pl
KDE - wsparcie dla jêzyka polskiego.


%package Portugnese
Summary:	K Desktop Environment - Portugnese language support
Summary(pl):	KDE - wsparcie dla jêzyka portugalskiego
Group:		X11/Applications

%description Portugnese
K Desktop Environment - Portugnese language support.

%description Portugnese -l pl
KDE - wsparcie dla jêzyka portugalskiego.


%package Brazil_Portugnese
Summary:	K Desktop Environment - Portugnese (Brazil) language support
Summary(pl):	KDE - wsparcie dla jêzyka portugalskiego (odmiany brazylijskiej)
Group:		X11/Applications

%description Brazil_Portugnese
K Desktop Environment - Portugnese (Brazil) language support.

%description Brazil_Portugnese -l pl
KDE - wsparcie dla jêzyka portugalskiego (odmiany brazylijskiej).


%package Romanian
Summary:	K Desktop Environment - Romanian language support
Summary(pl):	KDE - wsparcie dla jêzyka rumuñskiego
Group:		X11/Applications

%description Romanian
K Desktop Environment - Romanian language support.

%description Romanian -l pl
KDE - wsparcie dla jêzyka rumuñskiego.


%package Russian
Summary:	K Desktop Environment - Russian language support
Summary(pl):	KDE - wsparcie dla jêzyka rosyjskiego
Group:		X11/Applications

%description Russian
K Desktop Environment - Russian language support.

%description Russian -l pl
KDE - wsparcie dla jêzyka rosyjskiego.


%package Slovak
Summary:	K Desktop Environment - Slovak language support
Summary(pl):	KDE - wsparcie dla jêzyka s³owackiego
Group:		X11/Applications

%description Slovak
K Desktop Environment - Slovak language support.

%description Slovak -l pl
KDE - wsparcie dla jêzyka s³owackiego.


%package Slovenian
Summary:	K Desktop Environment - Slovenian language support
Summary(pl):	KDE - wsparcie dla jêzyka s³oweñskiego
Group:		X11/Applications

%description Slovenian
K Desktop Environment - Slovenian language support.

%description Slovenian -l pl
KDE - wsparcie dla jêzyka s³oweñskiego.


%package Serbian
Summary:	K Desktop Environment - Serbian language support
Summary(pl):	KDE - wsparcie dla jêzyka serbskiego
Group:		X11/Applications

%description Serbian
K Desktop Environment - Serbian language support.

%description Serbian -l pl
KDE - wsparcie dla jêzyka serbskiego.


%package Swedish
Summary:	K Desktop Environment - Swedish language support
Summary(pl):	KDE - wsparcie dla jêzyka szwedzkiego
Group:		X11/Applications

%description Swedish
K Desktop Environment - Swedish language support.

%description Swedish -l pl
KDE - wsparcie dla jêzyka szwedzkiego.


%package Tamil
Summary:	K Desktop Environment - Tamil language support
Summary(pl):	KDE - wsparcie dla jêzyka tamilskiego
Group:		X11/Applications

%description Tamil
K Desktop Environment - Tamil language support.

%description Tamil -l pl
KDE - wsparcie dla jêzyka tamilskiego.


%package Thai
Summary:	K Desktop Environment - Thai language support
Summary(pl):	KDE - wsparcie dla jêzyka tajnandzkiego
Group:		X11/Applications

%description Thai
K Desktop Environment - Thai language support.

%description Thai -l pl
KDE - wsparcie dla jêzyka tajnandzkiego.


%package Turkish
Summary:	K Desktop Environment - Turkish language support
Summary(pl):	KDE - wsparcie dla jêzyka tureckiego
Group:		X11/Applications

%description Turkish
K Desktop Environment - Turkish language support.

%description Turkish -l pl
KDE - wsparcie dla jêzyka tureckiego.


%package Ukrainian
Summary:	K Desktop Environment - Ukrainian language support
Summary(pl):	KDE - wsparcie dla jêzyka ukraiñskiego
Group:		X11/Applications

%description Ukrainian
K Desktop Environment - Ukrainian language support.

%description Ukrainian -l pl
KDE - wsparcie dla jêzyka ukraiñskiego.


#%package Walloon
#Summary:	K Desktop Environment - International Support
#Group:		X11/Applications
#
#%description Walloon
#K Desktop Environment - International Support.


%package Xhosa
Summary:	K Desktop Environment - Xhosa language support
Summary(pl):	KDE - wsparcie dla jêzyka xhosa
Group:		X11/Applications

%description Xhosa
K Desktop Environment - Xhosa language support.

%description Xhosa -l pl
KDE - wsparcie dla jêzyka xhosa.


%package Simplified_Chinese
Summary:	K Desktop Environment - simplified Chinese language support
Summary(pl):	KDE - wsparcie dla uproszczonego jêzyka chiñskiego
Group:		X11/Applications

%description Simplified_Chinese
K Desktop Environment - simplified Chinese language support.

%description Simplified_Chinese -l pl
KDE - wsparcie dla uproszczonego jêzyka chiñskiego.


%package Chinese
Summary:	K Desktop Environment - X language support
Summary(pl):	KDE - wsparcie dla jêzyka chiñskiego
Group:		X11/Applications

%description Chinese
K Desktop Environment - Chinese language support.

%description Chinese -l pl
KDE - wsparcie dla jêzyka chiñskiego.

%prep
%setup -q
#%patch0 -p1
%patch1 -p1
%patch2 -p1
mv -f no_NY nn
%patch3 -p1
mv -f zh_CN.GB2312 zh_CN
mv -f zh_TW.Big5   zh_TW
%patch4 -p1 

%build
%define         _sharedir       %{_datadir}
%define         _htmldir        /usr/share/doc/kde/HTML

kde_htmldir="%{_htmldir}"; export kde_htmldir

LDFLAGS="%{rpmldflags}"
#$%{__make} -f Makefile.cvs
cp -f %{SOURCE1} zh_CN/messages
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
	echo "%lang($1) %{_datadir}/locale/$1/[^L]*" >> "$2.lang"
    fi
    if [ -d "$RPM_BUILD_ROOT/%{_datadir}/locale/$1/LC_MESSAGES" ]; then
	echo "%lang($1) %{_datadir}/locale/$1/LC_MESSAGES/*" >> "$2.lang"
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

# These are included in ktouch
rm -f $RPM_BUILD_ROOT%{_datadir}/locale/{de,fr,no}/LC_MESSAGES/ktouch.po

FindLang af Affrikaans
FindLang az Azerbaijani
FindLang bg Bulgarian
# FindLang br Breton
# FindLang ca Catalan
FindLang cs Czech
# FindLang cy Cymraeg
FindLang da Danish
FindLang de German
FindLang el Greek
# FindLang en English
FindLang en_GB English_UK
FindLang eo Esperanto
FindLang es Spanish
FindLang et Estonian
# FindLang eu Basque
FindLang fi Finnish
FindLang fr French
# FindLang ga Irish
# FindLang gl Galician
FindLang he Hebrew
# FindLang hr Croatian
FindLang hu Hungarian
FindLang is Icelandic
FindLang it Italian
FindLang ja Japanese
FindLang ko Korean
FindLang lt Lithuanian
FindLang lv Latvian
# FindLang mi Maori
# FindLang mk Macedonian
FindLang mt Maltese
FindLang nl Dutch
FindLang no Norwegian_Bokmaal
FindLang nn Norwegian_Nynorsk
# FindLang oc Gascon_occitan
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
# FindLang wa Walloon
FindLang zh_CN Simplified_Chinese
FindLang zh_TW Chinese

%clean
rm -rf $RPM_BUILD_ROOT

%files -f Affrikaans.lang Affrikaans
%files -f Azerbaijani.lang Azerbaijani
%files -f Bulgarian.lang Bulgarian
# %files -f Breton.lang Breton
# %files -f Catalan.lang Catalan
%files -f Czech.lang Czech
# %files -f Cymraeg.lang Cymraeg
%files -f Danish.lang Danish
%files -f German.lang German
%files -f Greek.lang Greek
# %files -f English.lang English
%files -f English_UK.lang English_UK
%files -f Esperanto.lang Esperanto
%files -f Spanish.lang Spanish
%files -f Estonian.lang Estonian
# %files -f Basque.lang Basque
%files -f Finnish.lang Finnish
%files -f French.lang French
# %files -f Irish.lang Irish
# %files -f Galician.lang Galician
%files -f Hebrew.lang Hebrew
# %files -f Croatian.lang Croatian
%files -f Hungarian.lang Hungarian
%files -f Icelandic.lang Icelandic
%files -f Italian.lang Italian
%files -f Japanese.lang Japanese
%files -f Korean.lang Korean
%files -f Lithuanian.lang Lithuanian
%files -f Latvian.lang Latvian
%files -f Maltese.lang Maltese
# %files -f Maori.lang Maori
# %files -f Macedonian.lang Macedonian
%files -f Dutch.lang Dutch
%files -f Norwegian_Bokmaal.lang Norwegian_Bokmaal
%files -f Norwegian_Nynorsk.lang Norwegian_Nynorsk
# %files -f Gascon_occitan.lang Gascon_occitan
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
# %files -f Walloon.lang Walloon
%files -f Xhosa.lang Xhosa
%files -f Simplified_Chinese.lang Simplified_Chinese
%files -f Chinese.lang Chinese
