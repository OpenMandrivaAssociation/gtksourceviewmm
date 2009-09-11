%define api_version	2.0
%define lib_major 2
%define lib_name	%mklibname gtksourceviewmm- %{api_version} %{lib_major}
%define develname %mklibname -d gtksourceviewmm- %{api_version}

Summary:	Source code viewing library
Name:		gtksourceviewmm
Version: 2.3.1
Release:	%mkrel 2
License:	GPL
Group:		Editors
URL:		http://www.gnome.org/
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}
BuildRequires:	libgtksourceview-devel
BuildRequires:	gtkmm2.4-devel
BuildRequires:	doxygen

%description
GtkSourceview is a library that adds syntax highlighting,
line numbers, and other programming-editor features.
GtkSourceView specializes these features for a code editor.

This package contains the C++ language bindings for GtkSourceview.

%package -n %{lib_name}
Summary:	Source code viewing library
Group:	System/Libraries

%description -n %{lib_name}
GtkSourceview is a library that adds syntax highlighting,
line numbers, and other programming-editor features.
GtkSourceView specializes these features for a code editor.

This package contains the C++ language bindings for GtkSourceview.

%package -n %develname
Summary:        Libraries and include files for GtkSourceView
Group:          Development/C++
Requires: %lib_name = %version
Provides:	libgtksourceviewmm-devel = %{version}-%{release}
Provides:	libgtksourceviewmm-%{api_version}-devel = %{version}-%{release}
Obsoletes: %mklibname -d gtksourceviewmm- 1.0 2

%description -n %develname
GtkSourceView development files 

This package contains the C++ language bindings for GtkSourceview.

%prep
%setup -q

%build

%configure2_5x

%make

%install
rm -rf %{buildroot} installed-docs

%makeinstall_std
mv %buildroot%_datadir/doc/*/docs/reference/ installed-docs

%if %mdkversion < 200900
%post -n %{lib_name} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{lib_name} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}


%files -n %{lib_name} 
%defattr(-,root,root)
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/libgtksourceviewmm-%{api_version}.so.%{lib_major}*

%files -n %develname
%defattr(-,root,root)
%doc installed-docs/*
%{_libdir}/*.so
%attr(644,root,root) %{_libdir}/*.la
%{_includedir}/*
%{_libdir}/pkgconfig/*
%_libdir/gtksourceviewmm*


