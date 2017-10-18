Name:           ros-lunar-nerian-sp1
Version:        1.6.3
Release:        0%{?dist}
Summary:        ROS nerian_sp1 package

Group:          Development/Libraries
License:        MIT
URL:            http://wiki.ros.org/nerian_sp1
Source0:        %{name}-%{version}.tar.gz

Requires:       SDL-devel
Requires:       boost-devel
Requires:       ros-lunar-cv-bridge
Requires:       ros-lunar-message-runtime
Requires:       ros-lunar-roscpp
Requires:       ros-lunar-sensor-msgs
Requires:       ros-lunar-std-msgs
BuildRequires:  SDL-devel
BuildRequires:  boost-devel
BuildRequires:  ros-lunar-catkin
BuildRequires:  ros-lunar-cv-bridge
BuildRequires:  ros-lunar-message-generation
BuildRequires:  ros-lunar-roscpp
BuildRequires:  ros-lunar-sensor-msgs
BuildRequires:  ros-lunar-std-msgs

%description
Node for the SP1 Stereo Vision System by Nerian Vision Technologies

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/lunar" \
        -DCMAKE_PREFIX_PATH="/opt/ros/lunar" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/lunar

%changelog
* Wed Oct 18 2017 Konstantin Schauwecker <konstantin.schauwecker@nerian.com> - 1.6.3-0
- Autogenerated by Bloom

* Tue May 30 2017 Konstantin Schauwecker <konstantin.schauwecker@nerian.com> - 1.6.2-1
- Autogenerated by Bloom

* Tue May 30 2017 Konstantin Schauwecker <konstantin.schauwecker@nerian.com> - 1.6.2-0
- Autogenerated by Bloom

