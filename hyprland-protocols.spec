Summary:	Wayland protocol extensions for Hyprland
Name:		hyprland-protocols
Version:	0.6.1
Release:	1
License:	BSD
Group:		Development/Tools
#Source0Download: https://github.com/hyprwm/hyprland-protocols/releases
Source0:	https://github.com/hyprwm/hyprland-protocols/archive/v%{version}/%{name}-v%{version}.tar.gz
# Source0-md5:	6738ff12f0f93aa9876bc7241b6c5f54
URL:		https://hyprland.org/
BuildRequires:	meson >= 0.60.3
BuildRequires:	ninja
BuildRequires:	rpmbuild(macros) >= 1.736
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Wayland protocol extensions for Hyprland.

%prep
%setup -q

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%{_datadir}/hyprland-protocols
%{_npkgconfigdir}/hyprland-protocols.pc
