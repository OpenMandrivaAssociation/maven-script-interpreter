%_javapackages_macros
Name:           maven-script-interpreter
Version:        1.1
Release:        2.0%{?dist}
Summary:        Maven Script Interpreter
License:        ASL 2.0
URL:            http://maven.apache.org/shared/maven-script-interpreter/
Source0:        http://central.maven.org/maven2/org/apache/maven/shared/%{name}/%{version}/%{name}-%{version}-source-release.zip

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-components)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.beanshell:bsh)
BuildRequires:  mvn(org.codehaus.groovy:groovy)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)


%description
This component provides some utilities to interpret/execute some scripts for
various implementations: Groovy or BeanShell.


%package javadoc
Summary:        Javadoc for %{name}
    
%description javadoc
API documentation for %{name}.


%prep
%setup -q

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc DEPENDENCIES LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE
