%define major		2
%define libname		%mklibname lept %major
%define develname	%mklibname -d lept

Name:		leptonica
Version:	1.69
Release:	1
Summary:	C library for image processing and image analysis operations
URL:		http://www.leptonica.org
License:	MIT
Group:		Graphics

Source0:	%{name}-%{version}.tar.gz
BuildRequires:	zlib-devel
BuildRequires:	tiff-devel
BuildRequires:	jpeg-devel
BuildRequires:	png-devel
BuildRequires:	giflib-devel

%description
Well-tested C code for some basic image processing operations, along with
a description of the functions and some design methods. A full set of affine
transformations (translation, shear, rotation, scaling) on images of all depths
is included, with the exception that some of the scaling methods do not work
at all depths. There are also implementations of binary morphology, grayscale
morphology, convolution and rank order filters, and applications such as jbig2
image processing and color quantization.

%package -n %libname 
Summary:	C library for image processing and image analysis operations

%description -n %libname
Well-tested C code for some basic image processing operations, along with
a description of the functions and some design methods. A full set of affine
transformations (translation, shear, rotation, scaling) on images of all depths
is included, with the exception that some of the scaling methods do not work
at all depths. There are also implementations of binary morphology, grayscale
morphology, convolution and rank order filters, and applications such as jbig2
image processing and color quantization.

%files -n %libname
%{_libdir}/*.so.*

%package -n %develname
Summary:	C library for image processing and image analysis operations
Requires:	%libname = %{version}
Provides:	leptonica-devel = %version

%description -n %develname
Well-tested C code for some basic image processing operations, along with
a description of the functions and some design methods. A full set of affine
transformations (translation, shear, rotation, scaling) on images of all depths
is included, with the exception that some of the scaling methods do not work
at all depths. There are also implementations of binary morphology, grayscale
morphology, convolution and rank order filters, and applications such as jbig2
image processing and color quantization.

This package contains development files only.

%files -n %develname
%{_libdir}/*.so
%{_includedir}/leptonica
%doc leptonica-license.txt README.html

%prep
%setup -q

%build
%configure2_5x --disable-static --disable-programs
%make

%install
%makeinstall_std


%changelog
* Thu Feb 16 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.68-2
+ Revision: 775145
- rebuild and release bump

* Sat Nov 05 2011 Andrey Smirnov <asmirnov@mandriva.org> 1.68-1
+ Revision: 720806
- libpng15 compatibility fixed
- imported package leptonica

