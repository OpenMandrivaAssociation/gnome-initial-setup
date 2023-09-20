%define url_ver %(echo %{version}|cut -d. -f1,2)

Name:           gnome-initial-setup
Version:        45.0
Release:        1
Summary:        GNOME Initial Setup Assistant
License:        GPL-2.0-or-later
Group:          System/GUI/GNOME
URL:            https://wiki.gnome.org/Design/OS/InitialSetup
Source0:        https://download.gnome.org/sources/gnome-initial-setup/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:  pkgconfig(krb5)
BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  pkgconfig(accountsservice)
BuildRequires:  pkgconfig(cheese) >= 3.28
BuildRequires:  pkgconfig(cheese-gtk) >= 3.3.5
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(gdm) >= 3.8.3
BuildRequires:  pkgconfig(geocode-glib-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.53.0
BuildRequires:  pkgconfig(gnome-desktop-4)
BuildRequires:  pkgconfig(goa-1.0)
BuildRequires:  pkgconfig(goa-backend-1.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gsettings-desktop-schemas) >= 3.37.1
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gweather4)
BuildRequires:  pkgconfig(ibus-1.0) >= 1.4.99
BuildRequires:  pkgconfig(iso-codes)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(libgeoclue-2.0) >= 2.3.1
BuildRequires:  pkgconfig(libnm) >= 1.2
BuildRequires:  pkgconfig(libnma) >= 1.0
BuildRequires:  pkgconfig(libsecret-1) >= 0.18.8
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(pango) >= 1.32.5
BuildRequires:  pkgconfig(polkit-gobject-1) >= 0.103
BuildRequires:  pkgconfig(pwquality)
BuildRequires:  pkgconfig(rest-1.0)
BuildRequires:  pkgconfig(systemd) >= 242
BuildRequires:  pkgconfig(webkitgtk-6.0)

Requires:        tecla

%description
Initial assistant, helping you to get the system up and running.

%prep
%autosetup -p1

%build
%meson \
        -Dparental_controls=disabled
%meson_build

%install
%meson_install
%find_lang %{name} %{?no_lang_C}

%pre
useradd -rM -d /run/gnome-initial-setup/ -s /sbin/nologin %{name} || :

%files -f %{name}.lang
%license COPYING
%doc README.md
%{_datadir}/applications/gnome-initial-setup.desktop
%dir %{_datadir}/gnome-session
%dir %{_datadir}/gnome-session/sessions
%{_datadir}/gnome-session/sessions/gnome-initial-setup.session
%dir %{_datadir}/gnome-shell
%dir %{_datadir}/gnome-shell/modes
%{_datadir}/gnome-shell/modes/initial-setup.json
%{_datadir}/polkit-1/rules.d/20-gnome-initial-setup.rules
%{_libexecdir}/gnome-initial-setup
%{_libexecdir}/gnome-initial-setup-copy-worker
%{_libexecdir}/gnome-initial-setup-goa-helper
%{_sysconfdir}/xdg/autostart/gnome-initial-setup-copy-worker.desktop
%{_sysconfdir}/xdg/autostart/gnome-initial-setup-first-login.desktop
%{_userunitdir}/gnome-initial-setup-copy-worker.service
%{_userunitdir}/gnome-initial-setup-first-login.service
%{_prefix}/lib/sysusers.d/gnome-initial-setup.conf
%dir %{_userunitdir}/gnome-session@gnome-initial-setup.target.d
%{_userunitdir}/gnome-session@gnome-initial-setup.target.d/session.conf
%dir %{_userunitdir}/gnome-session.target.wants
%{_userunitdir}/gnome-session.target.wants/gnome-initial-setup-copy-worker.service
%{_userunitdir}/gnome-session.target.wants/gnome-initial-setup-first-login.service
