#
# Conditional build:
%bcond_with alltogether		# build single package containing support
				# for all languages
%bcond_with tarball_creation	# create tarballs with resources for specific
				# packages; don't create any RPMs
%bcond_with kdelibs		# create single small package containing
				# essential files only

Summary:	K Desktop Environment - international support
Summary(pl):	KDE - wsparcie dla wielu j�zyk�w
Name:		kde-i18n
Version:	3.2.0
Release:	1
License:	GPL/LGPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	fe6fe3d722a12760522b688b749beca6
Source1:	%{name}-splitmo
Source2:	%{name}-splitdoc
Source3:        %{name}-splitdoc-shared
Patch0:		%{name}-es.patch
%if %{with alltogether}
# NOTE: "Affrikaans", "Norwegian_Bookmal" and "Portugnese" are here
# intentionally, to allow upgrade from packages with misspelled names
Obsoletes:	kde-i18n-Affrikaans
Obsoletes:	kde-i18n-Afrikaans
Obsoletes:	kde-i18n-Arabic
# Obsoletes:	kde-i18n-Azerbaijani
Obsoletes:	kde-i18n-Bulgarian
Obsoletes:	kde-i18n-Bosnian
Obsoletes:	kde-i18n-Catalan
Obsoletes:	kde-i18n-Czech
Obsoletes:	kde-i18n-Danish
Obsoletes:	kde-i18n-German
Obsoletes:	kde-i18n-Greek
Obsoletes:	kde-i18n-English_UK
Obsoletes:	kde-i18n-British
Obsoletes:	kde-i18n-Esperanto
Obsoletes:	kde-i18n-Spanish
Obsoletes:	kde-i18n-Estonian
Obsoletes:	kde-i18n-Finnish
Obsoletes:	kde-i18n-French
Obsoletes:	kde-i18n-Hebrew
Obsoletes:	kde-i18n-Croatian
Obsoletes:	kde-i18n-Hungarian
# Obsoletes:	kde-i18n-Indonesian
Obsoletes:	kde-i18n-Icelandic
Obsoletes:	kde-i18n-Italian
Obsoletes:	kde-i18n-Japanese
# Obsoletes:	kde-i18n-Korean
Obsoletes:	kde-i18n-Lithuanian
# Obsoletes:	kde-i18n-Latvian
Obsoletes:	kde-i18n-Maltese
Obsoletes:	kde-i18n-Dutch
Obsoletes:	kde-i18n-Norwegian
Obsoletes:	kde-i18n-Norwegian_Bokmaal
Obsoletes:	kde-i18n-Norwegian_Bookmal
Obsoletes:	kde-i18n-Norwegian_Nynorsk
Obsoletes:	kde-i18n-Polish
Obsoletes:	kde-i18n-Portugnese
Obsoletes:	kde-i18n-Portuguese
Obsoletes:	kde-i18n-Brazil
Obsoletes:	kde-i18n-Brazil_Portugnese
Obsoletes:	kde-i18n-Brazil_Portuguese
Obsoletes:	kde-i18n-Romanian
Obsoletes:	kde-i18n-Russian
Obsoletes:	kde-i18n-Slovak
Obsoletes:	kde-i18n-Slovenian
Obsoletes:	kde-i18n-Serbian
Obsoletes:	kde-i18n-Swedish
Obsoletes:	kde-i18n-Tamil
Obsoletes:	kde-i18n-Thai
Obsoletes:	kde-i18n-Turkish
Obsoletes:	kde-i18n-Ukrainian
Obsoletes:	kde-i18n-Venda
Obsoletes:	kde-i18n-Vietnamese
Obsoletes:	kde-i18n-Xhosa
Obsoletes:	kde-i18n-Simplified_Chinese
Obsoletes:	kde-i18n-Chinese
Obsoletes:	kde-i18n-Chinese-Big5
Obsoletes:	kde-i18n-Zulu
%endif
BuildRequires:	gettext-devel
# It creates symlinks to some not-translated files.
BuildRequires:	kdelibs >= %{version}
BuildRequires:	kdelibs-devel
BuildRequires:	libxml2-progs >= 2.4.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr

%description
K Desktop Environment - international support.

%description -l pl
KDE - wsparcie dla wielu j�zyk�w.

%package kdelibs
Summary:	K Desktop Environment - International Support
Summary(pl):	KDE - wsparcie dla wielu j�zyk�w
Group:		X11/Applications

%description kdelibs
K Desktop Environment - international support. This package contains
essential files only.

%description kdelibs -l pl
KDE - wsparcie dla wielu j�zyk�w. Pakiet zawiera tylko pliki
podstawowe.

%package Afrikaans
Summary:	K Desktop Environment - Afrikaans language support
Summary(pl):	KDE - wsparcie dla j�zyka afrykanerskiego
Group:		X11/Applications
# "Affrikaans" is here intentionally, to allow upgrade from misspelled packages
Obsoletes:	kde-i18n-Affrikaans

%description Afrikaans
K Desktop Environment - Afrikaans language support.

%description Afrikaans -l pl
KDE - wsparcie dla j�zyka afrykanerskiego.

%package Arabic
Summary:	K Desktop Environment - Arabic language support
Summary(pl):	KDE - wsparcie dla j�zyka arabskiego
Group:		X11/Applications

%description Arabic
K Desktop Environment - Arabic language support.

%description Arabic -l pl
KDE - wsparcie dla j�zyka arabskiego.

%package Azerbaijani
Summary:	K Desktop Environment - Azerbaijani language support
Summary(pl):	KDE - wsparcie dla j�zyka azerskiego
Group:		X11/Applications

%description Azerbaijani
K Desktop Environment - Azerbaijani language support.

%description Azerbaijani -l pl
KDE - wsparcie dla j�zyka azerskiego.

%package Bulgarian
Summary:	K Desktop Environment - Bulgarian language support
Summary(pl):	KDE - wsparcie dla j�zyka bu�garskiego
Group:		X11/Applications

%description Bulgarian
K Desktop Environment - Bulgarian language support.

%description Bulgarian -l pl
KDE - wsparcie dla j�zyka bu�garskiego.

%package Breton
Summary:	K Desktop Environment - Breton language support
Summary(pl):	KDE - wsparcie dla j�zyka breto�skiego
Group:		X11/Applications

%description Breton
K Desktop Environment - Breton language support.

%description Breton -l pl
KDE - wsparcie dla j�zyka breto�skiego.

%package Bosnian
Summary:	K Desktop Environment - Bosnian language support
Summary(pl):	KDE - wsparcie dla j�zyka bo�nia�skiego
Group:		X11/Applications

%description Bosnian
K Desktop Environment - Bosnian language support.

%description Bosnian -l pl
KDE - wsparcie dla j�zyka bo�nia�skiego.

%package Catalan
Summary:	K Desktop Environment - Catalan language support
Summary(pl):	KDE - wsparcie dla j�zyka katalo�skiego
Group:		X11/Applications

%description Catalan
K Desktop Environment - Catalan language support.

%description Catalan -l pl
KDE - wsparcie dla j�zyka katalo�skiego.

%package Czech
Summary:	K Desktop Environment - Czech language support
Summary(pl):	KDE - wsparcie dla j�zyka czeskiego
Group:		X11/Applications

%description Czech
K Desktop Environment - Czech language support.

%description Czech -l pl
KDE - wsparcie dla j�zyka czeskiego.

%package Cymraeg
Summary:	K Desktop Environment - Cymraeg language support
Summary(pl):	KDE - wsparcie dla j�zyka walijskiego
Group:		X11/Applications

%description Cymraeg
K Desktop Environment - Cymraeg language support.

%description Cymraeg -l pl
KDE - wsparcie dla j�zyka walijskiego.

%package Danish
Summary:	K Desktop Environment - Danish language support
Summary(pl):	KDE - wsparcie dla j�zyka du�skiego
Group:		X11/Applications

%description Danish
K Desktop Environment - Danish language support.

%description Danish -l pl
KDE - wsparcie dla j�zyka du�skiego.

%package German
Summary:	K Desktop Environment - German language support
Summary(pl):	KDE - wsparcie dla j�zyka niemieckiego
Group:		X11/Applications

%description German
K Desktop Environment - German language support.

%description German -l pl
KDE - wsparcie dla j�zyka niemieckiego.

%package Greek
Summary:	K Desktop Environment - Greek language support
Summary(pl):	KDE - wsparcie dla j�zyka greckiego
Group:		X11/Applications

%description Greek
K Desktop Environment - Greek language support.

%description Greek -l pl
KDE - wsparcie dla j�zyka greckiego.

%package English
Summary:	K Desktop Environment - English language support
Summary(pl):	KDE - wsparcie dla j�zyka angielskiego
Group:		X11/Applications

%description English
K Desktop Environment - English language support.

%description English -l pl
KDE - wsparcie dla j�zyka angielskiego.

%package English_UK
Summary:	K Desktop Environment - K Desktop Environment - English (UK) language support
Summary(pl):	KDE - wsparcie dla j�zyka angielskiego (odmiany brytyjskiej)
Group:		X11/Applications

%description English_UK
K Desktop Environment - English (UK) language support.

%description English_UK -l pl
KDE - wsparcie dla j�zyka angielskiego (odmiany brytyjskiej).

%package Esperanto
Summary:	K Desktop Environment - Esperanto language support
Summary(pl):	KDE - wsparcie dla j�zyka esperanto
Group:		X11/Applications

%description Esperanto
K Desktop Environment - Esperanto language support.

%description Esperanto -l pl
KDE - wsparcie dla j�zyka esperanto.

%package Spanish
Summary:	K Desktop Environment - Spanish language support
Summary(pl):	KDE - wsparcie dla j�zyka hiszpa�skiego
Group:		X11/Applications

%description Spanish
K Desktop Environment - Spanish language support.

%description Spanish -l pl
KDE - wsparcie dla j�zyka hiszpa�skiego.

%package Estonian
Summary:	K Desktop Environment - Estonian language support
Summary(pl):	KDE - wsparcie dla j�zyka esto�skiego
Group:		X11/Applications

%description Estonian
K Desktop Environment - Estonian language support.

%description Estonian -l pl
KDE - wsparcie dla j�zyka esto�skiego.

%package Basque
Summary:	K Desktop Environment - Basque language support
Summary(pl):	KDE - wsparcie dla j�zyka baskijskiego
Group:		X11/Applications

%description Basque
K Desktop Environment - Basque language support.

%description Basque -l pl
KDE - wsparcie dla j�zyka baskijskiego.

%package Farsi
Summary:	K Desktop Environment - Farsi language support
Summary(pl):	KDE - wsparcie dla j�zyka perskiego (farsi)
Group:		X11/Applications

%description Farsi
K Desktop Environment - Farsi language support.

%description Farsi -l pl
KDE - wsparcie dla j�zyka perskiego (farsi).


%package Finnish
Summary:	K Desktop Environment - Finnish language support
Summary(pl):	KDE - wsparcie dla j�zyka fi�skiego
Group:		X11/Applications

%description Finnish
K Desktop Environment - Finnish language support.

%description Finnish -l pl
KDE - wsparcie dla j�zyka fi�skiego.

%package French
Summary:	K Desktop Environment - French language support
Summary(pl):	KDE - wsparcie dla j�zyka francuskiego
Group:		X11/Applications

%description French
K Desktop Environment - French language support.

%description French -l pl
KDE - wsparcie dla j�zyka francuskiego.

%package Irish
Summary:	K Desktop Environment - Irish language support
Summary(pl):	KDE - wsparcie dla j�zyka irlandzkiego
Group:		X11/Applications

%description Irish
K Desktop Environment - Irish language support.

%description Irish -l pl
KDE - wsparcie dla j�zyka irlandzkiego.

%package Galician
Summary:	K Desktop Environment - Galician language support
Summary(pl):	KDE - wsparcie dla j�zyka galijskiego
Group:		X11/Applications

%description Galician
K Desktop Environment - Galician language support.

%description Galician -l pl
KDE - wsparcie dla j�zyka galijskiego.

%package Hindi
Summary:        K Desktop Environment - Hindi language support
Summary(pl):    KDE - wsparcie dla j�zyka hindi
Group:          X11/Applications

%description Hindi
K Desktop Environment - Hindi language support.

%description Hindi -l pl
KDE - wsparcie dla j�zyka hindi.

%package Hebrew
Summary:	K Desktop Environment - Hebrew language support
Summary(pl):	KDE - wsparcie dla j�zyka hebrajskiego
Group:		X11/Applications

%description Hebrew
K Desktop Environment - Hebrew language support.

%description Hebrew -l pl
KDE - wsparcie dla j�zyka hebrajskiego.

%package Croatian
Summary:	K Desktop Environment - Croatian language support
Summary(pl):	KDE - wsparcie dla j�zyka chorwackiego
Group:		X11/Applications

%description Croatian
K Desktop Environment - Croatian language support.

%description Croatian -l pl
KDE - wsparcie dla j�zyka chorwackiego.

%package Hungarian
Summary:	K Desktop Environment - Hungarian language support
Summary(pl):	KDE - wsparcie dla j�zyka w�gierskiego
Group:		X11/Applications

%description Hungarian
K Desktop Environment - Hungarian language support.

%description Hungarian -l pl
KDE - wsparcie dla j�zyka w�gierskiego.

%package Indonesian
Summary:	K Desktop Environment - Indonesian language support
Summary(pl):	KDE - wsparcie dla j�zyka indonezyjskiego
Group:		X11/Applications

%description Indonesian
K Desktop Environment - Indonesian language support.

%description Indonesian -l pl
KDE - wsparcie dla j�zyka indonezyjskiego.

%package Icelandic
Summary:	K Desktop Environment - Icelandic language support
Summary(pl):	KDE - wsparcie dla j�zyka islandzkiego
Group:		X11/Applications

%description Icelandic
K Desktop Environment - Icelandic language support.

%description Icelandic -l pl
KDE - wsparcie dla j�zyka islandzkiego.

%package Italian
Summary:	K Desktop Environment - Italian language support
Summary(pl):	KDE - wsparcie dla j�zyka w�oskiego
Group:		X11/Applications

%description Italian
K Desktop Environment - Italian language support.

%description Italian -l pl
KDE - wsparcie dla j�zyka w�oskiego.

%package Japanese
Summary:	K Desktop Environment - Japanese language support
Summary(pl):	KDE - wsparcie dla j�zyka japo�skiego
Group:		X11/Applications

%description Japanese
K Desktop Environment - Japanese language support.

%description Japanese -l pl
KDE - wsparcie dla j�zyka japo�skiego.

%package Korean
Summary:	K Desktop Environment - Korean language support
Summary(pl):	KDE - wsparcie dla j�zyka korea�skiego
Group:		X11/Applications

%description Korean
K Desktop Environment - Korean language support.

%description Korean -l pl
KDE - wsparcie dla j�zyka korea�skiego.

%package Lithuanian
Summary:	K Desktop Environment - Lithuanian language support
Summary(pl):	KDE - wsparcie dla j�zyka litewskiego
Group:		X11/Applications

%description Lithuanian
K Desktop Environment - Lithuanian language support.

%description Lithuanian -l pl
KDE - Wsparcie dla j�zyka litewskiego.

%package Latvian
Summary:	K Desktop Environment - Latvian language support
Summary(pl):	KDE - wsparcie dla j�zyka �otewskiego
Group:		X11/Applications

%description Latvian
K Desktop Environment - Latvian language support.

%description Latvian -l pl
KDE - wsparcie dla j�zyka �otewskiego.

%package Maori
Summary:	K Desktop Environment - Maori language support
Summary(pl):	KDE - wsparcie dla j�zyka maoryjskiego
Group:		X11/Applications

%description Maori
K Desktop Environment - Maori language support.

%description Maori -l pl
KDE - wsparcie dla j�zyka maoryjskiego.

%package Macedonian
Summary:	K Desktop Environment - Macedonian language support
Summary(pl):	KDE - wsparcie dla j�zyka macedo�skiego
Group:		X11/Applications

%description Macedonian
K Desktop Environment - Macedonian language support.

%description Macedonian -l pl
KDE - wsparcie dla j�zyka macedo�skiego.

%package Malay
Summary:        K Desktop Environment - Malay language support
Summary(pl):    KDE - wsparcie dla j�zyka malajskiego
Group:          X11/Applications

%description Malay
K Desktop Environment - Malay language support.

%description Malay -l pl
KDE - wsparcie dla j�zyka malajskiego.

%package Maltese
Summary:	K Desktop Environment - Maltese language support
Summary(pl):	KDE - wsparcie dla j�zyka malta�skiego
Group:		X11/Applications

%description Maltese
K Desktop Environment - Maltese language support.

%description Maltese -l pl
KDE - wsparcie dla j�zyka malta�skiego.

%package Mongolian
Summary:        K Desktop Environment - Mongolian language support
Summary(pl):    KDE - wsparcie dla j�zyka malta�skiego
Group:          X11/Applications

%description Mongolian
K Desktop Environment - Mongolian language support.

%description Mongolian -l pl
KDE - wsparcie dla j�zyka malta�skiego.

%package Dutch
Summary:	K Desktop Environment - Dutch language support
Summary(pl):	KDE - wsparcie dla j�zyka holenderskiego
Group:		X11/Applications

%description Dutch
K Desktop Environment - Dutch language support.

%description Dutch -l pl
KDE - wsparcie dla j�zyka holenderskiego.

%package Norwegian_Bokmaal
Summary:	K Desktop Environment - Norwegian (Bokmaal) language support
Summary(pl):	KDE - wsparcie dla j�zyka norweskiego (odmiany bokmaal)
Group:		X11/Applications
# "Bookmal" is here intentionally, to allow upgrade from misspelled packages
Obsoletes:	kde-i18n-Norwegian_Bookmal

%description Norwegian_Bokmaal
K Desktop Environment - Norwegian (Bokmaal) language support.

%description Norwegian_Bokmaal -l pl
KDE - wsparcie dla j�zyka norweskiego (odmiany bokmaal).

%package Norwegian_Nynorsk
Summary:	K Desktop Environment - Norwegian (Nynorsk) language support
Summary(pl):	KDE - wsparcie dla j�zyka norweskiego (odmiany nynorsk)
Group:		X11/Applications

%description Norwegian_Nynorsk
K Desktop Environment - Norwegian (Nynorsk) language support.

%description Norwegian_Nynorsk -l pl
KDE - wsparcie dla j�zyka norweskiego (odmiany nynorsk).

%package Northern_Sotho
Summary:	K Desktop Environment - Northern Sotho language support
Summary(pl):	KDE - wsparcie dla p�nocnej odmiany j�zyka ludu Soto
Group:		X11/Applications

%description Northern_Sotho
K Desktop Environment - Northern Sotho language support.

%description Northern_Sotho -l pl
KDE - wsparcie dla p�nocnej odmiany j�zyka ludu Soto.

%package Gascon_occitan
Summary:	K Desktop Environment - Occitan (Gascon) language support
Summary(pl):	KDE - wsparcie dla j�zyka oksyta�skiego (dialektu gasko�skiego)
Group:		X11/Applications

%description Gascon_occitan
K Desktop Environment - Occitan (Gascon) language support.

%description Gascon_occitan -l pl
KDE - wsparcie dla j�zyka oksyta�skiego (dialektu gasko�skiego).

%package Polish
Summary:	K Desktop Environment - Polish language support
Summary(pl):	KDE - wsparcie dla j�zyka polskiego
Group:		X11/Applications

%description Polish
K Desktop Environment - Polish language support.

%description Polish -l pl
KDE - wsparcie dla j�zyka polskiego.

%package Portuguese
Summary:	K Desktop Environment - Portuguese language support
Summary(pl):	KDE - wsparcie dla j�zyka portugalskiego
Group:		X11/Applications
# "Portugnese" is here intentionally, to allow upgrade from misspelled packages
Obsoletes:	%{name}-Portugnese

%description Portuguese
K Desktop Environment - Portuguese language support.

%description Portuguese -l pl
KDE - wsparcie dla j�zyka portugalskiego.

%package Brazil_Portuguese
Summary:	K Desktop Environment - Portuguese (Brazil) language support
Summary(pl):	KDE - wsparcie dla j�zyka portugalskiego (odmiany brazylijskiej)
Group:		X11/Applications
Obsoletes:	%{name}-Brazil_Protugnese

%description Brazil_Portuguese
K Desktop Environment - Portuguese (Brazil) language support.

%description Brazil_Portuguese -l pl
KDE - wsparcie dla j�zyka portugalskiego (odmiany brazylijskiej).

%package Romanian
Summary:	K Desktop Environment - Romanian language support
Summary(pl):	KDE - wsparcie dla j�zyka rumu�skiego
Group:		X11/Applications

%description Romanian
K Desktop Environment - Romanian language support.

%description Romanian -l pl
KDE - wsparcie dla j�zyka rumu�skiego.

%package Russian
Summary:	K Desktop Environment - Russian language support
Summary(pl):	KDE - wsparcie dla j�zyka rosyjskiego
Group:		X11/Applications

%description Russian
K Desktop Environment - Russian language support.

%description Russian -l pl
KDE - wsparcie dla j�zyka rosyjskiego.

%package Swati
Summary:	K Desktop Environment - Swati language support
Summary(pl):	KDE - wsparcie dla j�zyka swati
Group:		X11/Applications

%description Swati
K Desktop Environment - Swati language support.

%description Swati -l pl
KDE - wsparcie dla j�zyka swati.

%package Northern_Sami
Summary:	K Desktop Environment - Northern Sami language support
Summary(pl):	KDE - wsparcie dla p�nocnego j�zyka saami (lapo�skiego)
Group:		X11/Applications

%description Northern_Sami
K Desktop Environment - Northern Sami language support.

%description Northern_Sami -l pl
KDE - wsparcie dla p�nocnego j�zyka saami (lapo�skiego).

%package Slovak
Summary:	K Desktop Environment - Slovak language support
Summary(pl):	KDE - wsparcie dla j�zyka s�owackiego
Group:		X11/Applications

%description Slovak
K Desktop Environment - Slovak language support.

%description Slovak -l pl
KDE - wsparcie dla j�zyka s�owackiego.

%package Slovenian
Summary:	K Desktop Environment - Slovenian language support
Summary(pl):	KDE - wsparcie dla j�zyka s�owe�skiego
Group:		X11/Applications

%description Slovenian
K Desktop Environment - Slovenian language support.

%description Slovenian -l pl
KDE - wsparcie dla j�zyka s�owe�skiego.

%package Serbian
Summary:	K Desktop Environment - Serbian language support
Summary(pl):	KDE - wsparcie dla j�zyka serbskiego
Group:		X11/Applications

%description Serbian
K Desktop Environment - Serbian language support.

%description Serbian -l pl
KDE - wsparcie dla j�zyka serbskiego.

%package Swedish
Summary:	K Desktop Environment - Swedish language support
Summary(pl):	KDE - wsparcie dla j�zyka szwedzkiego
Group:		X11/Applications

%description Swedish
K Desktop Environment - Swedish language support.

%description Swedish -l pl
KDE - wsparcie dla j�zyka szwedzkiego.

%package Tamil
Summary:	K Desktop Environment - Tamil language support
Summary(pl):	KDE - wsparcie dla j�zyka tamilskiego
Group:		X11/Applications

%description Tamil
K Desktop Environment - Tamil language support.

%description Tamil -l pl
KDE - wsparcie dla j�zyka tamilskiego.

%package Thai
Summary:	K Desktop Environment - Thai language support
Summary(pl):	KDE - wsparcie dla j�zyka tajlandzkiego
Group:		X11/Applications

%description Thai
K Desktop Environment - Thai language support.

%description Thai -l pl
KDE - wsparcie dla j�zyka tajlandzkiego.

%package Turkish
Summary:	K Desktop Environment - Turkish language support
Summary(pl):	KDE - wsparcie dla j�zyka tureckiego
Group:		X11/Applications

%description Turkish
K Desktop Environment - Turkish language support.

%description Turkish -l pl
KDE - wsparcie dla j�zyka tureckiego.

%package Ukrainian
Summary:	K Desktop Environment - Ukrainian language support
Summary(pl):	KDE - wsparcie dla j�zyka ukrai�skiego
Group:		X11/Applications

%description Ukrainian
K Desktop Environment - Ukrainian language support.

%description Ukrainian -l pl
KDE - wsparcie dla j�zyka ukrai�skiego.

%package Uzbek
Summary:        K Desktop Environment - Uzbek language support
Summary(pl):    KDE - wsparcie dla j�zyka uzbeckiego
Group:          X11/Applications

%description Uzbek
K Desktop Environment - Uzbek language support.

%description Uzbek -l pl
KDE - wsparcie dla j�zyka uzbeckiego.


%package Venda
Summary:	K Desktop Environment - Venda language support
Summary(pl):	KDE - wsparcie dla j�zyka venda
Group:		X11/Applications

%description Venda
K Desktop Environment - Venda language support.

%description Venda -l pl
KDE - wsparcie dla j�zyka venda.

%package Vietnamese
Summary:	K Desktop Environment - Vietnamese language support
Summary(pl):	KDE - wsparcie dla j�zyka wietnamskiego
Group:		X11/Applications

%description Vietnamese
K Desktop Environment - Vietnamese language support.

%description Vietnamese -l pl
KDE - wsparcie dla j�zyka wietnamskiego.

%package Walloon
Summary:	K Desktop Environment - Walloon language support
Summary(pl):	KDE - wsparcie dla j�zyka walo�skiego
Group:		X11/Applications

%description Walloon
K Desktop Environment - Walloon language support.

%description Walloon -l pl
KDE - wsparcie dla j�zyka walo�skiego.

%package Xhosa
Summary:	K Desktop Environment - Xhosa language support
Summary(pl):	KDE - wsparcie dla j�zyka khosa
Group:		X11/Applications

%description Xhosa
K Desktop Environment - Xhosa language support.

%description Xhosa -l pl
KDE - wsparcie dla j�zyka khosa.

%package Simplified_Chinese
Summary:	K Desktop Environment - simplified Chinese language support
Summary(pl):	KDE - wsparcie dla uproszczonego j�zyka chi�skiego
Group:		X11/Applications

%description Simplified_Chinese
K Desktop Environment - simplified Chinese language support.

%description Simplified_Chinese -l pl
KDE - wsparcie dla uproszczonego j�zyka chi�skiego.

%package Chinese
Summary:	K Desktop Environment - Chinese language support
Summary(pl):	KDE - wsparcie dla j�zyka chi�skiego
Group:		X11/Applications

%description Chinese
K Desktop Environment - Chinese language support.

%description Chinese -l pl
KDE - wsparcie dla j�zyka chi�skiego.

%package Zulu
Summary:	K Desktop Environment - Zulu language support
Summary(pl):	KDE - wsparcie dla j�zyka zuluskiego
Group:		X11/Applications

%description Zulu
K Desktop Environment - Zulu language support.

%description Zulu -l pl
KDE - wsparcie dla j�zyka zuluskiego.

%prep
%setup -q
%patch0 -p1

%build
%define         _sharedir       %{_datadir}
%define         _htmldir        /usr/share/doc/kde/HTML

kde_htmldir="%{_htmldir}"; export kde_htmldir

LDFLAGS="%{rpmldflags}"

%{__make} -f admin/Makefile.common cvs

%configure
%{__make} \
	RPM_OPT_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%if %{with kdelibs}
FindLang() {
	echo "%defattr(644,root,root,755)" > "$2.lang"
	cat allname.lang |grep -vE 'tmp|kdelibs\.mo|katepart\.mo' |grep "%lang($1)" >> "$2.lang"
}
%else
FindLang() {
#    $1 - short language name
#    $2 - long language name

    echo "%defattr(644,root,root,755)" > "$2.lang"

# share/doc/kde/HTML/(%%lang)
    if [ -d "$RPM_BUILD_ROOT%{_htmldir}/$1" ]; then
	echo "%lang($1) %{_htmldir}/$1" >> "$2.lang"
    fi

# share/locale/(%%lang)
    if [ -d "$RPM_BUILD_ROOT%{_datadir}/locale/$1" ]; then
	echo "%lang($1) %{_datadir}/locale/$1/[cef]*" >> "$2.lang"
	echo "%lang($1) %{_datadir}/locale/$1/LC_MESSAGES/*.mo" >> "$2.lang"
    fi

# share/apps/amor/tips-(%%lang)
    if [ -f "$RPM_BUILD_ROOT%{_datadir}/apps/amor/tips-$1" ]; then
	echo "%lang($1) %{_datadir}/apps/amor/tips-$1" >> "$2.lang"
    fi

# share/apps/ktuberling/sounds/(%%lang)
    if [ -d "$RPM_BUILD_ROOT%{_datadir}/apps/ktuberling/sounds/$1" ]; then
	echo "%lang($1) %{_datadir}/apps/ktuberling/sounds/$1" >> "$2.lang"
    fi
}
%endif

%{__make} DESTDIR=$RPM_BUILD_ROOT install

%if %{with tarball_creation}
package_list=`awk '!/^#/ { print $1 } ' %{SOURCE1} %{SOURCE2} | sort | uniq`
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
	    echo $DIR
# This moves the dir from the htmldir/lang/app to /tmp/package/htmldir/lang
	    if [ ! -d $DIR ] ; then
		install -d $DIR
	    fi
	    mv $f $DIR
	done
    fi
fi
done

grep -v '^#' < %{SOURCE3} | \
while read package directory file; do
if [ "$package" != "" -a "$directory" != "" -a "$file" != "" ] ; then
    if [ -d $RPM_BUILD_ROOT/tmp/$package ] ; then
	for f in $RPM_BUILD_ROOT%{_htmldir}/*/$directory/$file ; do
	    DIR=`echo $f | sed -e s,%{_htmldir}/,/tmp/$package%{_htmldir}/, -e s,/$file'$',,`
# This moves the docs from the htmldir/lang/app to /tmp/package/htmldir/lang
	    if [ ! -d $DIR ] ; then
		install -d $DIR
	    fi
	    mv $f $DIR
	done
    fi
fi
done


mv $RPM_BUILD_ROOT%{_datadir}/apps/ktuberling $RPM_BUILD_ROOT/tmp/kdegames%{_datadir}/apps

cd $RPM_BUILD_ROOT%{_datadir}/locale
for l in * ; do
	mv $l/[!L]* $RPM_BUILD_ROOT/tmp/kdebase%{_datadir}/locale/$l
done
cd -

ISDIR="`pwd`"
for i in $package_list ; do
	( cd $RPM_BUILD_ROOT/tmp/$i ; tar cjf %{_sourcedir}/%{name}-$i-%{version}.tar.bz2 . )
	echo "Wrote %{name}-$i-%{version}.tar.bz2"
done
cd "$ISDIR"
%endif

%if %{with kdelibs}
%find_lang tmp.allname --with-kde --all-name
cat tmp.allname.lang |grep en_GB |sed 's/(en)/(en_GB)/' > allname.lang
cat tmp.allname.lang |grep pt_BR |sed 's/(pt)/(pt_BR)/' >> allname.lang
cat tmp.allname.lang |grep zh_CN |sed 's/(zh)/(zh_CN)/' >> allname.lang
cat tmp.allname.lang |grep zh_TW |sed 's/(zh)/(zh_TW)/' >> allname.lang
cat tmp.allname.lang |grep -vE en_GB\|pt_BR\|zh_CN\|zh_TW >> allname.lang
%find_lang kdelibs
%find_lang katepart
cat katepart.lang >> kdelibs.lang
%endif

##FindLang af Afrikaans
##FindLang ar Arabic
FindLang az Azerbaijani
FindLang bg Bulgarian
# FindLang br Breton
FindLang bs Bosnian
FindLang ca Catalan
FindLang cs Czech
FindLang cy Cymraeg
FindLang da Danish
FindLang de German
FindLang el Greek
# FindLang en English
FindLang en_GB English_UK
##FindLang eo Esperanto
FindLang es Spanish
FindLang et Estonian
FindLang eu Basque
FindLang fa Farsi
FindLang fi Finnish
FindLang fr French
# FindLang ga Irish
FindLang gl Galician
FindLang he Hebrew
FindLang hi Hindi
##FindLang hr Croatian
FindLang hu Hungarian
# FindLang id Indonesian
##FindLang is Icelandic
FindLang it Italian
##FindLang ja Japanese
## FindLang ko Korean
##FindLang lt Lithuanian
## FindLang lv Latvian
# FindLang mi Maori
##FindLang mk Macedonian
FindLang mn Mongolian
FindLang ms Malay
##FindLang mt Maltese
FindLang nb Norwegian_Bokmaal
FindLang nl Dutch
FindLang nn Norwegian_Nynorsk
#indLang nso Northern_Sotho
# FindLang oc Gascon_occitan
FindLang pl Polish
FindLang pt Portuguese
FindLang pt_BR Brazil_Portuguese
FindLang ro Romanian
FindLang ru Russian
##FindLang ss Swati
FindLang se Northern_Sami
FindLang sk Slovak
FindLang sl Slovenian
FindLang sr Serbian
FindLang sv Swedish
FindLang ta Tamil
##FindLang th Thai
FindLang tr Turkish
FindLang uk Ukrainian
FindLang uz Uzbek
##FindLang ven Venda
##FindLang vi Vietnamese
# FindLang wa Walloon
##FindLang xh Xhosa
FindLang zh_CN Simplified_Chinese
FindLang zh_TW Chinese
##FindLang zu Zulu

%if %{with alltogether}
cat [A-Z]*.lang >all.lang
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if 0%{?_with_kdelibs:%{!?_with_tarball_creation:1}}
%files kdelibs -f kdelibs.lang
%endif

%if 0%{!?_with_alltogether:%{!?_with_tarball_creation:1}}
#%%files -f Afrikaans.lang Afrikaans
#%%files -f Arabic.lang Arabic
%files -f Azerbaijani.lang Azerbaijani
#%%files -f Bulgarian.lang Bulgarian
# %files -f Breton.lang Breton
%files -f Bosnian.lang Bosnian
%files -f Catalan.lang Catalan
%files -f Czech.lang Czech
%files -f Cymraeg.lang Cymraeg
%files -f Danish.lang Danish
%files -f German.lang German
%files -f Greek.lang Greek
# %files -f English.lang English
%files -f English_UK.lang English_UK
#%%files -f Esperanto.lang Esperanto
%files -f Spanish.lang Spanish
%files -f Estonian.lang Estonian
%files -f Basque.lang Basque
%files -f Farsi.lang Farsi
%files -f Finnish.lang Finnish
%files -f French.lang French
# %files -f Irish.lang Irish
%files -f Galician.lang Galician
%files -f Hindi.lang Hindi
%files -f Hebrew.lang Hebrew
#%%files -f Croatian.lang Croatian
%files -f Hungarian.lang Hungarian
##%files -f Indonesian.lang Indonesian
#%%files -f Icelandic.lang Icelandic
%files -f Italian.lang Italian
#%%files -f Japanese.lang Japanese
##%files -f Korean.lang Korean
#%%files -f Lithuanian.lang Lithuanian
##%files -f Latvian.lang Latvian
#%%files -f Maltese.lang Maltese
%files -f Malay.lang Malay
%files -f Mongolian.lang Mongolian
# %files -f Maori.lang Maori
#%%files -f Macedonian.lang Macedonian
%files -f Dutch.lang Dutch
%files -f Norwegian_Bokmaal.lang Norwegian_Bokmaal
%files -f Norwegian_Nynorsk.lang Norwegian_Nynorsk
#%%files -f Northern_Sotho.lang Northern_Sotho
# %files -f Gascon_occitan.lang Gascon_occitan
%files -f Polish.lang Polish
#%%{_datadir}/services/searchproviders/*.desktop
%files -f Portuguese.lang Portuguese
%files -f Brazil_Portuguese.lang Brazil_Portuguese
%files -f Romanian.lang Romanian
%files -f Russian.lang Russian
%files -f Northern_Sami.lang Northern_Sami
#%%files -f Swati.lang Swati
%files -f Slovak.lang Slovak
%files -f Slovenian.lang Slovenian
%files -f Serbian.lang Serbian
%files -f Swedish.lang Swedish
%files -f Tamil.lang Tamil
#%%files -f Thai.lang Thai
%files -f Turkish.lang Turkish
%files -f Ukrainian.lang Ukrainian
%files -f Uzbek.lang Uzbek
#%%files -f Venda.lang Venda
#%%files -f Vietnamese.lang Vietnamese
# %files -f Walloon.lang Walloon
#%%files -f Xhosa.lang Xhosa
%files -f Simplified_Chinese.lang Simplified_Chinese
%files -f Chinese.lang Chinese
#%%files -f Zulu.lang Zulu
%endif

%if 0%{?_with_alltogether:%{!?_with_tarball_creation:1}}
%files -f all.lang
%endif
