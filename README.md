# EbookGen - Multi-Agent Ebook Generator

> **Repository:** https://github.com/itsaslamopenclawdata/EbookGen
> **Status:** 🚀 Active Development
> **Architecture:** Lead Orchestrator + 6 Specialist Agents + 20 Parallel Subagents

---

## 🎯 Purpose

High-performance ebook generation system using **parallel processing** to generate complete ebooks from topic input in 15-25 minutes (vs 60-120 minutes sequential).

**Core Philosophy:** "Accuracy > Speed. Speed is good, accuracy is better."

---

## 🏗️ Architecture

### Lead Orchestrator Agent (The Conductor)
- Task decomposition and assignment
- Parallel subagent spawning
- Progress monitoring and error recovery
- Result aggregation and quality review

### 6 Specialist Agents
1. **Research Agent** - Gather, validate, organize sources
2. **Outline Agent** - Structure chapters, sections, flow
3. **Writer Agent** - Generate high-quality content
4. **Editor Agent** - Grammar, fact-checking, consistency
5. **Formatter Agent** - PDF, EPUB, MOBI, Word exports
6. **Delivery Agent** - GitHub + Google Drive delivery

### Parallel Subagent Execution
- Research: 6 subagents (news, papers, reports, announcements, discussions, history)
- Writing: 8 subagents (1-2 chapters each)
- Editing: 6 subagents (grammar, flow, facts, consistency, style, readability)
- Formatting: 6 subagents (PDF, EPUB, MOBI, Word, Markdown, cover)
- Delivery: 4 subagents (GitHub, Drive, links, archive)

**Speedup:** 4-8x faster than sequential execution

---

## 📊 Performance

| Metric | Target | Measurement |
|--------|---------|-------------|
| Generation Time | < 25 min (50k words) | End-to-end timing |
| Quality Score | > 0.9 | AI evaluation |
| Grammar Accuracy | 99% | Automated check |
| Fact Verification | 95% | Cross-reference |
| Subagent Success Rate | 99.9% | Monitoring |

---

## 🔄 Workflow

```
User Input (Topic)
    ↓
Lead Orchestrator (decomposes task)
    ↓
6 Specialist Agents (spawn 20+ subagents)
    ├── Research (6 parallel)
    ├── Outline (4 parallel)
    ├── Writer (8 parallel)
    ├── Editor (6 parallel)
    ├── Formatter (6 parallel)
    └── Delivery (4 parallel)
    ↓
Orchestrator (aggregates results)
    ↓
Final Product (eBook in 6 formats + delivery)
```

**Total Time:** 15-25 minutes (4-8x speedup)

---

## 📚 Documentation

- **[MULTI_AGENT_ARCHITECTURE.md](MULTI_AGENT_ARCHITECTURE.md)** - Complete architecture, agent details, best practices

---

## ✅ Key Features

- ✅ **Parallel Processing** - 20 subagents work simultaneously
- ✅ **Quality-First** - Accuracy > Speed, never compromise
- ✅ **Multi-Format** - PDF, EPUB, MOBI, Word, Markdown
- ✅ **Dual Delivery** - GitHub repository + Google Drive
- ✅ **Error Recovery** - Automatic fallback to sequential
- ✅ **Quality Gates** - Verification at each stage

---

## 🚀 Getting Started

See [MULTI_AGENT_ARCHITECTURE.md](MULTI_AGENT_ARCHITECTURE.md) for complete implementation guide.

---

**Last Updated:** 2026-02-18
**Author:** Clawsweety 🐾

---

*High-performance ebook generation through parallel agent orchestration*
