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

## Integrated Glass Home card

The separately named `custom:glass-home-card` adds matching glass person cards,
illustrated inline blind controls and timed-appliance controls inside rooms.
Cover commands respect availability and supported features; no physical commands
run during setup. Motion chips explicitly show motion/no motion/unavailable.
House-window assignments can be set explicitly with the upstream `windows` map.

Build with `python tools/build-glass-home.py`. Copy the generated
`custom_components/aurora_glass/frontend/glass-home.js` to Home Assistant's
`www/glass-home.js` and add `/local/glass-home.js?v=1` as a JavaScript module
resource. Increment the query version after updating. Keep the original
integration installed/configured because the illustrations use its
`/aurora_glass/btn/` assets. Hide its duplicate sidebar shortcut in profile
Appearance settings; the Glass Home dashboard is the customised entry.

Configuration additions:

```yaml
type: custom:glass-home-card
language: en
people:
  - entity: person.example
    name: Resident
rooms:
  - name: Living room
    lights: [light.example]
    motion: binary_sensor.example_motion
    covers:
      - entity: cover.example
        name: Window blind
  - name: Bedroom
    controls:
      - entity: switch.example_blanket
        name: Electric blanket
        boost: input_boolean.example_timed_boost
```

The boost helper must already have an automation that turns on the appliance,
waits for its configured duration, turns it off and resets the helper. This card
does not invent or change that automation. Turn off explicitly turns off the
switch and resets the boost helper; it does not add the appliance to All off.

Tests: `node src/tests/room-controls.test.cjs`. The Open and Close controls were
rendered and capability-checked without moving physical covers. Timed heating
was not physically activated as part of visual verification.

Do not publish credentials, private household configuration, location history
or current device data in this public fork. Upstream attribution and licence
remain in place; the modified UI is separately named Glass Home.
