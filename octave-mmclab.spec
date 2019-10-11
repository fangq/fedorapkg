%global octpkg mmclab
%global project mmc
%global branch  mmcl

Name:           octave-%{octpkg}
Version:        1.7.9
Release:        1%{?dist}
Summary:        A GPU mesh-based Monte Carlo photon simulator for MATLAB/Octave
License:        GPLv3+
URL:            http://mcx.space/#mmc
Source0:        https://github.com/fangq/%{project}/archive/v%{version}/%{project}-%{version}.tar.gz
BuildRequires:  octave-devel gcc-c++ vim-common opencl-headers ocl-icd-devel

Requires:       octave opencl-filesystem octave-iso2mesh
Requires(post): octave
Requires(postun): octave
Recommends:     %{octpkg}-demos

%description
MMCLAB is the native MEX version of MMC - Mesh-based Monte Carlo - for
MATLAB and GNU Octave. By converting the input and output files into
convenient in-memory variables, MMCLAB is very intuitive to use and
straightforward to be integrated with mesh generation and post-simulation
analyses. Because MMCLAB contains the same computational codes for
OpenCL-based photon simulation as in a MMC binary, running MMCLAB
inside MATLAB is expected to give similar speed as running a standalone
MMC binary using either a CPU or a GPU.

%package -n %{octpkg}-demos
Summary:        Example datasets and scripts for MMCLAB toolbox
BuildArch:      noarch
Requires:       octave octave-%{octpkg} octave-iso2mesh

%description -n %{octpkg}-demos
This package contains the demo script and sample datasets for octave-%{octpkg}. 

%package -n %{project}
Summary:        Example datasets and scripts for mesh-based Monte Carlo (MMC)
BuildRequires:  octave-devel gcc-c++  vim-common opencl-headers ocl-icd-devel
Requires:       octave opencl-filesystem octave-iso2mesh

%description -n %{project}
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

%package -n %{project}-demos
Summary:        Example datasets and scripts for Mesh-based Monte Carlo - MMC
BuildArch:      noarch
Requires:       octave octave-iso2mesh

%description -n %{project}-demos
This package contains the demo script and sample datasets for MMC. 

%prep
%autosetup -n %{project}-%{version}
rm -rf .git_filters .gitattributes deploy webmmc
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
pushd src
%make_build oct LFLAGS="-L`octave-config -p OCTLIBDIR` -lOpenCL"
popd
rm %{octpkg}/*.txt
mv %{octpkg}/example .
mv %{octpkg} inst
mv src/Makefile .
%octave_pkg_build

mv Makefile src
pushd src
%make_build clean
%make_build
mkdir -p ../bin
cp bin/%{branch} ../bin/%{project}
popd

%if 0%{?fedora} <=30
   %global octave_tar_suffix any-none
%endif

%install
%octave_pkg_install

install -m 0755 -vd %{buildroot}%{_bindir}
install -m 0755 -vt %{buildroot}%{_bindir} bin/%{project}

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

%files
%license LICENSE.txt
%doc README.txt AUTHORS.txt
%dir %{octpkgdir}
%{octpkgdir}/*.m
%{octpkgdir}/*.mex
%doc %{octpkgdir}/doc-cache
%{octpkgdir}/packinfo

%files -n %{octpkg}-demos
%license LICENSE.txt
%doc README.txt AUTHORS.txt
%doc example

%files -n %{project}
%license LICENSE.txt
%doc README.txt AUTHORS.txt
%{_bindir}/%{project}

%files -n %{project}-demos
%license LICENSE.txt
%doc README.txt AUTHORS.txt
%doc examples

%changelog
* Fri Oct 04 2019 Qianqian Fang <fangqq@gmail.com> - 1.7.9-1
- Initial package
