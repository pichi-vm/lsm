# Appliance LSM policy

This repository owns the fixed BPF `policy` and its `lsm` loader. Appliance
producers consume a pinned Git submodule and compile the loader, which embeds
the policy.

The policy requests a capability-check exemption for the `security.selinux`
xattr through `inode_xattr_skipcap`, preserving an earlier LSM's nonzero result.
The appliance starts `lsm PIN` to attach the policy and pin its link
at the supplied bpffs path.

The [CI workflow](.github/workflows/ci.yml) builds with Fedora's Rust sources
and LLVM 21, using `bpf-linker` 0.13.0. `RUSTC_BOOTSTRAP=1` enables Cargo's
`build-std=core` support for the BPF target. Formatting, Clippy, license headers,
dependency checks and kernel verification run on native amd64 and ARM64.
The verifier test loads the policy without attaching it. Appliance boot and
build integration tests belong to the consuming repositories.

The loader and build script use Apache-2.0. The BPF program uses
GPL-2.0-only OR BSD-2-Clause, as recorded in its source and manifest.
