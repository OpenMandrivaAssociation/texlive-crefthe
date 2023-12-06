Name:		texlive-crefthe
Version:	68813
Release:	1
Summary:	Cross referencing with proper definite articles
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/crefthe
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/crefthe.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/crefthe.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
By default, when using cleveref's \cref to reference
theorem-like environments, the names do not contain definite
articles. In languages such as French, Italian, Portuguese,
Spanish, etc. this results in incorrect grammar. For this
purpose, the current package offers \crefthe, which handles the
definite articles properly (especially for the article
contractions in many European languages).

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/crefthe
%doc %{_texmfdistdir}/doc/latex/crefthe

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
