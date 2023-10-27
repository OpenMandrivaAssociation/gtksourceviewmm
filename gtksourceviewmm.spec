%define url_ver %(echo %{version} | cut -d "." -f -2)

%global api 3.0
%global major 0
%global libname %mklibname %{name} %{api}
%global devname %mklibname %{name} %{api} -d

%global glibmm_version 2.46.1
%global gtkmm_version 3.18.0
%global gtksourceview_version 3.18.0

Summary:	Source code viewing library
Name:		gtksourceviewmm
Version:	3.18.0
Release:	1
License:	LGPLv2+
Group:		Editors
Url:		http://www.gnome.org/
Source0:	http://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	doxygen
BuildRequires:	graphviz
BuildRequires:	pkgconfig(glibmm-2.4) >= %{glibmm_version}
BuildRequires:	pkgconfig(gtkmm-3.0)  >= %{gtkmm_version}
BuildRequires:	pkgconfig(gtksourceview-3.0) >= %{gtksourceview_version}

%description
GtkSourceview is a library that adds syntax highlighting,
line numbers, and other programming-editor features.
GtkSourceView specializes these features for a code editor.

This package contains the C++ language bindings for GtkSourceview.

#--------------------------------------------------------------------

%package -n %{libname}
Summary:	Source code viewing library
Group:		System/Libraries

%description -n %{libname}
GtkSourceview is a library that adds syntax highlighting,
line numbers, and other programming-editor features.
GtkSourceView specializes these features for a code editor.

This package contains the C++ language bindings for GtkSourceview.

%files -n %{libname}
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/libgtksourceviewmm-%{api}.so.%{major}*

#--------------------------------------------------------------------

%package -n %{devname}
Summary:	Libraries and include files for GtkSourceView
Group:		Development/C++
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
GtkSourceView development files.

This package contains the C++ language bindings for GtkSourceview.

%files -n %{devname}
%doc %{_datadir}/doc/gtksourceviewmm-%{api}/
%{_datadir}/devhelp/books/gtksourceviewmm-%{api}
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{_libdir}/gtksourceviewmm*

#--------------------------------------------------------------------

%prep
%autosetup -p1

%build
%set_build_flags
./configure \
	--disable-static \
	--disable-silent-rules \
	--disable-dependency-tracking \
	--disable-rpath \
	--program-prefix= \
	--prefix=/usr \
	--libdir=/usr/lib64 \
	%{nil}
%make_build

%install
%make_install

