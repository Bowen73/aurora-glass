/* Glass Home room controls. Pure state helpers; no commands run on setup. */
(function (g) {
  "use strict";
  function available(s) { return !!s && s.state !== "unknown" && s.state !== "unavailable"; }
  function cover(s) {
    var ok = available(s), a = s && s.attributes || {}, f = Number(a.supported_features) || 0;
    var p = typeof a.current_position === "number" && isFinite(a.current_position) ? Math.max(0, Math.min(100, a.current_position)) : null;
    var state = ok ? s.state : "unavailable";
    return { available: ok, position: p, state: state,
      open: ok && !!(f & 1) && state !== "opening" && !(state === "open" && p === 100),
      close: ok && !!(f & 2) && state !== "closing" && state !== "closed" && p !== 0,
      stop: ok && !!(f & 8) };
  }
  function command(entity, action, s) {
    if (!/^cover\.[a-z0-9_]+$/.test(entity || "") || ["open", "close", "stop"].indexOf(action) < 0 || !cover(s)[action]) return null;
    return { domain: "cover", service: action + "_cover", data: { entity_id: entity } };
  }
  g.GlassHomeRoomControls = { available: available, cover: cover, command: command };
})(typeof window === "undefined" ? globalThis : window);
