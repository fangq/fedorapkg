%global octpkg iso2mesh

Name:           octave-%{octpkg}
Version:        1.9.0
Release:        1.1%{?dist}
Summary:        Iso2Mesh - a 3D surface and volumetric mesh generator for MATLAB/Octave
License:        GPLv3+
URL:            https://github.com/fangq/iso2mesh
Source0:        https://github.com/fangq/iso2mesh/archive/v%{version}/%{octpkg}-%{version}-1.tar.gz
Source1:        https://github.com/fangq/cork/archive/v0.9/cork-v0.9.tar.gz
Source2:        https://github.com/fangq/meshfix/archive/v1.2.1/meshfix-v1.2.1.tar.gz
Source3:        http://ftp.mcs.anl.gov/pub/petsc/externalpackages/tetgen1.5.1.tar.gz
ExclusiveArch:  x86_64
BuildRequires:  cmake, CGAL-devel, SuperLU, SuperLU-devel, blas-static, tetgen

Requires:       octave
Requires(post): octave
Requires(postun): octave

%description
Iso2Mesh is a MATLAB/Octave-based mesh generation toolbox,
designed for easy creation of high quality surface and 
tetrahedral meshes from 3D volumetric images. It contains 
a rich set of mesh processing scripts/programs, working 
either independently or interacting with external free 
meshing utilities. Iso2Mesh toolbox can directly convert
a 3D image stack, including binary, segmented or gray-scale 
images such as MRI or CT scans, into quality volumetric 
meshes. This makes it particularly suitable for multi-modality 
medical imaging data analysis and multi-physics modeling.
Above all, iso2mesh is open-source. You can download it for 
free. You are also allowed to extend the toolbox for your
own research and share with other users. Iso2Mesh is 
cross-platform and is compatible with both MATLAB and GNU Octave 
(a free MATLAB clone).

%prep
%autosetup -n %{octpkg}-%{version} -b 1 -b 2 -b 3

cp COPYING.txt COPYING

cat > DESCRIPTION << EOF
Name: %{octpkg}
Version: %{version}
Date: %(date +"%Y-%d-%m")
Title: %{summary}
Author: Qianqian Fang <fangqq@gmail.com>
Maintainer: Qianqian Fang <fangqq@gmail.com>
Description: Iso2Mesh is a MATLAB/Octave-based mesh generation toolbox,
 designed for easy creation of high quality surface and 
 tetrahedral meshes from 3D volumetric images. It contains 
 a rich set of mesh processing scripts/programs, working 
 either independently or interacting with external free 
 meshing utilities. Iso2Mesh toolbox can directly convert
 a 3D image stack, including binary, segmented or gray-scale 
 images such as MRI or CT scans, into quality volumetric 
 meshes. This makes it particularly suitable for multi-modality 
 medical imaging data analysis and multi-physics modeling.
 Above all, iso2mesh is open-source. You can download it for 
 free. You are also allowed to extend the toolbox for your
 own research and share with other users. Iso2Mesh is 
 cross-platform and is compatible with both MATLAB and GNU Octave 
 (a free MATLAB clone).

Categories: Mesh
EOF

cat > INDEX << EOF
zmat >> ZMat
ZMat
 zmat
EOF


mkdir -p inst/
mv *.m inst/
mv *.fig inst/

%build
cd tools
make clean
make
mv bin inst
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
%doc sample
%doc README.txt
%doc AUTHORS.txt
%doc ChangeLog.txt
%dir %{octpkgdir}
%{octpkgdir}/*.m
%{octpkgdir}/*.fig
%doc %{octpkgdir}/doc-cache
%{octpkgdir}/packinfo

%changelog
* Tue Oct 01 2019 Qianqian Fang <fangqq@gmail.com> - 1.9.0-1.1
- Initial package
