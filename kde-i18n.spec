# TODO:
# - add files to some ko locale
# - huge unpackaged list: http://glen.alkohol.ee/pld/kde-i18n-3.5.5.txt
#
# Conditional build:
%bcond_with	alltogether		# build single package containing support for all languages

%define		_state		stable
%define		_minlibsevr	9:%{version}

Summary:	K Desktop Environment - international support
Summary(pl):	KDE - wsparcie dla wielu j�zyk�w
Name:		kde-i18n
Version:	3.5.5
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-af-%{version}.tar.bz2
# Source0-md5:	3de24c2c32aba906b9e2cea304b151be
Source1:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-ar-%{version}.tar.bz2
# Source1-md5:	237879698e967ba9384b6800f8517ce2
Source2:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-az-%{version}.tar.bz2
# Source2-md5:	c63e0b5e0682571498b168e6f6707caf
Source3:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-bg-%{version}.tar.bz2
# Source3-md5:	28871147d247f33072a278f0d16a96be
Source4:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-bn-%{version}.tar.bz2
# Source4-md5:	bfd5159743442c47a02ee5af4bd17c68
Source5:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-br-%{version}.tar.bz2
# Source5-md5:	f96e07c3b9f4905dc3f37eb829feba89
Source6:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-bs-%{version}.tar.bz2
# Source6-md5:	8441891d28b9785504ab1151a603d8f4
Source7:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-ca-%{version}.tar.bz2
# Source7-md5:	fec16708dc8c3e9a864d5ad9e45f06b8
Source8:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-cs-%{version}.tar.bz2
# Source8-md5:	aaace6da2097b2f98f163a5da7667752
Source9:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-cy-%{version}.tar.bz2
# Source9-md5:	fae86d2ffa550c4d831eeb9a5a3ecdb2
Source10:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-da-%{version}.tar.bz2
# Source10-md5:	70c041ca96330834c6f988255d7bd6ae
Source11:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-de-%{version}.tar.bz2
# Source11-md5:	a99bf0e5d298fce191ad2c938af3afdb
Source12:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-el-%{version}.tar.bz2
# Source12-md5:	a2cb7afd4c5883bc2eb5d9c8a96d04c0
Source13:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-en_GB-%{version}.tar.bz2
# Source13-md5:	50af460c4b69e5cd91b820ed656f99bd
Source14:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-eo-%{version}.tar.bz2
# Source14-md5:	c55c9ae0c001e5214f1ad97f4b6d02a1
Source15:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-es-%{version}.tar.bz2
# Source15-md5:	d8dc649138fe136c57a808eac1fdd719
Source16:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-et-%{version}.tar.bz2
# Source16-md5:	d3065d66591fa0ea4e304e9bcbb6dc10
Source17:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-eu-%{version}.tar.bz2
# Source17-md5:	45a4361f11c14b8cbc0a5bb29ab18edb
Source18:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-fa-%{version}.tar.bz2
# Source18-md5:	e55d8c8d06097b3daaa71eb499114e3d
Source19:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-fi-%{version}.tar.bz2
# Source19-md5:	5693b184f6d3e2d79c78248a9506ba11
Source20:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-fr-%{version}.tar.bz2
# Source20-md5:	0a0e9ba98b33e81a092110563def9ca4
Source21:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-fy-%{version}.tar.bz2
# Source21-md5:	98a3bbe04e82b89c8ab2a821741ffc34
Source22:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-ga-%{version}.tar.bz2
# Source22-md5:	e82a3ff13cb0f8d73578f1a3770a119c
Source23:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-gl-%{version}.tar.bz2
# Source23-md5:	bf3ad88fea56ded7fd451cc83826e4c5
Source24:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-he-%{version}.tar.bz2
# Source24-md5:	2099f23192fe79f1e94c0da2184871c0
Source25:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-hi-%{version}.tar.bz2
# Source25-md5:	a046a16fd6575ee67a9086702414bac1
Source26:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-hr-%{version}.tar.bz2
# Source26-md5:	486262b00bab42965aa0d25c86d65f84
Source27:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-hu-%{version}.tar.bz2
# Source27-md5:	9638821a380cf7a8697b03dca2f3513d
Source28:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-is-%{version}.tar.bz2
# Source28-md5:	4bdd95af464b36e7d52b4848291c9717
Source29:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-it-%{version}.tar.bz2
# Source29-md5:	a69220e5a700a277238924a3675d9dbd
Source30:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-ja-%{version}.tar.bz2
# Source30-md5:	3b89aa140388f7b0e3beb80ef2b8b247
Source31:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-km-%{version}.tar.bz2
# Source31-md5:	c11c4653c9e211deb4c16bf346bd03ad
Source32:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-ko-%{version}.tar.bz2
# Source32-md5:	7a364e95e894e9c58d56054edab21142
Source33:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-lt-%{version}.tar.bz2
# Source33-md5:	aa799b8fac440c0b70188e0f9df16350
Source34:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-lv-%{version}.tar.bz2
# Source34-md5:	f541bb2957e1f0469d76711cc86ba851
Source35:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-mk-%{version}.tar.bz2
# Source35-md5:	014b290f599e808ff3b885c50d150fe5
Source36:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-mn-%{version}.tar.bz2
# Source36-md5:	67fb64745786c2ef908b192432e51040
Source37:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-ms-%{version}.tar.bz2
# Source37-md5:	2757eb622ace8a2f231dda1bd5cd454d
Source38:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-nb-%{version}.tar.bz2
# Source38-md5:	1b3edcfa11bb648e98bab07f93e898a9
Source39:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-nds-%{version}.tar.bz2
# Source39-md5:	f159dd39c2385403a0f95c0b102ef67b
Source40:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-nl-%{version}.tar.bz2
# Source40-md5:	44b404fc4d0b9d12714fdf2357fa3f56
Source41:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-nn-%{version}.tar.bz2
# Source41-md5:	964c91710f2b28cdde7b8cdfef961791
Source42:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-pa-%{version}.tar.bz2
# Source42-md5:	1881a7e5b1fc6b75ca74dc4c504ad16d
Source43:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-pl-%{version}.tar.bz2
# Source43-md5:	7444560d7d6cb3221e8f0907218157de
Source44:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-pt-%{version}.tar.bz2
# Source44-md5:	af8b477236f98e0fa7fcae21db3df5cc
Source45:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-pt_BR-%{version}.tar.bz2
# Source45-md5:	d9359ccc0040a5c6ac88d5cad12d4fcf
Source46:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-ro-%{version}.tar.bz2
# Source46-md5:	b31d031cbf2deae408c94a665677dfd2
Source47:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-ru-%{version}.tar.bz2
# Source47-md5:	4bfa140a22122446fd8ab356d32fee40
Source48:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-rw-%{version}.tar.bz2
# Source48-md5:	b94681f15ccb61cd9760e2e7830e7592
Source49:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-se-%{version}.tar.bz2
# Source49-md5:	4492ee7304d4539b3dfd4d1349c6a838
Source50:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-sk-%{version}.tar.bz2
# Source50-md5:	0a1bccde30cf25cf37974362585b118a
Source51:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-sl-%{version}.tar.bz2
# Source51-md5:	3574861dc47aa09ada8cc6c7bca2307e
Source52:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-sr-%{version}.tar.bz2
# Source52-md5:	e308f4f37c5509bd5583f7fcd90bcb32
Source53:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-sr@Latn-%{version}.tar.bz2
# Source53-md5:	0e3d6ba65882faadc89791c3691b19b6
Source54:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-ss-%{version}.tar.bz2
# Source54-md5:	8a08733c9cd4d367a42f0c0a69accc8a
Source55:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-sv-%{version}.tar.bz2
# Source55-md5:	0a614fc596f082a1a11d7ee91b1bae2a
Source56:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-ta-%{version}.tar.bz2
# Source56-md5:	4ab3c05628fc635609218d17cce6d138
Source57:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-tg-%{version}.tar.bz2
# Source57-md5:	135a419bb0d3429dde4bc698d095bf86
Source58:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-tr-%{version}.tar.bz2
# Source58-md5:	001d5909b3fd8121b1f4f7970d88215b
Source59:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-uk-%{version}.tar.bz2
# Source59-md5:	fc18b699825837e49e3062e5acc0a3f5
Source60:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-uz-%{version}.tar.bz2
# Source60-md5:	b66b574eff1fd2349a9a767098e5430e
Source61:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-zh_CN-%{version}.tar.bz2
# Source61-md5:	c0df78b39982a1ba117539e86c0dabb8
Source62:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-zh_TW-%{version}.tar.bz2
# Source62-md5:	6c1051a985f68563380844dec9080248

%if %{with alltogether}
# NOTE:		"Affrikaans", "Norwegian_Bookmal" and "Portugnese" are here
# intentionally, to allow upgrade from packages with misspelled names
Requires:	kde-i18n-base
Obsoletes:	kde-i18n-Affrikaans
Obsoletes:	kde-i18n-Afrikaans
Obsoletes:	kde-i18n-Arabic
Obsoletes:	kde-i18n-Azerbaijani
Obsoletes:	kde-i18n-Basque
Obsoletes:	kde-i18n-Bengali
Obsoletes:	kde-i18n-Bosnian
Obsoletes:	kde-i18n-Brazil
Obsoletes:	kde-i18n-Brazil_Portugnese
Obsoletes:	kde-i18n-Brazil_Portuguese
Obsoletes:	kde-i18n-British
Obsoletes:	kde-i18n-Bulgarian
Obsoletes:	kde-i18n-Catalan
Obsoletes:	kde-i18n-Chinese
Obsoletes:	kde-i18n-Chinese-Big5
Obsoletes:	kde-i18n-Croatian
Obsoletes:	kde-i18n-Cymraeg
Obsoletes:	kde-i18n-Czech
Obsoletes:	kde-i18n-Danish
Obsoletes:	kde-i18n-Dutch
Obsoletes:	kde-i18n-English_UK
Obsoletes:	kde-i18n-Esperanto
Obsoletes:	kde-i18n-Estonian
Obsoletes:	kde-i18n-Farsi
Obsoletes:	kde-i18n-Finnish
Obsoletes:	kde-i18n-French
Obsoletes:	kde-i18n-Frisian
Obsoletes:	kde-i18n-Galician
Obsoletes:	kde-i18n-Gascon_Occitan
Obsoletes:	kde-i18n-Gascon_occitan
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
Obsoletes:	kde-i18n-Norwegian
Obsoletes:	kde-i18n-Norwegian_Bokmaal
Obsoletes:	kde-i18n-Norwegian_Bookmal
Obsoletes:	kde-i18n-Norwegian_Nynorsk
Obsoletes:	kde-i18n-Polish
Obsoletes:	kde-i18n-Portugnese
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
###BuildRequires:	unsermake >= 040511
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
Summary(pl):	KDE - wsparcie dla j�zyka fryzyjskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Frisian
K Desktop Environment - Frisian language support.

%description Frisian -l pl
KDE - wsparcie dla j�zyka fryzyjskiego.

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

%package Khmer
Summary:	K Desktop Environment - Khmer language support
Summary(pl):	KDE - wsparcie dla j�zyka khmerskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Khmer
K Desktop Environment - Khmer language support.

%description Khmer -l pl
KDE - wsparcie dla j�zyka khmerskiego.

%package Kinyarwanda
Summary:	K Desktop Environment - Kinyarwanda language support
Summary(pl):	KDE - wsparcie dla j�zyka kinya-ruanda
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Kinyarwanda
K Desktop Environment - Kinyarwanda language support.

%description Kinyarwanda -l pl
KDE - wsparcie dla j�zyka kinya-ruanda.

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

%package Gascon_Occitan
Summary:	K Desktop Environment - Occitan (Gascon) language support
Summary(pl):	KDE - wsparcie dla j�zyka oksyta�skiego (dialektu gasko�skiego)
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	kde-i18n-Gascon_occitan

%description Gascon_Occitan
K Desktop Environment - Occitan (Gascon) language support.

%description Gascon_Occitan -l pl
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
Obsoletes:	kde-i18n-Portugnese

%description Portuguese
K Desktop Environment - Portuguese language support.

%description Portuguese -l pl
KDE - wsparcie dla j�zyka portugalskiego.

%package Brazil_Portuguese
Summary:	K Desktop Environment - Portuguese (Brazil) language support
Summary(pl):	KDE - wsparcie dla j�zyka portugalskiego (odmiany brazylijskiej)
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	kde-i18n-Brazil_Protugnese

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

%build
export kde_htmldir="%{_kdedocdir}"
export kde_libs_htmldir="%{_kdedocdir}"

LDFLAGS="%{rpmldflags}"

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

	# remove empty language catalogs (= 1 message only)
	find $RPM_BUILD_ROOT%{_datadir}/locale -type f -name '*.mo' | xargs file | egrep ', 1 messages$' | cut -d: -f1 | xargs rm -vf

	touch installed.stamp
fi

FindLang() {
#    $1 - short language name
#    $2 - long language name
	local lang="$1"
	local language="$2"

	echo "%defattr(644,root,root,755)" > "$language.lang"

# share/doc/kde/HTML/(%%lang)
	if [ -d "$RPM_BUILD_ROOT%{_kdedocdir}/$lang" ]; then
		echo "%lang($lang) %{_kdedocdir}/$lang" >> "$language.lang"
	fi

# share/locale/(%%lang)
	if [ -d "$RPM_BUILD_ROOT%{_datadir}/locale/$lang" ]; then
		echo "%lang($lang) %{_datadir}/locale/$lang/[cef]*" >> "$language.lang"
		echo "%lang($lang) %{_datadir}/locale/$lang/LC_MESSAGES/*.mo" >> "$language.lang"
	fi

# share/apps/amor/tips-(%%lang)
	if [ -f "$RPM_BUILD_ROOT%{_datadir}/apps/amor/tips-$lang" ]; then
		echo "%lang($lang) %{_datadir}/apps/amor/tips-$lang" >> "$language.lang"
	fi

# share/apps/katepart/syntax/logohighlightstyle.(%%lang).xml
	if [ -f "$RPM_BUILD_ROOT%{_datadir}/apps/katepart/syntax/logohighlightstyle.$lang.xml" ]; then
		echo "%lang($lang) %{_datadir}/apps/katepart/syntax/logohighlightstyle.$lang.xml" >> "$language.lang"
	fi

# share/apps/ktuberling/sounds/(%%lang)
	if [ -d "$RPM_BUILD_ROOT%{_datadir}/apps/ktuberling/sounds/$lang" ]; then
		echo "%lang($lang) %{_datadir}/apps/ktuberling/sounds/$lang" >> "$language.lang"
	fi

# share/apps/khangman/(%lang).txt
	if [ -f "$RPM_BUILD_ROOT%{_datadir}/apps/khangman/$lang.txt" ]; then
		echo "%lang($lang) %{_datadir}/apps/khangman/$lang.txt" >> "$language.lang"
	fi

# share/apps/khangman/data/(%lang)
	if [ -d "$RPM_BUILD_ROOT%{_datadir}/apps/khangman/data/$lang" ]; then
		echo "%lang($lang) %{_datadir}/apps/khangman/data/$lang" >> "$language.lang"
	fi

# share/apps/klatin/data/vocabs/(%lang)
	if [ -d "$RPM_BUILD_ROOT%{_datadir}/apps/klatin/data/vocabs/$lang" ]; then
		echo "%lang($lang) %{_datadir}/apps/klatin/data/vocabs/$lang" >> "$language.lang"
	fi

# share/apps/klettres/(%lang)
	if [ -d "$RPM_BUILD_ROOT%{_datadir}/apps/klettres/$lang" ]; then
		echo "%lang($lang) %{_datadir}/apps/klettres/$lang" >> "$language.lang"
	fi

# share/apps/kturtle/data/logokeywords.(%lang).xml
	if [ -f "$RPM_BUILD_ROOT%{_datadir}/apps/kturtle/data/logokeywords.$lang.xml" ]; then
		echo "%lang($lang) %{_datadir}/apps/kturtle/data/logokeywords.$lang.xml" >> "$language.lang"
	fi

# share/apps/kturtle/examples/(%lang)
	if [ -d "$RPM_BUILD_ROOT%{_datadir}/apps/kturtle/examples/$lang" ]; then
		echo "%lang($lang) %{_datadir}/apps/kturtle/examples/$lang" >> "$language.lang"
	fi

# share/apps/kanagram/data/et/elukutsed.kvtml
	if [ -d "$RPM_BUILD_ROOT%{_datadir}/apps/kanagram/data/$lang" ]; then
		echo "%lang($lang) %{_datadir}/apps/kanagram/data/$lang" >> "$language.lang"
	fi
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

rm -f *.lang *.cache __find.*

FindLang af Afrikaans
FindLang ar Arabic
FindLang az Azerbaijani
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
FindLang gl Galician
FindLang he Hebrew
FindLang hi Hindi
FindLang hr Croatian
#FindLang hsb Upper_Sorbian
FindLang hu Hungarian
# FindLang id Indonesian
FindLang is Icelandic
FindLang it Italian
FindLang ja Japanese
FindLang km Khmer
FindLang ko Korean
FindLang lt Lithuanian
FindLang lv Latvian
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
# FindLang oc Gascon_Occitan
FindLang pl Polish
FindLang pt Portuguese
FindLang pt_BR Brazil_Portuguese
FindLang ro Romanian
FindLang rw Kinyarwanda
FindLang ru Russian
##FindLang ss Swati
FindLang se Northern_Sami
FindLang sk Slovak
FindLang sl Slovenian
FindLang sr Serbian
FindLang sr@Latn Serbian_Latin
cat Serbian_Latin.lang >> Serbian.lang
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
cat [A-Z]*.lang > all.lang
%endif

%clean
rm -rf $RPM_BUILD_ROOT

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
# %files -f Gascon_Occitan.lang Gascon_Occitan

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
