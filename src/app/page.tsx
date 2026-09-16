import { buildHealthSnapshot } from "@/lib/health";

const engines = [
  ["Parallel Worktree Lab", "minimal / maintainable / performance"],
  ["Nightly Bug Hunt", "02:00 JST / static + dynamic checks"],
  ["Quality Gate", "lint / types / tests / build / security"],
  ["Evidence PR", "logs, test evidence, risks, rollback"],
] as const;

export default function Home() {
  const health = buildHealthSnapshot();

  return (
    <main className="shell">
      <header className="hero">
        <div>
          <p className="eyebrow">DIGITAL ZERØ / AUTONOMOUS ENGINEERING</p>
          <h1>Engineering Control Center</h1>
          <p className="lead">Detect → Analyze → Parallelize → Verify → PR → Human Gate.</p>
        </div>
        <div className="status" aria-label={`system status ${health.status}`}>
          <span className="statusDot" />
          <div><small>SYSTEM</small><strong>{health.status.toUpperCase()}</strong></div>
        </div>
      </header>

      <section className="grid" aria-label="engineering engines">
        {engines.map(([name, detail], index) => (
          <article className="card" key={name}>
            <span className="index">0{index + 1}</span>
            <h2>{name}</h2>
            <p>{detail}</p>
          </article>
        ))}
      </section>

      <section className="panel">
        <div><span>Service</span><strong>{health.service}</strong></div>
        <div><span>Version</span><strong>{health.version}</strong></div>
        <div><span>Health API</span><strong>/api/health</strong></div>
        <div><span>Merge policy</span><strong>HUMAN GATE</strong></div>
      </section>

      <footer>Raw &amp; Premium Engineering / DIGITAL ZERØ</footer>
    </main>
  );
}
