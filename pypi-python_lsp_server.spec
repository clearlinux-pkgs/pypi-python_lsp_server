#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-python_lsp_server
Version  : 1.7.4
Release  : 28
URL      : https://files.pythonhosted.org/packages/7e/56/b7c8569ab17ed75a858487d26fa5e8f489e72e8d5842107329490c6a6323/python-lsp-server-1.7.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/7e/56/b7c8569ab17ed75a858487d26fa5e8f489e72e8d5842107329490c6a6323/python-lsp-server-1.7.4.tar.gz
Summary  : Python Language Server for the Language Server Protocol
Group    : Development/Tools
License  : MIT
Requires: pypi-python_lsp_server-bin = %{version}-%{release}
Requires: pypi-python_lsp_server-license = %{version}-%{release}
Requires: pypi-python_lsp_server-python = %{version}-%{release}
Requires: pypi-python_lsp_server-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(setuptools)
BuildRequires : pypi(setuptools_scm)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Python LSP Server
[![image](https://github.com/python-ls/python-ls/workflows/Linux%20tests/badge.svg)](https://github.com/python-ls/python-ls/actions?query=workflow%3A%22Linux+tests%22) [![image](https://github.com/python-ls/python-ls/workflows/Mac%20tests/badge.svg)](https://github.com/python-ls/python-ls/actions?query=workflow%3A%22Mac+tests%22) [![image](https://github.com/python-ls/python-ls/workflows/Windows%20tests/badge.svg)](https://github.com/python-ls/python-ls/actions?query=workflow%3A%22Windows+tests%22) [![image](https://img.shields.io/github/license/python-ls/python-ls.svg)](https://github.com/python-ls/python-ls/blob/master/LICENSE)

%package bin
Summary: bin components for the pypi-python_lsp_server package.
Group: Binaries
Requires: pypi-python_lsp_server-license = %{version}-%{release}

%description bin
bin components for the pypi-python_lsp_server package.


%package license
Summary: license components for the pypi-python_lsp_server package.
Group: Default

%description license
license components for the pypi-python_lsp_server package.


%package python
Summary: python components for the pypi-python_lsp_server package.
Group: Default
Requires: pypi-python_lsp_server-python3 = %{version}-%{release}

%description python
python components for the pypi-python_lsp_server package.


%package python3
Summary: python3 components for the pypi-python_lsp_server package.
Group: Default
Requires: python3-core
Provides: pypi(python_lsp_server)
Requires: pypi(docstring_to_markdown)
Requires: pypi(jedi)
Requires: pypi(pluggy)
Requires: pypi(python_lsp_jsonrpc)
Requires: pypi(setuptools)
Requires: pypi(ujson)

%description python3
python3 components for the pypi-python_lsp_server package.


%prep
%setup -q -n python-lsp-server-1.7.4
cd %{_builddir}/python-lsp-server-1.7.4
pushd ..
cp -a python-lsp-server-1.7.4 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1690864513
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
pypi-dep-fix.py . jedi
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pypi-dep-fix.py . jedi
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-python_lsp_server
cp %{_builddir}/python-lsp-server-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-python_lsp_server/c0a4218ed5c81a62f45a9cc14735457e71102cee || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
pypi-dep-fix.py %{buildroot} jedi
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pylsp

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-python_lsp_server/c0a4218ed5c81a62f45a9cc14735457e71102cee

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
