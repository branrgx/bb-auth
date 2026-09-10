Name:           bb-auth
Version:        0.2.1
Release:        1%{?dist}
Summary:        Unified polkit, keyring, and pinentry authentication daemon

License:        BSD-3-Clause
URL:            https://github.com/branrgx/bb-auth
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  systemd-rpm-macros
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  qt6-qtbase-devel
BuildRequires:  polkit-devel
BuildRequires:  polkit-qt6-1-devel
BuildRequires:  gcr-devel
BuildRequires:  glib2-devel
BuildRequires:  json-glib-devel

Requires:       polkit
Requires:       polkit-qt6-1
Requires:       gcr
Requires:       json-glib
Requires:       gnome-keyring

%description
bb-auth is a unified Linux authentication daemon for Polkit,
GNOME Keyring prompts and GPG pinentry.

It supports external UI providers, allowing desktop shells and other
interfaces to provide their own authentication frontend while retaining
a built-in Qt fallback.

%prep
%autosetup
test "$(cat VERSION)" = "%{version}"

%build
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DBB_AUTH_SYSTEMD_USER_UNIT_DIR=%{_userunitdir} \
    -DBB_AUTH_GCR_PROMPTER_BINARY=%{_libexecdir}/gcr-prompter

%cmake_build

%install
%cmake_install

%check
QT_QPA_PLATFORM=offscreen QT_STYLE_OVERRIDE=Fusion %ctest

%post
%systemd_user_post bb-auth.service

%preun
%systemd_user_preun bb-auth.service

%postun
%systemd_user_postun bb-auth.service

%files
%license LICENSE
%doc README.md
%{_libexecdir}/bb-auth
%{_libexecdir}/bb-auth-fallback
%{_libexecdir}/bb-auth-bootstrap
%{_libexecdir}/bb-keyring-prompter
%{_libexecdir}/pinentry-bb
%{_userunitdir}/bb-auth.service
%{_datadir}/dbus-1/services/org.bb.auth.service
%{_datadir}/bb-auth/

%changelog
* Thu Sep 10 2026 branrgx - 0.2.1-1
- Initial Fedora COPR package
