# Conditional build:
# --with	alltogether		Build single package containing
#					support for all languages
#
# --with	tarball_creation	Create tarballs with resources for
#					specific packages
#
# --with	kdelibs			Create single small package containing
#					essential files only

Summary:	K Desktop Environment - international support
Summary(pl):	KDE - Wsparcie dla t³umaczeñ miêdzynarodowych
Name:		kde-i18n
Version:	3.0.3
Release:	0.1
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
Source1:	%{name}-splitmo
Source2:	%{name}-splitdoc
Patch0:		%{name}-nodoc.patch
%if %{?_with_alltogether:1}%{!?_with_alltogether:0}
Obsoletes:	kde-i18n-Affrikaans kde-i18n-Arabic kde-i18n-Azerbaijani
Obsoletes:	kde-i18n-Bulgarian kde-i18n-Bosnian kde-i18n-Catalan
Obsoletes:	kde-i18n-Czech kde-i18n-Danish kde-i18n-German kde-i18n-Greek
Obsoletes:	kde-i18n-English_UK kde-i18n-Esperanto kde-i18n-Spanish
Obsoletes:	kde-i18n-Estonian kde-i18n-Finnish kde-i18n-French
Obsoletes:	kde-i18n-Hebrew kde-i18n-Croatian kde-i18n-Hungarian
Obsoletes:	kde-i18n-Indonesian kde-i18n-Icelandic kde-i18n-Italian
Obsoletes:	kde-i18n-Japanese kde-i18n-Korean kde-i18n-Lithuanian
Obsoletes:	kde-i18n-Latvian kde-i18n-Maltese kde-i18n-Dutch
Obsoletes:	kde-i18n-Norwegian kde-i18n-Norwegian_Bokmaal
Obsoletes:	kde-i18n-Norwegian_Nynorsk kde-i18n-Polish kde-i18n-Portugnese
Obsoletes:	kde-i18n-Brazil_Portugnese kde-i18n-Romanian kde-i18n-Russian
Obsoletes:	kde-i18n-Slovak kde-i18n-Slovenian kde-i18n-Serbian
Obsoletes:	kde-i18n-Swedish kde-i18n-Tamil kde-i18n-Thai kde-i18n-Turkish
Obsoletes:	kde-i18n-Ukrainian kde-i18n-Venda kde-i18n-Vietnamese
Obsoletes:	kde-i18n-Xhosa kde-i18n-Simplified_Chinese kde-i18n-Chinese
Obsoletes:	kde-i18n-Zulu
%endif
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



%if %{?_with_kdelibs:1}%{!?_with_kdelibs:0}
%package kdelibs
Summary:	K Desktop Environment - International Support
Summary(pl):	KDE - Wsparcie dla t³umaczeñ miêdzynarodowych
Group:		X11/Applications

%description kdelibs
K Desktop Environment - international support. This package
contains essential files only.

%description -l pl kdelibs
KDE - Wsparcie dla t³umaczeñ miêdzynarodowych. Pakiet
zawiera tylko pliki podstawowe.
%endif


%if %{?_with_alltogether:0}%{!?_with_alltogether:1}
%package Affrikaans
Summary:	K Desktop Environment - Affrikaans language support
Summary(pl):	KDE - wsparcie dla jêzyka afrykanerskiego
Group:		X11/Applications

%description Affrikaans
K Desktop Environment - Affrikaans language support.

%description Affrikaans -l pl
KDE - wsparcie dla jêzyka afrykanerskiego.


%description Affrikaans -l pl
KDE - Wsparcie dla t³umaczeñ miêdzynarodowych.


%package Arabic
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Arabic
K Desktop Environment - International Support.

%description Arabic -l pl
KDE - Wsparcie dla t³umaczeñ miêdzynarodowych.


%package Azerbaijani
Summary:	K Desktop Environment - Azerbaijani language support
Summary(pl):	KDE - wsparcie dla jêzyka azerskiego
Group:		X11/Applications

%description Azerbaijani
K Desktop Environment - Azerbaijani language support.

%description Azerbaijani -l pl
KDE - wsparcie dla jêzyka azerskiego.


%description Azerbaijani -l pl
KDE - Wsparcie dla t³umaczeñ miêdzynarodowych.


%package Bulgarian
Summary:	K Desktop Environment - Bulgarian language support
Summary(pl):	KDE - wsparcie dla jêzyka bu³garskiego
Group:		X11/Applications

%description Bulgarian
K Desktop Environment - Bulgarian language support.

%description Bulgarian -l pl
KDE - wsparcie dla jêzyka bu³garskiego.

%package Bosnian
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Bosnian
K Desktop Environment - International Support.

%description Bosnian -l pl
KDE - Wsparcie dla t³umaczeñ miêdzynarodowych.


%package Catalan
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Catalan -l pl
KDE - Wsparcie dla t³umaczeñ miêdzynarodowych.


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
#
#%description Cymraeg -l pl
#KDE - Wsparcie dla t³umaczeñ miêdzynarodowych.


%package Danish
Summary:	K Desktop Environment - Danish language support
Summary(pl):	KDE - wsparcie dla jêzyka duñskiego
Group:		X11/Applications

%description Danish
K Desktop Environment - Danish language support.

%description Danish -l pl
KDE - wsparcie dla jêzyka duñskiego.


%description Danish -l pl
KDE - Wsparcie dla t³umaczeñ miêdzynarodowych.


%package German
Summary:	K Desktop Environment - German language support
Summary(pl):	KDE - wsparcie dla jêzyka niemieckiego
Group:		X11/Applications

%description German
K Desktop Environment - German language support.

%description German -l pl
KDE - wsparcie dla jêzyka niemieckiego.


%description German -l pl
KDE - Wsparcie dla t³umaczeñ miêdzynarodowych.


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
#
#%description English -l pl
#KDE - Wsparcie dla t³umaczeñ miêdzynarodowych.


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


%description Esperanto -l pl
KDE - Wsparcie dla t³umaczeñ miêdzynarodowych.


%package Spanish
Summary:	K Desktop Environment - Spanish language support
Summary(pl):	KDE - wsparcie dla jêzyka hiszpañskiego
Group:		X11/Applications

%description Spanish
K Desktop Environment - Spanish language support.

%description Spanish -l pl
KDE - wsparcie dla jêzyka hiszpañskiego.


%description Spanish -l pl
KDE - Wsparcie dla t³umaczeñ miêdzynarodowych.


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
#
#%description Basque -l pl
#KDE - Wsparcie dla t³umaczeñ miêdzynarodowych.


%package Finnish
Summary:	K Desktop Environment - Finnish language support
Summary(pl):	KDE - wsparcie dla jêzyka fiñskiego
Group:		X11/Applications

%description Finnish
K Desktop Environment - Finnish language support.

%description Finnish -l pl
KDE - wsparcie dla jêzyka fiñskiego.


%description Finnish -l pl
KDE - Wsparcie dla t³umaczeñ miêdzynarodowych.


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
#%description Irish -l pl
#KDE - Wsparcie dla t³umaczeñ miêdzynarodowych.


#%package Galician
#Summary:	K Desktop Environment - International Support
#Group:		X11/Applications
#
#%description Galician
#K Desktop Environment - International Support.
#
#%description Galician -l pl
#KDE - Wsparcie dla t³umaczeñ miêdzynarodowych.


%package Hebrew
Summary:	K Desktop Environment - Hebrew language support
Summary(pl):	KDE - wsparcie dla jêzyka hebrajskiego
Group:		X11/Applications

%description Hebrew
K Desktop Environment - Hebrew language support.

%description Hebrew -l pl
KDE - wsparcie dla jêzyka hebrajskiego.


%package Croatian
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Croatian
K Desktop Environment - International Support.

%description Croatian -l pl
KDE - Wsparcie dla t³umaczeñ miêdzynarodowych.


%package Hungarian
Summary:	K Desktop Environment - Hungarian language support
Summary(pl):	KDE - wsparcie dla jêzyka wêgierskiego
Group:		X11/Applications

%description Hungarian
K Desktop Environment - Hungarian language support.

%description Hungarian -l pl
KDE - wsparcie dla jêzyka wêgierskiego.


%description Hungarian -l pl
KDE - Wsparcie dla t³umaczeñ miêdzynarodowych.


%package Indonesian
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Indonesian
K Desktop Environment - International Support.

%description Indonesian -l pl
KDE - Wsparcie dla t³umaczeñ miêdzynarodowych.


%package Icelandic
Summary:	K Desktop Environment - Icelandic language support
Summary(pl):	KDE - wsparcie dla jêzyka islandzkiego
Group:		X11/Applications

%description Icelandic
K Desktop Environment - Icelandic language support.

%description Icelandic -l pl
KDE - wsparcie dla jêzyka islandzkiego.


%description Icelandic -l pl
KDE - Wsparcie dla t³umaczeñ miêdzynarodowych.


%package Italian
Summary:	K Desktop Environment - Italian language support
Summary(pl):	KDE - wsparcie dla jêzyka w³oskiego
Group:		X11/Applications

%description Italian
K Desktop Environment - Italian language support.

%description Italian -l pl
KDE - wsparcie dla jêzyka w³oskiego.


%description Italian -l pl
KDE - Wsparcie dla t³umaczeñ miêdzynarodowych.


%package Japanese
Summary:	K Desktop Environment - Japanese language support
Summary(pl):	KDE - wsparcie dla jêzyka japoñskiego
Group:		X11/Applications

%description Japanese
K Desktop Environment - Japanese language support.

%description Japanese -l pl
KDE - wsparcie dla jêzyka japoñskiego.


%description Japanese -l pl
KDE - Wsparcie dla t³umaczeñ miêdzynarodowych.


%package Korean
Summary:	K Desktop Environment - Korean language support
Summary(pl):    KDE - wsparcie dla jêzyka koreañskiego
Group:		X11/Applications

%description Korean
K Desktop Environment - Korean language support.

%description Korean -l pl
KDE - wsparcie dla jêzyka koreañskiego.


%description Korean -l pl
KDE - Wsparcie dla t³umaczeñ miêdzynarodowych.


%package Lithuanian
Summary:	K Desktop Environment - Lithuanian language support
Summary(pl):	KDE - wsparcie dla jêzyka litewskiego
Group:		X11/Applications

%description Lithuanian
K Desktop Environment - Lithuanian language support.

%description Lithuanian -l pl
KDE - Wsparcie dla jêzyka litewskiego.


%description Lithuanian -l pl
KDE - Wsparcie dla t³umaczeñ miêdzynarodowych.


%package Latvian
Summary:	K Desktop Environment - Latvian language support
Summary(pl):	KDE - wsparcie dla jêzyka ³otewskiego
Group:		X11/Applications

%description Latvian
K Desktop Environment - Latvian language support.

%description Latvian -l pl
KDE - wsparcie dla jêzyka ³otewskiego.


%description Latvian -l pl
KDE - Wsparcie dla t³umaczeñ miêdzynarodowych.


#%package Maori
#Summary:	K Desktop Environment - International Support
#Group:		X11/Applications
#
#%description Maori
#K Desktop Environment - International Support.
#
#%description Maori -l pl
#KDE - Wsparcie dla t³umaczeñ miêdzynarodowych.


#%package Macedonian
#Summary:	K Desktop Environment - International Support
#Group:		X11/Applications
#
#%description Macedonian
#K Desktop Environment - International Support.
#
#%description Macedonian -l pl
#KDE - Wsparcie dla t³umaczeñ miêdzynarodowych.


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

%description Dutch
K Desktop Environment - Dutch language support.

%description Dutch -l pl
KDE - wsparcie dla jêzyka holenderskiego.


%package Norwegian
Summary:	K Desktop Environment - International Support
Group:		X11/Applications
Obsoletes:	kde-i18n-Norwegian_Bokmaal

%description Norwegian
K Desktop Environment - International Support.

%description Norwegian -l pl
KDE - Wsparcie dla t³umaczeñ miêdzynarodowych.


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
#
#%description Gascon_occitan -l pl
#KDE - Wsparcie dla t³umaczeñ miêdzynarodowych.


%package Polish
Summary:	K Desktop Environment - Polish language support
Summary(pl):	KDE - wsparcie dla jêzyka polskiego
Group:		X11/Applications

%description Polish
K Desktop Environment - Polish language support.

%description Polish -l pl
KDE - wsparcie dla jêzyka polskiego.

%description Polish -l pl
KDE - Wsparcie dla t³umaczeñ miêdzynarodowych.


%package Portuguese
Summary:	K Desktop Environment - Portuguese language support
Summary(pl):	KDE - wsparcie dla jêzyka portugalskiego
Group:		X11/Applications
Obsoletes:	%{name}-Portugnese

%description Portuguese
K Desktop Environment - Portuguese language support.

%description Portuguese -l pl
KDE - wsparcie dla jêzyka portugalskiego.


%package Brazil_Portuguese
Summary:	K Desktop Environment - Portuguese (Brazil) language support
Summary(pl):	KDE - wsparcie dla jêzyka portugalskiego (odmiany brazylijskiej)
Group:		X11/Applications
Obsoletes:	%{name}-Brazil_Protugnese

%description Brazil_Portuguese
K Desktop Environment - Portuguese (Brazil) language support.

%description Brazil_Portuguese -l pl
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


%package Venda
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Venda
K Desktop Environment - International Support.

%description Venda -l pl
KDE - Wsparcie dla t³umaczeñ miêdzynarodowych.


%package Vietnamese
Summary:	K Desktop Environment - International Support
Group:		X11/Applications


%description Vietnamese
K Desktop Environment - International Support.

%description Vietnamese -l pl
KDE - Wsparcie dla t³umaczeñ miêdzynarodowych.


#%package Walloon
#Summary:	K Desktop Environment - International Support
#Group:		X11/Applications
#
#%description Walloon
#K Desktop Environment - International Support.
#
#%description Walloon -l pl
#KDE - Wsparcie dla t³umaczeñ miêdzynarodowych.


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


%package Zulu
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Zulu
K Desktop Environment - International Support.

%description Zulu -l pl
KDE - Wsparcie dla t³umaczeñ miêdzynarodowych.
%endif

%prep
%setup -q
%patch0 -p1

%build
%define         _sharedir       %{_datadir}
%define         _htmldir        /usr/share/doc/kde/HTML

kde_htmldir="%{_htmldir}"; export kde_htmldir

LDFLAGS="%{rpmldflags}"
%configure
%{__make} RPM_OPT_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%if %{?_with_kdelibs:1}%{!?_with_kdelibs:0}
FindLang() {
	echo "%defattr(644,root,root,755)" > "$2.lang"
	cat allname.lang |grep -vE tmp\|kdelibs.mo\|katepart.mo |grep "%lang($1)" >> "$2.lang"
}
%endif

%if %{?_with_kdelibs:0}%{!?_with_kdelibs:1}
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
%endif

%{__make} DESTDIR=$RPM_BUILD_ROOT install

package_list=`( grep -v '^#' < %{SOURCE1}; grep -v '^#' < %{SOURCE2} ) | cut -f 1 | sort | uniq`
for i in $package_list ; do
	install -d $RPM_BUILD_ROOT/tmp/$i
done

grep -v '^#' < %{SOURCE1} | \
while read package file ; do
if [ "$package" != "" -a "$file" != "" ] ; then
    if [ -d $RPM_BUILD_ROOT/tmp/$package ] ; then
	for f in $RPM_BUILD_ROOT%{_datadir}/locale/*/LC_MESSAGES/$file ; do
	    DIR=`echo $f | sed -e s,%{_datadir}/locale/,/tmp/$package%{_datadir}/locale/, -e s,/$file'$',,`
	    if [ ! -d $DIR ] ; then
		install -d $DIR
	    fi
	    mv $f $DIR
	done
    fi
fi
done

grep -v '^#' < %{SOURCE2} | \
while read package directory ; do
if [ "$package" != "" -a "$directory" != "" ] ; then
    if [ -d $RPM_BUILD_ROOT/tmp/$package ] ; then
	for f in $RPM_BUILD_ROOT%{_htmldir}/*/$directory ; do
	    DIR=`echo $f | sed -e s,%{_htmldir}/,/tmp/$package%{_htmldir}/, -e s,/$directory'$',,`
	    if [ ! -d $DIR ] ; then
		install -d $DIR
	    fi
	    mv $f $DIR
	done
    fi
fi
done

mv $RPM_BUILD_ROOT%{_datadir}/apps/ktuberling $RPM_BUILD_ROOT/tmp/kdegames%{_datadir}/apps
mv $RPM_BUILD_ROOT%{_datadir}/apps/amor $RPM_BUILD_ROOT/tmp/kdetoys%{_datadir}/apps

cd $RPM_BUILD_ROOT%{_datadir}/locale
for l in * ; do
	mv $l/[!L]* $RPM_BUILD_ROOT/tmp/kdebase%{_datadir}/locale/$l
done
cd -

%if %{?_with_tarball_creation:1}%{!?_tarball_creation:0}
ISDIR="`pwd`"
for i in $package_list ; do
	( cd $RPM_BUILD_ROOT/tmp/$i ; tar cjf %{_sourcedir}/%{name}-$i-%{version}.tar.bz2 . )
done
cd "$ISDIR"
%endif

%if %{?_with_kdelibs:1}%{!?_with_kdelibs:0}
%find_lang tmp.allname --with-kde --all-name
cat tmp.allname.lang |grep en_GB |sed 's/(en)/(en_GB)/' > allname.lang
cat tmp.allname.lang |grep pt_BR |sed 's/(pt)/(pt_BR)/' >> allname.lang
cat tmp.allname.lang |grep zh_CN |sed 's/(zh)/(zh_CN)/' >> allname.lang
cat tmp.allname.lang |grep zh_TW |sed 's/(zh)/(zh_TW)/' >> allname.lang
cat tmp.allname.lang |grep -vE en_GB\|pt_BR\|zh_CN\|zh_TW >> allname.lang
%endif

FindLang af Affrikaans
FindLang ar Arabic
FindLang az Azerbaijani
FindLang bg Bulgarian
# FindLang br Breton
FindLang bs Bosnian
FindLang ca Catalan
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
FindLang id Indonesian
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
FindLang nn Norwegian_Nynorsk
#FindLang no Norwegian
# FindLang oc Gascon_occitan
FindLang pl Polish
FindLang pt Portuguese
FindLang pt_BR Brazil_Portuguese
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
FindLang ven Venda 
FindLang vi Vietnamese
# FindLang wa Walloon
FindLang xh Xhosa
FindLang zh_CN Simplified_Chinese
FindLang zh_TW Chinese
FindLang zu Zulu

%if %{?_with_alltogether:1}%{!?_with_alltogether:0}
cat [A-Z]*.lang >all.lang
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{?_with_kdelibs:1}%{!?_with_kdelibs:0}
%files kdelibs
%defattr(644,root,root,755)
%{_datadir}/locale/*/LC_MESSAGES/kdelibs.mo
%{_datadir}/locale/*/LC_MESSAGES/katepart.mo
%endif

%if %{?_with_alltogether:0}%{!?_with_alltogether:1}
%files -f Affrikaans.lang Affrikaans
%files -f Arabic.lang Arabic
%files -f Azerbaijani.lang Azerbaijani
%files -f Bulgarian.lang Bulgarian
# %files -f Breton.lang Breton
%files -f Bosnian.lang Bosnian
%files -f Catalan.lang Catalan
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
%files -f Indonesian.lang Indonesian
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
#%files -f Norwegian.lang Norwegian
#%files -f Norwegian_Nynorsk.lang Norwegian_Nynorsk
# %files -f Gascon_occitan.lang Gascon_occitan
%files -f Polish.lang Polish
%files -f Portuguese.lang Portuguese
%files -f Brazil_Portuguese.lang Brazil_Portuguese
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
%files -f Venda.lang Venda
%files -f Vietnamese.lang Vietnamese
# %files -f Walloon.lang Walloon
%files -f Xhosa.lang Xhosa
%files -f Simplified_Chinese.lang Simplified_Chinese
%files -f Chinese.lang Chinese
%files -f Zulu.lang Zulu
%endif

%if %{?_with_alltogether:1}%{!?_with_alltogether:0}
%files -f all.lang
%endif
