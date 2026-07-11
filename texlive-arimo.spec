%global tl_name arimo
%global tl_revision 77682

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Arimo sans serif fonts with LaTeX support
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/arimo
License:	apache2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/arimo.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/arimo.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The Arimo family, designed by Steve Matteson, is an innovative,
refreshing sans serif design which is metrically compatible with Arial.

