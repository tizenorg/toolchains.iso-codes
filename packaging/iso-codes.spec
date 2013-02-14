Name:           iso-codes
Version:        3.13
Release:        1
License:        LGPL-2.0+
Summary:        ISO code lists and translations
Url:            http://alioth.debian.org/projects/pkg-isocodes/
Group:          System/Base
Source0:        ftp://pkg-isocodes.alioth.debian.org/pub/pkg-isocodes/iso-codes-%{version}.tar.bz2
Source1001:     iso-codes.manifest
BuildRequires:  gettext-tools >= 0.16
BuildArch:      noarch

%description
This package provides the ISO 639 Language code list, the ISO 4217
Currency code list, the ISO 3166 Territory code list, and ISO 3166-2
sub-territory lists, and all their translations in gettext format.

%package devel
Summary:        Files for development using %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}

%description devel
This package contains the pkg-config files for development
when building programs that use %{name}.

%prep
%setup -q


%build
cp %{SOURCE1001} .

%configure 
make %{?_smp_mflags}

%install
%make_install

%find_lang iso-codes --all-name

%files -f iso-codes.lang
%manifest iso-codes.manifest
%dir %{_datadir}/xml/iso-codes
%{_datadir}/xml/iso-codes/*.xml


%files devel
%manifest iso-codes.manifest
%{_datadir}/pkgconfig/iso-codes.pc

