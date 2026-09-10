# COPR SCM method: make srpm. Run from the repository root.
.PHONY: srpm
srpm:
	dnf -y install rpm-build rpmdevtools
	mkdir -p "$(outdir)"
	spectool -g -R bb-auth.spec
	rpmbuild -bs --define '_srcrpmdir $(outdir)' bb-auth.spec
