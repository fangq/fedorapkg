%global octpkg brain2mesh

Name:           octave-%{octpkg}
Version:        0.5
Release:        1%{?dist}
Summary:        A fully automated high-quality brain tetrahedral mesh generation toolbox
License:        GPLv2+
URL:            http://mcx.space/brain2mesh
Source0:        https://github.com/fangq/%{octpkg}/archive/v%{version}/%{octpkg}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  octave-devel

Requires:       octave octave-image octave-iso2mesh octave-jsonlab octave-zmat octave-jnifti
Requires(post): octave
Requires(postun): octave

%description
The Brain2Mesh toolbox provides a streamlined matlab function to convert
a segmented brain volumes and surfaces into a high-quality multi-layered
tetrahedral brain/full head mesh. Typical inputs include segmentation
outputs from SPM, FreeSurfer, FSL etc. This tool does not handle the
segmentation of MRI scans, but examples of how commonly encountered
segmented datasets can be used to create meshes can be found in the 
package named %{octpkg}-demos.


%package -n %{octpkg}-demos
Summary:        Example datasets and scripts for the brain2mesh toolbox
BuildArch:      noarch
Requires:       octave octave-%{octpkg}

%description -n %{octpkg}-demos
This package contains the demo script and sample datasets for octave-%{octpkg}. 

%prep
%autosetup -n %{octpkg}-%{version}

cp LICENSE.txt COPYING

cat > DESCRIPTION << EOF
Name: %{octpkg}
Version: %{version}
Date: %(date +"%Y-%d-%m")
Title: %{summary}
Author: Qianqian Fang <fangqq@gmail.com> and Anh Phong Tran <tran.anh@husky.neu.edu>
Maintainer: Qianqian Fang <fangqq@gmail.com>
Description:  The Brain2Mesh toolbox provides a streamlined matlab function to convert
 a segmented brain volumes and surfaces into a high-quality multi-layered
 tetrahedral brain/full head mesh. Typical inputs include segmentation
 outputs from SPM, FreeSurfer, FSL etc. This tool does not handle the
 segmentation of MRI scans, but examples of how commonly encountered
 segmented datasets can be used to create meshes can be found in the 
 package named %{octpkg}-demos.
URL: %{url}
Depends: image, iso2mesh, jsonlab, jnifti, zmat
EOF

cat > INDEX << EOF
brain2mesh >> Brain2Mesh
 brain2mesh
 intriangulation
EOF

mkdir -p inst/
mv *.m inst/

%build
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
%doc README.md
%dir %{octpkgdir}
%{octpkgdir}/*.m
%doc %{octpkgdir}/doc-cache
%{octpkgdir}/packinfo

%files -n %{octpkg}-demos
%license LICENSE.txt
%doc examples

%changelog
* Fri Oct 11 2019 Qianqian Fang <fangqq@gmail.com> - 0.5-1
- Initial package
