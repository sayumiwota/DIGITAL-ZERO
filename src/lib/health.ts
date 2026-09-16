export type HealthStatus = "ok" | "degraded";

export type HealthSnapshot = {
  service: "digital-zero-control-center";
  status: HealthStatus;
  timestamp: string;
  version: string;
};

export function buildHealthSnapshot(now: Date = new Date()): HealthSnapshot {
  return {
    service: "digital-zero-control-center",
    status: "ok",
    timestamp: now.toISOString(),
    version: process.env.VERCEL_GIT_COMMIT_SHA?.slice(0, 7) || "local",
  };
}
