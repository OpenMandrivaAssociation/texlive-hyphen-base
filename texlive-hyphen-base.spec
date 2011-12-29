# revision 23418
# category TLCore
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-hyphen-base
Version:	20111103
Release:	1
Summary:	TeXLive hyphen-base package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-base.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive hyphen-base package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%config(noreplace) %{_texmfdir}/tex/generic/config/language.dat
%config(noreplace) %{_texmfdir}/tex/generic/config/language.dat.lua
%config(noreplace) %{_texmfdir}/tex/generic/config/language.def
%{_texmfdir}/tex/generic/config/language.us
%{_texmfdir}/tex/generic/config/language.us.def
%{_texmfdir}/tex/generic/config/language.us.lua
%{_texmfdir}/tex/generic/hyphen/dumyhyph.tex
%{_texmfdir}/tex/generic/hyphen/hyphen.tex
%{_texmfdir}/tex/generic/hyphen/hypht1.tex
%{_texmfdir}/tex/generic/hyphen/zerohyph.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf %{buildroot}%{_datadir}
