Summary:	Wayland protocol extensions for Hyprland
Name:		hyprland-protocols
Version:	0.6.2
Release:	1
License:	BSD
Group:		Development/Tools
#Source0Download: https://github.com/hyprwm/hyprland-protocols/releases
Source0:	https://github.com/hyprwm/hyprland-protocols/archive/v%{version}/%{name}-v%{version}.tar.gz
# Source0-md5:	fee99cadb24c14c1d14fa42c88965417
URL:		https://hyprland.org/
BuildRequires:	meson >= 0.60.3
BuildRequires:	ninja
BuildRequires:	rpmbuild(macros) >= 2.042
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Wayland protocol extensions for Hyprland.

%prep
%setup -q

%build
%meson

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%{_datadir}/hyprland-protocols
%{_npkgconfigdir}/hyprland-protocols.pc
