%define url_ver %(echo %{version} | cut -d "." -f -2)

%define api_version	3.0
%define lib_major	0
%define lib_name	%mklibname gtksourceviewmm %{api_version} %{lib_major}
%define develname	%mklibname -d gtksourceviewmm %{api_version}

Summary:	Source code viewing library
Name:		gtksourceviewmm
Version:	3.2.0
Release:	%mkrel 1
License:	LGPLv2+
Group:		Editors
URL:		http://www.gnome.org/
Source0:	http://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:  gtksourceview-3.0-devel >= 3.0.0
BuildRequires:	gtkmm3.0-devel >= 3.0.0
BuildRequires:	doxygen

%description
GtkSourceview is a library that adds syntax highlighting,
line numbers, and other programming-editor features.
GtkSourceView specializes these features for a code editor.

This package contains the C++ language bindings for GtkSourceview.

#--------------------------------------------------------------------

%package -n %{lib_name}
Summary:	Source code viewing library
Group:	System/Libraries

%description -n %{lib_name}
GtkSourceview is a library that adds syntax highlighting,
line numbers, and other programming-editor features.
GtkSourceView specializes these features for a code editor.

This package contains the C++ language bindings for GtkSourceview.

%files -n %{lib_name}
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/libgtksourceviewmm-%{api_version}.so.%{lib_major}*

#--------------------------------------------------------------------

%package -n %develname
Summary:        Libraries and include files for GtkSourceView
Group:          Development/C++
Requires: 	%lib_name = %version
Provides:	libgtksourceviewmm-devel = %{version}-%{release}
Provides:	gtksourceviewmm-devel = %{version}-%{release}
Provides:	libgtksourceviewmm-%{api_version}-devel = %{version}-%{release}

%description -n %develname
GtkSourceView development files 

This package contains the C++ language bindings for GtkSourceview.

%files -n %develname
%doc %_datadir/doc/gtksourceviewmm-%{api_version}/
%_datadir/devhelp/books/gtksourceviewmm-%{api_version}
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*
%_libdir/gtksourceviewmm*

#--------------------------------------------------------------------

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

rm -fr %buildroot%_libdir/*.la
