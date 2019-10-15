Name:           zmat
Version:        0.9.2
Release:        1%{?dist}
Summary:        An easy-to-use data compression library
License:        GPLv3+
URL:            https://github.com/fangq/%{name}
Source0:        https://github.com/fangq/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/lloyd/easylzma/archive/0.0.7/easylzma-0.0.7.tar.gz
BuildRequires:  cmake gcc-c++

%description
ZMat is a portable C library to enable easy-to-use data compression
and decompression (such as zlib/gzip/lzma/lzip/lz4/lz4hc algorithms)
and base64 encoding/decoding in an application.
It is fast and compact, can process a large array within a fraction
of a second. Among the supported compression methods, lz4 is the
fastest for compression/decompression; lzma is the slowest but has
the highest compression ratio; zlib/gzip have the best balance
between speed and compression time.


%package devel
Summary:        Development files for zmat - an easy-to-use data compression library
Provides:       %{name}-static = %{version}-%{release}
Requires:       %{name} lz4-devel

%description devel
The %{name}-devel package provides the headers files and tools you may need to
develop applications using zmat.


%package static
Summary:        Static library for zmat - an easy-to-use data compression library
Requires:       %{name}-devel

%description static
The %{name}-static package provides the static library you may need to
develop applications using zmat.

%prep
%autosetup -n %{name}-%{version} -b 1
rm -rf src/easylzma
cp -r ../easylzma-0.0.7 src/easylzma


%build
%set_build_flags
mkdir lib
mkdir include
pushd src
pushd easylzma
%cmake .
%make_build
mv easylzma-0.0.7 easylzma-0.0.8
cp -r easylzma-0.0.8/include/easylzma ../../include
popd
popd

pushd src
%make_build clean
%make_build lib BINARY=lib%{name}.a
cp ../lib%{name}.a ../lib/
cp zmatlib.h ../include
%make_build clean
%make_build dll BINARY=lib%{name}.so
mv ../lib%{name}.so ../lib/lib%{name}.so.%{version}
popd


%install
install -m 755 -pd %{buildroot}/%{_includedir}/
install -m 644 -pt %{buildroot}/%{_includedir}/ include/%{name}lib.h

install -m 755 -pd %{buildroot}/%{_includedir}/easylzma
install -m 644 -pt %{buildroot}/%{_includedir}/easylzma include/easylzma/common.h
install -m 644 -pt %{buildroot}/%{_includedir}/easylzma include/easylzma/compress.h
install -m 644 -pt %{buildroot}/%{_includedir}/easylzma include/easylzma/decompress.h

install -m 755 -pd %{buildroot}/%{_libdir}/
install -m 755 -pt %{buildroot}/%{_libdir}/ lib/lib%{name}.so.%{version}
install -m 644 -pt %{buildroot}/%{_libdir}/ lib/lib%{name}.a
pushd %{buildroot}/%{_libdir}
    ln -s lib%{name}.so.%{version} lib%{name}.so
popd


%files
%license LICENSE.txt
%doc README.rst
%doc AUTHORS.txt
%doc ChangeLog.txt
%{_libdir}/lib%{name}.so.%{version}
%{_libdir}/lib%{name}.so.1

%files devel
%license LICENSE.txt
%doc README.rst
%doc AUTHORS.txt
%dir %{_includedir}/easylzma
%{_includedir}/%{name}lib.h
%{_includedir}/easylzma/common.h
%{_includedir}/easylzma/compress.h
%{_includedir}/easylzma/decompress.h
%{_libdir}/lib%{name}.so

%files static
%license LICENSE.txt
%doc README.rst
%doc AUTHORS.txt
%{_libdir}/lib%{name}.a


%changelog
* Mon Oct 14 2019 Qianqian Fang <fangqq@gmail.com> - 0.9.2-1
- Initial package
