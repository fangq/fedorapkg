%global octpkg iso2mesh

Name:           octave-%{octpkg}
Version:        1.9.1
Release:        1%{?dist}
Summary:        Iso2Mesh - a 3D surface and volumetric mesh generator for MATLAB/Octave
License:        GPLv3+
URL:            http://iso2mesh.sf.net
Source0:        https://github.com/fangq/iso2mesh/archive/v%{version}/%{octpkg}-%{version}.tar.gz
Source1:        https://github.com/fangq/cork/archive/v0.9/cork-v0.9.tar.gz
Source2:        https://github.com/fangq/meshfix/archive/v1.2.1/meshfix-v1.2.1.tar.gz
Source3:        http://ftp.mcs.anl.gov/pub/petsc/externalpackages/tetgen1.5.1.tar.gz
Source4:        http://ftp.mcs.anl.gov/pub/petsc/externalpackages/tetgen1.4.3.tar.gz
BuildArch:      i386, x86_64
BuildRequires:  cmake, CGAL-devel, SuperLU, SuperLU-devel, blas-static

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
%autosetup -b 1 -n %{octpkg}-%{version}
%autosetup -b 2 -n %{octpkg}-%{version}
%autosetup -b 3 -n %{octpkg}-%{version}
%autosetup -b 4 -n %{octpkg}-%{version}
rm -rf tools/cork
rm -rf tools/meshfix
rm -rf tools/tetgen
mv ../cork-0.9 tools/cork
mv ../meshfix-1.2.1 tools/meshfix
mv ../tetgen1.5.1 tools/tetgen
rm -rf bin/*.mex* bin/*.exe bin/*.dll
cd ../tetgen1.4.3
make
cd ../%{octpkg}-%{version}
mv ../tetgen1.4.3/tetgen bin

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
iso2mesh >> Iso2Mesh
Iso2Mesh
 advancefront
 barydualmesh
 base64decode
 base64encode
 bbxflatsegment
 binsurface
 bwislands
 cgals2m
 cgalv2m
 deislands2d
 deislands3d
 delendelem
 deletemeshfile
 edgeneighbors
 elemfacecenter
 elemvolume
 extractloops
 extrudecurve
 extrudesurf
 faceneighbors
 fallbackexeext
 fast_match_bracket
 fillholes3d
 fillsurf
 finddisconnsurf
 flatsegment
 getexeext
 getintersecttri
 getoptkey
 getplanefrom3pt
 getvarfrom
 gzipdecode
 gzipencode
 highordertet
 i2m
 imedge3d
 img2mesh
 innersurf
 insurface
 internalpoint
 iso2meshver
 isoctavemesh
 jdatadecode
 jdataencode
 jnifticreate
 jsonopt
 latticegrid
 loadjnifti
 loadjson
 loadmsgpack
 loadnifti
 loadubjson
 lz4decode
 lz4encode
 lz4hcdecode
 lz4hcencode
 lzipdecode
 lzipencode
 lzmadecode
 lzmaencode
 m2v
 maskdist
 match_bracket
 maxsurf
 mcpath
 memmapstream
 mergemesh
 mergestruct
 mergesurf
 mesh2mask
 mesh2vol
 meshabox
 meshacylinder
 meshanellip
 meshasphere
 meshcentroid
 meshcheckrepair
 meshconn
 meshcylinders
 meshedge
 mesheuler
 meshface
 meshgrid5
 meshgrid6
 meshinterp
 meshquality
 meshrefine
 meshremap
 meshreorient
 meshresample
 meshunitsphere
 mwpath
 neighborelem
 nestbracket2dim
 nifticreate
 nii2jnii
 niicodemap
 niiformat
 nodevolume
 orderloopedge
 orthdisk
 outersurf
 plotedges
 plotmesh
 plotsurf
 plottetra
 qmeshcut
 raysurf
 raytrace
 readasc
 readgts
 readinr
 readmedit
 readmptiff
 readnifti
 readnirfast
 readoff
 readsmf
 readtetgen
 remeshsurf
 removedupelem
 removedupnodes
 removeisolatednode
 removeisolatedsurf
 rotatevec3d
 rotmat2vec
 s2m
 s2v
 saveabaqus
 saveasc
 savebinstl
 savebnii
 savedxf
 savegts
 saveinr
 savejmesh
 savejnifti
 savejnii
 savejson
 savemedit
 savemphtxt
 savemsgpack
 savemsh
 savenifti
 savenirfast
 saveoff
 savesmf
 savestl
 savesurfpoly
 savetetgenele
 savetetgennode
 saveubjson
 savevrml
 smoothbinvol
 smoothsurf
 sms
 sortmesh
 surf2mesh
 surf2vol
 surf2volz
 surfaceclean
 surfacenorm
 surfboolean
 surfdiffuse
 surfedge
 surfinterior
 surfpart
 surfplane
 surfreorient
 surfseeds
 surfvolume
 thickenbinvol
 thinbinvol
 uniqedges
 uniqfaces
 v2m
 v2s
 varargin2struct
 vol2mesh
 vol2restrictedtri
 vol2surf
 volface
 volmap2mesh
 zlibdecode
 zlibencode
EOF

mkdir -p inst/
mv *.m inst/
mv img2mesh.fig inst/

%build
cd tools
make
cd ../
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
%license COPYING.txt
%doc sample
%doc README.txt
%doc Content.txt
%doc AUTHORS.txt
%doc ChangeLog.txt
%dir %{octpkgdir}
%{octpkgdir}/*.m
%{octpkgdir}/*.fig
%doc %{octpkgdir}/doc-cache
%{octpkgdir}/packinfo

%changelog
* Wed Oct 02 2019 Qianqian Fang <fangqq@gmail.com> - 1.9.1-1
- Initial package
