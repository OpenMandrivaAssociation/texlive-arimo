Name:		texlive-arimo
Version:	68950
Release:	1
Summary:	Arimo sans serif fonts with LaTeX support
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/arimo
License:	apache2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/arimo.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/arimo.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The Arimo family, designed by Steve Matteson, is an innovative,
refreshing sans serif design which is metrically compatible
with Arial.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/arimo
%{_texmfdistdir}/fonts/vf/google/arimo
%{_texmfdistdir}/fonts/type1/google/arimo
%{_texmfdistdir}/fonts/truetype/google/arimo
%{_texmfdistdir}/fonts/tfm/google/arimo
%{_texmfdistdir}/fonts/map/dvips/arimo
%{_texmfdistdir}/fonts/enc/dvips/arimo
%doc %{_texmfdistdir}/doc/fonts/arimo

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
