Name:           ros-kinetic-nerian-sp1
Version:        1.6.3
Release:        0%{?dist}
Summary:        ROS nerian_sp1 package

Group:          Development/Libraries
License:        MIT
URL:            http://wiki.ros.org/nerian_sp1
Source0:        %{name}-%{version}.tar.gz

Requires:       SDL-devel
Requires:       boost-devel
Requires:       ros-kinetic-cv-bridge
Requires:       ros-kinetic-message-runtime
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-sensor-msgs
Requires:       ros-kinetic-std-msgs
BuildRequires:  SDL-devel
BuildRequires:  boost-devel
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-cv-bridge
BuildRequires:  ros-kinetic-message-generation
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-sensor-msgs
BuildRequires:  ros-kinetic-std-msgs

%description
Node for the SP1 Stereo Vision System by Nerian Vision Technologies

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Wed Oct 18 2017 Konstantin Schauwecker <konstantin.schauwecker@nerian.com> - 1.6.3-0
- Autogenerated by Bloom

* Tue May 30 2017 Konstantin Schauwecker <konstantin.schauwecker@nerian.com> - 1.6.2-0
- Autogenerated by Bloom

* Mon Mar 27 2017 Konstantin Schauwecker <konstantin.schauwecker@nerian.com> - 1.6.1-0
- Autogenerated by Bloom

* Wed Feb 15 2017 Konstantin Schauwecker <konstantin.schauwecker@nerian.com> - 1.6.0-0
- Autogenerated by Bloom

* Thu Jan 19 2017 Konstantin Schauwecker <konstantin.schauwecker@nerian.com> - 1.5.1-0
- Autogenerated by Bloom

* Tue Jan 17 2017 Konstantin Schauwecker <konstantin.schauwecker@nerian.com> - 1.5.0-0
- Autogenerated by Bloom

* Fri Oct 07 2016 Konstantin Schauwecker <konstantin.schauwecker@nerian.com> - 1.4.0-0
- Autogenerated by Bloom

* Tue May 17 2016 Konstantin Schauwecker <konstantin.schauwecker@nerian.com> - 1.3.3-0
- Autogenerated by Bloom

* Mon May 09 2016 Konstantin Schauwecker <konstantin.schauwecker@nerian.com> - 1.3.2-0
- Autogenerated by Bloom

* Mon May 09 2016 Konstantin Schauwecker <konstantin.schauwecker@nerian.com> - 1.3.1-0
- Autogenerated by Bloom

