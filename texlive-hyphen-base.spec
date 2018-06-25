# revision 31131
# category TLCore
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-hyphen-base
Version:	20180404
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
%config(noreplace) %{_texmfdistdir}/tex/generic/config/language.dat
%config(noreplace) %{_texmfdistdir}/tex/generic/config/language.dat.lua
%config(noreplace) %{_texmfdistdir}/tex/generic/config/language.def
%{_texmfdistdir}/tex/generic/config/language.us
%{_texmfdistdir}/tex/generic/config/language.us.def
%{_texmfdistdir}/tex/generic/config/language.us.lua
%{_texmfdistdir}/tex/generic/hyphen/dumyhyph.tex
%{_texmfdistdir}/tex/generic/hyphen/hyphen.tex
%{_texmfdistdir}/tex/generic/hyphen/hypht1.tex
%{_texmfdistdir}/tex/generic/hyphen/zerohyph.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}
