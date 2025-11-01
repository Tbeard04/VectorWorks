import React, { useState } from 'react';
import './App.css';

export default function App() {
  const [view, setView] = useState('home');

  const handleKey = (e, next) => {
    if (e.key === 'Enter' || e.key === ' ') {
      e.preventDefault();
      setView(next);
    }
  };

  return (
    <div className="app-shell">
      {/* Sidebar */}
      <aside className="sidebar" aria-label="Sidebar">
        <div
          className="brand"
          role="button"
          tabIndex={0}
          aria-label="VectorWorks home"
          onClick={() => setView('home')}
          onKeyDown={(e) => handleKey(e, 'home')}
        >
          VectorWorks
        </div>

        <nav className="nav" aria-label="Primary">
          <button
            className="nav-btn"
            onClick={() => setView('ee_basic')}
            aria-label="Open Basic Electrical Engineering"
          >
            ⚡ Basic Electrical Engineering
          </button>
        </nav>

        <div className="sidebar-foot">
          <small>v0.1 • Foundation UI</small>
        </div>
      </aside>

      {/* Main */}
      <main className="main">
        {view === 'home' && <Home />}
        {view === 'ee_basic' && <EEBasicPlaceholder onBack={() => setView('home')} />}
        <div className="footer">© {new Date().getFullYear()} VectorWorks</div>
      </main>
    </div>
  );
}

function Home(){
  return (
    <>
      <div className="hero">
        <span className="kicker">Design system · Accessible · Fast</span>
        <h1 className="h1">
          Engineering calculators with <span className="grad">clarity</span> and <span className="grad">speed</span>.
        </h1>
        <p className="sub">
          VectorWorks provides a unified hub for electrical and mechanical calculations. Clean UI, strong contrast,
          and clear units—so you can focus on getting the numbers right.
        </p>
      </div>

      <div className="grid">
        <section className="card">
          <h3>Electrical</h3>
          <p>Single/Three-phase amps, kW, kVA, PF guidance, and line-to-line reminders.</p>
          <div style={{marginTop:12}}><span className="badge">Coming online first</span></div>
        </section>

        <section className="card">
          <h3>Mechanical</h3>
          <p>Stress/strain, torque, power, fluids & thermodynamics—structured for quick inputs.</p>
          <div style={{marginTop:12}}><span className="badge">Roadmap</span></div>
        </section>
      </div>

      <div style={{marginTop:16}} className="panel">
        <strong>Design notes</strong>
        <p style={{margin:'8px 0 0', color:'var(--color-muted)'}}>
          • High contrast dark theme with focus rings and keyboard navigation.<br/>
          • Cards and panels keep content scannable. <br/>
          • One-click access to Basic Electrical Engineering in the sidebar.
        </p>
      </div>
    </>
  );
}

function EEBasicPlaceholder({ onBack }){
  return (
    <>
      <div className="hero">
        <span className="kicker">Electrical · Placeholder</span>
        <h1 className="h1">Basic Electrical Engineering</h1>
        <p className="sub">
          This page will host the interactive calculators for: Amps (single/three-phase), Real Power (kW), and Apparent Power (kVA).
          Three-phase calculations will clearly indicate the use of line-to-line voltage.
        </p>
      </div>

      <div className="grid">
        <section className="card">
          <h3>What’s coming</h3>
          <p>Inputs with unit hints, PF ranges &amp; validation, and a results panel with engineering notation.</p>
        </section>
        <section className="card">
          <h3>Equations covered</h3>
          <p>I (A), kW, kVA for single and three-phase systems; PF relationships and helpful reminders.</p>
        </section>
      </div>

      <div style={{marginTop:16, display:'flex', gap:12}}>
        <button className="nav-btn" onClick={onBack} aria-label="Back to home">← Back</button>
      </div>

      <div style={{marginTop:16}} className="panel">
        <strong>Note</strong>
        <p style={{margin:'8px 0 0', color:'var(--color-muted)'}}>
          This is a design-only placeholder. Integration with the Python calculator will be added later.
        </p>
      </div>
    </>
  );
}

