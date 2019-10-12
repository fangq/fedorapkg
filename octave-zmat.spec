%global octpkg zmat

Name:           octave-%{octpkg}
Version:        0.9.1
Release:        2%{?dist}
Summary:        A portable data compression/decompression toolbox for MATLAB/Octave
License:        GPLv3+ or BSD
URL:            https://github.com/fangq/%{octpkg}
Source0:        https://github.com/fangq/%{octpkg}/archive/v%{version}/%{octpkg}-%{version}.tar.gz
Source1:        https://github.com/lloyd/easylzma/archive/0.0.7/easylzma-0.0.7.tar.gz
BuildRequires:  octave-devel zlib cmake gcc-c++

Requires:       octave zlib
Requires(post): octave
Requires(postun): octave

%description
ZMat is a portable mex function to enable zlib/gzip/lzma/lzip/lz4/lz4hc
based data compression/decompression and base64 encoding/decoding support
in MATLAB and GNU Octave. It is fast and compact, can process a large
array within a fraction of a second. Among the 6 supported compression
methods, lz4 is the fastest for compression/decompression; lzma is the
slowest but has the highest compression ratio; zlib/gzip have the best
balance between speed and compression time.


%package -n %{octpkg}-devel
Summary:        An eazy-to-use data compression library
Requires:       zlib

%description -n %{octpkg}-devel
The %{octpkg}-devel package provides the headers files and tools you may need to
develop applications using zmat.

%prep
%autosetup -n %{octpkg}-%{version} -b 1
rm -rf src/easylzma
cp -r ../easylzma-0.0.7 src/easylzma

cp LICENSE.txt COPYING

cat > DESCRIPTION << EOF
Name: %{octpkg}
Version: %{version}
Date: %(date +"%Y-%d-%m")
Title: %{summary}
Author: Qianqian Fang <fangqq@gmail.com>
Maintainer: Qianqian Fang <fangqq@gmail.com>
Description: ZMat is a portable mex function to enable zlib/gzip/lzma/lzip/lz4/lz4hc
 based data compression/decompression and base64 encoding/decoding support
 in MATLAB and GNU Octave. It is fast and compact, can process a large
 array within a fraction of a second. Among the 6 supported compression
 methods, lz4 is the fastest for compression/decompression; lzma is the
 slowest but has the highest compression ratio; zlib/gzip have the best
 balance between speed and compression time.

Categories: Zip
EOF

cat > INDEX << EOF
zmat >> ZMat
ZMat
 zmat
 zipmat
EOF


mkdir -p inst/
mv *.m inst/

%build
mkdir lib
mkdir include
pushd src
pushd easylzma
%cmake .
%make_build
mv easylzma-0.0.7 easylzma-0.0.8
popd
%make_build oct
popd
mv *.mex inst/
mv src/Makefile .
%octave_pkg_build

mv Makefile src
pushd src
%make_build clean
%make_build lib BINARY=lib%{octpkg}.a
cp ../lib%{octpkg}.a ../lib/lib%{octpkg}.a.%{version}
cp zmatlib.h ../include
%make_build clean
%make_build dll BINARY=lib%{octpkg}.so
mv ../lib%{octpkg}.so ../lib/lib%{octpkg}.so.%{version}
popd

%if 0%{?fedora} <=30
   %global octave_tar_suffix any-none
%endif

%install
%octave_pkg_install

install -m 755 -d %{buildroot}/%{_includedir}/
install -m 644 -t %{buildroot}/%{_includedir}/ include/%{octpkg}lib.h

install -m 755 -d %{buildroot}/%{_libdir}/
install -m 755 -t %{buildroot}/%{_libdir}/ lib/lib%{octpkg}.so.%{version}
install -m 755 -t %{buildroot}/%{_libdir}/ lib/lib%{octpkg}.a.%{version}
pushd %{buildroot}/%{_libdir}
    ln -s lib%{octpkg}.so.%{version} lib%{octpkg}.so
    ln -s lib%{octpkg}.a.%{version}  lib%{octpkg}.a
popd

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

%files
%license LICENSE.txt
%doc example
%doc README.rst
%doc AUTHORS.txt
%doc ChangeLog.txt
%dir %{octpkgdir}
%{octpkgdir}/*.m
%{octpkgdir}/*.mex
%doc %{octpkgdir}/doc-cache
%{octpkgdir}/packinfo


%files -n %{octpkg}-devel
%license LICENSE.txt
%doc README.rst
%doc AUTHORS.txt
%{_includedir}/%{octpkg}lib.h
%{_libdir}/lib%{octpkg}.so.%{version}
%{_libdir}/lib%{octpkg}.so
%{_libdir}/lib%{octpkg}.a.%{version}
%{_libdir}/lib%{octpkg}.a


%changelog
* Fri Oct 11 2019 Qianqian Fang <fangqq@gmail.com> - 0.9.1-2
- Add zmat-devel as a subpackage

* Tue Oct 01 2019 Qianqian Fang <fangqq@gmail.com> - 0.9.1-1
- Initial package
