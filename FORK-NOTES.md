# Glass Home customization branch

This fork keeps the original Aurora Glass source and GPL-3.0 attribution intact.
Upstream base: version 3.5.0, commit 9180a7fdd8595f24ac74d5efe692e46504e1bd7f.

The separate Glass Home dashboard composes the original English animated card
with standard Home Assistant presence and blind controls. Its private live
configuration stays outside this public repository.

`package/english/glass-home-example.yaml` is a generic example. Replace the
placeholder entities before using it. Open, Stop and Close use Home Assistant's
existing cover controls; adding the dashboard does not edit cover automations.
The Open and Close buttons have not been physically exercised as part of setup.

Keep dedicated heating schedule/frost controls separate from the card's generic
thermostat controls until the latter explicitly support that heating policy.
Do not expose boiler relays as ordinary light switches. Explicitly configure
scene behaviour instead of accepting default alarm-arm shortcuts.

Future integrated cover support should include position, availability and
supported-feature checks, and must not create schedules or move covers during
configuration. Any modified branded distribution must use a distinct name, as
required by the upstream README. Do not publish credentials, private household
configuration, location history or current device data in this public fork.
