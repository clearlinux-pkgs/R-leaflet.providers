#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-leaflet.providers
Version  : 1.9.0
Release  : 12
URL      : https://cran.r-project.org/src/contrib/leaflet.providers_1.9.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/leaflet.providers_1.9.0.tar.gz
Summary  : Leaflet Providers
Group    : Development/Tools
License  : BSD-2-Clause
BuildRequires : buildreq-R

%description
# leaflet.providers
<!-- badges: start -->
[![CRAN
status](https://www.r-pkg.org/badges/version/leaflet.providers)](https://CRAN.R-project.org/package=leaflet.providers)
[![Travis build
status](https://travis-ci.org/rstudio/leaflet.providers.svg?branch=master)](https://travis-ci.org/rstudio/leaflet.providers)
[![Codecov test
coverage](https://codecov.io/gh/rstudio/leaflet.providers/branch/master/graph/badge.svg)](https://codecov.io/gh/rstudio/leaflet.providers?branch=master)

%prep
%setup -q -c -n leaflet.providers
cd %{_builddir}/leaflet.providers

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589825592

%install
export SOURCE_DATE_EPOCH=1589825592
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
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library leaflet.providers
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library leaflet.providers
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library leaflet.providers
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc leaflet.providers || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/leaflet.providers/DESCRIPTION
/usr/lib64/R/library/leaflet.providers/INDEX
/usr/lib64/R/library/leaflet.providers/LICENSE
/usr/lib64/R/library/leaflet.providers/Meta/Rd.rds
/usr/lib64/R/library/leaflet.providers/Meta/features.rds
/usr/lib64/R/library/leaflet.providers/Meta/hsearch.rds
/usr/lib64/R/library/leaflet.providers/Meta/links.rds
/usr/lib64/R/library/leaflet.providers/Meta/nsInfo.rds
/usr/lib64/R/library/leaflet.providers/Meta/package.rds
/usr/lib64/R/library/leaflet.providers/NAMESPACE
/usr/lib64/R/library/leaflet.providers/NEWS.md
/usr/lib64/R/library/leaflet.providers/R/leaflet.providers
/usr/lib64/R/library/leaflet.providers/R/leaflet.providers.rdb
/usr/lib64/R/library/leaflet.providers/R/leaflet.providers.rdx
/usr/lib64/R/library/leaflet.providers/help/AnIndex
/usr/lib64/R/library/leaflet.providers/help/aliases.rds
/usr/lib64/R/library/leaflet.providers/help/leaflet.providers.rdb
/usr/lib64/R/library/leaflet.providers/help/leaflet.providers.rdx
/usr/lib64/R/library/leaflet.providers/help/paths.rds
/usr/lib64/R/library/leaflet.providers/html/00Index.html
/usr/lib64/R/library/leaflet.providers/html/R.css
/usr/lib64/R/library/leaflet.providers/leaflet-providers_1.9.0.js
/usr/lib64/R/library/leaflet.providers/tests/testthat.R
/usr/lib64/R/library/leaflet.providers/tests/testthat/test-providers.R
/usr/lib64/R/library/leaflet.providers/tests/testthat/test-providersdetails.R
