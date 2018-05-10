#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-lfe
Version  : 2.6.2291
Release  : 9
URL      : https://cran.r-project.org/src/contrib/lfe_2.6-2291.tar.gz
Source0  : https://cran.r-project.org/src/contrib/lfe_2.6-2291.tar.gz
Summary  : Linear Group Fixed Effects
Group    : Development/Tools
License  : Artistic-2.0
Requires: R-lfe-lib
Requires: R-Formula
Requires: R-sandwich
Requires: R-xtable
BuildRequires : R-Formula
BuildRequires : R-sandwich
BuildRequires : R-xtable
BuildRequires : clr-R-helpers

%description
Useful for estimating linear models with multiple group fixed effects, and for
  estimating linear models which uses factors with many levels as pure control variables.
  Includes support for instrumental variables, conditional F statistics for weak instruments,
  robust and multi-way clustered standard errors, as well as limited mobility bias correction.

%package lib
Summary: lib components for the R-lfe package.
Group: Libraries

%description lib
lib components for the R-lfe package.


%prep
%setup -q -c -n lfe

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523313393

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1523313393
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library lfe
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library lfe
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library lfe
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library lfe|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/lfe/CITATION
/usr/lib64/R/library/lfe/DESCRIPTION
/usr/lib64/R/library/lfe/INDEX
/usr/lib64/R/library/lfe/Meta/Rd.rds
/usr/lib64/R/library/lfe/Meta/features.rds
/usr/lib64/R/library/lfe/Meta/hsearch.rds
/usr/lib64/R/library/lfe/Meta/links.rds
/usr/lib64/R/library/lfe/Meta/nsInfo.rds
/usr/lib64/R/library/lfe/Meta/package.rds
/usr/lib64/R/library/lfe/Meta/vignette.rds
/usr/lib64/R/library/lfe/NAMESPACE
/usr/lib64/R/library/lfe/NEWS.Rd
/usr/lib64/R/library/lfe/R/lfe
/usr/lib64/R/library/lfe/R/lfe.rdb
/usr/lib64/R/library/lfe/R/lfe.rdx
/usr/lib64/R/library/lfe/TODO
/usr/lib64/R/library/lfe/doc/CHANGELOG
/usr/lib64/R/library/lfe/doc/biascorrection.Rnw
/usr/lib64/R/library/lfe/doc/biascorrection.pdf
/usr/lib64/R/library/lfe/doc/gen2.R
/usr/lib64/R/library/lfe/doc/identification.R
/usr/lib64/R/library/lfe/doc/identification.Rnw
/usr/lib64/R/library/lfe/doc/identification.pdf
/usr/lib64/R/library/lfe/doc/index.html
/usr/lib64/R/library/lfe/doc/lfeguide.txt
/usr/lib64/R/library/lfe/doc/lfehow.R
/usr/lib64/R/library/lfe/doc/lfehow.Rnw
/usr/lib64/R/library/lfe/doc/lfehow.pdf
/usr/lib64/R/library/lfe/doc/speed.R
/usr/lib64/R/library/lfe/doc/speed.Rnw
/usr/lib64/R/library/lfe/doc/speed.pdf
/usr/lib64/R/library/lfe/doc/test2.lfe
/usr/lib64/R/library/lfe/exec/lfescript
/usr/lib64/R/library/lfe/help/AnIndex
/usr/lib64/R/library/lfe/help/aliases.rds
/usr/lib64/R/library/lfe/help/lfe.rdb
/usr/lib64/R/library/lfe/help/lfe.rdx
/usr/lib64/R/library/lfe/help/paths.rds
/usr/lib64/R/library/lfe/html/00Index.html
/usr/lib64/R/library/lfe/html/R.css
/usr/lib64/R/library/lfe/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/lfe/libs/lfe.so
/usr/lib64/R/library/lfe/libs/lfe.so.avx2
/usr/lib64/R/library/lfe/libs/lfe.so.avx512
