Name:           zmat
Version:        0.9.2
Release:        1%{?dist}
Summary:        An eazy-to-use data compression library
License:        GPLv3+ or BSD
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


%package -n %{name}-devel
Summary:        Development files for zmat - an eazy-to-use data compression library
Provides:       %{name}-static = %{version}-%{release}
Requires:       %{name}

%description -n %{name}-devel
The %{name}-devel package provides the headers files and tools you may need to
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
install -m 755 -d %{buildroot}/%{_includedir}/
install -m 644 -t %{buildroot}/%{_includedir}/ include/%{name}lib.h

install -m 755 -d %{buildroot}/%{_libdir}/
install -m 755 -t %{buildroot}/%{_libdir}/ lib/lib%{name}.so.%{version}
install -m 644 -t %{buildroot}/%{_libdir}/ lib/lib%{name}.a
pushd %{buildroot}/%{_libdir}
    ln -s lib%{name}.so.%{version} lib%{name}.so
popd


%files
%license LICENSE.txt
%doc README.rst
%doc AUTHORS.txt
%doc ChangeLog.txt
%{_libdir}/lib%{name}.so.*


%files -n %{name}-devel
%license LICENSE.txt
%doc README.rst
%doc AUTHORS.txt
%{_includedir}/%{name}lib.h
%{_libdir}/lib%{name}.so
%{_libdir}/lib%{name}.a


%changelog
* Mon Oct 14 2019 Qianqian Fang <fangqq@gmail.com> - 0.9.2-1
- Initial package
