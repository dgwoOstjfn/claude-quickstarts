# App Spec Writing Guide

This guide explains how to write an effective `app_spec.txt` for the `/autonomous-build` skill.

## Why Spec Quality Matters

The Initializer agent generates **200 test cases** from your spec. Each test case needs:
- A clear description of what to verify
- Concrete steps to reproduce
- Expected results

**Rule of thumb:** You need ~80-100 atomic feature points in your spec to generate 200 quality test cases (each feature produces 2-3 tests covering functional + style aspects).

## Required Sections

### 1. `<project_name>` — What you're building

```xml
<project_name>Todo App - Task Management Interface</project_name>
```

### 2. `<overview>` — One paragraph summary

Describe the app in 2-4 sentences. Include the target user and core value proposition.

### 3. `<technology_stack>` — Exact tools and versions

Be specific. The agent will use exactly what you specify.

```xml
<!-- BAD: too vague -->
<frontend>Some frontend framework</frontend>

<!-- GOOD: precise -->
<frontend>
  <framework>React 18 with Vite</framework>
  <styling>Tailwind CSS (via CDN)</styling>
  <port>Launch on port 5173</port>
</frontend>
```

### 4. `<core_features>` — Atomic feature list, grouped by module

This is the most important section. Each `-` bullet becomes 1-3 test cases.

```xml
<!-- BAD: too coarse (1 bullet = vague, untestable) -->
<task_management>
  - Users can manage tasks
</task_management>

<!-- GOOD: atomic and testable -->
<task_management>
  - Create tasks with title (required), description (optional), due date, and category
  - Edit task title inline with click-to-edit
  - Mark tasks as complete/incomplete with animated checkbox
  - Delete tasks with confirmation dialog ("Are you sure?")
  - Drag-and-drop reordering within a list
</task_management>
```

**Target: 80-100 feature bullets minimum across all modules.**

### 5. `<database_schema>` — Table definitions with columns

Write out every table, every column, type, and constraint. The agent codes directly from this.

```xml
<tasks>
  - id INTEGER PRIMARY KEY AUTOINCREMENT
  - title TEXT NOT NULL
  - is_completed INTEGER NOT NULL DEFAULT 0
  - priority TEXT NOT NULL DEFAULT 'medium' CHECK(priority IN ('urgent','high','medium','low'))
  - category_id INTEGER REFERENCES categories(id) ON DELETE SET NULL
  - due_date TEXT (ISO 8601 or NULL)
  - created_at TEXT NOT NULL DEFAULT (datetime('now'))
</tasks>
```

### 6. `<api_endpoints_summary>` — Every route

```xml
<tasks>
  - GET    /api/tasks          List tasks (query: category, priority, status, search, sort)
  - POST   /api/tasks          Create task (body: title, description, priority, category_id)
  - PUT    /api/tasks/:id      Update task
  - DELETE /api/tasks/:id      Delete task
  - PATCH  /api/tasks/:id/toggle   Toggle complete/incomplete
</tasks>
```

### 7. `<ui_layout>` — Screen-by-screen layout description

Describe each major view: what's where, what elements are visible, how they're arranged.

### 8. `<design_system>` — Colors, typography, components

Include hex codes, font sizes, spacing, border radius, shadow values. The more specific, the better the style tests.

```xml
<!-- BAD -->
<color_palette>Use blue for primary</color_palette>

<!-- GOOD -->
<color_palette>
  - Primary: Indigo (#6366F1) for buttons, links, active states
  - Background: White (#FFFFFF light), Dark gray (#111827 dark)
  - Danger: Red-500 (#EF4444)
  - Priority: Urgent #EF4444, High #F97316, Medium #EAB308, Low #22C55E
</color_palette>
```

### 9. `<key_interactions>` — Step-by-step user flows

These map directly to test case `steps` fields. Write them as numbered sequences.

```xml
<task_completion_flow>
  1. User clicks checkbox on task card
  2. Checkbox fills with animated checkmark
  3. Title gets strikethrough animation
  4. After 500ms, task slides to "Completed" section
  5. If recurring, new task auto-created for next occurrence
</task_completion_flow>
```

### 10. `<implementation_steps>` — Build phases

Order from foundation to polish. The agent works through features by priority.

### 11. `<success_criteria>` — Acceptance criteria

Group by: functionality, UX, technical quality, design polish.

## Checklist

Before using your spec with `/autonomous-build`:

- [ ] 80+ atomic feature bullets in `<core_features>`
- [ ] All DB tables with columns and types
- [ ] All API endpoints with methods and parameters
- [ ] Color hex codes for every color used
- [ ] At least 4 key interaction flows with numbered steps
- [ ] Technology stack with exact framework names and ports
- [ ] Design system with component-level styling details
- [ ] Implementation steps ordered by dependency

## Size Reference

| Spec Size | Feature Points | Test Quality | Recommended |
|-----------|---------------|-------------|-------------|
| ~40 lines | ~15 | Poor — too many vague tests | No |
| ~200 lines | ~50 | Moderate — some gaps | Minimum |
| ~400 lines | ~80 | Good — solid coverage | Yes |
| ~600+ lines | ~100+ | Excellent — comprehensive | Ideal |

## Example

See [example_spec.txt](example_spec.txt) for a complete reference spec (~350 lines).
