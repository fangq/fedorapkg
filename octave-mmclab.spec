%global octpkg mmclab
%global project mmc
%global branch  mmcl
%global _binaries_in_noarch_packages_terminate_build   0
%global debug_package %{nil}

Name:           octave-%{octpkg}
Version:        1.7.9
Release:        1%{?dist}
Summary:        MMCLAB - A GPU Mesh-based Monte Carlo photon simulator for MATLAB/Octave
License:        GPLv3+
URL:            http://mcx.space/#mmc
Source0:        https://github.com/fangq/%{project}/archive/v%{version}/%{project}-%{version}.tar.gz
BuildArch:      noarch
ExclusiveArch:  %{ix86} x86_64
BuildRequires:  octave opencl-headers ocl-icd-devel

Requires:       octave opencl-filesystem
Requires(post): octave
Requires(postun): octave

%description
Mesh-based Monte Carlo (MMC) is a 3D Monte Carlo (MC) simulation software 
for photon transport in complex turbid media. MMC combines the strengths
of the MC-based technique and the finite-element (FE) method: on the 
one hand, it can handle general media, including low-scattering ones, 
as in the MC method; on the other hand, it can use an FE-like tetrahedral 
mesh to represent curved boundaries and complex structures, making it
even more accurate, flexible, and memory efficient. MMC uses the
state-of-the-art ray-tracing techniques to simulate photon propagation in 
a mesh space. It has been extensively optimized for excellent computational
efficiency and portability. MMC currently supports both multi-threaded 
parallel computing and GPU to maximize performance on modern processors.

%prep
%autosetup -n %{project}-%{version}
rm -rf .git_filters .gitattributes deploy webmmc examples
cp matlab/*.m mmclab

cp LICENSE.txt COPYING

cat > DESCRIPTION << EOF
Name: %{octpkg}
Version: %{version}
Date: %(date +"%Y-%d-%m")
Title: %{summary}
Author: Qianqian Fang <fangqq@gmail.com>
Maintainer: Qianqian Fang <fangqq@gmail.com>
Description: Mesh-based Monte Carlo (MMC) is a 3D Monte Carlo (MC) simulation software 
 for photon transport in complex turbid media. MMC combines the strengths
 of the MC-based technique and the finite-element (FE) method: on the 
 one hand, it can handle general media, including low-scattering ones, 
 as in the MC method; on the other hand, it can use an FE-like tetrahedral 
 mesh to represent curved boundaries and complex structures, making it
 even more accurate, flexible, and memory efficient. MMC uses the
 state-of-the-art ray-tracing techniques to simulate photon propagation in 
 a mesh space. It has been extensively optimized for excellent computational
 efficiency and portability. MMC currently supports both multi-threaded 
 parallel computing and GPU to maximize performance on a multi-core processor.
EOF

cat > INDEX << EOF
mmclab >> MMCLAB
MMCLAB
 besselhprime
 besseljprime
 besselyprime
 cart2sphorigin
 generate_g1
 genT5mesh
 genT6mesh
 loadmch
 load_mc_prop
 mmc2json
 mmcadddet
 mmcaddsrc
 mmcdettime
 mmcdettpsf
 mmcdetweight
 mmcjacobian
 mmcjmua
 mmcjmus
 mmclab
 mmcmeanpath
 mmcmeanscat
 mmcraytrace
 mmcsrcdomain
 readmmcelem
 readmmcface
 readmmcmesh
 readmmcnode
 savemmcmesh
 spbesselh
 spbesselhprime
 spbesselj
 spbesseljprime
 spbessely
 spbesselyprime
 spharmonic
 sphdiffAcoeff
 sphdiffBcoeff
 sphdiffCcoeff
 sphdiffexterior
 sphdiffincident
 sphdiffinterior
 sphdiffscatter
 sphdiffusioninfinite
 sphdiffusion
 sphdiffusionscatteronly
 sphdiffusionsemi
 sphdiffusionslab
EOF

%build
cd src
make oct LIBOPENCLDIR=`octave-config -p OCTLIBDIR`
cd ../
rm README.txt
mv mmclab/README.txt .
rm mmclab/*.txt
mv mmclab/example .
mv mmclab inst
rm -rf src
rm -rf commons
%octave_pkg_build

%install
%octave_pkg_install

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

%files
%license LICENSE.txt
%doc example README.txt AUTHORS.txt
%dir %{octpkgdir}
%{octpkgdir}/*.m
%{octpkgdir}/*.mex
%doc %{octpkgdir}/doc-cache
%{octpkgdir}/packinfo

%changelog
* Fri Oct 04 2019 Qianqian Fang <fangqq@gmail.com> - 1.7.9-1
- Initial package
