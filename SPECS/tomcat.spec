Summary: Tomcat application server
Name: tomcat
Version: 7.0.67
Release: 0.1
License: Proprietary
Group: System/Tools
URL: http://apache.tomcat.org/

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
# Debatable
Requires: java-1.8.0-openjdk

# Disable automatic dependency checking
Autoreqprov: 0
Autoreq: 0

# Sources
Source0:  apache-tomcat-7.0.67.tar.gz
Source1:  apache-log4j-1.2.16.tar.gz
Source2:  tomcat-juli-adapters.jar
Source3:  tomcat-juli.jar
Source4:  ojdbc6.jar
Source5:  http://apache.mirrorcatalogs.com//commons/logging/binaries/commons-logging-1.1.1-bin.tar.gz
Source6:  http://www.mysql.com/get/Downloads/Connector-J/mysql-connector-java-5.1.19.tar.gz
Source7:  http://download.oracle.com/otn-pub/java/javamail/1.4.5/javamail1_4_5.zip

%description
Apache Tomcat is an open source software implementation of the Java 
Servlet and JavaServer Pages technologies. The Java Servlet and 
JavaServer Pages specifications are developed under the Java Community
Process.

%pre

%prep

# Unpack the sources. Doing it this way because %setup is annoying

cd $RPM_BUILD_DIR
tar xvzf %{SOURCE0}
tar xvzf %{SOURCE1}
tar xvzf %{SOURCE5}
tar xvzf %{SOURCE6}
unzip -o %{SOURCE7}

# %setup

%build

%install
rm -rf $RPM_BUILD_ROOT

cd $RPM_BUILD_DIR/apache-tomcat-%{version}
mkdir -p $RPM_BUILD_ROOT/apps/tomcat/logs
cp -r bin $RPM_BUILD_ROOT/apps/tomcat/
cp -r conf $RPM_BUILD_ROOT/apps/tomcat/
cp -r lib $RPM_BUILD_ROOT/apps/tomcat/
cp -r work $RPM_BUILD_ROOT/apps/tomcat/

# log4j
cp -f $RPM_BUILD_DIR/apache-log4j-1.2.16/log4j-1.2.16.jar $RPM_BUILD_ROOT/apps/tomcat/lib/
cp -f %{SOURCE2} $RPM_BUILD_ROOT/apps/tomcat/lib/
cp -f %{SOURCE3} $RPM_BUILD_ROOT/apps/tomcat/bin/

# Get rid of logging.properties
rm -f $RPM_BUILD_ROOT/apps/tomcat/conf/logging.properties

# move server.xml to a sample
mv $RPM_BUILD_ROOT/apps/tomcat/conf/server.xml $RPM_BUILD_ROOT/apps/tomcat/conf/server_xml.sample

# Additional libs
cp -f %{SOURCE4} $RPM_BUILD_ROOT/apps/tomcat/lib/
cp -f $RPM_BUILD_DIR/mysql-connector-java-5.1.19/mysql-connector-java-5.1.19-bin.jar $RPM_BUILD_ROOT/apps/tomcat/lib/
cp -f $RPM_BUILD_DIR/commons-logging-1.1.1/commons-logging-1.1.1.jar $RPM_BUILD_ROOT/apps/tomcat/lib/
cp -f $RPM_BUILD_DIR/javamail-1.4.5/mail.jar $RPM_BUILD_ROOT/apps/tomcat/lib/mail-1.4.5.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%attr(755, root, root) /apps/tomcat

%post
