# TODO:
#   /usr/share/locale/mn/30x16.png
#   /usr/share/locale/mn/60x40.png
#
# Conditional build:
%bcond_with	alltogether		# build single package containing support for all languages

%define		_state		stable
%define		_minlibsevr	9:%{version}

Summary:	K Desktop Environment - international support
Summary(pl):	KDE - wsparcie dla wielu jêzyków
Name:		kde-i18n
Version:	3.5.6
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-af-%{version}.tar.bz2
# Source0-md5:	7771bdb76b76323a68da4700bd5eaf26
Source1:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-ar-%{version}.tar.bz2
# Source1-md5:	e79ef203dfc9196ea75089dfcd99339d
Source2:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-az-%{version}.tar.bz2
# Source2-md5:	416e628f6c3d27a334d26f1c5bd83406
Source3:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-bg-%{version}.tar.bz2
# Source3-md5:	a34d5e307d418fc87bcbb6ab150bc046
Source4:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-bn-%{version}.tar.bz2
# Source4-md5:	f5153ad329e8d7305aefa12f7ddfdfa3
Source5:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-br-%{version}.tar.bz2
# Source5-md5:	5c4ae705596f83ac2ee5df83a7900e5b
Source6:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-bs-%{version}.tar.bz2
# Source6-md5:	df40c6f49ebbc00155eea55f913d1600
Source7:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-ca-%{version}.tar.bz2
# Source7-md5:	84b3a011b9d594ce26fdee77cccdfb52
Source8:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-cs-%{version}.tar.bz2
# Source8-md5:	b2dab45ea572efbb2569781211c2a7fc
Source9:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-cy-%{version}.tar.bz2
# Source9-md5:	3d3ddcd729b5ade752b498a42aeac39c
Source10:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-da-%{version}.tar.bz2
# Source10-md5:	913550e6604b9423cea605d95a8a664f
Source11:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-de-%{version}.tar.bz2
# Source11-md5:	c8a52e825c610ae5779ef84d1bf7e3c5
Source12:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-el-%{version}.tar.bz2
# Source12-md5:	f395db170010c2a4ee9a7e27b1c8772e
Source13:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-en_GB-%{version}.tar.bz2
# Source13-md5:	6b81bfa733c5e1c8ae4d16208093f648
Source14:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-eo-%{version}.tar.bz2
# Source14-md5:	7f17faa2bda08f31e1f33a3242f0b960
Source15:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-es-%{version}.tar.bz2
# Source15-md5:	75f2b236131bcf89b6f2302c1fb8780f
Source16:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-et-%{version}.tar.bz2
# Source16-md5:	55647fdaf91b9626618015017be954b4
Source17:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-eu-%{version}.tar.bz2
# Source17-md5:	6413e62d868721be5b269e50e979d4b1
Source18:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-fa-%{version}.tar.bz2
# Source18-md5:	be881e4b7be80e289b9dcdf00753ce79
Source19:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-fi-%{version}.tar.bz2
# Source19-md5:	227d47ad0232daf190653b4f8d9cd508
Source20:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-fr-%{version}.tar.bz2
# Source20-md5:	f700524f68cf6d34770784c69f9cc293
Source21:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-fy-%{version}.tar.bz2
# Source21-md5:	f69c07af129e084a4166cdfb3e5db173
Source22:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-ga-%{version}.tar.bz2
# Source22-md5:	0ffdca99a102c4e1320916de3bf35adb
Source23:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-gl-%{version}.tar.bz2
# Source23-md5:	590bd015071b21ba0dcd55fc2955ca55
Source24:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-he-%{version}.tar.bz2
# Source24-md5:	b416073a3503a01056e14107fc797dae
Source25:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-hi-%{version}.tar.bz2
# Source25-md5:	25f0b08c99c952f443f32a86d5d4d4ad
Source26:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-hr-%{version}.tar.bz2
# Source26-md5:	99a94e8fc1fcdf1837f7030760c3deeb
Source27:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-hu-%{version}.tar.bz2
# Source27-md5:	575734a98fa2984f47adb49d6c023cc0
Source28:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-is-%{version}.tar.bz2
# Source28-md5:	f41752647ef59cb9fd179e2e1f77738c
Source29:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-it-%{version}.tar.bz2
# Source29-md5:	3a9bea48fb5ac7d3703abfdaa8a50c3c
Source30:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-ja-%{version}.tar.bz2
# Source30-md5:	79b62e00ae4bbcc0d874588ccba177be
Source63:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-kk-%{version}.tar.bz2
# Source63-md5:	f878ce771f32ea800c285e5a813b17e7
Source31:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-km-%{version}.tar.bz2
# Source31-md5:	2f83f915e5ee4932ce8c7f26abb8b542
Source32:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-ko-%{version}.tar.bz2
# Source32-md5:	eb47d4c6f46c161835c5255f399e1ac9
Source33:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-lt-%{version}.tar.bz2
# Source33-md5:	2769c90376add2e49addcaa2f39df577
Source34:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-lv-%{version}.tar.bz2
# Source34-md5:	c3f7cca71708d2894510bdd30b264bff
Source35:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-mk-%{version}.tar.bz2
# Source35-md5:	2e374c32eb02a6421b2076ac305926a2
Source36:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-mn-%{version}.tar.bz2
# Source36-md5:	7158b53fec42b7ed43525bacfa57e0e4
Source37:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-ms-%{version}.tar.bz2
# Source37-md5:	edeaa43311fc0935d0a5b79b5db8f39e
Source38:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-nb-%{version}.tar.bz2
# Source38-md5:	bf087b3c116770dcffa008da74e767e2
Source39:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-nds-%{version}.tar.bz2
# Source39-md5:	a12623e0d68f3737447b663e070e3f61
Source40:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-nl-%{version}.tar.bz2
# Source40-md5:	6f4eea25839984463e70d1c635813a11
Source41:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-nn-%{version}.tar.bz2
# Source41-md5:	9dc810b75c2cb7c864ec5bf82a2bed2f
Source42:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-pa-%{version}.tar.bz2
# Source42-md5:	6a9be2176930ceb07600913cbee525e3
Source43:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-pl-%{version}.tar.bz2
# Source43-md5:	71852ce8f2549cfc19ffe71468a82349
Source44:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-pt-%{version}.tar.bz2
# Source44-md5:	ee8322ab521d796fbfafef471d845d6d
Source45:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-pt_BR-%{version}.tar.bz2
# Source45-md5:	29836d3d914f41a2cab1567d1df6feff
Source46:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-ro-%{version}.tar.bz2
# Source46-md5:	af2fc2dbc745614c7286a430a7874a54
Source47:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-ru-%{version}.tar.bz2
# Source47-md5:	348d72dfa83d51cbb65f6c7e964d64b3
Source48:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-rw-%{version}.tar.bz2
# Source48-md5:	8d07d207bb2e933a7b0130e593313842
Source49:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-se-%{version}.tar.bz2
# Source49-md5:	11d5888678814a442589c995d6307cd8
Source50:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-sk-%{version}.tar.bz2
# Source50-md5:	3a7b1b8bd44c92713d5e4db52655915b
Source51:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-sl-%{version}.tar.bz2
# Source51-md5:	2064f33c3f76ee60ddf1aef010d92399
Source52:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-sr-%{version}.tar.bz2
# Source52-md5:	e38ff9abe6f68bc69e0df5891e7bce69
Source53:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-sr@Latn-%{version}.tar.bz2
# Source53-md5:	9dcf67d0837f8ad2448d07c3ba3d5015
Source54:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-ss-%{version}.tar.bz2
# Source54-md5:	7ecd86abba7c02c73b248ba5452c4bed
Source55:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-sv-%{version}.tar.bz2
# Source55-md5:	a826fb26b9378b12dae31b15ac22d995
Source56:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-ta-%{version}.tar.bz2
# Source56-md5:	11da7704ec348481c392cfd47af85caa
Source57:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-tg-%{version}.tar.bz2
# Source57-md5:	33f3b735e9cbd8a736146dae8a764d06
Source58:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-tr-%{version}.tar.bz2
# Source58-md5:	b56062b9908ecb6909bc4a7e4c4bb62a
Source59:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-uk-%{version}.tar.bz2
# Source59-md5:	82f0f3f3567d551307c03ebad12f3a1c
Source60:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-uz-%{version}.tar.bz2
# Source60-md5:	2208bb14ae419e20f2179d586ba49ff5
Source64:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-vi-%{version}.tar.bz2
# Source64-md5:	58602a074a5868b3c1ae299080289d9a
Source61:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-zh_CN-%{version}.tar.bz2
# Source61-md5:	a74fb6fee6d36a8bd975bb7b1b97fb4c
Source62:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-zh_TW-%{version}.tar.bz2
# Source62-md5:	f6211661d09cf7dcc381147d084537a7

%if %{with alltogether}
Requires:	kde-i18n-base
# NOTE:	"Affrikaans", "Norwegian_Bookmal", "Brazil_Portugnese" and "Portugnese" are here
# intentionally, to allow upgrade from packages with misspelled names
Obsoletes:	kde-i18n-Affrikaans
Obsoletes:	kde-i18n-Brazil
Obsoletes:	kde-i18n-Brazil_Portugnese
Obsoletes:	kde-i18n-British
Obsoletes:	kde-i18n-Chinese-Big5
Obsoletes:	kde-i18n-Gascon_occitan
Obsoletes:	kde-i18n-Norwegian
Obsoletes:	kde-i18n-Norwegian_Bookmal
Obsoletes:	kde-i18n-Portugnese
# currently existing packages, you may script to update these
Obsoletes:	kde-i18n-Afrikaans
Obsoletes:	kde-i18n-Arabic
Obsoletes:	kde-i18n-Azerbaijani
Obsoletes:	kde-i18n-Basque
Obsoletes:	kde-i18n-Bengali
Obsoletes:	kde-i18n-Bosnian
Obsoletes:	kde-i18n-Brazil_Portuguese
Obsoletes:	kde-i18n-Breton
Obsoletes:	kde-i18n-Bulgarian
Obsoletes:	kde-i18n-Catalan
Obsoletes:	kde-i18n-Chinese
Obsoletes:	kde-i18n-Croatian
Obsoletes:	kde-i18n-Cymraeg
Obsoletes:	kde-i18n-Czech
Obsoletes:	kde-i18n-Danish
Obsoletes:	kde-i18n-Dutch
Obsoletes:	kde-i18n-English
Obsoletes:	kde-i18n-English_UK
Obsoletes:	kde-i18n-Esperanto
Obsoletes:	kde-i18n-Estonian
Obsoletes:	kde-i18n-Farsi
Obsoletes:	kde-i18n-Finnish
Obsoletes:	kde-i18n-French
Obsoletes:	kde-i18n-Frisian
Obsoletes:	kde-i18n-Galician
Obsoletes:	kde-i18n-Gascon_Occitan
Obsoletes:	kde-i18n-German
Obsoletes:	kde-i18n-Greek
Obsoletes:	kde-i18n-Hebrew
Obsoletes:	kde-i18n-Hindi
Obsoletes:	kde-i18n-Hungarian
Obsoletes:	kde-i18n-Icelandic
Obsoletes:	kde-i18n-Indonesian
Obsoletes:	kde-i18n-Irish
Obsoletes:	kde-i18n-Italian
Obsoletes:	kde-i18n-Japanese
Obsoletes:	kde-i18n-Kazakh
Obsoletes:	kde-i18n-Khmer
Obsoletes:	kde-i18n-Kinyarwanda
Obsoletes:	kde-i18n-Korean
Obsoletes:	kde-i18n-Lao
Obsoletes:	kde-i18n-Latvian
Obsoletes:	kde-i18n-Lithuanian
Obsoletes:	kde-i18n-Low_Saxon
Obsoletes:	kde-i18n-Macedonian
Obsoletes:	kde-i18n-Malay
Obsoletes:	kde-i18n-Maltese
Obsoletes:	kde-i18n-Maori
Obsoletes:	kde-i18n-Mongolian
Obsoletes:	kde-i18n-Northern_Sami
Obsoletes:	kde-i18n-Northern_Sotho
Obsoletes:	kde-i18n-Norwegian_Bokmaal
Obsoletes:	kde-i18n-Norwegian_Nynorsk
Obsoletes:	kde-i18n-Polish
Obsoletes:	kde-i18n-Portuguese
Obsoletes:	kde-i18n-Punjabi
Obsoletes:	kde-i18n-Romanian
Obsoletes:	kde-i18n-Russian
Obsoletes:	kde-i18n-Serbian
Obsoletes:	kde-i18n-Simplified_Chinese
Obsoletes:	kde-i18n-Slovak
Obsoletes:	kde-i18n-Slovenian
Obsoletes:	kde-i18n-Spanish
Obsoletes:	kde-i18n-Swati
Obsoletes:	kde-i18n-Swedish
Obsoletes:	kde-i18n-Tajik
Obsoletes:	kde-i18n-Tamil
Obsoletes:	kde-i18n-Thai
Obsoletes:	kde-i18n-Turkish
Obsoletes:	kde-i18n-Ukrainian
Obsoletes:	kde-i18n-Upper_Sorbian
Obsoletes:	kde-i18n-Uzbek
Obsoletes:	kde-i18n-Venda
Obsoletes:	kde-i18n-Vietnamese
Obsoletes:	kde-i18n-Walloon
Obsoletes:	kde-i18n-Xhosa
Obsoletes:	kde-i18n-Zulu
%endif
BuildRequires:	gettext-devel
# It creates symlinks to some not-translated files.
BuildRequires:	kdelibs-devel >= %{_minlibsevr}
BuildRequires:	libxml2-progs >= 2.4.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
K Desktop Environment - international support.

%description -l pl
KDE - wsparcie dla wielu jêzyków.

%package base
Summary:	Empty metapackage to handle obsoletes
Summary(pl):	Pusty metapakiet z obsoletes
Group:		X11/Applications
Obsoletes:	common-filemanagement-i18n
Obsoletes:	kde-decoration-b2-i18n
Obsoletes:	kde-decoration-cde-i18n
Obsoletes:	kde-decoration-common-i18n
Obsoletes:	kde-decoration-glow-i18n
Obsoletes:	kde-decoration-icewm-i18n
Obsoletes:	kde-decoration-kde1-i18n
Obsoletes:	kde-decoration-kstep-i18n
Obsoletes:	kde-decoration-modernsys-i18n
Obsoletes:	kde-decoration-openlook-i18n
Obsoletes:	kde-decoration-plastik-i18n
Obsoletes:	kde-decoration-quartz-i18n
Obsoletes:	kde-decoration-riscos-i18n
Obsoletes:	kde-decoration-system-i18n
Obsoletes:	kde-i18n-kdelibs
Obsoletes:	kde-kgreet-classic-i18n
Obsoletes:	kde-kio-imap4-i18n
Obsoletes:	kde-kio-ldap-i18n
Obsoletes:	kde-kio-newimap4-i18n
Obsoletes:	kde-kio-nntp-i18n
Obsoletes:	kde-kio-pop3-i18n
Obsoletes:	kde-kio-smtp-i18n
Obsoletes:	kde-style-plastik-i18n
Obsoletes:	kdeaccessibility-i18n
Obsoletes:	kdeaccessibility-kmag-i18n
Obsoletes:	kdeaccessibility-kmousetool-i18n
Obsoletes:	kdeaccessibility-kmouth-i18n
Obsoletes:	kdeaddons-ark-i18n
Obsoletes:	kdeaddons-atlantikdesigner-i18n
Obsoletes:	kdeaddons-fsview-i18n
Obsoletes:	kdeaddons-i18n
Obsoletes:	kdeaddons-kaddressbook-i18n
Obsoletes:	kdeaddons-kate-i18n
Obsoletes:	kdeaddons-kicker-i18n
Obsoletes:	kdeaddons-konqueror-i18n
Obsoletes:	kdeaddons-kontact-i18n
Obsoletes:	kdeaddons-ksig-i18n
Obsoletes:	kdeaddons-kvim-i18n
Obsoletes:	kdeaddons-lnkforward-i18n
Obsoletes:	kdeaddons-noatun-i18n
Obsoletes:	kdeadmin-i18n
Obsoletes:	kdeadmin-kcmlilo-i18n
Obsoletes:	kdeadmin-kcmlinuz-i18n
Obsoletes:	kdeadmin-kcron-i18n
Obsoletes:	kdeadmin-kdat-i18n
Obsoletes:	kdeadmin-kpackage-i18n
Obsoletes:	kdeadmin-ksysv-i18n
Obsoletes:	kdeadmin-kuser-i18n
Obsoletes:	kdeartwork-i18n
Obsoletes:	kdeartwork-screensavers-i18n
Obsoletes:	kdebase-common-filemanagement-i18n
Obsoletes:	kdebase-core-i18n
Obsoletes:	kdebase-desktop-i18n
Obsoletes:	kdebase-desktop-libs-i18n
Obsoletes:	kdebase-i18n
Obsoletes:	kdebase-infocenter-i18n
Obsoletes:	kdebase-kappfinder-i18n
Obsoletes:	kdebase-kate-i18n
Obsoletes:	kdebase-kdcop-i18n
Obsoletes:	kdebase-kdeprintfax-i18n
Obsoletes:	kdebase-kdialog-i18n
Obsoletes:	kdebase-kfind-i18n
Obsoletes:	kdebase-kfontinst-i18n
Obsoletes:	kdebase-kicker-i18n
Obsoletes:	kdebase-kicker-libs-i18n
Obsoletes:	kdebase-kjobviewer-i18n
Obsoletes:	kdebase-klipper-i18n
Obsoletes:	kdebase-kmenuedit-i18n
Obsoletes:	kdebase-konsole-i18n
Obsoletes:	kdebase-kpager-i18n
Obsoletes:	kdebase-kpersonalizer-i18n
Obsoletes:	kdebase-ksysguard-i18n
Obsoletes:	kdebase-ksystraycmd-i18n
Obsoletes:	kdebase-kwrite-i18n
Obsoletes:	kdebase-libkonq-i18n
Obsoletes:	kdebase-mailnews-i18n
Obsoletes:	kdebase-screensavers-i18n
Obsoletes:	kdebase-useraccount-i18n
Obsoletes:	kdeedu-flashkard-i18n
Obsoletes:	kdeedu-i18n
Obsoletes:	kdeedu-kalzium-i18n
Obsoletes:	kdeedu-kbruch-i18n
Obsoletes:	kdeedu-keduca-i18n
Obsoletes:	kdeedu-khangman-i18n
Obsoletes:	kdeedu-kig-i18n
Obsoletes:	kdeedu-kiten-i18n
Obsoletes:	kdeedu-klatin-i18n
Obsoletes:	kdeedu-klettres-i18n
Obsoletes:	kdeedu-kmessedwords-i18n
Obsoletes:	kdeedu-kmplot-i18n
Obsoletes:	kdeedu-kpercentage-i18n
Obsoletes:	kdeedu-kstars-i18n
Obsoletes:	kdeedu-ktouch-i18n
Obsoletes:	kdeedu-kturtle-i18n
Obsoletes:	kdeedu-kverbos-i18n
Obsoletes:	kdeedu-kvoctrain-i18n
Obsoletes:	kdeedu-kwordquiz-i18n
Obsoletes:	kdegames-atlantik-i18n
Obsoletes:	kdegames-i18n
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
Obsoletes:	kdegames-kmahjongg-i18n
Obsoletes:	kdegames-kmines-i18n
Obsoletes:	kdegames-kolf-i18n
Obsoletes:	kdegames-konquest-i18n
Obsoletes:	kdegames-kpat-i18n
Obsoletes:	kdegames-kpoker-i18n
Obsoletes:	kdegames-kreversi-i18n
Obsoletes:	kdegames-ksame-i18n
Obsoletes:	kdegames-kshisen-i18n
Obsoletes:	kdegames-ksirtet-i18n
Obsoletes:	kdegames-ksmiletris-i18n
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
Obsoletes:	kdegraphics-kfax-i18n
Obsoletes:	kdegraphics-kfile-i18n
Obsoletes:	kdegraphics-kgamma-i18n
Obsoletes:	kdegraphics-kghostview-i18n
Obsoletes:	kdegraphics-kiconedit-i18n
Obsoletes:	kdegraphics-kmrml-i18n
Obsoletes:	kdegraphics-kolourpaint-i18n
Obsoletes:	kdegraphics-kooka-i18n
Obsoletes:	kdegraphics-kpaint-i18n
Obsoletes:	kdegraphics-kpdf-i18n
Obsoletes:	kdegraphics-kpovmodeler-i18n
Obsoletes:	kdegraphics-kruler-i18n
Obsoletes:	kdegraphics-ksnapshot-i18n
Obsoletes:	kdegraphics-ksvg-i18n
Obsoletes:	kdegraphics-kuickshow-i18n
Obsoletes:	kdegraphics-kview-i18n
Obsoletes:	kdelibs-i18n
Obsoletes:	kdemultimedia-arts-i18n
Obsoletes:	kdemultimedia-artsbuilder-i18n
Obsoletes:	kdemultimedia-artscontrol-i18n
Obsoletes:	kdemultimedia-audiocd-i18n
Obsoletes:	kdemultimedia-i18n
Obsoletes:	kdemultimedia-juk-i18n
Obsoletes:	kdemultimedia-kaboodle-i18n
Obsoletes:	kdemultimedia-kaudiocreator-i18n
Obsoletes:	kdemultimedia-kfile-i18n
Obsoletes:	kdemultimedia-kmid-i18n
Obsoletes:	kdemultimedia-kmix-i18n
Obsoletes:	kdemultimedia-krec-i18n
Obsoletes:	kdemultimedia-kscd-i18n
Obsoletes:	kdemultimedia-libkcddb-i18n
Obsoletes:	kdemultimedia-noatun-i18n
Obsoletes:	kdenetwork-filesharing-i18n
Obsoletes:	kdenetwork-i18n
Obsoletes:	kdenetwork-kdict-i18n
Obsoletes:	kdenetwork-kget-i18n
Obsoletes:	kdenetwork-kinetd-i18n
Obsoletes:	kdenetwork-knewsticker-i18n
Obsoletes:	kdenetwork-kopete-i18n
Obsoletes:	kdenetwork-kpf-i18n
Obsoletes:	kdenetwork-kppp-i18n
Obsoletes:	kdenetwork-krfb-i18n
Obsoletes:	kdenetwork-ksirc-i18n
Obsoletes:	kdenetwork-ktalkd-i18n
Obsoletes:	kdenetwork-kwifimanager-i18n
Obsoletes:	kdenetwork-lanbrowser-i18n
Obsoletes:	kdenetwork-rss-i18n
Obsoletes:	kdepim-i18n
Obsoletes:	kdepim-i18n
Obsoletes:	kdepim-kaddressbook-i18n
Obsoletes:	kdepim-kandy-i18n
Obsoletes:	kdepim-karm-i18n
Obsoletes:	kdepim-kgantt-i18n
Obsoletes:	kdepim-kmail-i18n
Obsoletes:	kdepim-kmail-libs-i18n
Obsoletes:	kdepim-knode-i18n
Obsoletes:	kdepim-knotes-i18n
Obsoletes:	kdepim-konsolekalendar-i18n
Obsoletes:	kdepim-kontact-i18n
Obsoletes:	kdepim-korganizer-i18n
Obsoletes:	kdepim-korganizer-libs-i18n
Obsoletes:	kdepim-korn-i18n
Obsoletes:	kdepim-kpilot-i18n
Obsoletes:	kdepim-ktnef-i18n
Obsoletes:	kdepim-libkcal-i18n
Obsoletes:	kdepim-libkdenetwork-i18n
Obsoletes:	kdepim-libkdepim-i18n
Obsoletes:	kdepim-libksieve-i18n
Obsoletes:	kdepim-libs-i18n
Obsoletes:	kdesdk-cervisia-i18n
Obsoletes:	kdesdk-i18n
Obsoletes:	kdesdk-kbabel-i18n
Obsoletes:	kdesdk-kbugbuster-i18n
Obsoletes:	kdesdk-kcachegrind-i18n
Obsoletes:	kdesdk-kfile-i18n
Obsoletes:	kdesdk-kfilereplace-i18n
Obsoletes:	kdesdk-kompare-i18n
Obsoletes:	kdesdk-kspy-i18n
Obsoletes:	kdesdk-kstartperf-i18n
Obsoletes:	kdesdk-kuiviewer-i18n
Obsoletes:	kdesdk-libcvsservice-i18n
Obsoletes:	kdesdk-spy-i18n
Obsoletes:	kdesdk-umbrello-i18n
Obsoletes:	kdetoys-amor-i18n
Obsoletes:	kdetoys-fifteen-i18n
Obsoletes:	kdetoys-i18n
Obsoletes:	kdetoys-kmoon-i18n
Obsoletes:	kdetoys-kodo-i18n
Obsoletes:	kdetoys-kteatime-i18n
Obsoletes:	kdetoys-ktux-i18n
Obsoletes:	kdetoys-kweather-i18n
Obsoletes:	kdetoys-kworldclock-i18n
Obsoletes:	kdeutils-ark-i18n
Obsoletes:	kdeutils-i18n
Obsoletes:	kdeutils-kcalc-i18n
Obsoletes:	kdeutils-kcharselect-i18n
Obsoletes:	kdeutils-kdelirc-i18n
Obsoletes:	kdeutils-kdepasswd-i18n
Obsoletes:	kdeutils-kdessh-i18n
Obsoletes:	kdeutils-kdf-i18n
Obsoletes:	kdeutils-kedit-i18n
Obsoletes:	kdeutils-kfloppy-i18n
Obsoletes:	kdeutils-kgpg-i18n
Obsoletes:	kdeutils-khexedit-i18n
Obsoletes:	kdeutils-kjots-i18n
Obsoletes:	kdeutils-klaptopdaemon-i18n
Obsoletes:	kdeutils-kmilo-i18n
Obsoletes:	kdeutils-kregexpeditor-i18n
Obsoletes:	kdeutils-ksim-i18n
Obsoletes:	kdeutils-ktimer-i18n
Obsoletes:	kdeutils-kwalletmanager-i18n
Obsoletes:	kdeutils-userinfo-i18n
Obsoletes:	kdevelop-i18n
Obsoletes:	kdewebdev-kfilereplace-i18n
Obsoletes:	kdewebdev-kimagemapeditor-i18n
Obsoletes:	kdewebdev-klinkstatus-i18n
Obsoletes:	kdewebdev-kommander-i18n
Obsoletes:	kdewebdev-kxsldbg-i18n
Obsoletes:	kdewebdev-quanta-i18n
Obsoletes:	kdm-i18n
Obsoletes:	konqueror-i18n
Obsoletes:	konqueror-libs-i18n
Obsoletes:	quanta-i18n

%description base
Empty metapackage to handle obsoletes for individual i18n subpackages.

%description base -l pl
Pusty metapakiet z Obsoletes dla oddzielnych podpakietów i18n.

%package Afrikaans
Summary:	K Desktop Environment - Afrikaans language support
Summary(pl):	KDE - wsparcie dla jêzyka afrykanerskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
# "Affrikaans" is here intentionally, to allow upgrade from misspelled packages
Obsoletes:	kde-i18n-Affrikaans

%description Afrikaans
K Desktop Environment - Afrikaans language support.

%description Afrikaans -l pl
KDE - wsparcie dla jêzyka afrykanerskiego.

%package Arabic
Summary:	K Desktop Environment - Arabic language support
Summary(pl):	KDE - wsparcie dla jêzyka arabskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Arabic
K Desktop Environment - Arabic language support.

%description Arabic -l pl
KDE - wsparcie dla jêzyka arabskiego.

%package Azerbaijani
Summary:	K Desktop Environment - Azerbaijani language support
Summary(pl):	KDE - wsparcie dla jêzyka azerskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Azerbaijani
K Desktop Environment - Azerbaijani language support.

%description Azerbaijani -l pl
KDE - wsparcie dla jêzyka azerskiego.

%package Bulgarian
Summary:	K Desktop Environment - Bulgarian language support
Summary(pl):	KDE - wsparcie dla jêzyka bu³garskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Bulgarian
K Desktop Environment - Bulgarian language support.

%description Bulgarian -l pl
KDE - wsparcie dla jêzyka bu³garskiego.

%package Bengali
Summary:	K Desktop Environment - Bengali language support
Summary(pl):	KDE - wsparcie dla jêzyka bengalskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Bengali
K Desktop Environment - Bengali language support.

%description Bengali -l pl
KDE - wsparcie dla jêzyka bengalskiego.

%package Breton
Summary:	K Desktop Environment - Breton language support
Summary(pl):	KDE - wsparcie dla jêzyka bretoñskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Breton
K Desktop Environment - Breton language support.

%description Breton -l pl
KDE - wsparcie dla jêzyka bretoñskiego.

%package Bosnian
Summary:	K Desktop Environment - Bosnian language support
Summary(pl):	KDE - wsparcie dla jêzyka bo¶niackiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Bosnian
K Desktop Environment - Bosnian language support.

%description Bosnian -l pl
KDE - wsparcie dla jêzyka bo¶niackiego.

%package Catalan
Summary:	K Desktop Environment - Catalan language support
Summary(pl):	KDE - wsparcie dla jêzyka kataloñskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Catalan
K Desktop Environment - Catalan language support.

%description Catalan -l pl
KDE - wsparcie dla jêzyka kataloñskiego.

%package Czech
Summary:	K Desktop Environment - Czech language support
Summary(pl):	KDE - wsparcie dla jêzyka czeskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Czech
K Desktop Environment - Czech language support.

%description Czech -l pl
KDE - wsparcie dla jêzyka czeskiego.

%package Cymraeg
Summary:	K Desktop Environment - Cymraeg language support
Summary(pl):	KDE - wsparcie dla jêzyka walijskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Cymraeg
K Desktop Environment - Cymraeg language support.

%description Cymraeg -l pl
KDE - wsparcie dla jêzyka walijskiego.

%package Danish
Summary:	K Desktop Environment - Danish language support
Summary(pl):	KDE - wsparcie dla jêzyka duñskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Danish
K Desktop Environment - Danish language support.

%description Danish -l pl
KDE - wsparcie dla jêzyka duñskiego.

%package German
Summary:	K Desktop Environment - German language support
Summary(pl):	KDE - wsparcie dla jêzyka niemieckiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description German
K Desktop Environment - German language support.

%description German -l pl
KDE - wsparcie dla jêzyka niemieckiego.

%package Greek
Summary:	K Desktop Environment - Greek language support
Summary(pl):	KDE - wsparcie dla jêzyka greckiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Greek
K Desktop Environment - Greek language support.

%description Greek -l pl
KDE - wsparcie dla jêzyka greckiego.

%package English
Summary:	K Desktop Environment - English language support
Summary(pl):	KDE - wsparcie dla jêzyka angielskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description English
K Desktop Environment - English language support.

%description English -l pl
KDE - wsparcie dla jêzyka angielskiego.

%package English_UK
Summary:	K Desktop Environment - K Desktop Environment - English (UK) language support
Summary(pl):	KDE - wsparcie dla jêzyka angielskiego (odmiany brytyjskiej)
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description English_UK
K Desktop Environment - English (UK) language support.

%description English_UK -l pl
KDE - wsparcie dla jêzyka angielskiego (odmiany brytyjskiej).

%package Esperanto
Summary:	K Desktop Environment - Esperanto language support
Summary(pl):	KDE - wsparcie dla jêzyka esperanto
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Esperanto
K Desktop Environment - Esperanto language support.

%description Esperanto -l pl
KDE - wsparcie dla jêzyka esperanto.

%package Spanish
Summary:	K Desktop Environment - Spanish language support
Summary(pl):	KDE - wsparcie dla jêzyka hiszpañskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Spanish
K Desktop Environment - Spanish language support.

%description Spanish -l pl
KDE - wsparcie dla jêzyka hiszpañskiego.

%package Estonian
Summary:	K Desktop Environment - Estonian language support
Summary(pl):	KDE - wsparcie dla jêzyka estoñskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Estonian
K Desktop Environment - Estonian language support.

%description Estonian -l pl
KDE - wsparcie dla jêzyka estoñskiego.

%package Basque
Summary:	K Desktop Environment - Basque language support
Summary(pl):	KDE - wsparcie dla jêzyka baskijskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Basque
K Desktop Environment - Basque language support.

%description Basque -l pl
KDE - wsparcie dla jêzyka baskijskiego.

%package Farsi
Summary:	K Desktop Environment - Farsi language support
Summary(pl):	KDE - wsparcie dla jêzyka perskiego (farsi)
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Farsi
K Desktop Environment - Farsi language support.

%description Farsi -l pl
KDE - wsparcie dla jêzyka perskiego (farsi).

%package Finnish
Summary:	K Desktop Environment - Finnish language support
Summary(pl):	KDE - wsparcie dla jêzyka fiñskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Finnish
K Desktop Environment - Finnish language support.

%description Finnish -l pl
KDE - wsparcie dla jêzyka fiñskiego.

%package French
Summary:	K Desktop Environment - French language support
Summary(pl):	KDE - wsparcie dla jêzyka francuskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description French
K Desktop Environment - French language support.

%description French -l pl
KDE - wsparcie dla jêzyka francuskiego.

%package Frisian
Summary:	K Desktop Environment - Frisian language support
Summary(pl):	KDE - wsparcie dla jêzyka fryzyjskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Frisian
K Desktop Environment - Frisian language support.

%description Frisian -l pl
KDE - wsparcie dla jêzyka fryzyjskiego.

%package Irish
Summary:	K Desktop Environment - Irish language support
Summary(pl):	KDE - wsparcie dla jêzyka irlandzkiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Irish
K Desktop Environment - Irish language support.

%description Irish -l pl
KDE - wsparcie dla jêzyka irlandzkiego.

%package Galician
Summary:	K Desktop Environment - Galician language support
Summary(pl):	KDE - wsparcie dla jêzyka galicyjskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Galician
K Desktop Environment - Galician language support.

%description Galician -l pl
KDE - wsparcie dla jêzyka galicyjskiego.

%package Hindi
Summary:	K Desktop Environment - Hindi language support
Summary(pl):	KDE - wsparcie dla jêzyka hindi
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Hindi
K Desktop Environment - Hindi language support.

%description Hindi -l pl
KDE - wsparcie dla jêzyka hindi.

%package Hebrew
Summary:	K Desktop Environment - Hebrew language support
Summary(pl):	KDE - wsparcie dla jêzyka hebrajskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Hebrew
K Desktop Environment - Hebrew language support.

%description Hebrew -l pl
KDE - wsparcie dla jêzyka hebrajskiego.

%package Croatian
Summary:	K Desktop Environment - Croatian language support
Summary(pl):	KDE - wsparcie dla jêzyka chorwackiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Croatian
K Desktop Environment - Croatian language support.

%description Croatian -l pl
KDE - wsparcie dla jêzyka chorwackiego.

%package Upper_Sorbian
Summary:	K Desktop Environment - Upper Sorbian language support
Summary(pl):	KDE - wsparcie dla jêzyka górno³u¿yckiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Upper_Sorbian
K Desktop Environment - Upper Sorbian language support.

%description Upper_Sorbian  -l pl
KDE - wsparcie dla jêzyka górno³u¿yckiego.

%package Hungarian
Summary:	K Desktop Environment - Hungarian language support
Summary(pl):	KDE - wsparcie dla jêzyka wêgierskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Hungarian
K Desktop Environment - Hungarian language support.

%description Hungarian -l pl
KDE - wsparcie dla jêzyka wêgierskiego.

%package Indonesian
Summary:	K Desktop Environment - Indonesian language support
Summary(pl):	KDE - wsparcie dla jêzyka indonezyjskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Indonesian
K Desktop Environment - Indonesian language support.

%description Indonesian -l pl
KDE - wsparcie dla jêzyka indonezyjskiego.

%package Icelandic
Summary:	K Desktop Environment - Icelandic language support
Summary(pl):	KDE - wsparcie dla jêzyka islandzkiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Icelandic
K Desktop Environment - Icelandic language support.

%description Icelandic -l pl
KDE - wsparcie dla jêzyka islandzkiego.

%package Italian
Summary:	K Desktop Environment - Italian language support
Summary(pl):	KDE - wsparcie dla jêzyka w³oskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Italian
K Desktop Environment - Italian language support.

%description Italian -l pl
KDE - wsparcie dla jêzyka w³oskiego.

%package Japanese
Summary:	K Desktop Environment - Japanese language support
Summary(pl):	KDE - wsparcie dla jêzyka japoñskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Japanese
K Desktop Environment - Japanese language support.

%description Japanese -l pl
KDE - wsparcie dla jêzyka japoñskiego.

%package Kazakh
Summary:	K Desktop Environment - Kazakh language support
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Kazakh
K Desktop Environment - Kazakh language support.

%package Khmer
Summary:	K Desktop Environment - Khmer language support
Summary(pl):	KDE - wsparcie dla jêzyka khmerskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Khmer
K Desktop Environment - Khmer language support.

%description Khmer -l pl
KDE - wsparcie dla jêzyka khmerskiego.

%package Kinyarwanda
Summary:	K Desktop Environment - Kinyarwanda language support
Summary(pl):	KDE - wsparcie dla jêzyka kinya-ruanda
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Kinyarwanda
K Desktop Environment - Kinyarwanda language support.

%description Kinyarwanda -l pl
KDE - wsparcie dla jêzyka kinya-ruanda.

%package Korean
Summary:	K Desktop Environment - Korean language support
Summary(pl):	KDE - wsparcie dla jêzyka koreañskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Korean
K Desktop Environment - Korean language support.

%description Korean -l pl
KDE - wsparcie dla jêzyka koreañskiego.

%package Lithuanian
Summary:	K Desktop Environment - Lithuanian language support
Summary(pl):	KDE - wsparcie dla jêzyka litewskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Lithuanian
K Desktop Environment - Lithuanian language support.

%description Lithuanian -l pl
KDE - Wsparcie dla jêzyka litewskiego.

%package Lao
Summary:	K Desktop Environment - Lao language support
Summary(pl):	KDE - wsparcie dla jêzyka laotañskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Lao
K Desktop Environment - lao language support.

%description Lao -l pl
KDE - wsparcie dla jêzyka laotañskiego.

%package Latvian
Summary:	K Desktop Environment - Latvian language support
Summary(pl):	KDE - wsparcie dla jêzyka ³otewskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Latvian
K Desktop Environment - Latvian language support.

%description Latvian -l pl
KDE - wsparcie dla jêzyka ³otewskiego.

%package Maori
Summary:	K Desktop Environment - Maori language support
Summary(pl):	KDE - wsparcie dla jêzyka maoryjskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Maori
K Desktop Environment - Maori language support.

%description Maori -l pl
KDE - wsparcie dla jêzyka maoryjskiego.

%package Macedonian
Summary:	K Desktop Environment - Macedonian language support
Summary(pl):	KDE - wsparcie dla jêzyka macedoñskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Macedonian
K Desktop Environment - Macedonian language support.

%description Macedonian -l pl
KDE - wsparcie dla jêzyka macedoñskiego.

%package Malay
Summary:	K Desktop Environment - Malay language support
Summary(pl):	KDE - wsparcie dla jêzyka malajskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Malay
K Desktop Environment - Malay language support.

%description Malay -l pl
KDE - wsparcie dla jêzyka malajskiego.

%package Maltese
Summary:	K Desktop Environment - Maltese language support
Summary(pl):	KDE - wsparcie dla jêzyka maltañskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Maltese
K Desktop Environment - Maltese language support.

%description Maltese -l pl
KDE - wsparcie dla jêzyka maltañskiego.

%package Mongolian
Summary:	K Desktop Environment - Mongolian language support
Summary(pl):	KDE - wsparcie dla jêzyka mongolskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Mongolian
K Desktop Environment - Mongolian language support.

%description Mongolian -l pl
KDE - wsparcie dla jêzyka mongolskiego.

%package Low_Saxon
Summary:	K Desktop Environment - Low_Saxon language support
Summary(pl):	KDE - wsparcie dla jêzyka dolnosaksoñskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Low_Saxon
K Desktop Environment - Low_Saxon language support.

%description Low_Saxon -l pl
KDE - wsparcie dla jêzyka dolnosaksoñskiego.

%package Dutch
Summary:	K Desktop Environment - Dutch language support
Summary(pl):	KDE - wsparcie dla jêzyka holenderskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Dutch
K Desktop Environment - Dutch language support.

%description Dutch -l pl
KDE - wsparcie dla jêzyka holenderskiego.

%package Norwegian_Bokmaal
Summary:	K Desktop Environment - Norwegian (Bokmaal) language support
Summary(pl):	KDE - wsparcie dla jêzyka norweskiego (odmiany bokmaal)
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
# "Bookmal" is here intentionally, to allow upgrade from misspelled packages
Obsoletes:	kde-i18n-Norwegian_Bookmal

%description Norwegian_Bokmaal
K Desktop Environment - Norwegian (Bokmaal) language support.

%description Norwegian_Bokmaal -l pl
KDE - wsparcie dla jêzyka norweskiego (odmiany bokmaal).

%package Norwegian_Nynorsk
Summary:	K Desktop Environment - Norwegian (Nynorsk) language support
Summary(pl):	KDE - wsparcie dla jêzyka norweskiego (odmiany nynorsk)
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Norwegian_Nynorsk
K Desktop Environment - Norwegian (Nynorsk) language support.

%description Norwegian_Nynorsk -l pl
KDE - wsparcie dla jêzyka norweskiego (odmiany nynorsk).

%package Northern_Sotho
Summary:	K Desktop Environment - Northern Sotho language support
Summary(pl):	KDE - wsparcie dla pó³nocnej odmiany jêzyka ludu Soto
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Northern_Sotho
K Desktop Environment - Northern Sotho language support.

%description Northern_Sotho -l pl
KDE - wsparcie dla pó³nocnej odmiany jêzyka ludu Soto.

%package Gascon_Occitan
Summary:	K Desktop Environment - Occitan (Gascon) language support
Summary(pl):	KDE - wsparcie dla jêzyka oksytañskiego (dialektu gaskoñskiego)
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	kde-i18n-Gascon_occitan

%description Gascon_Occitan
K Desktop Environment - Occitan (Gascon) language support.

%description Gascon_Occitan -l pl
KDE - wsparcie dla jêzyka oksytañskiego (dialektu gaskoñskiego).

%package Punjabi
Summary:	K Desktop Environment - Punjabi language support
Summary(pl):	KDE - wsparcie dla jêzyka pend¿abskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Punjabi
K Desktop Environment - Punjabi language support.

%description Punjabi -l pl
KDE - wsparcie dla jêzyka pend¿abskiego.

%package Polish
Summary:	K Desktop Environment - Polish language support
Summary(pl):	KDE - wsparcie dla jêzyka polskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Polish
K Desktop Environment - Polish language support.

%description Polish -l pl
KDE - wsparcie dla jêzyka polskiego.

%package Portuguese
Summary:	K Desktop Environment - Portuguese language support
Summary(pl):	KDE - wsparcie dla jêzyka portugalskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
# "Portugnese" is here intentionally, to allow upgrade from misspelled packages
Obsoletes:	kde-i18n-Portugnese

%description Portuguese
K Desktop Environment - Portuguese language support.

%description Portuguese -l pl
KDE - wsparcie dla jêzyka portugalskiego.

%package Brazil_Portuguese
Summary:	K Desktop Environment - Portuguese (Brazil) language support
Summary(pl):	KDE - wsparcie dla jêzyka portugalskiego (odmiany brazylijskiej)
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
# "Brazil_Protugnese" is here intentionally, to allow upgrade from misspelled packages
Obsoletes:	kde-i18n-Brazil_Protugnese

%description Brazil_Portuguese
K Desktop Environment - Portuguese (Brazil) language support.

%description Brazil_Portuguese -l pl
KDE - wsparcie dla jêzyka portugalskiego (odmiany brazylijskiej).

%package Romanian
Summary:	K Desktop Environment - Romanian language support
Summary(pl):	KDE - wsparcie dla jêzyka rumuñskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Romanian
K Desktop Environment - Romanian language support.

%description Romanian -l pl
KDE - wsparcie dla jêzyka rumuñskiego.

%package Russian
Summary:	K Desktop Environment - Russian language support
Summary(pl):	KDE - wsparcie dla jêzyka rosyjskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Russian
K Desktop Environment - Russian language support.

%description Russian -l pl
KDE - wsparcie dla jêzyka rosyjskiego.

%package Swati
Summary:	K Desktop Environment - Swati language support
Summary(pl):	KDE - wsparcie dla jêzyka swati
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Swati
K Desktop Environment - Swati language support.

%description Swati -l pl
KDE - wsparcie dla jêzyka swati.

%package Northern_Sami
Summary:	K Desktop Environment - Northern Sami language support
Summary(pl):	KDE - wsparcie dla pó³nocnego jêzyka saami (lapoñskiego)
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Northern_Sami
K Desktop Environment - Northern Sami language support.

%description Northern_Sami -l pl
KDE - wsparcie dla pó³nocnego jêzyka saami (lapoñskiego).

%package Slovak
Summary:	K Desktop Environment - Slovak language support
Summary(pl):	KDE - wsparcie dla jêzyka s³owackiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Slovak
K Desktop Environment - Slovak language support.

%description Slovak -l pl
KDE - wsparcie dla jêzyka s³owackiego.

%package Slovenian
Summary:	K Desktop Environment - Slovenian language support
Summary(pl):	KDE - wsparcie dla jêzyka s³oweñskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Slovenian
K Desktop Environment - Slovenian language support.

%description Slovenian -l pl
KDE - wsparcie dla jêzyka s³oweñskiego.

%package Serbian
Summary:	K Desktop Environment - Serbian language support
Summary(pl):	KDE - wsparcie dla jêzyka serbskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Serbian
K Desktop Environment - Serbian language support.

%description Serbian -l pl
KDE - wsparcie dla jêzyka serbskiego.

%package Swedish
Summary:	K Desktop Environment - Swedish language support
Summary(pl):	KDE - wsparcie dla jêzyka szwedzkiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Swedish
K Desktop Environment - Swedish language support.

%description Swedish -l pl
KDE - wsparcie dla jêzyka szwedzkiego.

%package Tajik
Summary:	K Desktop Environment - Tajik language support
Summary(pl):	KDE - wsparcie dla jêzyka tad¿yckiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Tajik
K Desktop Environment - Tajik language support.

%description Tajik -l pl
KDE - wsparcie dla jêzyka tad¿yckiego.

%package Tamil
Summary:	K Desktop Environment - Tamil language support
Summary(pl):	KDE - wsparcie dla jêzyka tamilskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Tamil
K Desktop Environment - Tamil language support.

%description Tamil -l pl
KDE - wsparcie dla jêzyka tamilskiego.

%package Thai
Summary:	K Desktop Environment - Thai language support
Summary(pl):	KDE - wsparcie dla jêzyka tajlandzkiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Thai
K Desktop Environment - Thai language support.

%description Thai -l pl
KDE - wsparcie dla jêzyka tajlandzkiego.

%package Turkish
Summary:	K Desktop Environment - Turkish language support
Summary(pl):	KDE - wsparcie dla jêzyka tureckiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Turkish
K Desktop Environment - Turkish language support.

%description Turkish -l pl
KDE - wsparcie dla jêzyka tureckiego.

%package Ukrainian
Summary:	K Desktop Environment - Ukrainian language support
Summary(pl):	KDE - wsparcie dla jêzyka ukraiñskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Ukrainian
K Desktop Environment - Ukrainian language support.

%description Ukrainian -l pl
KDE - wsparcie dla jêzyka ukraiñskiego.

%package Uzbek
Summary:	K Desktop Environment - Uzbek language support
Summary(pl):	KDE - wsparcie dla jêzyka uzbeckiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Uzbek
K Desktop Environment - Uzbek language support.

%description Uzbek -l pl
KDE - wsparcie dla jêzyka uzbeckiego.

%package Venda
Summary:	K Desktop Environment - Venda language support
Summary(pl):	KDE - wsparcie dla jêzyka venda
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Venda
K Desktop Environment - Venda language support.

%description Venda -l pl
KDE - wsparcie dla jêzyka venda.

%package Vietnamese
Summary:	K Desktop Environment - Vietnamese language support
Summary(pl):	KDE - wsparcie dla jêzyka wietnamskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Vietnamese
K Desktop Environment - Vietnamese language support.

%description Vietnamese -l pl
KDE - wsparcie dla jêzyka wietnamskiego.

%package Walloon
Summary:	K Desktop Environment - Walloon language support
Summary(pl):	KDE - wsparcie dla jêzyka waloñskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Walloon
K Desktop Environment - Walloon language support.

%description Walloon -l pl
KDE - wsparcie dla jêzyka waloñskiego.

%package Xhosa
Summary:	K Desktop Environment - Xhosa language support
Summary(pl):	KDE - wsparcie dla jêzyka khosa
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Xhosa
K Desktop Environment - Xhosa language support.

%description Xhosa -l pl
KDE - wsparcie dla jêzyka khosa.

%package Simplified_Chinese
Summary:	K Desktop Environment - simplified Chinese language support
Summary(pl):	KDE - wsparcie dla uproszczonego jêzyka chiñskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Simplified_Chinese
K Desktop Environment - simplified Chinese language support.

%description Simplified_Chinese -l pl
KDE - wsparcie dla uproszczonego jêzyka chiñskiego.

%package Chinese
Summary:	K Desktop Environment - Chinese language support
Summary(pl):	KDE - wsparcie dla jêzyka chiñskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Chinese
K Desktop Environment - Chinese language support.

%description Chinese -l pl
KDE - wsparcie dla jêzyka chiñskiego.

%package Zulu
Summary:	K Desktop Environment - Zulu language support
Summary(pl):	KDE - wsparcie dla jêzyka zuluskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Zulu
K Desktop Environment - Zulu language support.

%description Zulu -l pl
KDE - wsparcie dla jêzyka zuluskiego.

%prep
%setup -qcT %(seq -f '-a %g' 0 64 | xargs)

%build
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
if [ ! -f installed.stamp -o ! -d $RPM_BUILD_ROOT ]; then
	rm -rf $RPM_BUILD_ROOT

	for dir in kde-i18n-*-%{version}; do
		%{__make} -C "$dir" install \
			DESTDIR=$RPM_BUILD_ROOT \
			kde_htmldir="%{_kdedocdir}" \
			kde_libs_htmldir="%{_kdedocdir}"
	done

	# TODO: verify is this renaming ok
	mv $RPM_BUILD_ROOT%{_datadir}/apps/kturtle/examples/de{_DE,}
	mv $RPM_BUILD_ROOT%{_datadir}/apps/kturtle/examples/fr{_FR,}
	mv $RPM_BUILD_ROOT%{_datadir}/apps/kturtle/data/logokeywords.de{_DE,}.xml
	mv $RPM_BUILD_ROOT%{_datadir}/apps/kturtle/data/logokeywords.fr{_FR,}.xml
	mv $RPM_BUILD_ROOT%{_datadir}/apps/katepart/syntax/logohighlightstyle.de{_DE,}.xml
	mv $RPM_BUILD_ROOT%{_datadir}/apps/katepart/syntax/logohighlightstyle.fr{_FR,}.xml

	rm $RPM_BUILD_ROOT/usr/share/locale/fa/COPYING
	rm $RPM_BUILD_ROOT/usr/share/locale/nb/README
	rm $RPM_BUILD_ROOT/usr/share/locale/se/ChangeLog
	rm $RPM_BUILD_ROOT/usr/share/locale/fr/nbsp_gui_fr.txt
	rm $RPM_BUILD_ROOT/usr/share/locale/fr/relecture_docs
	rm $RPM_BUILD_ROOT/usr/share/locale/fr/relecture_gui

	# remove empty language catalogs (= 1 message only)
	find $RPM_BUILD_ROOT%{_datadir}/locale -type f -name '*.mo' | xargs file | egrep ', 1 messages$' | cut -d: -f1 | xargs rm -vf

	touch installed.stamp
fi

rm $RPM_BUILD_ROOT/usr/share/locale/da/da.compendium

FindLang() {
	# $1 - short language name
	local lang="$1"

	echo "%defattr(644,root,root,755)"

	# share/doc/kde/HTML/(%%lang)
	if [ -d "$RPM_BUILD_ROOT%{_kdedocdir}/$lang" ]; then
		echo "%lang($lang) %{_kdedocdir}/$lang"
	fi

	# share/locale/(%%lang)
	if [ -d "$RPM_BUILD_ROOT%{_datadir}/locale/$lang" ]; then
		echo "%lang($lang) %{_datadir}/locale/$lang/[cef]*"
		echo "%lang($lang) %{_datadir}/locale/$lang/LC_MESSAGES/*.mo"
	fi

	# share/apps/amor/tips-(%%lang)
	if [ -f "$RPM_BUILD_ROOT%{_datadir}/apps/amor/tips-$lang" ]; then
		echo "%lang($lang) %{_datadir}/apps/amor/tips-$lang"
	fi

	# share/apps/katepart/syntax/logohighlightstyle.(%%lang).xml
	if [ -f "$RPM_BUILD_ROOT%{_datadir}/apps/katepart/syntax/logohighlightstyle.$lang.xml" ]; then
		echo "%lang($lang) %{_datadir}/apps/katepart/syntax/logohighlightstyle.$lang.xml"
	fi

	# share/apps/ktuberling/sounds/(%%lang)
	if [ -d "$RPM_BUILD_ROOT%{_datadir}/apps/ktuberling/sounds/$lang" ]; then
		echo "%lang($lang) %{_datadir}/apps/ktuberling/sounds/$lang"
	fi

	# share/apps/khangman/(%lang).txt
	if [ -f "$RPM_BUILD_ROOT%{_datadir}/apps/khangman/$lang.txt" ]; then
		echo "%lang($lang) %{_datadir}/apps/khangman/$lang.txt"
	fi

	# share/apps/khangman/data/(%lang)
	if [ -d "$RPM_BUILD_ROOT%{_datadir}/apps/khangman/data/$lang" ]; then
		echo "%lang($lang) %{_datadir}/apps/khangman/data/$lang"
	fi

	# share/apps/klatin/data/vocabs/(%lang)
	if [ -d "$RPM_BUILD_ROOT%{_datadir}/apps/klatin/data/vocabs/$lang" ]; then
		echo "%lang($lang) %{_datadir}/apps/klatin/data/vocabs/$lang"
	fi

	# share/apps/klettres/(%lang)
	if [ -d "$RPM_BUILD_ROOT%{_datadir}/apps/klettres/$lang" ]; then
		echo "%lang($lang) %{_datadir}/apps/klettres/$lang"
	fi

	# share/apps/kturtle/data/logokeywords.(%lang).xml
	if [ -f "$RPM_BUILD_ROOT%{_datadir}/apps/kturtle/data/logokeywords.$lang.xml" ]; then
		echo "%lang($lang) %{_datadir}/apps/kturtle/data/logokeywords.$lang.xml"
	fi

	# share/apps/kturtle/examples/(%lang)
	if [ -d "$RPM_BUILD_ROOT%{_datadir}/apps/kturtle/examples/$lang" ]; then
		echo "%lang($lang) %{_datadir}/apps/kturtle/examples/$lang"
	fi

	# share/apps/kanagram/data/et/elukutsed.kvtml
	if [ -d "$RPM_BUILD_ROOT%{_datadir}/apps/kanagram/data/$lang" ]; then
		echo "%lang($lang) %{_datadir}/apps/kanagram/data/$lang"
	fi

	touch $lang.ok
}

%if 0
# make symlinks relative
for lang in $RPM_BUILD_ROOT%{_kdedocdir}/*; do
	[ -d $lang ] || continue

	if [ ! -d $lang/common ]; then
		ln -s ../en/common $lang/common
	fi

	for i in $lang/*/*/*; do
		if [ -d $i -a -L $i/common ]; then
			rm -f $i/common
			ln -sf ../../../common $i
		fi
	done

	for i in $lang/*/*; do
		if [ -d $i -a -L $i/common ]; then
			rm -f $i/common
			ln -sf ../../common $i
		fi
	done

	for i in $lang/*; do
		if [ -d $i -a -L $i/common ]; then
			rm -f $i/common
			ln -sf ../common $i
		fi
	done
done
%endif

rm -f *.lang *.cache __find.* *.ok

FindLang af > Afrikaans.lang
FindLang ar > Arabic.lang
FindLang az > Azerbaijani.lang
FindLang bg > Bulgarian.lang
FindLang bn > Bengali.lang
FindLang br > Breton.lang
FindLang bs > Bosnian.lang
FindLang ca > Catalan.lang
FindLang cs > Czech.lang
FindLang cy > Cymraeg.lang
FindLang da > Danish.lang
FindLang de > German.lang
FindLang el > Greek.lang
# FindLang en > English.lang
FindLang en_GB > English_UK.lang
FindLang eo > Esperanto.lang
FindLang es > Spanish.lang
FindLang et > Estonian.lang
FindLang eu > Basque.lang
FindLang fa > Farsi.lang
FindLang fi > Finnish.lang
FindLang fr > French.lang
FindLang fy > Frisian.lang
FindLang ga > Irish.lang
FindLang gl > Galician.lang
FindLang he > Hebrew.lang
FindLang hi > Hindi.lang
FindLang hr > Croatian.lang
#FindLang hsb > Upper_Sorbian.lang
FindLang hu > Hungarian.lang
# FindLang id > Indonesian.lang
FindLang is > Icelandic.lang
FindLang it > Italian.lang
FindLang ja > Japanese.lang
FindLang kk > Kazakh.lang
FindLang km > Khmer.lang
FindLang ko > Korean.lang
FindLang lt > Lithuanian.lang
FindLang lv > Latvian.lang
# FindLang mi > Maori.lang
FindLang mk > Macedonian.lang
FindLang mn > Mongolian.lang
FindLang ms > Malay.lang
##FindLang mt > Maltese.lang
FindLang nb > Norwegian_Bokmaal.lang
FindLang nds > Low_Saxon.lang
FindLang nl > Dutch.lang
FindLang nn > Norwegian_Nynorsk.lang
FindLang pa > Punjabi.lang
#indLang nso > Northern_Sotho.lang
# FindLang oc > Gascon_Occitan.lang
FindLang pl > Polish.lang
FindLang pt > Portuguese.lang
FindLang pt_BR > Brazil_Portuguese.lang
FindLang ro > Romanian.lang
FindLang rw > Kinyarwanda.lang
FindLang ru > Russian.lang
FindLang ss > Swati.lang
FindLang se > Northern_Sami.lang
FindLang sk > Slovak.lang
FindLang sl > Slovenian.lang
FindLang sr > Serbian.lang
FindLang sr@Latn >> Serbian.lang
FindLang sv > Swedish.lang
FindLang ta > Tamil.lang
FindLang tg > Tajik.lang
##FindLang th > Thai.lang
FindLang tr > Turkish.lang
FindLang uk > Ukrainian.lang
FindLang uz > Uzbek.lang
##FindLang ven > Venda.lang
FindLang vi > Vietnamese.lang
# FindLang wa > Walloon.lang
##FindLang xh > Xhosa.lang
FindLang zh_CN > Simplified_Chinese.lang
FindLang zh_TW > Chinese.lang
##FindLang zu > Zulu.lang

check_installed_languages() {
	err=0
	# we ignore dialects (currently sr@Latn is the only case)
	for a in $(ls -1d %{name}-*-%{version} | %{__sed} '/@/d'); do
		l=${a#%{name}-}
		l=${l%%-%{version}}
		if [ ! -f $l.ok ]; then
			echo >&2 "language $l not processed"
			err=1
		fi
	done
	if [ "$err" = 1 ]; then
		exit 1
	fi
}
check_installed_languages

%if %{with alltogether}
cat [A-Z]*.lang > all.lang
%endif

%clean
check_installed_files() {
	err=0
	for a in *.lang; do
		lang=${a%%.lang}

		rpmfile=%{_rpmdir}/%{name}-$lang-%{version}-%{release}.%{_target_cpu}.rpm
		if [ ! -f $rpmfile ]; then
			echo >&2 "Missing %%files section for $lang"
			err=1
		fi
	done
	if [ "$err" = 1 ]; then
		exit 1
	fi
}
check_installed_files
%{!?debug:rm -rf $RPM_BUILD_ROOT}

%files base
%defattr(644,root,root,755)

%if %{without alltogether}
%files -f Afrikaans.lang Afrikaans
%defattr(644,root,root,755)

%files -f Arabic.lang Arabic
%defattr(644,root,root,755)

%files -f Azerbaijani.lang Azerbaijani
%defattr(644,root,root,755)

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

%files -f Galician.lang Galician
%defattr(644,root,root,755)

%files -f Hindi.lang Hindi
%defattr(644,root,root,755)

%files -f Hebrew.lang Hebrew
%defattr(644,root,root,755)

%files -f Croatian.lang Croatian
%defattr(644,root,root,755)

#%files -f Upper_Sorbian.lang Upper_Sorbian
#%defattr(644,root,root,755)

%files -f Hungarian.lang Hungarian
%defattr(644,root,root,755)

##%files -f Indonesian.lang Indonesian
%files -f Icelandic.lang Icelandic
%defattr(644,root,root,755)

%files -f Italian.lang Italian
%defattr(644,root,root,755)

%files -f Japanese.lang Japanese
%defattr(644,root,root,755)

%files -f Kazakh.lang Kazakh
%defattr(644,root,root,755)

%files -f Khmer.lang Khmer
%defattr(644,root,root,755)

%files -f Korean.lang Korean
%defattr(644,root,root,755)

%files -f Lithuanian.lang Lithuanian
%defattr(644,root,root,755)

%files -f Kinyarwanda.lang Kinyarwanda
%defattr(644,root,root,755)

%files -f Latvian.lang Latvian
%defattr(644,root,root,755)

#%%files -f Maltese.lang Maltese
%files -f Malay.lang Malay
%defattr(644,root,root,755)

%files -f Mongolian.lang Mongolian
%defattr(644,root,root,755)

#%files -f Maori.lang Maori
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
#%%files -f Gascon_Occitan.lang Gascon_Occitan

%files -f Punjabi.lang Punjabi
%defattr(644,root,root,755)

%files -f Polish.lang Polish
%defattr(644,root,root,755)

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

%files -f Swati.lang Swati
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

%files -f Vietnamese.lang Vietnamese
%defattr(644,root,root,755)

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
