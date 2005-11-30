#
# Conditional build:
%bcond_with	alltogether		# build single package containing support
					# for all languages
%define	_kdever	3.5

Summary:	K Desktop Environment - international support
Summary(pl):	KDE - wsparcie dla wielu jêzyków
Name:		kde-i18n
Version:	3.5.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:        ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-af-%{version}.tar.bz2
# Source0-md5:	147f1e8d2fbc34044803a001d7bcdfa5
Source1:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-ar-%{version}.tar.bz2
# Source1-md5:	ddae126b0e6f157c7ab216886da9a9cc
Source2:        ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-az-%{version}.tar.bz2
# Source2-md5:	9ca3b621dbe45ffcaec01050e7cd723c
Source3:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-bg-%{version}.tar.bz2
# Source3-md5:	14a1c0ffca9b70befd62aac08a76ce26
Source4:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-bn-%{version}.tar.bz2
# Source4-md5:	76eb28c1ace6f2279657d8574f9f0814
Source5:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-br-%{version}.tar.bz2
# Source5-md5:	88ada204a76c69b594d704fdefc102eb
Source6:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-bs-%{version}.tar.bz2
# Source6-md5:	f7c7e067fc001592eda493be30d84f8d
Source7:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-ca-%{version}.tar.bz2
# Source7-md5:	1757ccb438e4cc2edb9c5af7c0ffc736
Source8:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-cs-%{version}.tar.bz2
# Source8-md5:	d7ccfd209c90ddb92e60476481bd20e3
Source9:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-cy-%{version}.tar.bz2
# Source9-md5:	77be5513037a06d51e287d262a50afbe
Source10:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-da-%{version}.tar.bz2
# Source10-md5:	2fabb8a20a0c197b4749b93359d25fc1
Source11:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-de-%{version}.tar.bz2
# Source11-md5:	71e66fbc6d497808364ff2ae02e2f9a3
Source12:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-el-%{version}.tar.bz2
# Source12-md5:	bd70e25fc9ad9ac7c09584bab498cf4c
Source13:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-en_GB-%{version}.tar.bz2
# Source13-md5:	bb505653bdd061665b48dd1438a7373d
Source14:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-eo-%{version}.tar.bz2
# Source14-md5:	0028cfb93075bba73d902d68d56ab529
Source15:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-es-%{version}.tar.bz2
# Source15-md5:	8bf984ce3aaaa7d58156458d4eafd5bd
Source16:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-et-%{version}.tar.bz2
# Source16-md5:	4c6be2284f34897fffa4cdce85f51fb4
Source17:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-eu-%{version}.tar.bz2
# Source17-md5:	ef6917edb2c87f2386feb7c1b2d175c7
Source18:        ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-fa-%{version}.tar.bz2
# Source18-md5:	e4e976adb8eb5150ff35436f38f4e218
Source19:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-fi-%{version}.tar.bz2
# Source19-md5:	f4b68d979d9181561e04e0ec3cb6c5f2
Source20:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-fr-%{version}.tar.bz2
# Source20-md5:	aec9d5ab04f9dc5a3cc4a8093bd9f7d4
Source21:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-fy-%{version}.tar.bz2
# Source21-md5:	643d1f5d1ff3a21e2b16a8bcdd4b477d
Source22:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-ga-%{version}.tar.bz2
# Source22-md5:	b98c98d80e2a5f8e4d1935df49ad92f0
Source23:        ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-gl-%{version}.tar.bz2
# Source23-md5:	a9b224d7a4cc7011401e7b8b305667f5
Source24:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-he-%{version}.tar.bz2
# Source24-md5:	3a5c77420709d437521c2a9b7d4183a5
Source25:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-hi-%{version}.tar.bz2
# Source25-md5:	afdc78d57f13e7999178d5784222e0be
Source26:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-hr-%{version}.tar.bz2
# Source26-md5:	04fcf08871542ff837a56c33b1544f5e
Source27:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-hu-%{version}.tar.bz2
# Source27-md5:	9e4108754b8b9d84157f8a139749f96e
Source28:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-is-%{version}.tar.bz2
# Source28-md5:	9ecfc0c82796bca3f7cbb621b2535b51
Source29:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-it-%{version}.tar.bz2
# Source29-md5:	1d2c594bf5c6f853822ae869ae101373
Source30:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-ja-%{version}.tar.bz2
# Source30-md5:	404c4ad98acc237eb4ea36b1b637f708
Source31:        ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-km-%{version}.tar.bz2
# Source31-md5:	b3aebc0c475b6a297d15bef69d630483
Source32:        ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-ko-%{version}.tar.bz2
# Source32-md5:	6e04c93815138fb78b182e82335a2b74
Source33:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-lt-%{version}.tar.bz2
# Source33-md5:	f03e5c7dac20f93f215c01e4f76de2bc
Source34:        ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-lv-%{version}.tar.bz2
# Source34-md5:	4c3f19b6208784da447535d39cbe617b
Source35:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-mk-%{version}.tar.bz2
# Source35-md5:	e047bf6f6eb21af2530781aabe871c55
Source36:        ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-mn-%{version}.tar.bz2
# Source36-md5:	8dde14be38b61dd41e6a7ed456203370
Source37:        ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-ms-%{version}.tar.bz2
# Source37-md5:	ea00b5ade265ab07513ba3c61443daaf
Source38:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-nb-%{version}.tar.bz2
# Source38-md5:	a9d408cb53d33d9ad2a27b7e75878ff2
Source39:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-nds-%{version}.tar.bz2
# Source39-md5:	11c2c720ca547e95ae0e3ff620525219
Source40:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-nl-%{version}.tar.bz2
# Source40-md5:	5253d78852e4692abbfaf422eb13612f
Source41:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-nn-%{version}.tar.bz2
# Source41-md5:	e8f4d8fc6600f34667c2426908e9e87c
Source42:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-pa-%{version}.tar.bz2
# Source42-md5:	c62a690a4e8e2f20da3e69ad9459168b
Source43:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-pl-%{version}.tar.bz2
# Source43-md5:	dd1a8db5e7ac7fb7fbf88fc89c6248d6
Source44:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-pt-%{version}.tar.bz2
# Source44-md5:	14e6a97e5f03902449ef7f79a8c6ca3f
Source45:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-pt_BR-%{version}.tar.bz2
# Source45-md5:	94bf46c3b6b3f2f3d315c17b7b0df496
Source46:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-ro-%{version}.tar.bz2
# Source46-md5:	5dcaf0e47bc367bbc8a93b8325e95007
Source47:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-ru-%{version}.tar.bz2
# Source47-md5:	8f6c9961e3df806d1bb2ecab073436fe
Source48:        ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-rw-%{version}.tar.bz2
# Source48-md5:	69c161066d1f8f51b9442728b8d1939a
Source49:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-se-%{version}.tar.bz2
# Source49-md5:	12eda3a6000f45624dba73a43e0151db
Source50:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-sk-%{version}.tar.bz2
# Source50-md5:	64289a8a8d2ffd4de136faca3b901453
Source51:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-sl-%{version}.tar.bz2
# Source51-md5:	29618443a77a8b657f6003ce28db8471
Source52:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-sr-%{version}.tar.bz2
# Source52-md5:	305e7594a705c1ffaf566f0adb543dc8
Source53:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-sr@Latn-%{version}.tar.bz2
# Source53-md5:	f3a2dfb04cfa1d41ec55d2e5112654a7
Source54:        ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-ss-%{version}.tar.bz2
# Source54-md5:	5a787015dfd4ac97defae1e05358e4ec
Source55:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-sv-%{version}.tar.bz2
# Source55-md5:	34837afb8eb7c808ffeecdb7dff66a98
Source56:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-ta-%{version}.tar.bz2
# Source56-md5:	4776430c0e6d5aa4455ebc8406e8a373
Source57:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-tg-%{version}.tar.bz2
# Source57-md5:	33331fd43fa6f7026ca40dd95184dfa2
Source58:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-tr-%{version}.tar.bz2
# Source58-md5:	0fd7a1e932ec5bf1bfe494ee00b3cd09
Source59:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-uk-%{version}.tar.bz2
# Source59-md5:	039bf39e0b7df0906358667f2bbefe46
Source60:        ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-uz-%{version}.tar.bz2
# Source60-md5:	2b443fcb4e226bb8ce18829e734e6ad7
Source61:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-zh_CN-%{version}.tar.bz2
# Source61-md5:	aba75e252510e999a17650994934065c
Source62:        ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/kde-i18n/%{name}-zh_TW-%{version}.tar.bz2
# Source62-md5:	833f3c6c4ae5ea433509ff48de88019a

%if %{with alltogether}
# NOTE: "Affrikaans", "Norwegian_Bookmal" and "Portugnese" are here
# intentionally, to allow upgrade from packages with misspelled names
Obsoletes:	kde-i18n-Affrikaans
Obsoletes:	kde-i18n-Afrikaans
Obsoletes:	kde-i18n-Arabic
Obsoletes:	kde-i18n-Azerbaijani
Obsoletes:	kde-i18n-Bengali
Obsoletes:	kde-i18n-Bosnian
Obsoletes:	kde-i18n-Bulgarian
Obsoletes:	kde-i18n-Catalan
Obsoletes:	kde-i18n-Cymraeg
Obsoletes:	kde-i18n-Czech
Obsoletes:	kde-i18n-Danish
Obsoletes:	kde-i18n-German
Obsoletes:	kde-i18n-Greek
Obsoletes:	kde-i18n-English_UK
Obsoletes:	kde-i18n-British
Obsoletes:	kde-i18n-Esperanto
Obsoletes:	kde-i18n-Spanish
Obsoletes:	kde-i18n-Estonian
Obsoletes:	kde-i18n-Basque
Obsoletes:	kde-i18n-Farsi
Obsoletes:	kde-i18n-Finnish
Obsoletes:	kde-i18n-French
Obsoletes:	kde-i18n-Frisian
Obsoletes:	kde-i18n-Irish
Obsoletes:	kde-i18n-Galician
Obsoletes:	kde-i18n-Hebrew
Obsoletes:	kde-i18n-Hindi
Obsoletes:	kde-i18n-Croatian
Obsoletes:	kde-i18n-Upper_Sorbian
Obsoletes:	kde-i18n-Hungarian
Obsoletes:	kde-i18n-Indonesian
Obsoletes:	kde-i18n-Icelandic
Obsoletes:	kde-i18n-Italian
Obsoletes:	kde-i18n-Japanese
Obsoletes:	kde-i18n-Korean
Obsoletes:	kde-i18n-Lithuanian
Obsoletes:	kde-i18n-Lao
Obsoletes:	kde-i18n-Latvian
Obsoletes:	kde-i18n-Maori
Obsoletes:	kde-i18n-Macedonian
Obsoletes:	kde-i18n-Maltese
Obsoletes:	kde-i18n-Malay
Obsoletes:	kde-i18n-Mongolian
Obsoletes:	kde-i18n-Low_Saxon
Obsoletes:	kde-i18n-Dutch
Obsoletes:	kde-i18n-Norwegian
Obsoletes:	kde-i18n-Norwegian_Bokmaal
Obsoletes:	kde-i18n-Norwegian_Bookmal
Obsoletes:	kde-i18n-Norwegian_Nynorsk
Obsoletes:	kde-i18n-Northern_Sotho
Obsoletes:	kde-i18n-Gascon_occitan
Obsoletes:	kde-i18n-Gascon_Occitan
Obsoletes:	kde-i18n-Punjabi
Obsoletes:	kde-i18n-Polish
Obsoletes:	kde-i18n-Portugnese
Obsoletes:	kde-i18n-Portuguese
Obsoletes:	kde-i18n-Brazil
Obsoletes:	kde-i18n-Brazil_Portugnese
Obsoletes:	kde-i18n-Brazil_Portuguese
Obsoletes:	kde-i18n-Romanian
Obsoletes:	kde-i18n-Russian
Obsoletes:	kde-i18n-Swati
Obsoletes:	kde-i18n-Northern_Sami
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
Obsoletes:	kde-i18n-Walloon
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
KDE - wsparcie dla wielu jêzyków.

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
Summary(pl):	KDE - wsparcie dla jêzyka Frisian
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Frisian
K Desktop Environment - Frisian language support.

%description Frisian -l pl
KDE - wsparcie dla jêzyka Frisian.

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
Obsoletes:	%{name}-Portugnese

%description Portuguese
K Desktop Environment - Portuguese language support.

%description Portuguese -l pl
KDE - wsparcie dla jêzyka portugalskiego.

%package Brazil_Portuguese
Summary:	K Desktop Environment - Portuguese (Brazil) language support
Summary(pl):	KDE - wsparcie dla jêzyka portugalskiego (odmiany brazylijskiej)
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	%{name}-Brazil_Protugnese

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
%setup -q -c -T -a0 -a1 -a2 -a3 -a4 -a5 -a6 -a7 -a8 -a9 -a10 -a11 -a12 -a13 -a14 -a15 -a16 -a17 -a18 -a19 -a20 -a21 -a22 -a23 -a24 -a25 -a26 -a27 -a28 -a29 -a30 -a31 -a32 -a33 -a34 -a35 -a36 -a37 -a38 -a39 -a40 -a41 -a42 -a43 -a44 -a45 -a45 -a47 -a48 -a49

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
