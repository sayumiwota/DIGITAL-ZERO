import assert from "node:assert/strict";
import test from "node:test";
import { buildHealthSnapshot } from "../src/lib/health.ts";

test("health snapshot is deterministic for a supplied time", () => {
  const now = new Date("2026-09-17T00:00:00.000Z");
  const snapshot = buildHealthSnapshot(now);
  assert.equal(snapshot.service, "digital-zero-control-center");
  assert.equal(snapshot.status, "ok");
  assert.equal(snapshot.timestamp, "2026-09-17T00:00:00.000Z");
});
