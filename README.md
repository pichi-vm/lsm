# LSM

Allows image builders to set SELinux labels inside user namespaces.

Run `pichi-lsm PIN` to load the policy and pin its attachment at `PIN`
in a mounted BPF filesystem.

## Distribution packages

Main snapshots are built for `amd64`/`x86_64` and `arm64`/`aarch64` in
[`npmccallum/pichi` COPR](https://copr.fedorainfracloud.org/coprs/npmccallum/pichi/)
and [`ppa:nmccallum/pichi`](https://launchpad.net/~nmccallum/+archive/ubuntu/pichi).
The package name is `pichi-lsm`. These are guest packages for releases with
kernel 7.0 or newer. The package owns `/usr/libexec/pichi-lsm` and
`pichi-lsm.service`. The appliance configures consumers to require and run
after the policy service. Installing the package does not start the service.

COPR tracks `main`, uses `.copr/lsm.spec`, and runs the
`.copr/Makefile` source-RPM target. GitHub pushes prepared Debian source to
Launchpad; see [debian/README.source](debian/README.source) for that process.
