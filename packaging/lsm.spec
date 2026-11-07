Name:           pichi-lsm
Version:        0.1.0~dev
Release:        1%{?buildtag}%{?dist}
Summary:        BPF LSM helper for Conglobate filesystem labels

License:        Apache-2.0 AND MIT AND BSD-3-Clause AND Unicode-3.0 AND Zlib AND (GPL-2.0-only OR BSD-2-Clause)
URL:            https://github.com/pichi-vm/lsm
Source0:        %{name}-%{version}.tar.gz
ExclusiveArch:  x86_64 aarch64

BuildRequires:  cargo
BuildRequires:  rust
BuildRequires:  gcc
BuildRequires:  git
BuildRequires:  rust-src
BuildRequires:  systemd-rpm-macros
BuildRequires:  llvm-devel
BuildRequires:  gcc-c++
Requires:       systemd

%description
BPF LSM helper for Conglobate filesystem labels.

%prep
%autosetup

%build
export CARGO_HOME="$PWD/.cargo-home"
cargo install --locked --version '=0.13.0' --root "$PWD/.build-tools" \
    --no-default-features --features "llvm-$(llvm-config --version | cut -d. -f1)" bpf-linker
export PATH="$PWD/.build-tools/bin:$PATH"
export RUSTC_BOOTSTRAP=1
cargo build --locked --release --bin pichi-lsm

%install
install -Dpm0755 target/release/pichi-lsm %{buildroot}%{_libexecdir}/pichi-lsm
install -Dpm0644 packaging/systemd/pichi-lsm.service %{buildroot}%{_unitdir}/pichi-lsm.service

find .cargo-home -type f \( -iname 'license*' -o -iname 'licence*' -o \
    -iname 'copying*' -o -iname 'notice*' -o -iname 'copyright*' \) \
    -exec install -Dm0644 '{}' '%{buildroot}%{_licensedir}/%{name}/dependencies/{}' \;

%check
! target/release/pichi-lsm 2> usage.txt
grep -q "usage: pichi-lsm PIN" usage.txt

%post
if [ -d /run/systemd/system ]; then systemctl daemon-reload || :; fi

%postun
if [ -d /run/systemd/system ]; then systemctl daemon-reload || :; fi

%files
%license %{_licensedir}/%{name}/dependencies/
%license LICENSE policy/LICENSE.BSD-2-Clause
%doc README.md
%{_libexecdir}/pichi-lsm
%{_unitdir}/pichi-lsm.service
