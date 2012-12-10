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


%changelog
* Sat May 05 2012 Alexander Khrukin <akhrukin@mandriva.org> 3.2.0-1mdv2012.0
+ Revision: 796904
- verson update 3.2.0

* Thu Sep 22 2011 Götz Waschk <waschk@mandriva.org> 2.10.2-2
+ Revision: 700864
- rebuild

* Sat Jun 25 2011 Götz Waschk <waschk@mandriva.org> 2.10.2-1
+ Revision: 687168
- new version
- xz tarball

* Tue Jul 20 2010 Götz Waschk <waschk@mandriva.org> 2.10.1-1mdv2011.0
+ Revision: 555097
- update to new version 2.10.1

* Tue Apr 06 2010 Götz Waschk <waschk@mandriva.org> 2.10.0-1mdv2010.1
+ Revision: 532348
- update to new version 2.10.0

* Fri Feb 26 2010 Götz Waschk <waschk@mandriva.org> 2.9.2-1mdv2010.1
+ Revision: 511751
- update to new version 2.9.2

* Sun Jan 17 2010 Götz Waschk <waschk@mandriva.org> 2.9.1-1mdv2010.1
+ Revision: 492867
- update to new version 2.9.1

* Wed Jan 13 2010 Götz Waschk <waschk@mandriva.org> 2.9.0-1mdv2010.1
+ Revision: 490683
- new version
- bump deps
- update file list for new devel docs location

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Thu Feb 26 2009 Götz Waschk <waschk@mandriva.org> 2.3.1-1mdv2009.1
+ Revision: 345194
- update to new version 2.3.1

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 2.2.0-2mdv2009.0
+ Revision: 266997
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Wed Apr 30 2008 Götz Waschk <waschk@mandriva.org> 2.2.0-1mdv2009.0
+ Revision: 199568
- new version
- rename the source package
- new version
- bump major

* Wed Feb 27 2008 Götz Waschk <waschk@mandriva.org> 1.9.4-1mdv2008.1
+ Revision: 175733
- new version

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Oct 10 2007 Götz Waschk <waschk@mandriva.org> 1.9.3-1mdv2008.1
+ Revision: 96637
- new version
- new major
- new devel name

* Mon Jun 04 2007 Götz Waschk <waschk@mandriva.org> 0.3.1-1mdv2008.0
+ Revision: 35007
- new version

