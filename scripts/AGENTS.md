# Validation and diagnostics

Read [DEVELOPMENT](../docs/DEVELOPMENT.md). verify/doctor must remain read-only
with respect to the session and sources; isolated temporary tests are allowed.
Do not start/repair services, install packages, or conceal skips as PASS.
Check errors must propagate; missing dependencies produce NOT RUN/UNKNOWN.
Resolve the root relative to the script and test missing-file/link detection.
