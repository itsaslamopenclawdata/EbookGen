# EbookGen - Implementation Plan

## Project Analysis

### Current State
- **Repository**: https://github.com/itsaslamopenclawdata/EbookGen
- **Status**: Architecture specification only (no code)
- **Contents**: 2 files (README.md, MULTI_AGENT_ARCHITECTURE.md)
- **Purpose**: Multi-agent ebook generation system

### What Needs to Be Built
A complete working system that implements:
1. Lead Orchestrator Agent
2. 6 Specialist Agents (Research, Outline, Writer, Editor, Formatter, Delivery)
3. 20+ Parallel Subagents
4. API endpoints for user input
5. Web interface for users
6. File generation (PDF, EPUB, MOBI, Word, Markdown)
7. Delivery system (GitHub, Google Drive)

---

## Implementation Phases

### Phase 1: Foundation (Week 1)
**Goal**: Core infrastructure and orchestrator

#### 1.1 Project Setup
```
EbookGen/
├── backend/                    # FastAPI backend
│   ├── app/
│   │   ├── api/               # API routes
│   │   ├── agents/            # Agent implementations
│   │   ├── services/          # Business logic
│   │   └── models/            # Database models
│   └── requirements.txt
├── frontend/                   # React frontend
│   ├── src/
│   │   ├── pages/            # Page components
│   │   ├── components/       # UI components
│   │   └── services/         # API calls
│   └── package.json
├── agents/                     # Agent configurations
│   ├── orchestrator/          # Lead orchestrator
│   ├── research/              # Research agent
│   ├── outline/               # Outline agent
│   ├── writer/                # Writer agent
│   ├── editor/                # Editor agent
│   ├── formatter/             # Formatter agent
│   └── delivery/              # Delivery agent
├── config/                     # Configuration files
├── logs/                       # Execution logs
├── outputs/                    # Generated ebooks
└── docker-compose.yml
```

#### 1.2 Backend Core
- [ ] FastAPI application setup
- [ ] Database models (SQLAlchemy)
- [ ] User authentication (JWT)
- [ ] Project/Task models
- [ ] Basic API endpoints:
  - POST /projects - Create new ebook project
  - GET /projects/{id} - Get project status
  - POST /projects/{id}/start - Start generation
  - GET /projects/{id}/status - Get current status

#### 1.3 Lead Orchestrator
- [ ] Task decomposition logic
- [ ] Subagent spawning system
- [ ] Progress monitoring
- [ ] Error handling and recovery
- [ ] Result aggregation

### Phase 2: Specialist Agents (Week 2)
**Goal**: Implement each specialist agent

#### 2.1 Research Agent
- [ ] web_search integration
- [ ] Source validation
- [ ] Subagent spawning (6 parallel)
- [ ] Output: Structured research JSON

#### 2.2 Outline Agent
- [ ] Chapter structure generator
- [ ] Section planning
- [ ] Word count allocation
- [ ] Subagent spawning (4 parallel)

#### 2.3 Writer Agent
- [ ] Chapter writing engine
- [ ] Style guidelines enforcement
- [ ] Subagent spawning (8 parallel)
- [ ] Output: Markdown content

#### 2.4 Editor Agent
- [ ] Grammar checking
- [ ] Fact verification
- [ ] Consistency checking
- [ ] Subagent spawning (6 parallel)

#### 2.5 Formatter Agent
- [ ] PDF generation (WeasyPrint/Puppeteer)
- [ ] EPUB generation (Pandoc)
- [ ] MOBI generation (KindleGen)
- [ ] Word export (python-docx)
- [ ] Markdown export
- [ ] Cover image generation

#### 2.6 Delivery Agent
- [ ] GitHub repository creation
- [ ] Google Drive upload
- [ ] Link generation
- [ ] Email notifications (optional)

### Phase 3: Frontend (Week 3)
**Goal**: User-facing web interface

#### 3.1 Pages
- [ ] Home - Landing page
- [ ] Dashboard - User projects list
- [ ] New Project - Create new ebook
- [ ] Project View - View generation progress
- [ ] Downloads - Download finished ebooks

#### 3.2 Components
- [ ] Progress tracker
- [ ] Agent status indicators
- [ ] Preview viewer
- [ ] Download manager

### Phase 4: Quality & Testing (Week 4)
**Goal**: Ensure reliability and quality

#### 4.1 Quality Gates
- [ ] Research → Outline gate (min 5 sources)
- [ ] Outline → Write gate (logical flow check)
- [ ] Write → Edit gate (word count validation)
- [ ] Edit → Format gate (quality score > 0.9)
- [ ] Format → Delivery gate (all formats valid)

#### 4.2 Testing
- [ ] Unit tests for each agent
- [ ] Integration tests
- [ ] E2E flow tests
- [ ] Performance benchmarks
- [ ] Load testing (10 concurrent)

### Phase 5: Deployment (Week 5)
**Goal**: Production-ready system

#### 5.1 Infrastructure
- [ ] Docker containers
- [ ] PostgreSQL database
- [ ] Redis for caching
- [ ] Celery for background tasks
- [ ] S3 for file storage

#### 5.2 CI/CD
- [ ] GitHub Actions
- [ ] Automated tests
- [ ] Deployment to cloud

---

## API Specification

### Endpoints

#### Authentication
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /api/v1/auth/register | Register new user |
| POST | /api/v1/auth/token | Login (get JWT) |
| GET | /api/v1/auth/me | Get current user |

#### Projects
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /api/v1/projects | List user projects |
| POST | /api/v1/projects | Create new project |
| GET | /api/v1/projects/{id} | Get project details |
| DELETE | /api/v1/projects/{id} | Delete project |
| POST | /api/v1/projects/{id}/start | Start generation |
| GET | /api/v1/projects/{id}/status | Get generation status |

#### Downloads
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /api/v1/projects/{id}/download/{format} | Download specific format |

---

## Agent Configuration

### Lead Orchestrator
```yaml
name: orchestrator
model: gpt-4
tools:
  - sessions_spawn
  - subagents
  - memory_search
  - web_search
  - web_fetch
```

### Research Agent
```yaml
name: research
model: gpt-4
subagents: 6
parallel: true
tools:
  - web_search
  - web_fetch
```

### Writer Agent
```yaml
name: writer
model: gpt-4
subagents: 8
parallel: true
output: markdown
```

---

## Database Schema

### Tables

#### users
- id (UUID, PK)
- email (unique)
- hashed_password
- full_name
- created_at

#### projects
- id (UUID, PK)
- user_id (FK)
- topic
- description
- word_count
- style
- status (pending, research, outline, writing, editing, formatting, delivery, completed, failed)
- created_at
- updated_at

#### chapters
- id (UUID, PK)
- project_id (FK)
- number
- title
- content (markdown)
- word_count
- status

#### research_data
- id (UUID, PK)
- project_id (FK)
- sources (JSON)
- findings (JSON)
- created_at

---

## Acceptance Criteria

### Performance
- [ ] Generate 50k word ebook in < 25 minutes
- [ ] 4-8x speedup vs sequential
- [ ] 99.9% subagent success rate
- [ ] < 5% timeout rate

### Quality
- [ ] 99% grammar accuracy
- [ ] 100% spelling accuracy
- [ ] 95% fact verification
- [ ] 0.9+ coherence score

### Features
- [ ] PDF export
- [ ] EPUB export
- [ ] MOBI export
- [ ] Word export
- [ ] GitHub delivery
- [ ] Google Drive delivery

### UI/UX
- [ ] Project creation flow
- [ ] Real-time progress tracking
- [ ] Download management
- [ ] Responsive design

---

## Implementation Notes

### Key Principles
1. **Accuracy > Speed** - Never compromise quality
2. **Modular** - Each agent has single responsibility
3. **Resilient** - Automatic error recovery
4. **Measured** - Quality gates at each stage

### Error Handling
- Subagent timeout: Retry with new subagent
- Partial failure: Continue with available data
- Complete failure: Sequential fallback
- Quality failure: Return to previous stage

### Monitoring
- Real-time progress updates
- Agent status tracking
- Performance metrics
- Error logging

---

## Next Steps

1. **Initialize project structure** - Create directories and config files
2. **Set up backend** - FastAPI with database models
3. **Implement orchestrator** - Core coordination logic
4. **Build specialist agents** - One by one
5. **Create frontend** - React interface
6. **Add formatting** - PDF/EPUB/MOBI generation
7. **Implement delivery** - GitHub/Drive integration
8. **Test thoroughly** - All quality gates
9. **Deploy** - Production infrastructure

---

**Last Updated:** 2026-02-28
