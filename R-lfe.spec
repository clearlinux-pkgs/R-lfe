#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-lfe
Version  : 2.9.0
Release  : 64
URL      : https://cran.r-project.org/src/contrib/lfe_2.9-0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/lfe_2.9-0.tar.gz
Summary  : Linear Group Fixed Effects
Group    : Development/Tools
License  : Artistic-2.0
Requires: R-lfe-lib = %{version}-%{release}
Requires: R-Formula
Requires: R-sandwich
Requires: R-xtable
BuildRequires : R-Formula
BuildRequires : R-sandwich
BuildRequires : R-xtable
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Useful for estimating linear models with multiple group fixed effects, and for

%package extras
Summary: extras components for the R-lfe package.
Group: Default

%description extras
extras components for the R-lfe package.


%package lib
Summary: lib components for the R-lfe package.
Group: Libraries

%description lib
lib components for the R-lfe package.


%prep
%setup -q -n lfe
cd %{_builddir}/lfe

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1676394513

%install
export SOURCE_DATE_EPOCH=1676394513
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


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
/usr/lib64/R/library/lfe/WORDLIST
/usr/lib64/R/library/lfe/devtools_internal.R
/usr/lib64/R/library/lfe/doc/biascorrection.Rnw
/usr/lib64/R/library/lfe/doc/biascorrection.pdf
/usr/lib64/R/library/lfe/doc/identification.R
/usr/lib64/R/library/lfe/doc/identification.Rnw
/usr/lib64/R/library/lfe/doc/identification.pdf
/usr/lib64/R/library/lfe/doc/index.html
/usr/lib64/R/library/lfe/doc/lfehow.R
/usr/lib64/R/library/lfe/doc/lfehow.Rnw
/usr/lib64/R/library/lfe/doc/lfehow.pdf
/usr/lib64/R/library/lfe/doc/speed.R
/usr/lib64/R/library/lfe/doc/speed.Rnw
/usr/lib64/R/library/lfe/doc/speed.pdf
/usr/lib64/R/library/lfe/help/AnIndex
/usr/lib64/R/library/lfe/help/aliases.rds
/usr/lib64/R/library/lfe/help/figures/README-pressure-1.png
/usr/lib64/R/library/lfe/help/lfe.rdb
/usr/lib64/R/library/lfe/help/lfe.rdx
/usr/lib64/R/library/lfe/help/paths.rds
/usr/lib64/R/library/lfe/html/00Index.html
/usr/lib64/R/library/lfe/html/R.css
/usr/lib64/R/library/lfe/misc/CHANGELOG
/usr/lib64/R/library/lfe/misc/gen2.R
/usr/lib64/R/library/lfe/misc/index.html
/usr/lib64/R/library/lfe/misc/lfeguide.txt
/usr/lib64/R/library/lfe/misc/test2.lfe
/usr/lib64/R/library/lfe/tests/anomalies.R
/usr/lib64/R/library/lfe/tests/anomalies.Rout.save
/usr/lib64/R/library/lfe/tests/bctest.R
/usr/lib64/R/library/lfe/tests/bctest.Rout.save
/usr/lib64/R/library/lfe/tests/cgsolve.R
/usr/lib64/R/library/lfe/tests/cgsolve.Rout.save
/usr/lib64/R/library/lfe/tests/cluster.R
/usr/lib64/R/library/lfe/tests/cluster.Rout.save
/usr/lib64/R/library/lfe/tests/comparelm.R
/usr/lib64/R/library/lfe/tests/comparelm.Rout.save
/usr/lib64/R/library/lfe/tests/degenerate.R
/usr/lib64/R/library/lfe/tests/degenerate.Rout.save
/usr/lib64/R/library/lfe/tests/efcheck.R
/usr/lib64/R/library/lfe/tests/efcheck.Rout.save
/usr/lib64/R/library/lfe/tests/fourfac.R
/usr/lib64/R/library/lfe/tests/fourfac.Rout.save
/usr/lib64/R/library/lfe/tests/intact.R
/usr/lib64/R/library/lfe/tests/intact.Rout.save
/usr/lib64/R/library/lfe/tests/interact.R
/usr/lib64/R/library/lfe/tests/interact.Rout.save
/usr/lib64/R/library/lfe/tests/ivtest.R
/usr/lib64/R/library/lfe/tests/ivtest.Rout.save
/usr/lib64/R/library/lfe/tests/lfetest.R
/usr/lib64/R/library/lfe/tests/lfetest.Rout.save
/usr/lib64/R/library/lfe/tests/mlhs.R
/usr/lib64/R/library/lfe/tests/mlhs.Rout.save
/usr/lib64/R/library/lfe/tests/multiway.R
/usr/lib64/R/library/lfe/tests/multiway.Rout.save
/usr/lib64/R/library/lfe/tests/naomit.R
/usr/lib64/R/library/lfe/tests/naomit.Rout.save
/usr/lib64/R/library/lfe/tests/nonest.R
/usr/lib64/R/library/lfe/tests/nonest.Rout.save
/usr/lib64/R/library/lfe/tests/onefac.R
/usr/lib64/R/library/lfe/tests/onefac.Rout.save
/usr/lib64/R/library/lfe/tests/testthat.R
/usr/lib64/R/library/lfe/tests/testthat/test_clustering.R
/usr/lib64/R/library/lfe/tests/verify.R
/usr/lib64/R/library/lfe/tests/verify.Rout.save
/usr/lib64/R/library/lfe/tests/weights.R
/usr/lib64/R/library/lfe/tests/weights.Rout.save

%files extras
%defattr(-,root,root,-)
/usr/lib64/R/library/lfe/exec/lfescript

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/lfe/libs/lfe.so
/usr/lib64/R/library/lfe/libs/lfe.so.avx2
/usr/lib64/R/library/lfe/libs/lfe.so.avx512
