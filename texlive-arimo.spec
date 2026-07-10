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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The Arimo family, designed by Steve Matteson, is an innovative,
refreshing sans serif design which is metrically compatible with Arial.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/fonts
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/fonts
%dir %{_datadir}/texmf-dist/fonts/enc
%dir %{_datadir}/texmf-dist/fonts/map
%dir %{_datadir}/texmf-dist/fonts/tfm
%dir %{_datadir}/texmf-dist/fonts/truetype
%dir %{_datadir}/texmf-dist/fonts/type1
%dir %{_datadir}/texmf-dist/fonts/vf
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/fonts/arimo
%dir %{_datadir}/texmf-dist/fonts/enc/dvips
%dir %{_datadir}/texmf-dist/fonts/map/dvips
%dir %{_datadir}/texmf-dist/fonts/tfm/google
%dir %{_datadir}/texmf-dist/fonts/truetype/google
%dir %{_datadir}/texmf-dist/fonts/type1/google
%dir %{_datadir}/texmf-dist/fonts/vf/google
%dir %{_datadir}/texmf-dist/tex/latex/arimo
%dir %{_datadir}/texmf-dist/fonts/enc/dvips/arimo
%dir %{_datadir}/texmf-dist/fonts/map/dvips/arimo
%dir %{_datadir}/texmf-dist/fonts/tfm/google/arimo
%dir %{_datadir}/texmf-dist/fonts/truetype/google/arimo
%dir %{_datadir}/texmf-dist/fonts/type1/google/arimo
%dir %{_datadir}/texmf-dist/fonts/vf/google/arimo
%doc %{_datadir}/texmf-dist/doc/fonts/arimo/LICENSE.txt
%doc %{_datadir}/texmf-dist/doc/fonts/arimo/README
%doc %{_datadir}/texmf-dist/doc/fonts/arimo/arimo-samples.pdf
%doc %{_datadir}/texmf-dist/doc/fonts/arimo/arimo-samples.tex
%{_datadir}/texmf-dist/fonts/enc/dvips/arimo/arm_7miqnq.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/arimo/arm_c3z4r2.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/arimo/arm_f4duzd.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/arimo/arm_l3opzb.enc
%{_datadir}/texmf-dist/fonts/map/dvips/arimo/arimo.map
%{_datadir}/texmf-dist/fonts/tfm/google/arimo/Arimo-Bold-tlf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/google/arimo/Arimo-Bold-tlf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/google/arimo/Arimo-Bold-tlf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/google/arimo/Arimo-Bold-tlf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/google/arimo/Arimo-Bold-tlf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/google/arimo/Arimo-Bold-tlf-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/google/arimo/Arimo-BoldItalic-tlf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/google/arimo/Arimo-BoldItalic-tlf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/google/arimo/Arimo-BoldItalic-tlf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/google/arimo/Arimo-BoldItalic-tlf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/google/arimo/Arimo-BoldItalic-tlf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/google/arimo/Arimo-BoldItalic-tlf-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/google/arimo/Arimo-Italic-tlf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/google/arimo/Arimo-Italic-tlf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/google/arimo/Arimo-Italic-tlf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/google/arimo/Arimo-Italic-tlf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/google/arimo/Arimo-Italic-tlf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/google/arimo/Arimo-Italic-tlf-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/google/arimo/Arimo-tlf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/google/arimo/Arimo-tlf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/google/arimo/Arimo-tlf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/google/arimo/Arimo-tlf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/google/arimo/Arimo-tlf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/google/arimo/Arimo-tlf-ts1.tfm
%{_datadir}/texmf-dist/fonts/truetype/google/arimo/Arimo-Bold.ttf
%{_datadir}/texmf-dist/fonts/truetype/google/arimo/Arimo-BoldItalic.ttf
%{_datadir}/texmf-dist/fonts/truetype/google/arimo/Arimo-Italic.ttf
%{_datadir}/texmf-dist/fonts/truetype/google/arimo/Arimo-Regular.ttf
%{_datadir}/texmf-dist/fonts/type1/google/arimo/Arimo-Bold.pfb
%{_datadir}/texmf-dist/fonts/type1/google/arimo/Arimo-BoldItalic.pfb
%{_datadir}/texmf-dist/fonts/type1/google/arimo/Arimo-Italic.pfb
%{_datadir}/texmf-dist/fonts/type1/google/arimo/Arimo.pfb
%{_datadir}/texmf-dist/fonts/vf/google/arimo/Arimo-Bold-tlf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/google/arimo/Arimo-Bold-tlf-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/google/arimo/Arimo-BoldItalic-tlf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/google/arimo/Arimo-BoldItalic-tlf-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/google/arimo/Arimo-Italic-tlf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/google/arimo/Arimo-Italic-tlf-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/google/arimo/Arimo-tlf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/google/arimo/Arimo-tlf-ts1.vf
%{_datadir}/texmf-dist/tex/latex/arimo/LY1Arimo-TLF.fd
%{_datadir}/texmf-dist/tex/latex/arimo/OT1Arimo-TLF.fd
%{_datadir}/texmf-dist/tex/latex/arimo/T1Arimo-TLF.fd
%{_datadir}/texmf-dist/tex/latex/arimo/TS1Arimo-TLF.fd
%{_datadir}/texmf-dist/tex/latex/arimo/arimo.sty
