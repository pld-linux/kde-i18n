# Conditional build:
# --with	alltogether		Build single package containing
#					support for all languages
#
# --with	tarball_creation	Create tarballs with resources for
#					specific packages
#
# --with	kdelibs_only		Create single small package containing
#					essential files only



Summary:	K Desktop Environment - International Support
Summary(pl):	KDE - Wsparcie dla t³umaczeñ miêdzynarodowych
Name:		kde-i18n
Version:	3.0.1
Release:	1.2
License:	GPL/LGPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/stable/3.0/src/%{name}-%{version}.tar.bz2
Source1:	%{name}-splitmo
Source2:	%{name}-splitdoc
Patch0:		%{name}-nodoc.patch
Patch1:		%{name}-3.0.1-pl_lang_names.patch
Patch2:		%{name}-nb_to_no.patch
Patch3:		%{name}-3.0.1-core.patch
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
K Desktop Environment - International Support.

%description -l pl
KDE - Wsparcie dla t³umaczeñ miêdzynarodowych.

%if %{?_with_kdelibs_only:1}%{!?_with_kdelibs_only:0}
%package kdelibs
Summary:	K Desktop Environment - International Support
Summary(pl):	KDE - Wsparcie dla t³umaczeñ miêdzynarodowych
Group:		X11/Applications
Conflicts:	kde-i18n-Affrikaans kde-i18n-Arabic kde-i18n-Azerbaijani
Conflicts:	kde-i18n-Bulgarian kde-i18n-Bosnian kde-i18n-Catalan
Conflicts:	kde-i18n-Czech kde-i18n-Danish kde-i18n-German kde-i18n-Greek
Conflicts:	kde-i18n-English_UK kde-i18n-Esperanto kde-i18n-Spanish
Conflicts:	kde-i18n-Estonian kde-i18n-Finnish kde-i18n-French
Conflicts:	kde-i18n-Hebrew kde-i18n-Croatian kde-i18n-Hungarian
Conflicts:	kde-i18n-Indonesian kde-i18n-Icelandic kde-i18n-Italian
Conflicts:	kde-i18n-Japanese kde-i18n-Korean kde-i18n-Lithuanian
Conflicts:	kde-i18n-Latvian kde-i18n-Maltese kde-i18n-Dutch
Conflicts:	kde-i18n-Norwegian kde-i18n-Norwegian_Bokmaal
Conflicts:	kde-i18n-Norwegian_Nynorsk kde-i18n-Polish kde-i18n-Portugnese
Conflicts:	kde-i18n-Brazil_Portugnese kde-i18n-Romanian kde-i18n-Russian
Conflicts:	kde-i18n-Slovak kde-i18n-Slovenian kde-i18n-Serbian
Conflicts:	kde-i18n-Swedish kde-i18n-Tamil kde-i18n-Thai kde-i18n-Turkish
Conflicts:	kde-i18n-Ukrainian kde-i18n-Venda kde-i18n-Vietnamese
Conflicts:	kde-i18n-Xhosa kde-i18n-Simplified_Chinese kde-i18n-Chinese
Conflicts:	kde-i18n-Zulu kde-i18n

%description kdelibs
K Desktop Environment - International Support. Package
contains essential files only

%description -l pl kdelibs
KDE - Wsparcie dla t³umaczeñ miêdzynarodowych. Pakiet
zawiera tylko pliki podstawowe.
%endif

%if %{?_with_alltogether:0}%{!?_with_alltogether:1} && %{?_with_kdelibs_only:0}%{!?_with_kdelibs_only:1}
%package Affrikaans
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Affrikaans
K Desktop Environment - International Support.

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
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Azerbaijani
K Desktop Environment - International Support.

%description Azerbaijani -l pl
KDE - Wsparcie dla t³umaczeñ miêdzynarodowych.


%package Bulgarian
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Bulgarian
K Desktop Environment - International Support.

%description Bulgarian -l pl
KDE - Wsparcie dla t³umaczeñ miêdzynarodowych.


#%package Breton
#Summary:	K Desktop Environment - International Support
#Group:		X11/Applications
#
#%description Breton
#K Desktop Environment - International Support.
#
#%description Breton -l pl
#KDE - Wsparcie dla t³umaczeñ miêdzynarodowych.


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

%description Catalan
K Desktop Environment - International Support.

%description Catalan -l pl
KDE - Wsparcie dla t³umaczeñ miêdzynarodowych.


%package Czech
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Czech
K Desktop Environment - International Support.

%description Czech -l pl
KDE - Wsparcie dla t³umaczeñ miêdzynarodowych.


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
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Danish
K Desktop Environment - International Support.

%description Danish -l pl
KDE - Wsparcie dla t³umaczeñ miêdzynarodowych.


%package German
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description German
K Desktop Environment - International Support.

%description German -l pl
KDE - Wsparcie dla t³umaczeñ miêdzynarodowych.


%package Greek
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Greek
K Desktop Environment - International Support.

%description Greek -l pl
KDE - Wsparcie dla t³umaczeñ miêdzynarodowych.


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
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description English_UK
K Desktop Environment - International Support.

%description English_UK -l pl
KDE - Wsparcie dla t³umaczeñ miêdzynarodowych.


%package Esperanto
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Esperanto
K Desktop Environment - International Support.

%description Esperanto -l pl
KDE - Wsparcie dla t³umaczeñ miêdzynarodowych.


%package Spanish
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Spanish
K Desktop Environment - International Support.

%description Spanish -l pl
KDE - Wsparcie dla t³umaczeñ miêdzynarodowych.


%package Estonian
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Estonian
K Desktop Environment - International Support.

%description Estonian -l pl
KDE - Wsparcie dla t³umaczeñ miêdzynarodowych.


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
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Finnish
K Desktop Environment - International Support.

%description Finnish -l pl
KDE - Wsparcie dla t³umaczeñ miêdzynarodowych.


%package French
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description French
K Desktop Environment - International Support.

%description French -l pl
KDE - Wsparcie dla t³umaczeñ miêdzynarodowych.


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
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Hebrew
K Desktop Environment - International Support.

%description Hebrew -l pl
KDE - Wsparcie dla t³umaczeñ miêdzynarodowych.


%package Croatian
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Croatian
K Desktop Environment - International Support.

%description Croatian -l pl
KDE - Wsparcie dla t³umaczeñ miêdzynarodowych.


%package Hungarian
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Hungarian
K Desktop Environment - International Support.

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
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Icelandic
K Desktop Environment - International Support.

%description Icelandic -l pl
KDE - Wsparcie dla t³umaczeñ miêdzynarodowych.


%package Italian
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Italian
K Desktop Environment - International Support.

%description Italian -l pl
KDE - Wsparcie dla t³umaczeñ miêdzynarodowych.


%package Japanese
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Japanese
K Desktop Environment - International Support.

%description Japanese -l pl
KDE - Wsparcie dla t³umaczeñ miêdzynarodowych.


%package Korean
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Korean
K Desktop Environment - International Support.

%description Korean -l pl
KDE - Wsparcie dla t³umaczeñ miêdzynarodowych.


%package Lithuanian
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Lithuanian
K Desktop Environment - International Support.

%description Lithuanian -l pl
KDE - Wsparcie dla t³umaczeñ miêdzynarodowych.


%package Latvian
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Latvian
K Desktop Environment - International Support.

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
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Maltese
K Desktop Environment - International Support.

%description Maltese -l pl
KDE - Wsparcie dla t³umaczeñ miêdzynarodowych.


%package Dutch
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Dutch
K Desktop Environment - International Support.

%description Dutch -l pl
KDE - Wsparcie dla t³umaczeñ miêdzynarodowych.


%package Norwegian
Summary:	K Desktop Environment - International Support
Group:		X11/Applications
Obsoletes:	kde-i18n-Norwegian_Bokmaal

%description Norwegian
K Desktop Environment - International Support.

%description Norwegian -l pl
KDE - Wsparcie dla t³umaczeñ miêdzynarodowych.


%package Norwegian_Nynorsk
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Norwegian_Nynorsk
K Desktop Environment - International Support.

%description Norwegian_Nynorsk -l pl
KDE - Wsparcie dla t³umaczeñ miêdzynarodowych.


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
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Polish
K Desktop Environment - International Support.

%description Polish -l pl
KDE - Wsparcie dla t³umaczeñ miêdzynarodowych.


%package Portugnese
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Portugnese
K Desktop Environment - International Support.

%description Portugnese -l pl
KDE - Wsparcie dla t³umaczeñ miêdzynarodowych.


%package Brazil_Portugnese
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Brazil_Portugnese
K Desktop Environment - International Support.

%description Brazil_Portugnese -l pl
KDE - Wsparcie dla t³umaczeñ miêdzynarodowych.


%package Romanian
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Romanian
K Desktop Environment - International Support.

%description Romanian -l pl
KDE - Wsparcie dla t³umaczeñ miêdzynarodowych.


%package Russian
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Russian
K Desktop Environment - International Support.

%description Russian -l pl
KDE - Wsparcie dla t³umaczeñ miêdzynarodowych.


%package Slovak
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Slovak
K Desktop Environment - International Support.

%description Slovak -l pl
KDE - Wsparcie dla t³umaczeñ miêdzynarodowych.


%package Slovenian
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Slovenian
K Desktop Environment - International Support.

%description Slovenian -l pl
KDE - Wsparcie dla t³umaczeñ miêdzynarodowych.


%package Serbian
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Serbian
K Desktop Environment - International Support.

%description Serbian -l pl
KDE - Wsparcie dla t³umaczeñ miêdzynarodowych.


%package Swedish
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Swedish
K Desktop Environment - International Support.

%description Swedish -l pl
KDE - Wsparcie dla t³umaczeñ miêdzynarodowych.


%package Tamil
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Tamil
K Desktop Environment - International Support.

%description Tamil -l pl
KDE - Wsparcie dla t³umaczeñ miêdzynarodowych.


%package Thai
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Thai
K Desktop Environment - International Support.

%description Thai -l pl
KDE - Wsparcie dla t³umaczeñ miêdzynarodowych.


%package Turkish
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Turkish
K Desktop Environment - International Support.

%description Turkish -l pl
KDE - Wsparcie dla t³umaczeñ miêdzynarodowych.


%package Ukrainian
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Ukrainian
K Desktop Environment - International Support.

%description Ukrainian -l pl
KDE - Wsparcie dla t³umaczeñ miêdzynarodowych.


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
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Xhosa
K Desktop Environment - International Support.

%description Xhosa -l pl
KDE - Wsparcie dla t³umaczeñ miêdzynarodowych.


%package Simplified_Chinese
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Simplified_Chinese
K Desktop Environment - International Support.

%description Simplified_Chinese -l pl
KDE - Wsparcie dla t³umaczeñ miêdzynarodowych.


%package Chinese
Summary:	K Desktop Environment - International Support
Group:		X11/Applications

%description Chinese
K Desktop Environment - International Support.

%description Chinese -l pl
KDE - Wsparcie dla t³umaczeñ miêdzynarodowych.


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
%patch1 -p1
rm -rf no; mv nb no
%patch2 -p1
%patch3 -p1

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

%if %{?_with_tarball_creation:1}%{!?_tarball_creation:0}

cd $RPM_BUILD_ROOT%{_datadir}/locale
for l in * ; do
	cp $l/[!L]* $RPM_BUILD_ROOT/tmp/kdebase%{_datadir}/locale/$l
done
cd -

ISDIR="`pwd`"
for i in $package_list ; do
	( cd $RPM_BUILD_ROOT/tmp/$i ; tar cjf %{_sourcedir}/%{name}-$i-%{version}.tar.bz2 . )
done
cd "$ISDIR"
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
FindLang hr Croatian
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
FindLang no Norwegian
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

%if %{?_with_kdelibs_only:1}%{!?_with_kdelibs_only:0}
%files kdelibs
%defattr(644,root,root,755)
#%{_datadir}/locale/*/[!L]*
%{_datadir}/locale/*/LC_MESSAGES/kdelibs.mo
%{_datadir}/locale/*/LC_MESSAGES/katepart.mo
#%{_datadir}/locale/*/LC_MESSAGES/cupsdconf.mo
#%{_datadir}/locale/*/LC_MESSAGES/desktop.mo
#%{_datadir}/locale/*/LC_MESSAGES/kmcop.mo
#%{_datadir}/locale/*/LC_MESSAGES/knotify.mo
#%{_datadir}/locale/*/LC_MESSAGES/libkscreensaver.mo
#%{_datadir}/locale/*/LC_MESSAGES/ppdtranslations.mo
%endif

%if %{?_with_alltogether:0}%{!?_with_alltogether:1} && %{?_with_kdelibs_only:0}%{!?_with_kdelibs_only:1}
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
%files -f Croatian.lang Croatian
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
%files -f Norwegian.lang Norwegian
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
