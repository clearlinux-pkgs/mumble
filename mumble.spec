#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
#
# Source0 file verified with key 0x69F82AFF148DC0FF (mumble-auto-build-2023@mumble.info)
#
Name     : mumble
Version  : 1.5.517
Release  : 24
URL      : https://github.com/mumble-voip/mumble/releases/download/v1.5.517/mumble-1.5.517.tar.gz
Source0  : https://github.com/mumble-voip/mumble/releases/download/v1.5.517/mumble-1.5.517.tar.gz
Source1  : https://github.com/mumble-voip/mumble/releases/download/v1.5.517/mumble-1.5.517.tar.gz.sig
Summary  : Speexdsp is a speech processing library that goes along with the Speex codec
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause BSD-3-Clause BSL-1.0 FTL GPL-2.0 IJG ISC LGPL-2.0 LGPL-2.1 Libpng MIT OpenSSL Sleepycat Unlicense Zlib bzip2-1.0.6
Requires: mumble-bin = %{version}-%{release}
Requires: mumble-data = %{version}-%{release}
Requires: mumble-lib = %{version}-%{release}
Requires: mumble-license = %{version}-%{release}
Requires: mumble-man = %{version}-%{release}
BuildRequires : boost-dev
BuildRequires : buildreq-cmake
BuildRequires : git
BuildRequires : glibc-dev
BuildRequires : mesa-dev
BuildRequires : openssl-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(Qt5Core)
BuildRequires : pkgconfig(Qt5Svg)
BuildRequires : pkgconfig(alsa)
BuildRequires : pkgconfig(avahi-compat-libdns_sd)
BuildRequires : pkgconfig(libcap)
BuildRequires : pkgconfig(libpulse)
BuildRequires : pkgconfig(openssl)
BuildRequires : pkgconfig(opus)
BuildRequires : pkgconfig(sndfile)
BuildRequires : pkgconfig(speex)
BuildRequires : pkgconfig(speexdsp)
BuildRequires : pkgconfig(x11)
BuildRequires : poco-dev
BuildRequires : protobuf-dev
BuildRequires : python3
BuildRequires : qttools-dev
BuildRequires : speex-dev
BuildRequires : speexdsp-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
XInputCheck is an XInput check abstracted away from SDL.
The content of xinputcheck.c is originally from SDL Hg c7932bb6dcee.
The files used are "src/joystick/windows/SDL_dinputjoystick.c" and
"include/SDL_stdinc.h".

%package bin
Summary: bin components for the mumble package.
Group: Binaries
Requires: mumble-data = %{version}-%{release}
Requires: mumble-license = %{version}-%{release}

%description bin
bin components for the mumble package.


%package data
Summary: data components for the mumble package.
Group: Data

%description data
data components for the mumble package.


%package extras
Summary: extras components for the mumble package.
Group: Default

%description extras
extras components for the mumble package.


%package lib
Summary: lib components for the mumble package.
Group: Libraries
Requires: mumble-data = %{version}-%{release}
Requires: mumble-license = %{version}-%{release}

%description lib
lib components for the mumble package.


%package license
Summary: license components for the mumble package.
Group: Default

%description license
license components for the mumble package.


%package man
Summary: man components for the mumble package.
Group: Default

%description man
man components for the mumble package.


%prep
%setup -q -n mumble-1.5.517
cd %{_builddir}/mumble-1.5.517

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1685592192
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%cmake .. -Dbundled-celt=ON \
-Dbundled-speex=OFF \
-Drnnoise=ON \
-Dspeechd=OFF \
-Dupdate=OFF \
-Dice=OFF \
-Doverlay-xcompile=OFF \
-DMUMBLE_INSTALL_ABS_SYSCONFDIR=/usr/share/mumble
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FCFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CFLAGS="$CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake .. -Dbundled-celt=ON \
-Dbundled-speex=OFF \
-Drnnoise=ON \
-Dspeechd=OFF \
-Dupdate=OFF \
-Dice=OFF \
-Doverlay-xcompile=OFF \
-DMUMBLE_INSTALL_ABS_SYSCONFDIR=/usr/share/mumble
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1685592192
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/mumble
cp %{_builddir}/mumble-%{version}/3rdPartyLicenses/appimage_runtime_license.txt %{buildroot}/usr/share/package-licenses/mumble/56e286039c4b5a9370b7f45f0baf7eb5b5753277 || :
cp %{_builddir}/mumble-%{version}/3rdPartyLicenses/avahi_license.txt %{buildroot}/usr/share/package-licenses/mumble/7b7930ba0e891f9f64d2f3ff395eaab7f385244f || :
cp %{_builddir}/mumble-%{version}/3rdPartyLicenses/berkeleydb_license.txt %{buildroot}/usr/share/package-licenses/mumble/7cc1ed4976e3c34c90cd98ba60c6335d4a65a77c || :
cp %{_builddir}/mumble-%{version}/3rdPartyLicenses/boost_license.txt %{buildroot}/usr/share/package-licenses/mumble/3cba29011be2b9d59f6204d6fa0a386b1b2dbd90 || :
cp %{_builddir}/mumble-%{version}/3rdPartyLicenses/bzip2_license.txt %{buildroot}/usr/share/package-licenses/mumble/7026f40da8af45f6fde59e10d519dbb9f333f22e || :
cp %{_builddir}/mumble-%{version}/3rdPartyLicenses/dbus_license.txt %{buildroot}/usr/share/package-licenses/mumble/090586b9e4c51fd5ef3c39f25d2469a8be8e33c9 || :
cp %{_builddir}/mumble-%{version}/3rdPartyLicenses/expat_license.txt %{buildroot}/usr/share/package-licenses/mumble/7ba7b9158e4fb8c9d2eb46ad8c693bf85c96e1e4 || :
cp %{_builddir}/mumble-%{version}/3rdPartyLicenses/freetype_license.txt %{buildroot}/usr/share/package-licenses/mumble/f755eabf10832203b9599193223672756e1fb1df || :
cp %{_builddir}/mumble-%{version}/3rdPartyLicenses/glib_license.txt %{buildroot}/usr/share/package-licenses/mumble/bf50bac24e7ec325dbb09c6b6c4dcc88a7d79e8f || :
cp %{_builddir}/mumble-%{version}/3rdPartyLicenses/harfbuzzng_license.txt %{buildroot}/usr/share/package-licenses/mumble/e911adf5641a09f13fdd5d59962ad37da043df79 || :
cp %{_builddir}/mumble-%{version}/3rdPartyLicenses/libcap2_license.txt %{buildroot}/usr/share/package-licenses/mumble/1f65128ca2bb6715d81ca6c60f997c997d0ac69e || :
cp %{_builddir}/mumble-%{version}/3rdPartyLicenses/libdaemon_license.txt %{buildroot}/usr/share/package-licenses/mumble/050e568027dc9b12163835fdc6eb23198d8e2079 || :
cp %{_builddir}/mumble-%{version}/3rdPartyLicenses/libffi_license.txt %{buildroot}/usr/share/package-licenses/mumble/0155a7d592674828653b18e044fe6ea2685fac13 || :
cp %{_builddir}/mumble-%{version}/3rdPartyLicenses/libflac_license.txt %{buildroot}/usr/share/package-licenses/mumble/11464e106e37066a94a23fe4912581799daa3e41 || :
cp %{_builddir}/mumble-%{version}/3rdPartyLicenses/libfuse_license.txt %{buildroot}/usr/share/package-licenses/mumble/7e2849dfbbc6b796cbb2190922eda896697382a2 || :
cp %{_builddir}/mumble-%{version}/3rdPartyLicenses/libjpeg_turbo_license.txt %{buildroot}/usr/share/package-licenses/mumble/835053b08a3965bbb44385acf5789b0f931dbd3d || :
cp %{_builddir}/mumble-%{version}/3rdPartyLicenses/libogg_license.txt %{buildroot}/usr/share/package-licenses/mumble/bc252631805cf037048f64fef562f98c2a0bdc9e || :
cp %{_builddir}/mumble-%{version}/3rdPartyLicenses/libpng_license.txt %{buildroot}/usr/share/package-licenses/mumble/6a649b891335cb2a8a20dc64c6b362c97dd7712b || :
cp %{_builddir}/mumble-%{version}/3rdPartyLicenses/libsndfile_license.txt %{buildroot}/usr/share/package-licenses/mumble/157d5db59507ff877c63b812f4f30e4a29a26d64 || :
cp %{_builddir}/mumble-%{version}/3rdPartyLicenses/libvorbis_license.txt %{buildroot}/usr/share/package-licenses/mumble/4406aeb00f12a2c9cfba8066eef1a7a0c9b32f43 || :
cp %{_builddir}/mumble-%{version}/3rdPartyLicenses/mach_override_license.txt %{buildroot}/usr/share/package-licenses/mumble/0b3be77bd86c98f691c869fc9f48b6babb2291c6 || :
cp %{_builddir}/mumble-%{version}/3rdPartyLicenses/mariadb_c_connector_license.txt %{buildroot}/usr/share/package-licenses/mumble/ce4afcb9f641e25eb3467a2760759035639c3b7e || :
cp %{_builddir}/mumble-%{version}/3rdPartyLicenses/mcpp_license.txt %{buildroot}/usr/share/package-licenses/mumble/3661c9746c938d10f7c20dfc8d844a1ba46487e2 || :
cp %{_builddir}/mumble-%{version}/3rdPartyLicenses/mdnsresponder_license.txt %{buildroot}/usr/share/package-licenses/mumble/0d731ea50fb6a99588c95357114e78dd853c2afe || :
cp %{_builddir}/mumble-%{version}/3rdPartyLicenses/mumble-old-license-headers/LICENSE.txt %{buildroot}/usr/share/package-licenses/mumble/236c2ef764273c86adfcd0456ba5c3c5e1931417 || :
cp %{_builddir}/mumble-%{version}/3rdPartyLicenses/openssl_license.txt %{buildroot}/usr/share/package-licenses/mumble/65d424837b214fcdf4e95f0b408c8851465a615c || :
cp %{_builddir}/mumble-%{version}/3rdPartyLicenses/pcre_license.txt %{buildroot}/usr/share/package-licenses/mumble/512f24346f2ff4458c1b782f7d737a5837749cd8 || :
cp %{_builddir}/mumble-%{version}/3rdPartyLicenses/protobuf_license.txt %{buildroot}/usr/share/package-licenses/mumble/a0bcc878d7e7181b120ae51837c8d1703fe919ab || :
cp %{_builddir}/mumble-%{version}/3rdPartyLicenses/qt_license.txt %{buildroot}/usr/share/package-licenses/mumble/fe04fe44c5e1a407572a5cca79d39afd674bccf3 || :
cp %{_builddir}/mumble-%{version}/3rdPartyLicenses/squashfuse_license.txt %{buildroot}/usr/share/package-licenses/mumble/18bfcba3d79cb8c4122da9aa7bf080906eb211d7 || :
cp %{_builddir}/mumble-%{version}/3rdPartyLicenses/xar_license.txt %{buildroot}/usr/share/package-licenses/mumble/a599ef676fb179a995accc72c60056163021091c || :
cp %{_builddir}/mumble-%{version}/3rdPartyLicenses/zeroc_ice_license.txt %{buildroot}/usr/share/package-licenses/mumble/bf9becec987678f3d8836ecb67dd1c43c44a175e || :
cp %{_builddir}/mumble-%{version}/3rdPartyLicenses/zlib_license.txt %{buildroot}/usr/share/package-licenses/mumble/b16cea866086d615aef9bee45bc9d343c30d84ce || :
cp %{_builddir}/mumble-%{version}/3rdparty/FindPythonInterpreter/LICENSE %{buildroot}/usr/share/package-licenses/mumble/41d061cf8dcd324416fc7a477344ecb7aef641d8 || :
cp %{_builddir}/mumble-%{version}/3rdparty/SPSCQueue/LICENSE %{buildroot}/usr/share/package-licenses/mumble/6b8587e490ec72d8a5bfed011cb3d6b630e17af2 || :
cp %{_builddir}/mumble-%{version}/3rdparty/arc4random/LICENSE %{buildroot}/usr/share/package-licenses/mumble/62c67fe91c02173222a9e6ecdcdca1d5f35da5bd || :
cp %{_builddir}/mumble-%{version}/3rdparty/gsl/LICENSE %{buildroot}/usr/share/package-licenses/mumble/2ab73d040346630efdea7285408229c0effd56b9 || :
cp %{_builddir}/mumble-%{version}/3rdparty/minhook/LICENSE.txt %{buildroot}/usr/share/package-licenses/mumble/6c30d77b67f44704514f77c27fa93175b5370796 || :
cp %{_builddir}/mumble-%{version}/3rdparty/nlohmann_json/LICENSE.MIT %{buildroot}/usr/share/package-licenses/mumble/1d773eb6081e8c622d9bd4e29dfcc860270c67df || :
cp %{_builddir}/mumble-%{version}/3rdparty/qqbonjour/LICENSE %{buildroot}/usr/share/package-licenses/mumble/bfec03f4c228ee1afd393be267268731353b54d6 || :
cp %{_builddir}/mumble-%{version}/3rdparty/rnnoise-src/COPYING %{buildroot}/usr/share/package-licenses/mumble/5f8e73e1f293d0f127c2bcad2ab6fc5fa2a58139 || :
cp %{_builddir}/mumble-%{version}/3rdparty/smallft/LICENSE %{buildroot}/usr/share/package-licenses/mumble/731b20e0b908255017e7721f13153acf59ec737a || :
cp %{_builddir}/mumble-%{version}/3rdparty/speexdsp/COPYING %{buildroot}/usr/share/package-licenses/mumble/7f3f67aef48ead049bebdab307c04c2e03342710 || :
cp %{_builddir}/mumble-%{version}/3rdparty/tracy/LICENSE %{buildroot}/usr/share/package-licenses/mumble/142c799e043e3916e131b1e969b376ec13a5f00b || :
cp %{_builddir}/mumble-%{version}/3rdparty/tracy/examples/ToyPathTracer/license.md %{buildroot}/usr/share/package-licenses/mumble/24944bf7920108f5a4790e6071c32e9102760c37 || :
cp %{_builddir}/mumble-%{version}/3rdparty/tracy/imgui/LICENSE.txt %{buildroot}/usr/share/package-licenses/mumble/a026d74d2d93bad6c8e7f263a28caec3b187dc8a || :
cp %{_builddir}/mumble-%{version}/3rdparty/tracy/libbacktrace/LICENSE %{buildroot}/usr/share/package-licenses/mumble/555657fe7ff5be9969fa3387d8e465e0a1afa2f4 || :
cp %{_builddir}/mumble-%{version}/3rdparty/tracy/nfd/LICENSE %{buildroot}/usr/share/package-licenses/mumble/1623df77cf65deb995f3cf35f0b2fde050adf000 || :
cp %{_builddir}/mumble-%{version}/3rdparty/xinputcheck-src/COPYING.txt %{buildroot}/usr/share/package-licenses/mumble/b360492bb2fa9b429e460a3f99d30dfea61885b4 || :
cp %{_builddir}/mumble-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/mumble/7361e9ef21369edf3ebb1997eb33c954e84a6c66 || :
cp %{_builddir}/mumble-%{version}/icons/flags/LICENSE.md %{buildroot}/usr/share/package-licenses/mumble/e31d75c9ecb70be058abe89484fe711012d9db46 || :
cp %{_builddir}/mumble-%{version}/installer/gpl.txt %{buildroot}/usr/share/package-licenses/mumble/b47456e2c1f38c40346ff00db976a2badf36b5e3 || :
cp %{_builddir}/mumble-%{version}/src/mumble/qttranslations/LICENSE %{buildroot}/usr/share/package-licenses/mumble/a086566c447c42592640d238e5ca117a99e89fff || :
cp %{_builddir}/mumble-%{version}/themes/Default/LICENSE %{buildroot}/usr/share/package-licenses/mumble/f6067df486cbdbb0aac026b799b26261c92734a3 || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
## install_append content
## Put these files somewhere useful:
# /usr/etc/mumble/MumbleServer.ice
# /usr/etc/mumble/mumble-server.ini
# /usr/etc/sysconfig.d/mumble-server.conf
# /usr/etc/systemd/system/mumble-server.service

## Note: This will change significantly in version 1.6, once this PR is merged:
# https://github.com/mumble-voip/mumble/pull/6100

# Most of this goes in /usr/share/mumble:
mkdir -p %{buildroot}/usr/share/mumble
mv \
%{buildroot}/usr/etc/sysconfig.d/*	\
%{buildroot}/usr/etc/mumble/*		\
%{buildroot}/usr/share/mumble/

# But install the systemd.service in /usr/lib:
mkdir -p %{buildroot}/usr/lib/systemd/system
mv %{buildroot}/usr/etc/systemd/system/* %{buildroot}/usr/lib/systemd/system/

# We stashed the example ini file in /usr/share/mumble, but at runtime, need to read it from /etc
sed -i 's|\(-ini.*\)/usr\(/etc/.*\.ini\)|\1\2|' %{buildroot}/usr/lib/systemd/system/mumble*.service

# Make sure the mumble-server-user-wrapper script knows where to find the template ini file
sed -i 's|^SYSDIR=.*|SYSDIR=/usr/share/mumble|g' %{buildroot}/usr/bin/mumble-server-user-wrapper
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/mumble
/usr/bin/mumble
/usr/bin/mumble-overlay

%files data
%defattr(-,root,root,-)
/usr/share/applications/info.mumble.Mumble.desktop
/usr/share/icons/hicolor/256x256/apps/mumble.png
/usr/share/icons/hicolor/scalable/apps/mumble.svg
/usr/share/metainfo/info.mumble.Mumble.appdata.xml

%files extras
%defattr(-,root,root,-)
/V3/usr/bin/mumble-server
/usr/bin/mumble-server
/usr/bin/mumble-server-user-wrapper
/usr/lib/systemd/system/mumble-server.service
/usr/share/dbus-1/system.d/mumble-server.conf
/usr/share/man/man1/mumble-server-user-wrapper.1
/usr/share/man/man1/mumble-server.1
/usr/share/mumble/MumbleServer.ice
/usr/share/mumble/mumble-server.conf
/usr/share/mumble/mumble-server.ini

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/mumble/libmumbleoverlay.so.1.5.0
/V3/usr/lib64/mumble/plugins/libamongus.so
/V3/usr/lib64/mumble/plugins/libaoc.so
/V3/usr/lib64/mumble/plugins/libarma2.so
/V3/usr/lib64/mumble/plugins/libbf1.so
/V3/usr/lib64/mumble/plugins/libbf1942.so
/V3/usr/lib64/mumble/plugins/libbf2.so
/V3/usr/lib64/mumble/plugins/libbf2142.so
/V3/usr/lib64/mumble/plugins/libbf3.so
/V3/usr/lib64/mumble/plugins/libbf4.so
/V3/usr/lib64/mumble/plugins/libbf4_x86.so
/V3/usr/lib64/mumble/plugins/libbfbc2.so
/V3/usr/lib64/mumble/plugins/libbfheroes.so
/V3/usr/lib64/mumble/plugins/libblacklight.so
/V3/usr/lib64/mumble/plugins/libborderlands.so
/V3/usr/lib64/mumble/plugins/libborderlands2.so
/V3/usr/lib64/mumble/plugins/libbreach.so
/V3/usr/lib64/mumble/plugins/libcod2.so
/V3/usr/lib64/mumble/plugins/libcod4.so
/V3/usr/lib64/mumble/plugins/libcod5.so
/V3/usr/lib64/mumble/plugins/libcodmw2.so
/V3/usr/lib64/mumble/plugins/libcodmw2so.so
/V3/usr/lib64/mumble/plugins/libcs.so
/V3/usr/lib64/mumble/plugins/libdys.so
/V3/usr/lib64/mumble/plugins/libetqw.so
/V3/usr/lib64/mumble/plugins/libffxiv.so
/V3/usr/lib64/mumble/plugins/libffxiv_x64.so
/V3/usr/lib64/mumble/plugins/libgmod.so
/V3/usr/lib64/mumble/plugins/libgtaiv.so
/V3/usr/lib64/mumble/plugins/libgtasa.so
/V3/usr/lib64/mumble/plugins/libgtav.so
/V3/usr/lib64/mumble/plugins/libgw.so
/V3/usr/lib64/mumble/plugins/libinsurgency.so
/V3/usr/lib64/mumble/plugins/libjc2.so
/V3/usr/lib64/mumble/plugins/liblink.so
/V3/usr/lib64/mumble/plugins/liblol.so
/V3/usr/lib64/mumble/plugins/liblotro.so
/V3/usr/lib64/mumble/plugins/libql.so
/V3/usr/lib64/mumble/plugins/librl.so
/V3/usr/lib64/mumble/plugins/libse.so
/V3/usr/lib64/mumble/plugins/libsr.so
/V3/usr/lib64/mumble/plugins/libut2004.so
/V3/usr/lib64/mumble/plugins/libut3.so
/V3/usr/lib64/mumble/plugins/libut99.so
/V3/usr/lib64/mumble/plugins/libwolfet.so
/V3/usr/lib64/mumble/plugins/libwow.so
/V3/usr/lib64/mumble/plugins/libwow_x64.so
/usr/lib64/mumble/libmumbleoverlay.so
/usr/lib64/mumble/libmumbleoverlay.so.1.5.0
/usr/lib64/mumble/plugins/libamongus.so
/usr/lib64/mumble/plugins/libaoc.so
/usr/lib64/mumble/plugins/libarma2.so
/usr/lib64/mumble/plugins/libbf1.so
/usr/lib64/mumble/plugins/libbf1942.so
/usr/lib64/mumble/plugins/libbf2.so
/usr/lib64/mumble/plugins/libbf2142.so
/usr/lib64/mumble/plugins/libbf3.so
/usr/lib64/mumble/plugins/libbf4.so
/usr/lib64/mumble/plugins/libbf4_x86.so
/usr/lib64/mumble/plugins/libbfbc2.so
/usr/lib64/mumble/plugins/libbfheroes.so
/usr/lib64/mumble/plugins/libblacklight.so
/usr/lib64/mumble/plugins/libborderlands.so
/usr/lib64/mumble/plugins/libborderlands2.so
/usr/lib64/mumble/plugins/libbreach.so
/usr/lib64/mumble/plugins/libcod2.so
/usr/lib64/mumble/plugins/libcod4.so
/usr/lib64/mumble/plugins/libcod5.so
/usr/lib64/mumble/plugins/libcodmw2.so
/usr/lib64/mumble/plugins/libcodmw2so.so
/usr/lib64/mumble/plugins/libcs.so
/usr/lib64/mumble/plugins/libdys.so
/usr/lib64/mumble/plugins/libetqw.so
/usr/lib64/mumble/plugins/libffxiv.so
/usr/lib64/mumble/plugins/libffxiv_x64.so
/usr/lib64/mumble/plugins/libgmod.so
/usr/lib64/mumble/plugins/libgtaiv.so
/usr/lib64/mumble/plugins/libgtasa.so
/usr/lib64/mumble/plugins/libgtav.so
/usr/lib64/mumble/plugins/libgw.so
/usr/lib64/mumble/plugins/libinsurgency.so
/usr/lib64/mumble/plugins/libjc2.so
/usr/lib64/mumble/plugins/liblink.so
/usr/lib64/mumble/plugins/liblol.so
/usr/lib64/mumble/plugins/liblotro.so
/usr/lib64/mumble/plugins/libql.so
/usr/lib64/mumble/plugins/librl.so
/usr/lib64/mumble/plugins/libse.so
/usr/lib64/mumble/plugins/libsr.so
/usr/lib64/mumble/plugins/libut2004.so
/usr/lib64/mumble/plugins/libut3.so
/usr/lib64/mumble/plugins/libut99.so
/usr/lib64/mumble/plugins/libwolfet.so
/usr/lib64/mumble/plugins/libwow.so
/usr/lib64/mumble/plugins/libwow_x64.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mumble/0155a7d592674828653b18e044fe6ea2685fac13
/usr/share/package-licenses/mumble/050e568027dc9b12163835fdc6eb23198d8e2079
/usr/share/package-licenses/mumble/090586b9e4c51fd5ef3c39f25d2469a8be8e33c9
/usr/share/package-licenses/mumble/0b3be77bd86c98f691c869fc9f48b6babb2291c6
/usr/share/package-licenses/mumble/0d731ea50fb6a99588c95357114e78dd853c2afe
/usr/share/package-licenses/mumble/11464e106e37066a94a23fe4912581799daa3e41
/usr/share/package-licenses/mumble/142c799e043e3916e131b1e969b376ec13a5f00b
/usr/share/package-licenses/mumble/157d5db59507ff877c63b812f4f30e4a29a26d64
/usr/share/package-licenses/mumble/1623df77cf65deb995f3cf35f0b2fde050adf000
/usr/share/package-licenses/mumble/18bfcba3d79cb8c4122da9aa7bf080906eb211d7
/usr/share/package-licenses/mumble/1d773eb6081e8c622d9bd4e29dfcc860270c67df
/usr/share/package-licenses/mumble/1f65128ca2bb6715d81ca6c60f997c997d0ac69e
/usr/share/package-licenses/mumble/236c2ef764273c86adfcd0456ba5c3c5e1931417
/usr/share/package-licenses/mumble/24944bf7920108f5a4790e6071c32e9102760c37
/usr/share/package-licenses/mumble/2ab73d040346630efdea7285408229c0effd56b9
/usr/share/package-licenses/mumble/3661c9746c938d10f7c20dfc8d844a1ba46487e2
/usr/share/package-licenses/mumble/3cba29011be2b9d59f6204d6fa0a386b1b2dbd90
/usr/share/package-licenses/mumble/41d061cf8dcd324416fc7a477344ecb7aef641d8
/usr/share/package-licenses/mumble/4406aeb00f12a2c9cfba8066eef1a7a0c9b32f43
/usr/share/package-licenses/mumble/512f24346f2ff4458c1b782f7d737a5837749cd8
/usr/share/package-licenses/mumble/555657fe7ff5be9969fa3387d8e465e0a1afa2f4
/usr/share/package-licenses/mumble/56e286039c4b5a9370b7f45f0baf7eb5b5753277
/usr/share/package-licenses/mumble/5f8e73e1f293d0f127c2bcad2ab6fc5fa2a58139
/usr/share/package-licenses/mumble/62c67fe91c02173222a9e6ecdcdca1d5f35da5bd
/usr/share/package-licenses/mumble/65d424837b214fcdf4e95f0b408c8851465a615c
/usr/share/package-licenses/mumble/6a649b891335cb2a8a20dc64c6b362c97dd7712b
/usr/share/package-licenses/mumble/6b8587e490ec72d8a5bfed011cb3d6b630e17af2
/usr/share/package-licenses/mumble/6c30d77b67f44704514f77c27fa93175b5370796
/usr/share/package-licenses/mumble/7026f40da8af45f6fde59e10d519dbb9f333f22e
/usr/share/package-licenses/mumble/731b20e0b908255017e7721f13153acf59ec737a
/usr/share/package-licenses/mumble/7361e9ef21369edf3ebb1997eb33c954e84a6c66
/usr/share/package-licenses/mumble/7b7930ba0e891f9f64d2f3ff395eaab7f385244f
/usr/share/package-licenses/mumble/7ba7b9158e4fb8c9d2eb46ad8c693bf85c96e1e4
/usr/share/package-licenses/mumble/7cc1ed4976e3c34c90cd98ba60c6335d4a65a77c
/usr/share/package-licenses/mumble/7e2849dfbbc6b796cbb2190922eda896697382a2
/usr/share/package-licenses/mumble/7f3f67aef48ead049bebdab307c04c2e03342710
/usr/share/package-licenses/mumble/835053b08a3965bbb44385acf5789b0f931dbd3d
/usr/share/package-licenses/mumble/a026d74d2d93bad6c8e7f263a28caec3b187dc8a
/usr/share/package-licenses/mumble/a086566c447c42592640d238e5ca117a99e89fff
/usr/share/package-licenses/mumble/a0bcc878d7e7181b120ae51837c8d1703fe919ab
/usr/share/package-licenses/mumble/a599ef676fb179a995accc72c60056163021091c
/usr/share/package-licenses/mumble/b16cea866086d615aef9bee45bc9d343c30d84ce
/usr/share/package-licenses/mumble/b360492bb2fa9b429e460a3f99d30dfea61885b4
/usr/share/package-licenses/mumble/b47456e2c1f38c40346ff00db976a2badf36b5e3
/usr/share/package-licenses/mumble/bc252631805cf037048f64fef562f98c2a0bdc9e
/usr/share/package-licenses/mumble/bf50bac24e7ec325dbb09c6b6c4dcc88a7d79e8f
/usr/share/package-licenses/mumble/bf9becec987678f3d8836ecb67dd1c43c44a175e
/usr/share/package-licenses/mumble/bfec03f4c228ee1afd393be267268731353b54d6
/usr/share/package-licenses/mumble/ce4afcb9f641e25eb3467a2760759035639c3b7e
/usr/share/package-licenses/mumble/e31d75c9ecb70be058abe89484fe711012d9db46
/usr/share/package-licenses/mumble/e911adf5641a09f13fdd5d59962ad37da043df79
/usr/share/package-licenses/mumble/f6067df486cbdbb0aac026b799b26261c92734a3
/usr/share/package-licenses/mumble/f755eabf10832203b9599193223672756e1fb1df
/usr/share/package-licenses/mumble/fe04fe44c5e1a407572a5cca79d39afd674bccf3

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/mumble-overlay.1
/usr/share/man/man1/mumble.1
