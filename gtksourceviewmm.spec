%define url_ver %(echo %{version} | cut -d "." -f -2)

%define api 3.0
%define major 0
%define libname %mklibname gtksourceviewmm %{api} %{major}
%define devname %mklibname gtksourceviewmm %{api} -d

Summary:	Source code viewing library
Name:		gtksourceviewmm
Version:	3.2.0
Release:	2
License:	LGPLv2+
Group:		Editors
Url:		http://www.gnome.org/
Source0:	http://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	doxygen
BuildRequires:	pkgconfig(gtkmm-3.0)
BuildRequires:	pkgconfig(gtksourceview-3.0)

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
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std
