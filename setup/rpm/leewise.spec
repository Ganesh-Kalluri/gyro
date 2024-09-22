%global name leewise
%global release 1
%global unmangled_version %{version}
%global __requires_exclude ^.*leewise/addons/mail/static/scripts/leewise-mailgate.py$

Summary: Leewise Server
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{unmangled_version}.tar.gz
License: LGPL-3
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Leewise <info@leewise.com>
Requires: sassc
BuildRequires: python3-devel
BuildRequires: pyproject-rpm-macros
Url: https://www.leewise.in

%description
Leewise is a complete ERP and CRM. The main features are accounting (analytic
and financial), stock management, sales and purchases management, tasks
automation, marketing campaigns, help desk, POS, etc. Technical features include
a distributed server, an object database, a dynamic GUI,
customizable reports, and XML-RPC interfaces.

%generate_buildrequires
%pyproject_buildrequires

%prep
%autosetup

%build
%py3_build

%install
%py3_install

%post
#!/bin/sh

set -e

LEEWISE_CONFIGURATION_DIR=/etc/leewise
LEEWISE_CONFIGURATION_FILE=$LEEWISE_CONFIGURATION_DIR/leewise.conf
LEEWISE_DATA_DIR=/var/lib/leewise
LEEWISE_GROUP="leewise"
LEEWISE_LOG_DIR=/var/log/leewise
LEEWISE_LOG_FILE=$LEEWISE_LOG_DIR/leewise-server.log
LEEWISE_USER="leewise"

if ! getent passwd | grep -q "^leewise:"; then
    groupadd $LEEWISE_GROUP
    adduser --system --no-create-home $LEEWISE_USER -g $LEEWISE_GROUP
fi
# Register "$LEEWISE_USER" as a postgres user with "Create DB" role attribute
su - postgres -c "createuser -d -R -S $LEEWISE_USER" 2> /dev/null || true
# Configuration file
mkdir -p $LEEWISE_CONFIGURATION_DIR
# can't copy debian config-file as addons_path is not the same
if [ ! -f $LEEWISE_CONFIGURATION_FILE ]
then
    echo "[options]
; This is the password that allows database operations:
; admin_passwd = admin
db_host = False
db_port = False
db_user = $LEEWISE_USER
db_password = False
addons_path = %{python3_sitelib}/leewise/addons
default_productivity_apps = True
" > $LEEWISE_CONFIGURATION_FILE
    chown $LEEWISE_USER:$LEEWISE_GROUP $LEEWISE_CONFIGURATION_FILE
    chmod 0640 $LEEWISE_CONFIGURATION_FILE
fi
# Log
mkdir -p $LEEWISE_LOG_DIR
chown $LEEWISE_USER:$LEEWISE_GROUP $LEEWISE_LOG_DIR
chmod 0750 $LEEWISE_LOG_DIR
# Data dir
mkdir -p $LEEWISE_DATA_DIR
chown $LEEWISE_USER:$LEEWISE_GROUP $LEEWISE_DATA_DIR

INIT_FILE=/lib/systemd/system/leewise.service
touch $INIT_FILE
chmod 0700 $INIT_FILE
cat << EOF > $INIT_FILE
[Unit]
Description=Leewise Open Source ERP and CRM
After=network.target

[Service]
Type=simple
User=leewise
Group=leewise
ExecStart=/usr/bin/leewise --config $LEEWISE_CONFIGURATION_FILE --logfile $LEEWISE_LOG_FILE
KillMode=mixed

[Install]
WantedBy=multi-user.target
EOF


%files
%{_bindir}/leewise
%{python3_sitelib}/%{name}-*.egg-info
%{python3_sitelib}/%{name}
