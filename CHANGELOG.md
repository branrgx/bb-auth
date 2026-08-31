# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.1] - 2026-08-30

### Changed
- Document this repository as an independently maintained fork of the original bb-auth project
- Clarify that this fork primarily supports the BB Auth provider in the Noctalia plugin collection

### Fixed
- Include the POSIX header required for `getpid()`, fixing builds with GCC 16

## [0.1.0] - 2025-02-15

### Added
- Initial public release
- Unified polkit, keyring, and pinentry authentication daemon
- Shell provider IPC protocol for Waybar, ags, and custom widgets
- Fallback window with touch sensor support (fingerprint, FIDO2)
- Systemd user service with security hardening
- D-Bus service integration
- Bootstrap script for automatic configuration
- Migration script (`bb-auth-migrate`) for users upgrading from noctalia-auth
- Comprehensive documentation (README, troubleshooting, provider contract)
- Test suite with QtTest coverage
- AUR PKGBUILD with check() function
- Nix flake support
- CI workflows for Arch Linux and Nix builds
