import os

PHASE_STANDARD_TEMPLATE = """# Phase {num:02d} — {name}

## Status
{status}

## Purpose
{goal}

## Why This Phase Exists
This phase establishes the necessary foundation for {name}, ensuring that Omnix can fulfill its architectural requirements without resorting to hardcoded solutions.

## User / System Outcome
Upon completion, the system will support {name} capabilities dynamically and safely.

## Dependencies
{dependencies}

## Prerequisites
Completion of dependent phases and architectural review.

## Architecture Context
Integrates into the Omnix Executive pipeline. Adheres to the Zero Hardcoded Command principle.

## Scope
{scope}

## Out of Scope
{out_of_scope}

## Components Introduced
- (To be defined during detailed design)

## Responsibilities
- Implement {name} interfaces and logic.

## Interfaces / Contracts Required
- Standard Omnix Agent/Capability contracts.

## Data Models / Concepts
{concepts}

## Runtime Flow
1. Executive requests capability.
2. Capability executes.
3. Verification checks outcome.

## Detailed Tasks
- TBD during implementation planning.

## Suggested Task IDs
- OMX-PH{num:02d}-001

## Development Order
1. Define interfaces.
2. Implement core logic.
3. Integrate with Capability Router.
4. Add tests.

## Architecture Constraints
- MUST NOT use hardcoded natural-language command routing.
- MUST NOT bypass the Omnix Executive.

## Failure Cases
- Missing permissions.
- Timeout during execution.

## Safety Considerations
- Follow `SECURITY.md` guidelines for all new capabilities.

## Observability Requirements
- Structured logging for all state changes.

## Unit Testing Requirements
- 100% coverage on core logic.

## Integration Testing Requirements
- Test with simulated World State.

## Real Runtime Testing Requirements
- {runtime_tests}

## Acceptance Criteria
- {acceptance}

## Definition of Done
- Code merged.
- Tests passing (including real runtime).
- Documentation updated.

## Required Evidence
- Test logs demonstrating successful dynamic execution.

## Documentation Updates
- Update `MEMORY.md` and `TASKS.md`.

## Risks
- Unexpected OS behavior.

## Open Questions
- (To be determined)

## Next Phase
Proceed to Phase {next_num:02d} once completed.
"""

phases = [
    {
        "num": 0, "name": "Blueprint", "status": "IN PROGRESS", "goal": "Create and lock the architecture/documentation blueprint.",
        "dependencies": "None", "scope": "project vision, requirements, architecture, agent boundaries, capability boundaries, world state model, canonical lifecycle, zero-hardcoded-task law, testing strategy, security model, development rules, roadmap, decision records",
        "out_of_scope": "Implementation of real Omnix features (Python runtime, AI integrations, etc.)",
        "concepts": "- Architecture blueprint\n- Phase standard\n- Rules",
        "runtime_tests": "None (Documentation only)",
        "acceptance": "All foundational docs exist. They agree. No major architecture contradiction remains. Phase 1 can be started without inventing foundational architecture."
    },
    {
        "num": 1, "name": "Runtime Foundation", "status": "NOT STARTED", "goal": "Build the runtime foundation without intelligence.",
        "dependencies": "Phase 0", "scope": "configuration, application/runtime bootstrap, startup, shutdown, service lifecycle, dependency management, health, logging, structured errors, event infrastructure, environment configuration, test infrastructure",
        "out_of_scope": "AI reasoning, LLM integrations",
        "concepts": "- Service Container\n- Event Bus\n- Structured Logger",
        "runtime_tests": "Run application bootstrap and verify graceful shutdown.",
        "acceptance": "System can start, load config, emit events, log structured data, and shutdown gracefully."
    },
    {
        "num": 2, "name": "Omnix Executive", "status": "NOT STARTED", "goal": "Create the central Omnix Executive.",
        "dependencies": "Phase 1", "scope": "owning user goal, owning active session/task, coordinating specialists, task lifecycle, cancellation, receiving results, deciding continuation/completion, maintaining orchestration authority",
        "out_of_scope": "Specific agent implementations",
        "concepts": "- Omnix Executive\n- Task Lifecycle\n- Orchestration Loop",
        "runtime_tests": "Execute a mocked task graph through the Executive.",
        "acceptance": "Executive can receive a goal, dispatch to a dummy agent, and track task completion."
    },
    {
        "num": 3, "name": "Agent Capability Framework", "status": "NOT STARTED", "goal": "Establish agent and capability architecture.",
        "dependencies": "Phase 2", "scope": "Agent interface, metadata, lifecycle, registry, discovery, health, availability, result contracts. Capability interface, metadata, registry, discovery, router, safety metadata, execution result.",
        "out_of_scope": "Natural-language hardcoded routing.",
        "concepts": "- Agent Registry\n- Capability Registry\n- Capability Router",
        "runtime_tests": "Register, discover, and route a dummy capability safely.",
        "acceptance": "Agents and capabilities can be dynamically registered and discovered without hardcoded links."
    },
    {
        "num": 4, "name": "Input Output Voice", "status": "NOT STARTED", "goal": "Create interaction foundation.",
        "dependencies": "Phase 2", "scope": "Input Gateway, text input, voice input, speech recognition abstraction, VAD, wake system, interruption, barge-in, cancellation, TTS abstraction, Output Gateway, interaction states.",
        "out_of_scope": "Final NLP logic",
        "concepts": "- Input/Output Gateways\n- Audio streams",
        "runtime_tests": "Trigger a request via text and voice mock, verify flow into Executive.",
        "acceptance": "All input converges into Omnix Executive."
    },
    {
        "num": 5, "name": "World State Context", "status": "NOT STARTED", "goal": "Give Omnix coherent contextual/environment awareness.",
        "dependencies": "Phase 2", "scope": "World State, Session State, Conversation Context, Task State, Computer State, Perception State, Recent Action State, references (it, that), state snapshots, state updates.",
        "out_of_scope": "Actual perception data gathering (done in later phases)",
        "concepts": "- WorldState Singleton\n- Context Engine",
        "runtime_tests": "Update state concurrently and resolve a pronoun reference.",
        "acceptance": "State can be updated and queried reliably by the Executive."
    },
    {
        "num": 6, "name": "Brain Goals Planning", "status": "NOT STARTED", "goal": "Create cognitive interpretation and dynamic planning.",
        "dependencies": "Phase 3, Phase 5", "scope": "Brain Agent, model abstraction, goal interpreter, goal representation, constraint extraction, success condition, planner, task graph, plan validation, dynamic replanning.",
        "out_of_scope": "Direct capability execution inside the brain.",
        "concepts": "- Goal Representation\n- Task Graph\n- Planner",
        "runtime_tests": "Pass natural language input, verify it generates a valid Task Graph representing the goal.",
        "acceptance": "Natural-language input -> abstract goal representation (NOT command ID)."
    },
    {
        "num": 7, "name": "Application Window System", "status": "NOT STARTED", "goal": "Provide generic Windows control foundations.",
        "dependencies": "Phase 3", "scope": "Application: discover, inspect, launch, focus, terminate. Window: enumerate, inspect, focus, restore, move, resize, minimize, maximize. System: keyboard, mouse, clipboard, process/state primitives.",
        "out_of_scope": "App-specific launch scripts (e.g., open_chrome).",
        "concepts": "- Window Handles\n- Process Primitives",
        "runtime_tests": "Launch calc.exe, move its window, and close it.",
        "acceptance": "Can manage app/window lifecycle dynamically via OS APIs."
    },
    {
        "num": 8, "name": "Perception Vision Grounding", "status": "NOT STARTED", "goal": "Give Omnix layered computer perception.",
        "dependencies": "Phase 7", "scope": "screenshots/frame provider, UI Automation/accessibility, OCR, vision model abstraction, scene model, element representation, grounding, confidence, multi-monitor awareness, perception caching.",
        "out_of_scope": "Blind coordinate automation.",
        "concepts": "- Scene Model\n- Grounding targets",
        "runtime_tests": "Extract UI tree and bounding boxes from current screen.",
        "acceptance": "Generates a fused Scene Model from UIA and OCR."
    },
    {
        "num": 9, "name": "Generic Desktop Interaction", "status": "NOT STARTED", "goal": "Combine perception + grounding + generic capabilities so Omnix can interact with unfamiliar desktop applications.",
        "dependencies": "Phase 8", "scope": "generic interaction, no app scripts, inspect before action, verify after action, support unknown applications.",
        "out_of_scope": "Fixed application workflows.",
        "concepts": "- Coordinate Mapping\n- Semantic UI execution",
        "runtime_tests": "Click a specific button in an unfamiliar application based on its label.",
        "acceptance": "Can ground a semantic request to a UI action and execute it."
    },
    {
        "num": 10, "name": "Browser Intelligence", "status": "NOT STARTED", "goal": "Create a generic Browser Agent.",
        "dependencies": "Phase 9", "scope": "browser discovery, navigation, tabs, page state, DOM, accessibility, page text, forms, links, downloads, browser grounding, visual fallback.",
        "out_of_scope": "Chrome-specific hardcoded macros.",
        "concepts": "- DOM State\n- Web Navigation",
        "runtime_tests": "Navigate to a URL, extract DOM, click a link.",
        "acceptance": "Can interact with web pages generically."
    },
    {
        "num": 11, "name": "Filesystem Intelligence", "status": "NOT STARTED", "goal": "Create generic filesystem intelligence.",
        "dependencies": "Phase 3", "scope": "search, metadata, timestamps, directories, content, recent files, read, write, copy, move, rename, delete, verify filesystem result.",
        "out_of_scope": "Arbitrary unprotected shell commands.",
        "concepts": "- FS Primitives",
        "runtime_tests": "Create file, read it, and delete it.",
        "acceptance": "Can manipulate and search files safely."
    },
    {
        "num": 12, "name": "Verification Engine", "status": "NOT STARTED", "goal": "Make verification a formal subsystem.",
        "dependencies": "Phase 6, Phase 8", "scope": "Expected Outcome -> Execution -> Observation -> Verification -> PASS / FAIL / UNCERTAIN. Document verification providers.",
        "out_of_scope": "Assuming success.",
        "concepts": "- Pre/Post Conditions\n- Verification State",
        "runtime_tests": "Run an action and verify its outcome via perception.",
        "acceptance": "Action success requires explicit verification evidence."
    },
    {
        "num": 13, "name": "Recovery Replanning", "status": "NOT STARTED", "goal": "Handle real-world failures intelligently.",
        "dependencies": "Phase 12", "scope": "failure classification, diagnosis, retry policy, wait policy, re-grounding, alternative capability, specialist reassignment, replanning, ask-user fallback, bounded attempts, safe abort.",
        "out_of_scope": "Infinite loops.",
        "concepts": "- Failure classification\n- Bounded Retry",
        "runtime_tests": "Induce a failure and watch the system replan and recover.",
        "acceptance": "Failure correctly triggers bounded recovery strategies."
    },
    {
        "num": 14, "name": "Memory", "status": "NOT STARTED", "goal": "Design purposeful Omnix memory.",
        "dependencies": "Phase 5", "scope": "working memory, conversation memory, task memory, episodic memory, semantic/user memory, environmental memory, write policy, retrieval, relevance, retention, privacy, deletion, context injection.",
        "out_of_scope": "Indiscriminate raw data dumping.",
        "concepts": "- Episodic Memory\n- Vector Storage",
        "runtime_tests": "Store a user preference and retrieve it later.",
        "acceptance": "Can recall facts and past context."
    },
    {
        "num": 15, "name": "Communication Personality", "status": "NOT STARTED", "goal": "Make Omnix communicate naturally without mixing speech with execution.",
        "dependencies": "Phase 6", "scope": "Communication Agent, response planning, task progress narration, personality, expression/emotional tone, concise speech, technical-output filtering, uncertainty expression, success/failure communication.",
        "out_of_scope": "Reading raw JSON logs to the user.",
        "concepts": "- Personality Filter\n- Natural Language Generation",
        "runtime_tests": "Transform a technical exception into a polite apology.",
        "acceptance": "Output is strictly separated from internal technical state."
    },
    {
        "num": 16, "name": "Safety Permissions", "status": "NOT STARTED", "goal": "Implement policy and permission architecture.",
        "dependencies": "Phase 3", "scope": "action risk classification, confirmation, capability authorization, destructive operations, privacy-sensitive actions, external side effects, secrets, safe cancellation, audit.",
        "out_of_scope": "Bypassing safety for speed.",
        "concepts": "- Risk Levels\n- Capability Authorization",
        "runtime_tests": "Attempt a DESTRUCTIVE action and verify it is blocked pending confirmation.",
        "acceptance": "Safety bounds are enforced on all Capability Router calls."
    },
    {
        "num": 17, "name": "Multi Agent Collaboration", "status": "NOT STARTED", "goal": "Enable true dynamic collaboration between specialists.",
        "dependencies": "Phase 6", "scope": "delegation, collaboration, shared context, bounded authority, result contracts, conflict resolution, concurrency, task ownership.",
        "out_of_scope": "Uncontrolled peer-to-peer swarms.",
        "concepts": "- Inter-agent delegation",
        "runtime_tests": "Agent A requests help from Agent B via Executive.",
        "acceptance": "Specialists can collaborate while Executive maintains overall goal."
    },
    {
        "num": 18, "name": "Complex Long Running Tasks", "status": "NOT STARTED", "goal": "Support long, multi-step goals.",
        "dependencies": "Phase 17", "scope": "large task graphs, dependencies, parallel steps, checkpoints, pause, resume, cancel, partial success, progress, persistent task state, replanning, long-running verification.",
        "out_of_scope": "In-memory only execution (must survive restarts).",
        "concepts": "- Persistent Task State\n- Checkpointing",
        "runtime_tests": "Pause a multi-step task, restart process, and resume.",
        "acceptance": "Tasks can be safely persisted, paused, and resumed."
    },
    {
        "num": 19, "name": "Background Automation Events", "status": "NOT STARTED", "goal": "Add asynchronous/event-driven behavior.",
        "dependencies": "Phase 18", "scope": "scheduler, timers, event triggers, background tasks, condition monitoring, notifications, task persistence, recurring tasks.",
        "out_of_scope": "Bypassing safety/capabilities for crons.",
        "concepts": "- Scheduler\n- Event Triggers",
        "runtime_tests": "Schedule a task for +1 minute and verify execution.",
        "acceptance": "System can trigger tasks asynchronously using standard capability architecture."
    },
    {
        "num": 20, "name": "External Integrations", "status": "NOT STARTED", "goal": "Extend Omnix beyond local desktop operation.",
        "dependencies": "Phase 3", "scope": "email, calendar, messaging, cloud storage, GitHub, APIs, smart-home/device systems, external tools/services.",
        "out_of_scope": "Hardcoding providers into Omnix Core.",
        "concepts": "- Integration Plugins",
        "runtime_tests": "Call a mocked external API safely.",
        "acceptance": "External integrations adhere to the standard safety and capability interfaces."
    }
]

out_dir = "e:/Best/Omnix/docs/phases"
for p in phases:
    file_name = f"PHASE_{p['num']:02d}_{p['name'].replace(' ', '_').upper()}.md"
    file_path = os.path.join(out_dir, file_name)
    next_num = p['num'] + 1
    content = PHASE_STANDARD_TEMPLATE.format(
        num=p['num'],
        name=p['name'],
        status=p['status'],
        goal=p['goal'],
        dependencies=p['dependencies'],
        scope=p['scope'],
        out_of_scope=p['out_of_scope'],
        concepts=p['concepts'],
        runtime_tests=p['runtime_tests'],
        acceptance=p['acceptance'],
        next_num=next_num
    )
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

print(f"Generated {len(phases)} phase documents.")
