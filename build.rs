// SPDX-FileCopyrightText: Advanced Micro Devices, Inc.
// SPDX-License-Identifier: Apache-2.0

fn main() -> aya_build::Result<()> {
    aya_build::build_ebpf(
        [aya_build::Package {
            name: "policy",
            root_dir: "policy",
            ..Default::default()
        }],
        aya_build::Toolchain::Custom("nightly-2026-07-06"),
    )
}
