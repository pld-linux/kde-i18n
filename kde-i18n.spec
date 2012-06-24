#
# Conditional build:
%bcond_with	alltogether		# build single package containing support
					# for all languages
%define	_kdever	3.4.2

Summary:	K Desktop Environment - international support
Summary(pl):	KDE - wsparcie dla wielu j�zyk�w
Name:		kde-i18n
Version:	3.4.2
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-ar-%{version}.tar.bz2
# Source0-md5:	58e437f117e280045be25004e520ba19
Source1:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-bg-%{version}.tar.bz2
# Source1-md5:	97456e12193b1024612a4195a6a1f9a3
Source2:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-bn-%{version}.tar.bz2
# Source2-md5:	3c7aea7fc0ce616e14938930bb56a5e5
Source3:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-br-%{version}.tar.bz2
# Source3-md5:	d59ae4df8d1eb3ef04d2621988f9404f
Source4:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-bs-%{version}.tar.bz2
# Source4-md5:	9077aa0725246ec249cf2ead67fd9f62
Source5:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-ca-%{version}.tar.bz2
# Source5-md5:	f5a3431ccc351571b1646eca32506830
Source6:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-cs-%{version}.tar.bz2
# Source6-md5:	f73dd7bef15e5cc816c0bea13d6f7c83
Source7:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-cy-%{version}.tar.bz2
# Source7-md5:	f7269da85c77bdfb030a604785b353b0
Source8:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-da-%{version}.tar.bz2
# Source8-md5:	9ca37ca653ca4318cccd123a9f7b2a7b
Source9:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-de-%{version}.tar.bz2
# Source9-md5:	d08b08dfb9913ccae65c12030755eeeb
Source10:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-el-%{version}.tar.bz2
# Source10-md5:	a62e585ede740230c2b361f76af8d816
Source11:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-en_GB-%{version}.tar.bz2
# Source11-md5:	e3c2226ad67ad1ce73d48f3a57cbb00c
Source12:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-eo-%{version}.tar.bz2
# Source12-md5:	2d6fd4e41b0590ecfb584f40d0d54edd
Source13:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-es-%{version}.tar.bz2
# Source13-md5:	8f85ee4ed2e2450076e0df44e234b465
Source14:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-et-%{version}.tar.bz2
# Source14-md5:	f48b7b0b9077c61d49f8c612b2726e73
Source15:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-eu-%{version}.tar.bz2
# Source15-md5:	333d6cf136bb3aa1468f2e6eb228084c
Source16:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-fi-%{version}.tar.bz2
# Source16-md5:	757f3c63d837551286ba3e3d82043f18
Source17:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-fr-%{version}.tar.bz2
# Source17-md5:	2e1a215fe50aa2cc778f0d60d7d8e3c2
Source18:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-fy-%{version}.tar.bz2
# Source18-md5:	089311764b43d5c8266dd61df8d75c38
Source19:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-ga-%{version}.tar.bz2
# Source19-md5:	85bf37520fbd0c7bed454689c9e13cbe
Source20:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-he-%{version}.tar.bz2
# Source20-md5:	ca6d2f889e80b619c0e7c506751925b9
Source21:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-hi-%{version}.tar.bz2
# Source21-md5:	9e48c3943219b4ca203de1db61dfe84d
Source22:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-hsb-%{version}.tar.bz2
# Source22-md5:	4629c38ae936e82fcc2282af0d07b724
Source23:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-hu-%{version}.tar.bz2
# Source23-md5:	3006f19275124a1c72174eb57fe828ce
Source24:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-is-%{version}.tar.bz2
# Source24-md5:	df6ddbd88f8494ee29a7d10b38acfac8
Source25:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-it-%{version}.tar.bz2
# Source25-md5:	9bb6a0522e32ae078cba3a928d3012fe
Source26:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-ja-%{version}.tar.bz2
# Source26-md5:	c46face4b4bcc75fb593b523eadd7d6d
Source27:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-lt-%{version}.tar.bz2
# Source27-md5:	b614e6dede0b77813ca1181754b1e113
Source28:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-mk-%{version}.tar.bz2
# Source28-md5:	da100cfd29fed0134dc29d37d2dccd24
Source29:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-nb-%{version}.tar.bz2
# Source29-md5:	ef20071e63fe76fc6c7e116bd14ebbd5
Source30:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-nds-%{version}.tar.bz2
# Source30-md5:	4b0b302cf56b8db010aa5befdbba3455
Source31:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-nl-%{version}.tar.bz2
# Source31-md5:	5ffeabd3de47ed44942c3e87631a3b50
Source32:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-nn-%{version}.tar.bz2
# Source32-md5:	6207ace27fa8c332a40afe911c63259c
Source33:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-pa-%{version}.tar.bz2
# Source33-md5:	da2f01224ed8bd4bc776cc306d903e75
Source34:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-pl-%{version}.tar.bz2
# Source34-md5:	713b81ba611096e3af55510dbf3c8dc1
Source35:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-pt-%{version}.tar.bz2
# Source35-md5:	f364f0dbd79efa2b55819353b62d497d
Source36:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-pt_BR-%{version}.tar.bz2
# Source36-md5:	fed87f573f3042b4962f9542ea9ab700
Source37:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-ro-%{version}.tar.bz2
# Source37-md5:	89b1c4c64633475709b037c6c3f9f696
Source38:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-ru-%{version}.tar.bz2
# Source38-md5:	512c68b42c33fecb39fc8d6af05668a1
Source39:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-se-%{version}.tar.bz2
# Source39-md5:	b0466f4ca33baefb609d0d38aac08b3a
Source40:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-sk-%{version}.tar.bz2
# Source40-md5:	ffa21cab8e4c97c74176b36fff8b2f9b
Source41:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-sl-%{version}.tar.bz2
# Source41-md5:	0702b0cdcce4f0c9b835a140713fbd86
Source42:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-sr-%{version}.tar.bz2
# Source42-md5:	0d9e803c9284ce0cca672c5548072a54
Source43:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-sr@Latn-%{version}.tar.bz2
# Source43-md5:	8f95eac7ead01718fc34a092f75932db
Source44:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-sv-%{version}.tar.bz2
# Source44-md5:	2f2f3f79924bfb2f75ee9f389e030b96
Source45:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-ta-%{version}.tar.bz2
# Source45-md5:	c92b95f128530b14d141d786c3c48b97
Source46:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-tg-%{version}.tar.bz2
# Source46-md5:	484588e6d100c642cba625386e9216fc
Source47:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-tr-%{version}.tar.bz2
# Source47-md5:	d39e731444cd310c67206eb2875a0b67
Source48:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-uk-%{version}.tar.bz2
# Source48-md5:	d5893cc238e1a6d5e1a80a9a2a31dee2
Source49:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-zh_CN-%{version}.tar.bz2
# Source49-md5:	68d7901893e8154a9beec0cb87207013
Patch0:		%{name}-pt_BR-fixes.patch
%if %{with alltogether}
# NOTE: "Affrikaans", "Norwegian_Bookmal" and "Portugnese" are here
# intentionally, to allow upgrade from packages with misspelled names
Obsoletes:	kde-i18n-Affrikaans
Obsoletes:	kde-i18n-Afrikaans
Obsoletes:	kde-i18n-Arabic
Obsoletes:	kde-i18n-Azerbaijani
Obsoletes:	kde-i18n-Bengali
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
Obsoletes:	kde-i18n-Hindi
Obsoletes:	kde-i18n-Croatian
Obsoletes:	kde-i18n-Hungarian
Obsoletes:	kde-i18n-Indonesian
Obsoletes:	kde-i18n-Icelandic
Obsoletes:	kde-i18n-Italian
Obsoletes:	kde-i18n-Japanese
Obsoletes:	kde-i18n-Korean
Obsoletes:	kde-i18n-Lithuanian
Obsoletes:	kde-i18n-Latvian
Obsoletes:	kde-i18n-Maltese
Obsoletes:	kde-i18n-Malay
Obsoletes:	kde-i18n-Mongolian
Obsoletes:	kde-i18n-Low_Saxon
Obsoletes:	kde-i18n-Dutch
Obsoletes:	kde-i18n-Norwegian
Obsoletes:	kde-i18n-Norwegian_Bokmaal
Obsoletes:	kde-i18n-Norwegian_Bookmal
Obsoletes:	kde-i18n-Norwegian_Nynorsk
Obsoletes:	kde-i18n-Punjabi
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
Obsoletes:	kde-i18n-Tajik
Obsoletes:	kde-i18n-Tamil
Obsoletes:	kde-i18n-Thai
Obsoletes:	kde-i18n-Turkish
Obsoletes:	kde-i18n-Ukrainian
Obsoletes:	kde-i18n-Uzbek
Obsoletes:	kde-i18n-Venda
Obsoletes:	kde-i18n-Vietnamese
Obsoletes:	kde-i18n-Xhosa
Obsoletes:	kde-i18n-Simplified_Chinese
Obsoletes:	kde-i18n-Chinese
Obsoletes:	kde-i18n-Chinese-Big5
Obsoletes:	kde-i18n-Zulu
Requires:	kde-i18n-base
%endif
BuildRequires:	gettext-devel
# It creates symlinks to some not-translated files.
###BuildRequires:	unsermake >= 040511
BuildRequires:	kdelibs-devel >= 9:%{version}
BuildRequires:	libxml2-progs >= 2.4.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
K Desktop Environment - international support.

%description -l pl
KDE - wsparcie dla wielu j�zyk�w.

%package base
Summary:	Empty metapackage to handle obsoletes
Summary(pl):	Pusty metapakiet z obsoletes
Group:		X11/Applications
Obsoletes:	kdeaccessibility-i18n
Obsoletes:	kdeaccessibility-kmag-i18n
Obsoletes:	kdeaccessibility-kmousetool-i18n
Obsoletes:	kdeaccessibility-kmouth-i18n
Obsoletes:	kdeaddons-i18n
Obsoletes:	kdeaddons-kate-i18n
Obsoletes:	kdeaddons-kicker-i18n
Obsoletes:	kdeaddons-konqueror-i18n
Obsoletes:	kdeaddons-atlantikdesigner-i18n
Obsoletes:	kdeaddons-kontact-i18n
Obsoletes:	kdeaddons-ksig-i18n
Obsoletes:	kdeaddons-kaddressbook-i18n
Obsoletes:	kdeaddons-fsview-i18n
Obsoletes:	kdeaddons-noatun-i18n
Obsoletes:	kdeaddons-kvim-i18n
Obsoletes:	kdeadmin-i18n
Obsoletes:	kdeadmin-kcron-i18n
Obsoletes:	kdeadmin-kdat-i18n
Obsoletes:	kdeadmin-kpackage-i18n
Obsoletes:	kdeadmin-ksysv-i18n
Obsoletes:	kdeadmin-kuser-i18n
Obsoletes:	kdeadmin-kcmlinuz-i18n
Obsoletes:	kdeadmin-kcmlilo-i18n
Obsoletes:	kdeartwork-i18n
Obsoletes:	kde-decoration-cde-i18n
Obsoletes:	kde-decoration-icewm-i18n
Obsoletes:	kde-decoration-glow-i18n
Obsoletes:	kde-decoration-plastik-i18n
Obsoletes:	kde-style-plastik-i18n
Obsoletes:	kdeartwork-screensavers-i18n
Obsoletes:	kdebase-desktop-i18n
Obsoletes:	kdebase-infocenter-i18n
Obsoletes:	kdebase-kate-i18n
Obsoletes:	kdebase-kfind-i18n
Obsoletes:	kdebase-kfontinst-i18n
Obsoletes:	kdebase-kicker-i18n
Obsoletes:	kdebase-klipper-i18n
Obsoletes:	kdebase-kmenuedit-i18n
Obsoletes:	kdebase-konsole-i18n
Obsoletes:	kdebase-kpager-i18n
Obsoletes:	kdebase-ksysguard-i18n
Obsoletes:	kdebase-kwrite-i18n
Obsoletes:	kdebase-screensavers-i18n
Obsoletes:	kdm-i18n
Obsoletes:	konqueror-i18n
Obsoletes:	kdebase-core-i18n
Obsoletes:	kdebase-i18n
Obsoletes:	kde-decoration-b2-i18n
Obsoletes:	kde-decoration-modernsys-i18n
Obsoletes:	kde-decoration-quartz-i18n
Obsoletes:	common-filemanagement-i18n
Obsoletes:	kdebase-common-filemanagement-i18n
Obsoletes:	kdebase-desktop-libs-i18n
Obsoletes:	kdebase-kappfinder-i18n
Obsoletes:	kdebase-kdcop-i18n
Obsoletes:	kdebase-kdeprintfax-i18n
Obsoletes:	kdebase-kdialog-i18n
Obsoletes:	kdebase-kicker-libs-i18n
Obsoletes:	kdebase-kjobviewer-i18n
Obsoletes:	kdebase-kpersonalizer-i18n
Obsoletes:	kdebase-ksystraycmd-i18n
Obsoletes:	kdebase-libkonq-i18n
Obsoletes:	konqueror-libs-i18n
Obsoletes:	kdebase-mailnews-i18n
Obsoletes:	kdeedu-i18n
Obsoletes:	kdeedu-flashkard-i18n
Obsoletes:	kdeedu-kalzium-i18n
Obsoletes:	kdeedu-kbruch-i18n
Obsoletes:	kdeedu-keduca-i18n
Obsoletes:	kdeedu-khangman-i18n
Obsoletes:	kdeedu-kig-i18n
Obsoletes:	kdeedu-kiten-i18n
Obsoletes:	kdeedu-klettres-i18n
Obsoletes:	kdeedu-kmessedwords-i18n
Obsoletes:	kdeedu-kmplot-i18n
Obsoletes:	kdeedu-kpercentage-i18n
Obsoletes:	kdeedu-kstars-i18n
Obsoletes:	kdeedu-ktouch-i18n
Obsoletes:	kdeedu-kverbos-i18n
Obsoletes:	kdeedu-kvoctrain-i18n
Obsoletes:	kdegames-ksmiletris-i18n
Obsoletes:	kdegames-kmahjongg-i18n
Obsoletes:	kdegames-i18n
Obsoletes:	kdegames-atlantik-i18n
Obsoletes:	kdegames-kasteroids-i18n
Obsoletes:	kdegames-katomic-i18n
Obsoletes:	kdegames-kbackgammon-i18n
Obsoletes:	kdegames-kbattleship-i18n
Obsoletes:	kdegames-kblackbox-i18n
Obsoletes:	kdegames-kbounce-i18n
Obsoletes:	kdegames-kenolaba-i18n
Obsoletes:	kdegames-kfouleggs-i18n
Obsoletes:	kdegames-kgoldrunner-i18n
Obsoletes:	kdegames-kjumpingcube-i18n
Obsoletes:	kdegames-klickety-i18n
Obsoletes:	kdegames-klines-i18n
Obsoletes:	kdegames-kmines-i18n
Obsoletes:	kdegames-kolf-i18n
Obsoletes:	kdegames-konquest-i18n
Obsoletes:	kdegames-kpat-i18n
Obsoletes:	kdegames-kpoker-i18n
Obsoletes:	kdegames-kreversi-i18n
Obsoletes:	kdegames-ksame-i18n
Obsoletes:	kdegames-kshisen-i18n
Obsoletes:	kdegames-ksirtet-i18n
Obsoletes:	kdegames-ksnake-i18n
Obsoletes:	kdegames-ksokoban-i18n
Obsoletes:	kdegames-kspaceduel-i18n
Obsoletes:	kdegames-ktron-i18n
Obsoletes:	kdegames-ktuberling-i18n
Obsoletes:	kdegames-kwin4-i18n
Obsoletes:	kdegames-lskat-i18n
Obsoletes:	kdegames-megami-i18n
Obsoletes:	kdegraphics-i18n
Obsoletes:	kdegraphics-kamera-i18n
Obsoletes:	kdegraphics-kcoloredit-i18n
Obsoletes:	kdegraphics-kdvi-i18n
Obsoletes:	kdegraphics-kgamma-i18n
Obsoletes:	kdegraphics-kghostview-i18n
Obsoletes:	kdegraphics-kiconedit-i18n
Obsoletes:	kdegraphics-kooka-i18n
Obsoletes:	kdegraphics-kpaint-i18n
Obsoletes:	kdegraphics-kpdf-i18n
Obsoletes:	kdegraphics-kpovmodeler-i18n
Obsoletes:	kdegraphics-kruler-i18n
Obsoletes:	kdegraphics-ksnapshot-i18n
Obsoletes:	kdegraphics-kuickshow-i18n
Obsoletes:	kdegraphics-kview-i18n
Obsoletes:	kdegraphics-kfile-i18n
Obsoletes:	kdegraphics-kmrml-i18n
Obsoletes:	kdegraphics-ksvg-i18n
Obsoletes:	kdegraphics-kfax-i18n
Obsoletes:	kdemultimedia-i18n
Obsoletes:	kdemultimedia-artsbuilder-i18n
Obsoletes:	kdemultimedia-artscontrol-i18n
Obsoletes:	kdemultimedia-arts-i18n
Obsoletes:	kdemultimedia-juk-i18n
Obsoletes:	kdemultimedia-kaboodle-i18n
Obsoletes:	kdemultimedia-kmid-i18n
Obsoletes:	kdemultimedia-kmix-i18n
Obsoletes:	kdemultimedia-kscd-i18n
Obsoletes:	kdemultimedia-krec-i18n
Obsoletes:	kdemultimedia-noatun-i18n
Obsoletes:	kdemultimedia-kfile-i18n
Obsoletes:	kdemultimedia-audiocd-i18n
Obsoletes:	kdemultimedia-kaudiocreator-i18n
Obsoletes:	kdemultimedia-libkcddb-i18n
Obsoletes:	kdenetwork-i18n
Obsoletes:	kdenetwork-kdict-i18n
Obsoletes:	kdenetwork-kget-i18n
Obsoletes:	kdenetwork-knewsticker-i18n
Obsoletes:	kdenetwork-kopete-i18n
Obsoletes:	kdenetwork-kpf-i18n
Obsoletes:	kdenetwork-kppp-i18n
Obsoletes:	kdenetwork-krfb-i18n
Obsoletes:	kdenetwork-ksirc-i18n
Obsoletes:	kdenetwork-ktalkd-i18n
Obsoletes:	kdenetwork-kwifimanager-i18n
Obsoletes:	kdenetwork-lanbrowser-i18n
Obsoletes:	kdenetwork-kinetd-i18n
Obsoletes:	kdenetwork-rss-i18n
Obsoletes:	kdepim-i18n
Obsoletes:	kdepim-kaddressbook-i18n
Obsoletes:	kdepim-kandy-i18n
Obsoletes:	kdepim-karm-i18n
Obsoletes:	kdepim-kmail-i18n
Obsoletes:	kdepim-knode-i18n
Obsoletes:	kdepim-knotes-i18n
Obsoletes:	kdepim-konsolekalendar-i18n
Obsoletes:	kdepim-kontact-i18n
Obsoletes:	kdepim-korganizer-i18n
Obsoletes:	kdepim-korn-i18n
Obsoletes:	kdepim-kpilot-i18n
Obsoletes:	kdepim-libkdepim-i18n
Obsoletes:	kdepim-libkdenetwork-i18n
Obsoletes:	kdepim-libksieve-i18n
Obsoletes:	kdepim-korganizer-libs-i18n
Obsoletes:	kdepim-libkcal-i18n
Obsoletes:	kdepim-ktnef-i18n
Obsoletes:	kdepim-kgantt-i18n
Obsoletes:	kdesdk-i18n
Obsoletes:	kdesdk-kfile-i18n
Obsoletes:	kdesdk-cervisia-i18n
Obsoletes:	kdesdk-kbabel-i18n
Obsoletes:	kdesdk-kbugbuster-i18n
Obsoletes:	kdesdk-kcachegrind-i18n
Obsoletes:	kdesdk-kompare-i18n
Obsoletes:	kdesdk-kfilereplace-i18n
Obsoletes:	kdesdk-kstartperf-i18n
Obsoletes:	kdesdk-kuiviewer-i18n
Obsoletes:	kdesdk-spy-i18n
Obsoletes:	kdesdk-kspy-i18n
Obsoletes:	kdesdk-umbrello-i18n
Obsoletes:	kdetoys-i18n
Obsoletes:	kdetoys-amor-i18n
Obsoletes:	kdetoys-kmoon-i18n
Obsoletes:	kdetoys-kodo-i18n
Obsoletes:	kdetoys-kteatime-i18n
Obsoletes:	kdetoys-kweather-i18n
Obsoletes:	kdetoys-kworldclock-i18n
Obsoletes:	kdetoys-fifteen-i18n
Obsoletes:	kdetoys-ktux-i18n
Obsoletes:	kdeutils-i18n
Obsoletes:	kdeutils-ark-i18n
Obsoletes:	kdeutils-kcalc-i18n
Obsoletes:	kdeutils-kcharselect-i18n
Obsoletes:	kdeutils-kdf-i18n
Obsoletes:	kdeutils-kedit-i18n
Obsoletes:	kdeutils-kfloppy-i18n
Obsoletes:	kdeutils-kgpg-i18n
Obsoletes:	kdeutils-khexedit-i18n
Obsoletes:	kdeutils-kjots-i18n
Obsoletes:	kdeutils-klaptopdaemon-i18n
Obsoletes:	kdeutils-kregexpeditor-i18n
Obsoletes:	kdeutils-ksim-i18n
Obsoletes:	kdeutils-ktimer-i18n
Obsoletes:	kdeutils-kwalletmanager-i18n
Obsoletes:	kdeutils-kdelirc-i18n
Obsoletes:	kdeutils-userinfo-i18n
Obsoletes:	kdeutils-kdessh-i18n
Obsoletes:	kdeutils-kdepasswd-i18n
Obsoletes:	kdevelop-i18n
Obsoletes:	quanta-i18n
Obsoletes:	kdepim-kmail-libs-i18n
Obsoletes:	kdeutils-kmilo-i18n
Obsoletes:	kde-i18n-kdelibs
Obsoletes:	kdelibs-i18n
Obsoletes:	kde-kgreet-classic-i18n
Obsoletes:	kde-kio-smtp-i18n
Obsoletes:	kde-kio-nntp-i18n
Obsoletes:	kde-kio-imap4-i18n
Obsoletes:	kde-kio-pop3-i18n
Obsoletes:	kdeaddons-ark-i18n
Obsoletes:	kdeaddons-lnkforward-i18n
Obsoletes:	kdebase-useraccount-i18n
Obsoletes:	kde-decoration-kde1-i18n
Obsoletes:	kde-decoration-kstep-i18n
Obsoletes:	kde-decoration-openlook-i18n
Obsoletes:	kde-decoration-riscos-i18n
Obsoletes:	kde-decoration-system-i18n
Obsoletes:	kde-decoration-common-i18n
Obsoletes:	kdeedu-klatin-i18n
Obsoletes:	kdeedu-kturtle-i18n
Obsoletes:	kdeedu-kwordquiz-i18n
Obsoletes:	kdegraphics-kolourpaint-i18n
Obsoletes:	kde-kio-ldap-i18n
Obsoletes:	kde-kio-newimap4-i18n
Obsoletes:	kdenetwork-filesharing-i18n
Obsoletes:	kdepim-i18n
Obsoletes:	kdepim-libs-i18n
Obsoletes:	kdesdk-libcvsservice-i18n
Obsoletes:	kdewebdev-kfilereplace-i18n
Obsoletes:	kdewebdev-kimagemapeditor-i18n
Obsoletes:	kdewebdev-klinkstatus-i18n
Obsoletes:	kdewebdev-kommander-i18n
Obsoletes:	kdewebdev-kxsldbg-i18n
Obsoletes:	kdewebdev-quanta-i18n

%description base
Empty metapackage to handle obsoletes for individual i18n subpackages.

%description base -l pl
Pusty metapakiet z Obsoletes dla oddzielnych podpakiet�w i18n.

%package Afrikaans
Summary:	K Desktop Environment - Afrikaans language support
Summary(pl):	KDE - wsparcie dla j�zyka afrykanerskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
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
Requires:	%{name}-base = %{version}-%{release}

%description Arabic
K Desktop Environment - Arabic language support.

%description Arabic -l pl
KDE - wsparcie dla j�zyka arabskiego.

%package Azerbaijani
Summary:	K Desktop Environment - Azerbaijani language support
Summary(pl):	KDE - wsparcie dla j�zyka azerskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Azerbaijani
K Desktop Environment - Azerbaijani language support.

%description Azerbaijani -l pl
KDE - wsparcie dla j�zyka azerskiego.

%package Bulgarian
Summary:	K Desktop Environment - Bulgarian language support
Summary(pl):	KDE - wsparcie dla j�zyka bu�garskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Bulgarian
K Desktop Environment - Bulgarian language support.

%description Bulgarian -l pl
KDE - wsparcie dla j�zyka bu�garskiego.

%package Bengali
Summary:	K Desktop Environment - Bengali language support
Summary(pl):	KDE - wsparcie dla j�zyka bengalskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Bengali
K Desktop Environment - Bengali language support.

%description Bengali -l pl
KDE - wsparcie dla j�zyka bengalskiego.

%package Breton
Summary:	K Desktop Environment - Breton language support
Summary(pl):	KDE - wsparcie dla j�zyka breto�skiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Breton
K Desktop Environment - Breton language support.

%description Breton -l pl
KDE - wsparcie dla j�zyka breto�skiego.

%package Bosnian
Summary:	K Desktop Environment - Bosnian language support
Summary(pl):	KDE - wsparcie dla j�zyka bo�niackiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Bosnian
K Desktop Environment - Bosnian language support.

%description Bosnian -l pl
KDE - wsparcie dla j�zyka bo�niackiego.

%package Catalan
Summary:	K Desktop Environment - Catalan language support
Summary(pl):	KDE - wsparcie dla j�zyka katalo�skiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Catalan
K Desktop Environment - Catalan language support.

%description Catalan -l pl
KDE - wsparcie dla j�zyka katalo�skiego.

%package Czech
Summary:	K Desktop Environment - Czech language support
Summary(pl):	KDE - wsparcie dla j�zyka czeskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Czech
K Desktop Environment - Czech language support.

%description Czech -l pl
KDE - wsparcie dla j�zyka czeskiego.

%package Cymraeg
Summary:	K Desktop Environment - Cymraeg language support
Summary(pl):	KDE - wsparcie dla j�zyka walijskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Cymraeg
K Desktop Environment - Cymraeg language support.

%description Cymraeg -l pl
KDE - wsparcie dla j�zyka walijskiego.

%package Danish
Summary:	K Desktop Environment - Danish language support
Summary(pl):	KDE - wsparcie dla j�zyka du�skiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Danish
K Desktop Environment - Danish language support.

%description Danish -l pl
KDE - wsparcie dla j�zyka du�skiego.

%package German
Summary:	K Desktop Environment - German language support
Summary(pl):	KDE - wsparcie dla j�zyka niemieckiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description German
K Desktop Environment - German language support.

%description German -l pl
KDE - wsparcie dla j�zyka niemieckiego.

%package Greek
Summary:	K Desktop Environment - Greek language support
Summary(pl):	KDE - wsparcie dla j�zyka greckiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Greek
K Desktop Environment - Greek language support.

%description Greek -l pl
KDE - wsparcie dla j�zyka greckiego.

%package English
Summary:	K Desktop Environment - English language support
Summary(pl):	KDE - wsparcie dla j�zyka angielskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description English
K Desktop Environment - English language support.

%description English -l pl
KDE - wsparcie dla j�zyka angielskiego.

%package English_UK
Summary:	K Desktop Environment - K Desktop Environment - English (UK) language support
Summary(pl):	KDE - wsparcie dla j�zyka angielskiego (odmiany brytyjskiej)
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description English_UK
K Desktop Environment - English (UK) language support.

%description English_UK -l pl
KDE - wsparcie dla j�zyka angielskiego (odmiany brytyjskiej).

%package Esperanto
Summary:	K Desktop Environment - Esperanto language support
Summary(pl):	KDE - wsparcie dla j�zyka esperanto
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Esperanto
K Desktop Environment - Esperanto language support.

%description Esperanto -l pl
KDE - wsparcie dla j�zyka esperanto.

%package Spanish
Summary:	K Desktop Environment - Spanish language support
Summary(pl):	KDE - wsparcie dla j�zyka hiszpa�skiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Spanish
K Desktop Environment - Spanish language support.

%description Spanish -l pl
KDE - wsparcie dla j�zyka hiszpa�skiego.

%package Estonian
Summary:	K Desktop Environment - Estonian language support
Summary(pl):	KDE - wsparcie dla j�zyka esto�skiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Estonian
K Desktop Environment - Estonian language support.

%description Estonian -l pl
KDE - wsparcie dla j�zyka esto�skiego.

%package Basque
Summary:	K Desktop Environment - Basque language support
Summary(pl):	KDE - wsparcie dla j�zyka baskijskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Basque
K Desktop Environment - Basque language support.

%description Basque -l pl
KDE - wsparcie dla j�zyka baskijskiego.

%package Farsi
Summary:	K Desktop Environment - Farsi language support
Summary(pl):	KDE - wsparcie dla j�zyka perskiego (farsi)
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Farsi
K Desktop Environment - Farsi language support.

%description Farsi -l pl
KDE - wsparcie dla j�zyka perskiego (farsi).

%package Finnish
Summary:	K Desktop Environment - Finnish language support
Summary(pl):	KDE - wsparcie dla j�zyka fi�skiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Finnish
K Desktop Environment - Finnish language support.

%description Finnish -l pl
KDE - wsparcie dla j�zyka fi�skiego.

%package French
Summary:	K Desktop Environment - French language support
Summary(pl):	KDE - wsparcie dla j�zyka francuskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description French
K Desktop Environment - French language support.

%description French -l pl
KDE - wsparcie dla j�zyka francuskiego.

%package Frisian
Summary:	K Desktop Environment - Frisian language support
Summary(pl):	KDE - wsparcie dla j�zyka Frisian
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Frisian
K Desktop Environment - Frisian language support.

%description Frisian -l pl
KDE - wsparcie dla j�zyka Frisian.

%package Irish
Summary:	K Desktop Environment - Irish language support
Summary(pl):	KDE - wsparcie dla j�zyka irlandzkiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Irish
K Desktop Environment - Irish language support.

%description Irish -l pl
KDE - wsparcie dla j�zyka irlandzkiego.

%package Galician
Summary:	K Desktop Environment - Galician language support
Summary(pl):	KDE - wsparcie dla j�zyka galicyjskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Galician
K Desktop Environment - Galician language support.

%description Galician -l pl
KDE - wsparcie dla j�zyka galicyjskiego.

%package Hindi
Summary:	K Desktop Environment - Hindi language support
Summary(pl):	KDE - wsparcie dla j�zyka hindi
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Hindi
K Desktop Environment - Hindi language support.

%description Hindi -l pl
KDE - wsparcie dla j�zyka hindi.

%package Hebrew
Summary:	K Desktop Environment - Hebrew language support
Summary(pl):	KDE - wsparcie dla j�zyka hebrajskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Hebrew
K Desktop Environment - Hebrew language support.

%description Hebrew -l pl
KDE - wsparcie dla j�zyka hebrajskiego.

%package Croatian
Summary:	K Desktop Environment - Croatian language support
Summary(pl):	KDE - wsparcie dla j�zyka chorwackiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Croatian
K Desktop Environment - Croatian language support.

%description Croatian -l pl
KDE - wsparcie dla j�zyka chorwackiego.

%package Upper_Sorbian
Summary:	K Desktop Environment - Upper Sorbian language support
Summary(pl):	KDE - wsparcie dla j�zyka g�rno�u�yckiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Upper_Sorbian
K Desktop Environment - Upper Sorbian language support.

%description Upper_Sorbian  -l pl
KDE - wsparcie dla j�zyka g�rno�u�yckiego.

%package Hungarian
Summary:	K Desktop Environment - Hungarian language support
Summary(pl):	KDE - wsparcie dla j�zyka w�gierskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Hungarian
K Desktop Environment - Hungarian language support.

%description Hungarian -l pl
KDE - wsparcie dla j�zyka w�gierskiego.

%package Indonesian
Summary:	K Desktop Environment - Indonesian language support
Summary(pl):	KDE - wsparcie dla j�zyka indonezyjskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Indonesian
K Desktop Environment - Indonesian language support.

%description Indonesian -l pl
KDE - wsparcie dla j�zyka indonezyjskiego.

%package Icelandic
Summary:	K Desktop Environment - Icelandic language support
Summary(pl):	KDE - wsparcie dla j�zyka islandzkiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Icelandic
K Desktop Environment - Icelandic language support.

%description Icelandic -l pl
KDE - wsparcie dla j�zyka islandzkiego.

%package Italian
Summary:	K Desktop Environment - Italian language support
Summary(pl):	KDE - wsparcie dla j�zyka w�oskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Italian
K Desktop Environment - Italian language support.

%description Italian -l pl
KDE - wsparcie dla j�zyka w�oskiego.

%package Japanese
Summary:	K Desktop Environment - Japanese language support
Summary(pl):	KDE - wsparcie dla j�zyka japo�skiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Japanese
K Desktop Environment - Japanese language support.

%description Japanese -l pl
KDE - wsparcie dla j�zyka japo�skiego.

%package Korean
Summary:	K Desktop Environment - Korean language support
Summary(pl):	KDE - wsparcie dla j�zyka korea�skiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Korean
K Desktop Environment - Korean language support.

%description Korean -l pl
KDE - wsparcie dla j�zyka korea�skiego.

%package Lithuanian
Summary:	K Desktop Environment - Lithuanian language support
Summary(pl):	KDE - wsparcie dla j�zyka litewskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Lithuanian
K Desktop Environment - Lithuanian language support.

%description Lithuanian -l pl
KDE - Wsparcie dla j�zyka litewskiego.

%package Lao
Summary:	K Desktop Environment - Lao language support
Summary(pl):	KDE - wsparcie dla j�zyka laota�skiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Lao
K Desktop Environment - lao language support.

%description Lao -l pl
KDE - wsparcie dla j�zyka laota�skiego.

%package Latvian
Summary:	K Desktop Environment - Latvian language support
Summary(pl):	KDE - wsparcie dla j�zyka �otewskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Latvian
K Desktop Environment - Latvian language support.

%description Latvian -l pl
KDE - wsparcie dla j�zyka �otewskiego.

%package Maori
Summary:	K Desktop Environment - Maori language support
Summary(pl):	KDE - wsparcie dla j�zyka maoryjskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Maori
K Desktop Environment - Maori language support.

%description Maori -l pl
KDE - wsparcie dla j�zyka maoryjskiego.

%package Macedonian
Summary:	K Desktop Environment - Macedonian language support
Summary(pl):	KDE - wsparcie dla j�zyka macedo�skiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Macedonian
K Desktop Environment - Macedonian language support.

%description Macedonian -l pl
KDE - wsparcie dla j�zyka macedo�skiego.

%package Malay
Summary:	K Desktop Environment - Malay language support
Summary(pl):	KDE - wsparcie dla j�zyka malajskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Malay
K Desktop Environment - Malay language support.

%description Malay -l pl
KDE - wsparcie dla j�zyka malajskiego.

%package Maltese
Summary:	K Desktop Environment - Maltese language support
Summary(pl):	KDE - wsparcie dla j�zyka malta�skiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Maltese
K Desktop Environment - Maltese language support.

%description Maltese -l pl
KDE - wsparcie dla j�zyka malta�skiego.

%package Mongolian
Summary:	K Desktop Environment - Mongolian language support
Summary(pl):	KDE - wsparcie dla j�zyka mongolskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Mongolian
K Desktop Environment - Mongolian language support.

%description Mongolian -l pl
KDE - wsparcie dla j�zyka mongolskiego.

%package Low_Saxon
Summary:	K Desktop Environment - Low_Saxon language support
Summary(pl):	KDE - wsparcie dla j�zyka dolnosakso�skiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Low_Saxon
K Desktop Environment - Low_Saxon language support.

%description Low_Saxon -l pl
KDE - wsparcie dla j�zyka dolnosakso�skiego.

%package Dutch
Summary:	K Desktop Environment - Dutch language support
Summary(pl):	KDE - wsparcie dla j�zyka holenderskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Dutch
K Desktop Environment - Dutch language support.

%description Dutch -l pl
KDE - wsparcie dla j�zyka holenderskiego.

%package Norwegian_Bokmaal
Summary:	K Desktop Environment - Norwegian (Bokmaal) language support
Summary(pl):	KDE - wsparcie dla j�zyka norweskiego (odmiany bokmaal)
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
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
Requires:	%{name}-base = %{version}-%{release}

%description Norwegian_Nynorsk
K Desktop Environment - Norwegian (Nynorsk) language support.

%description Norwegian_Nynorsk -l pl
KDE - wsparcie dla j�zyka norweskiego (odmiany nynorsk).

%package Northern_Sotho
Summary:	K Desktop Environment - Northern Sotho language support
Summary(pl):	KDE - wsparcie dla p�nocnej odmiany j�zyka ludu Soto
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Northern_Sotho
K Desktop Environment - Northern Sotho language support.

%description Northern_Sotho -l pl
KDE - wsparcie dla p�nocnej odmiany j�zyka ludu Soto.

%package Gascon_occitan
Summary:	K Desktop Environment - Occitan (Gascon) language support
Summary(pl):	KDE - wsparcie dla j�zyka oksyta�skiego (dialektu gasko�skiego)
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Gascon_occitan
K Desktop Environment - Occitan (Gascon) language support.

%description Gascon_occitan -l pl
KDE - wsparcie dla j�zyka oksyta�skiego (dialektu gasko�skiego).

%package Punjabi
Summary:	K Desktop Environment - Punjabi language support
Summary(pl):	KDE - wsparcie dla j�zyka pend�abskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Punjabi
K Desktop Environment - Punjabi language support.

%description Punjabi -l pl
KDE - wsparcie dla j�zyka pend�abskiego.

%package Polish
Summary:	K Desktop Environment - Polish language support
Summary(pl):	KDE - wsparcie dla j�zyka polskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Polish
K Desktop Environment - Polish language support.

%description Polish -l pl
KDE - wsparcie dla j�zyka polskiego.

%package Portuguese
Summary:	K Desktop Environment - Portuguese language support
Summary(pl):	KDE - wsparcie dla j�zyka portugalskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
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
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	%{name}-Brazil_Protugnese

%description Brazil_Portuguese
K Desktop Environment - Portuguese (Brazil) language support.

%description Brazil_Portuguese -l pl
KDE - wsparcie dla j�zyka portugalskiego (odmiany brazylijskiej).

%package Romanian
Summary:	K Desktop Environment - Romanian language support
Summary(pl):	KDE - wsparcie dla j�zyka rumu�skiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Romanian
K Desktop Environment - Romanian language support.

%description Romanian -l pl
KDE - wsparcie dla j�zyka rumu�skiego.

%package Russian
Summary:	K Desktop Environment - Russian language support
Summary(pl):	KDE - wsparcie dla j�zyka rosyjskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Russian
K Desktop Environment - Russian language support.

%description Russian -l pl
KDE - wsparcie dla j�zyka rosyjskiego.

%package Swati
Summary:	K Desktop Environment - Swati language support
Summary(pl):	KDE - wsparcie dla j�zyka swati
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Swati
K Desktop Environment - Swati language support.

%description Swati -l pl
KDE - wsparcie dla j�zyka swati.

%package Northern_Sami
Summary:	K Desktop Environment - Northern Sami language support
Summary(pl):	KDE - wsparcie dla p�nocnego j�zyka saami (lapo�skiego)
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Northern_Sami
K Desktop Environment - Northern Sami language support.

%description Northern_Sami -l pl
KDE - wsparcie dla p�nocnego j�zyka saami (lapo�skiego).

%package Slovak
Summary:	K Desktop Environment - Slovak language support
Summary(pl):	KDE - wsparcie dla j�zyka s�owackiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Slovak
K Desktop Environment - Slovak language support.

%description Slovak -l pl
KDE - wsparcie dla j�zyka s�owackiego.

%package Slovenian
Summary:	K Desktop Environment - Slovenian language support
Summary(pl):	KDE - wsparcie dla j�zyka s�owe�skiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Slovenian
K Desktop Environment - Slovenian language support.

%description Slovenian -l pl
KDE - wsparcie dla j�zyka s�owe�skiego.

%package Serbian
Summary:	K Desktop Environment - Serbian language support
Summary(pl):	KDE - wsparcie dla j�zyka serbskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Serbian
K Desktop Environment - Serbian language support.

%description Serbian -l pl
KDE - wsparcie dla j�zyka serbskiego.

%package Swedish
Summary:	K Desktop Environment - Swedish language support
Summary(pl):	KDE - wsparcie dla j�zyka szwedzkiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Swedish
K Desktop Environment - Swedish language support.

%description Swedish -l pl
KDE - wsparcie dla j�zyka szwedzkiego.

%package Tajik
Summary:	K Desktop Environment - Tajik language support
Summary(pl):	KDE - wsparcie dla j�zyka tad�yckiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Tajik
K Desktop Environment - Tajik language support.

%description Tajik -l pl
KDE - wsparcie dla j�zyka tad�yckiego.

%package Tamil
Summary:	K Desktop Environment - Tamil language support
Summary(pl):	KDE - wsparcie dla j�zyka tamilskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Tamil
K Desktop Environment - Tamil language support.

%description Tamil -l pl
KDE - wsparcie dla j�zyka tamilskiego.

%package Thai
Summary:	K Desktop Environment - Thai language support
Summary(pl):	KDE - wsparcie dla j�zyka tajlandzkiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Thai
K Desktop Environment - Thai language support.

%description Thai -l pl
KDE - wsparcie dla j�zyka tajlandzkiego.

%package Turkish
Summary:	K Desktop Environment - Turkish language support
Summary(pl):	KDE - wsparcie dla j�zyka tureckiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Turkish
K Desktop Environment - Turkish language support.

%description Turkish -l pl
KDE - wsparcie dla j�zyka tureckiego.

%package Ukrainian
Summary:	K Desktop Environment - Ukrainian language support
Summary(pl):	KDE - wsparcie dla j�zyka ukrai�skiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Ukrainian
K Desktop Environment - Ukrainian language support.

%description Ukrainian -l pl
KDE - wsparcie dla j�zyka ukrai�skiego.

%package Uzbek
Summary:	K Desktop Environment - Uzbek language support
Summary(pl):	KDE - wsparcie dla j�zyka uzbeckiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Uzbek
K Desktop Environment - Uzbek language support.

%description Uzbek -l pl
KDE - wsparcie dla j�zyka uzbeckiego.


%package Venda
Summary:	K Desktop Environment - Venda language support
Summary(pl):	KDE - wsparcie dla j�zyka venda
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Venda
K Desktop Environment - Venda language support.

%description Venda -l pl
KDE - wsparcie dla j�zyka venda.

%package Vietnamese
Summary:	K Desktop Environment - Vietnamese language support
Summary(pl):	KDE - wsparcie dla j�zyka wietnamskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Vietnamese
K Desktop Environment - Vietnamese language support.

%description Vietnamese -l pl
KDE - wsparcie dla j�zyka wietnamskiego.

%package Walloon
Summary:	K Desktop Environment - Walloon language support
Summary(pl):	KDE - wsparcie dla j�zyka walo�skiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Walloon
K Desktop Environment - Walloon language support.

%description Walloon -l pl
KDE - wsparcie dla j�zyka walo�skiego.

%package Xhosa
Summary:	K Desktop Environment - Xhosa language support
Summary(pl):	KDE - wsparcie dla j�zyka khosa
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Xhosa
K Desktop Environment - Xhosa language support.

%description Xhosa -l pl
KDE - wsparcie dla j�zyka khosa.

%package Simplified_Chinese
Summary:	K Desktop Environment - simplified Chinese language support
Summary(pl):	KDE - wsparcie dla uproszczonego j�zyka chi�skiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Simplified_Chinese
K Desktop Environment - simplified Chinese language support.

%description Simplified_Chinese -l pl
KDE - wsparcie dla uproszczonego j�zyka chi�skiego.

%package Chinese
Summary:	K Desktop Environment - Chinese language support
Summary(pl):	KDE - wsparcie dla j�zyka chi�skiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Chinese
K Desktop Environment - Chinese language support.

%description Chinese -l pl
KDE - wsparcie dla j�zyka chi�skiego.

%package Zulu
Summary:	K Desktop Environment - Zulu language support
Summary(pl):	KDE - wsparcie dla j�zyka zuluskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Zulu
K Desktop Environment - Zulu language support.

%description Zulu -l pl
KDE - wsparcie dla j�zyka zuluskiego.

%prep
%setup -q -c -T -a0 -a1 -a2 -a3 -a4 -a5 -a6 -a7 -a8 -a9 -a10 -a11 -a12 -a13 -a14 -a15 -a16 -a17 -a18 -a19 -a20 -a21 -a22 -a23 -a24 -a25 -a26 -a27 -a28 -a29 -a30 -a31 -a32 -a33 -a34 -a35 -a36 -a37 -a38 -a39 -a40 -a41 -a42 -a43 -a44 -a45 -a45 -a47 -a48 -a49
cd kde-i18n-pt_BR-*
%patch0 -p1
cd ..

%build
kde_htmldir="%{_kdedocdir}"; export kde_htmldir
kde_libs_htmldir="%{_kdedocdir}"; export kde_libs_htmldir

LDFLAGS="%{rpmldflags}"
#export UNSERMAKE=%{_datadir}/unsermake/unsermake

for dir in kde-i18n-*-%{version}; do
	cd "$dir"

	%configure

	%{__make} \
		RPM_OPT_FLAGS="%{rpmcflags}" \
		kde_htmldir="%{_kdedocdir}" \
		kde_libs_htmldir="%{_kdedocdir}"
	cd ..
done

%install
rm -rf $RPM_BUILD_ROOT


FindLang() {
#    $1 - short language name
#    $2 - long language name

    echo "%defattr(644,root,root,755)" > "$2.lang"

# share/doc/kde/HTML/(%%lang)
    if [ -d "$RPM_BUILD_ROOT%{_kdedocdir}/$1" ]; then
	echo "%lang($1) %{_kdedocdir}/$1" >> "$2.lang"
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

# share/apps/katepart/syntax/logohighlightstyle.(%%lang).xml
    if [ -f "$RPM_BUILD_ROOT%{_datadir}/apps/katepart/syntax/logohighlightstyle.$1.xml" ]; then
        echo "%lang($1) %{_datadir}/apps/katepart/syntax/logohighlightstyle.$1.xml" >> "$2.lang"
    fi

# share/apps/ktuberling/sounds/(%%lang)
    if [ -d "$RPM_BUILD_ROOT%{_datadir}/apps/ktuberling/sounds/$1" ]; then
        echo "%lang($1) %{_datadir}/apps/ktuberling/sounds/$1" >> "$2.lang"
    fi

# share/apps/khangman/(%lang).txt
    if [ -f "$RPM_BUILD_ROOT%{_datadir}/apps/khangman/$1.txt" ]; then
        echo "%lang($1) %{_datadir}/apps/khangman/$1.txt" >> "$2.lang"
    fi

# share/apps/khangman/data/(%lang)
    if [ -d "$RPM_BUILD_ROOT%{_datadir}/apps/khangman/data/$1" ]; then
	echo "%lang($1) %{_datadir}/apps/khangman/data/$1" >> "$2.lang"
    fi

# share/apps/klatin/data/vocabs/(%lang)
    if [ -d "$RPM_BUILD_ROOT%{_datadir}/apps/klatin/data/vocabs/$1" ]; then
        echo "%lang($1) %{_datadir}/apps/klatin/data/vocabs/$1" >> "$2.lang"
    fi

# share/apps/klettres/(%lang)
    if [ -d "$RPM_BUILD_ROOT%{_datadir}/apps/klettres/$1" ]; then
	echo "%lang($1) %{_datadir}/apps/klettres/$1" >> "$2.lang"
    fi

# share/apps/kturtle/data/logokeywords.(%lang).xml
    if [ -f "$RPM_BUILD_ROOT%{_datadir}/apps/kturtle/data/logokeywords.$1.xml" ]; then
        echo "%lang($1) %{_datadir}/apps/kturtle/data/logokeywords.$1.xml" >> "$2.lang"
    fi

# share/apps/kturtle/examples/(%lang)
    if [ -d "$RPM_BUILD_ROOT%{_datadir}/apps/kturtle/examples/$1" ]; then
        echo "%lang($1) %{_datadir}/apps/kturtle/examples/$1" >> "$2.lang"
    fi
}

for dir in kde-i18n-*-%{version}; do
	%{__make} -C "$dir" install \
		DESTDIR=$RPM_BUILD_ROOT \
		kde_htmldir="%{_kdedocdir}" \
		kde_libs_htmldir="%{_kdedocdir}"
done

##FindLang af Afrikaans
FindLang ar Arabic
#FindLang az Azerbaijani
FindLang bg Bulgarian
FindLang bn Bengali
FindLang br Breton
FindLang bs Bosnian
FindLang ca Catalan
FindLang cs Czech
FindLang cy Cymraeg
FindLang da Danish
FindLang de German
FindLang el Greek
# FindLang en English
FindLang en_GB English_UK
FindLang eo Esperanto
FindLang es Spanish
FindLang et Estonian
FindLang eu Basque
FindLang fa Farsi
FindLang fi Finnish
FindLang fr French
FindLang fy Frisian
FindLang ga Irish
#FindLang gl Galician
FindLang he Hebrew
FindLang hi Hindi
FindLang hr Croatian
FindLang hsb Upper_Sorbian
FindLang hu Hungarian
# FindLang id Indonesian
FindLang is Icelandic
FindLang it Italian
FindLang ja Japanese
## FindLang ko Korean
FindLang lt Lithuanian
## FindLang lv Latvian
# FindLang mi Maori
FindLang mk Macedonian
FindLang mn Mongolian
FindLang ms Malay
##FindLang mt Maltese
FindLang nb Norwegian_Bokmaal
FindLang nds Low_Saxon
FindLang nl Dutch
FindLang nn Norwegian_Nynorsk
FindLang pa Punjabi
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
FindLang sr@Latn Serbian_Latin
cat Serbian_Latin.lang >>Serbian.lang
FindLang sv Swedish
FindLang ta Tamil
FindLang tg Tajik
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


%files base
%defattr(644,root,root,755)

%if %{without alltogether}
#%%files -f Afrikaans.lang Afrikaans
%files -f Arabic.lang Arabic
%defattr(644,root,root,755)

#%files -f Azerbaijani.lang Azerbaijani
#%defattr(644,root,root,755)

%files -f Bulgarian.lang Bulgarian
%defattr(644,root,root,755)

%files -f Bengali.lang Bengali
%defattr(644,root,root,755)

%files -f Breton.lang Breton
%defattr(644,root,root,755)

%files -f Bosnian.lang Bosnian
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

# %files -f English.lang English
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

%files -f Farsi.lang Farsi
%defattr(644,root,root,755)

%files -f Finnish.lang Finnish
%defattr(644,root,root,755)

%files -f French.lang French
%defattr(644,root,root,755)

%files -f Frisian.lang Frisian
%defattr(644,root,root,755)

%files -f Irish.lang Irish
%defattr(644,root,root,755)

#%files -f Galician.lang Galician
#%defattr(644,root,root,755)

%files -f Hindi.lang Hindi
%defattr(644,root,root,755)

%files -f Hebrew.lang Hebrew
%defattr(644,root,root,755)

%files -f Croatian.lang Croatian
%defattr(644,root,root,755)

%files -f Upper_Sorbian.lang Upper_Sorbian
%defattr(644,root,root,755)

%files -f Hungarian.lang Hungarian
%defattr(644,root,root,755)

##%files -f Indonesian.lang Indonesian
%files -f Icelandic.lang Icelandic
%defattr(644,root,root,755)

%files -f Italian.lang Italian
%defattr(644,root,root,755)

%files -f Japanese.lang Japanese
%defattr(644,root,root,755)

##%files -f Korean.lang Korean
%files -f Lithuanian.lang Lithuanian
%defattr(644,root,root,755)

##%files -f Latvian.lang Latvian
#%%files -f Maltese.lang Maltese
%files -f Malay.lang Malay
%defattr(644,root,root,755)

%files -f Mongolian.lang Mongolian
%defattr(644,root,root,755)
#{_datadir}/locale/mn/*.png

# %files -f Maori.lang Maori
%files -f Macedonian.lang Macedonian
%defattr(644,root,root,755)

%files -f Low_Saxon.lang Low_Saxon
%defattr(644,root,root,755)

%files -f Dutch.lang Dutch
%defattr(644,root,root,755)

%files -f Norwegian_Bokmaal.lang Norwegian_Bokmaal
%defattr(644,root,root,755)

%files -f Norwegian_Nynorsk.lang Norwegian_Nynorsk
%defattr(644,root,root,755)

#%%files -f Northern_Sotho.lang Northern_Sotho
# %files -f Gascon_occitan.lang Gascon_occitan

%files -f Punjabi.lang Punjabi
%defattr(644,root,root,755)


%files -f Polish.lang Polish
%defattr(644,root,root,755)

#%%{_datadir}/services/searchproviders/*.desktop
%files -f Portuguese.lang Portuguese
%defattr(644,root,root,755)

%files -f Brazil_Portuguese.lang Brazil_Portuguese
%defattr(644,root,root,755)

%files -f Romanian.lang Romanian
%defattr(644,root,root,755)

%files -f Russian.lang Russian
%defattr(644,root,root,755)

%files -f Northern_Sami.lang Northern_Sami
%defattr(644,root,root,755)

#%%files -f Swati.lang Swati
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

#%%files -f Thai.lang Thai
%files -f Turkish.lang Turkish
%defattr(644,root,root,755)

%files -f Tajik.lang Tajik
%defattr(644,root,root,755)

%files -f Ukrainian.lang Ukrainian
%defattr(644,root,root,755)

%files -f Uzbek.lang Uzbek
%defattr(644,root,root,755)

#%%files -f Venda.lang Venda
#%%files -f Vietnamese.lang Vietnamese
# %files -f Walloon.lang Walloon
#%%files -f Xhosa.lang Xhosa
%files -f Simplified_Chinese.lang Simplified_Chinese
%defattr(644,root,root,755)

%files -f Chinese.lang Chinese
%defattr(644,root,root,755)

#%%files -f Zulu.lang Zulu
%endif

%if %{with alltogether}
%files -f all.lang
%defattr(644,root,root,755)
%endif
