---
name: testing
description: Select Ricy test levels or combinations, plan integration/recovery validation, or distinguish PASS, UNKNOWN, and NOT RUN; not required to execute an already known check.
---

# testing

Consult the “Levels and evidence” section in [DEVELOPMENT](../../../docs/DEVELOPMENT.md)
and component rules to select Static, Component, Integration, Recovery, Visual, and
Environment. Read the selected validators before running them.

Use verify for safe checks and doctor for read-only diagnostics.
Do not install/restart services or run applicators as if they were tests.
A missing dependency means NOT RUN/UNKNOWN, never PASS. Doctor exit 0 does not
certify health. Do not report historical tests as if they had just been run.
Fix problems caused by the change; record preexisting problems.

At completion, use the following format with concrete commands and results:
```text
Validation:
PASS <check and scope>
FAIL <check and error, when applicable>
NOT RUN <check and reason>
NOT APPLICABLE <level and reason>
```

Do not conclude “This should work.”, “Probably fixed.”, or “Everything is
working.” without evidence. A passing offline test does not prove the entire session.
