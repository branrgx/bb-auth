# Fedora releases and COPR

`bb-auth.spec` downloads `v%{version}` from GitHub. Keep `VERSION`, the
spec's `Version`, and the release tag synchronized (for example `0.2.1`,
`0.2.1`, `v0.2.1`). Commit changes before creating the tag. Do not move
published tags. For a packaging-only rebuild, increment `Release`.

## COPR setup

Create the `bb-auth` project with the `fedora-44-x86_64` chroot, then add
an SCM package named `bb-auth`:

- Type: Git
- Clone URL: `https://github.com/branrgx/bb-auth.git`
- Committish: `main` (the tag event overrides this for release builds)
- Spec file: `bb-auth.spec`
- Subdirectory: empty
- SRPM build method: **make srpm** (uses `.copr/Makefile`)
- Enable automatic rebuilds for webhook handling.

In COPR Settings → Integrations, copy the **GitHub** webhook URL and append
`bb-auth/` so version-only tags select the package:

```text
https://copr.fedorainfracloud.org/webhooks/github/<ID>/<UUID>/bb-auth/
```

In GitHub Settings → Secrets and variables → Actions, create the repository
secret `COPR_WEBHOOK_URL` with that URL. Do not register the URL under GitHub
Webhooks: that would trigger builds before validation. This workflow uses the
GitHub webhook endpoint, not the custom webhook endpoint.

## Publish

Merge the packaging and workflow changes after CI passes. Update `VERSION`
and `Version` in the spec together, commit, then create a GitHub release with
the matching `vX.Y.Z` tag. Both workflows must exist in that tagged commit.

`.github/workflows/fedora.yml` builds, tests, and installs an RPM in Fedora 44
on pushes to `main` and pull requests.

`.github/workflows/copr-release.yml` runs when a stable release is published.
It checks that the tag is `v<VERSION>` and queries the latest Fedora push run
on `main` for the exact commit checked out from the release tag. Only a completed,
successful run allows the COPR webhook. It does not rebuild the RPM or rerun tests.
Prereleases are skipped. Missing, pending, failed, or cancelled validation blocks
the webhook; finish or fix the Fedora validation, then rerun the release workflow.
Publish releases after their commit passes validation on `main`. Pull-request
validation alone does not qualify. GitHub API access uses the workflow token with
`actions: read`; no additional secret is needed.

COPR checks out the tag, reads its spec, and downloads the versioned archive
to build the SRPM. A successful webhook request only means the request was
accepted; check the resulting build in COPR. If you add supported Fedora
versions, extend the validation job to cover them before publishing there.

The RPM configures `/usr/libexec/gcr-prompter` and installs the user unit in
`/usr/lib/systemd/user`, independently of Fedora's `/usr/lib64` library path.
Container validation does not test interactive authentication in a desktop
session; check polkit, keyring, and pinentry on Fedora before announcing support.

References: [COPR SCM and webhooks](https://docs.copr.fedorainfracloud.org/user_documentation.html),
[GitHub release events](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#release).
