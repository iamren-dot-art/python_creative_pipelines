# Python for Creative Pipelines Syllabus v1.1

**Student:** Arian  
**Background:** 20+ years motion design (C4D, After Effects), Python Weeks 1-3 complete (shortKing curriculum)  
**Goal:** Python proficiency for Cinema 4D automation, TouchDesigner, and installation hardware communication  
**Schedule:** Flexible pace, ~1-2 hours/session  
**Duration:** 10 weeks  
**Started:** February 2026

---

## Version History

| Version | Date | Summary |
|---------|------|---------|
| v1.1 | Feb 15, 2026 | Swapped pillar order — C4D first (fluent), TD second (learning) |
| v1.0 | Feb 15, 2026 | Initial syllabus, branched from shortKing Week 3 completion |

---

## Three Pillars

This curriculum has three interwoven threads. Each week emphasizes one but reinforces the others.

### Pillar 1: Python for Cinema 4D

Scene automation, batch operations, pipeline tools, procedural object creation. You already think in C4D — now you script it.

### Pillar 2: Python for TouchDesigner

Scripting, callbacks, dynamic network creation, data-driven visuals, real-time logic. New environment, familiar Python.

### Pillar 3: Python for Device Communication

OSC, serial, WebSocket, MQTT — talking to Arduino, sensors, lighting rigs, and custom hardware for installations.

### How They Connect

| Python Week | Primary Pillar | What You Build |
|-------------|---------------|----------------|
| Week 1 | Foundation | Lists, dicts, comprehensions in creative contexts |
| Week 2 | Foundation | Functions, decorators, callbacks |
| Week 3 | Cinema 4D | C4D Python console, scene traversal, object creation |
| Week 4 | Cinema 4D | Batch operations, asset pipeline tools |
| Week 5 | TouchDesigner | TD Python basics — `op()`, `me`, `.par`, DAT scripting |
| Week 6 | Devices | Serial communication, Arduino/sensor data parsing |
| Week 7 | TouchDesigner | Dynamic networks, CHOP/TOP scripting, callbacks |
| Week 8 | Devices | OSC protocol, UDP networking, TD ↔ hardware |
| Week 9 | All Three | Data processing — CSV, APIs, real-time data feeds |
| Week 10 | Integration | Capstone: Interactive installation prototype |

---

## Learning Philosophy

- **Project-integrated:** Every concept ties to C4D, TD, or installations
- **Hands-on first:** Do, then understand why
- **Break things:** Learn error patterns by causing them
- **Predict before running:** Build mental model of execution
- **Creative context:** Exercises use real creative scenarios, not abstract puzzles

---

## What You Already Know (Weeks 1-3 of shortKing Curriculum)

These are assumed. They'll be reinforced through creative context, not re-taught in isolation.

| Concept | Status | Reinforced In |
|---------|--------|---------------|
| Variables & types | ✓ Solid | Every week |
| F-strings | ✓ Solid | Every week |
| Lists & dictionaries | ✓ Solid | Week 1 deepens |
| Conditionals | ✓ Solid | Every week |
| Functions (basic) | ✓ Needs practice | Week 2 deepens |
| File I/O & JSON | ✓ Complete | Week 3 (C4D configs), Week 9 (data feeds) |
| Classes & objects | ✓ Complete | Week 3 (C4D tools), Week 6 (device classes) |
| `__init__`, `self`, methods | ✓ Complete | Ongoing |
| `__str__`, `__repr__` | ✓ Complete | Ongoing |
| Class composition | ✓ Complete | Week 7 (TD networks) |
| try/except/finally | ✓ Complete | Week 6 (serial errors), Week 8 (network errors) |
| Custom exceptions | ✓ Complete | Week 6 (device exceptions) |
| Logging module | ✓ Complete | Week 6 (device logging), Week 10 (installation logging) |

### Known Weak Spots to Watch

| Pattern | How We'll Address It |
|---------|---------------------|
| Forgetting `return` statements | Flagged in every exercise review |
| Forgetting `self.` prefix | C4D and TD classes will hammer this |
| `=` vs `==` confusion | Quiz questions targeting this |
| Tracking execution flow | Code tracing exercises each week |
| Multi-class architecture | Weeks 4, 7, 10 build progressively |

---

## Progress Tracking

- [ ] Week 1: Collections & Comprehensions
- [ ] Week 2: Functions, Decorators & Callbacks
- [ ] Week 3: Cinema 4D Python Fundamentals
- [ ] Week 4: Cinema 4D Pipeline Automation
- [ ] Week 5: TouchDesigner Python Fundamentals
- [ ] Week 6: Serial Communication & Hardware
- [ ] Week 7: TouchDesigner Advanced Scripting
- [ ] Week 8: OSC & Network Protocols
- [ ] Week 9: Data Processing & Real-Time Feeds
- [ ] Week 10: Integration — Interactive Installation Prototype

---

## Week 1: Collections & Comprehensions

**Goal:** Master Python's data manipulation tools — the backbone of creative scripting  
**Primary Pillar:** Foundation  
**Creative Application:** Processing parameter lists, building color palettes, transforming coordinate data

### Why This Matters

C4D and TD scripting constantly manipulate lists of objects, parameter values, and data streams. Comprehensions are how Pythonic code processes these efficiently — you'll use them daily.

### Concepts

| Concept | Why It Matters |
|---------|----------------|
| List slicing | Extracting subsets of keyframes, samples, objects |
| List comprehensions | Transform data in one line (e.g., normalize 100 values) |
| Dict comprehensions | Build lookup tables from scene data |
| Nested structures | JSON configs, scene hierarchies, multi-channel data |
| `enumerate()` and `zip()` | Pairing indices with values, merging parallel data |
| Tuple unpacking | Clean extraction from structured data |

### Daily Breakdown

**Day 1:** List slicing, `enumerate()`, `zip()` — with audio sample and keyframe data  
**Day 2:** List comprehensions — filtering and transforming creative data  
**Day 3:** Dict comprehensions — building scene lookups and parameter maps  
**Day 4:** Nested data structures — multi-layer configs, scene hierarchies  
**Day 5:** Mini-project: Color palette generator and transformer

### C4D Analogy

- List comprehension = Processing every clone's parameter in one expression
- Dict comprehension = Building a User Data tag lookup from scene objects
- `zip()` = Linking keyframe times to keyframe values
- Slicing = Trimming a timeline to a specific frame range

### Week 1 Checkpoint

Ready for Week 2 when you can:
- [ ] Slice lists with `[start:stop:step]` syntax
- [ ] Write list and dict comprehensions with conditions
- [ ] Navigate nested dicts/lists confidently
- [ ] Use `enumerate()` and `zip()` without looking up syntax

---

## Week 2: Functions, Decorators & Callbacks

**Goal:** Write flexible, reusable functions — the building blocks of scripting in C4D and TD  
**Primary Pillar:** Foundation  
**Creative Application:** C4D command plugins, TD callbacks, reusable pipeline utilities

### Why This Matters

Cinema 4D plugins use decorated functions and command patterns. TouchDesigner is callback-driven. Understanding higher-order functions, `*args`/`**kwargs`, and lambda expressions makes you dangerous in both environments.

### Concepts

| Concept | Why It Matters |
|---------|----------------|
| `*args` and `**kwargs` | Flexible parameter passing (callbacks vary in signature) |
| Lambda functions | Inline transforms for sorting, filtering, mapping |
| Functions as arguments | Passing behavior (callbacks, event handlers) |
| Closures | Functions that remember their context |
| Decorators (basics) | C4D commands, Flask routes, TD extensions |
| Type hints | Self-documenting code, IDE autocompletion |

### Daily Breakdown

**Day 1:** `*args`, `**kwargs`, default values — flexible function signatures  
**Day 2:** Lambda functions and sorting/filtering with `key=`  
**Day 3:** Functions as arguments, callbacks pattern  
**Day 4:** Closures and decorators  
**Day 5:** Mini-project: Event system with callbacks

### C4D Analogy

- Callback = Python tag that executes on specific events (frame change, render)
- Decorator = C4D's `@register` for plugin commands
- Lambda = Quick inline expression like a Formula Effector expression
- Closure = A function that "remembers" the scene state it was created in

### Week 2 Checkpoint

Ready for Week 3 when you can:
- [ ] Write functions with `*args` and `**kwargs`
- [ ] Use lambda for sorting and filtering
- [ ] Pass functions as arguments (callback pattern)
- [ ] Write and apply a basic decorator
- [ ] Add type hints to function signatures

---

## Week 3: Cinema 4D Python Fundamentals

**Goal:** Automate Cinema 4D with Python scripting  
**Primary Pillar:** Cinema 4D  
**Creative Application:** Scene manipulation, batch operations, procedural object creation

### Why This Matters

C4D's Python API (c4d module) lets you automate repetitive tasks, build pipeline tools, and create procedural setups that would take hours manually. Your 20 years of C4D knowledge means you already understand *what* to build — now you learn *how* to script it.

### Concepts

| Concept | Why It Matters |
|---------|----------------|
| Script Manager vs plugins | Where Python runs in C4D |
| `c4d.documents` | Accessing the active document and scene |
| Object traversal | Walking the Object Manager hierarchy |
| Creating objects | Programmatic scene building |
| Tags and materials | Assigning properties via script |
| `c4d.EventAdd()` | Refreshing the viewport after changes |

### Daily Breakdown

**Day 1:** C4D Script Manager, `doc`, `op` (active object), basic scene access  
**Day 2:** Object hierarchy traversal — `GetDown()`, `GetNext()`, `GetChildren()`  
**Day 3:** Creating objects, setting position/rotation/scale  
**Day 4:** Tags, materials, and user data  
**Day 5:** Mini-project: Scene builder — script that generates a structured scene from a JSON config

### TD Analogy (Preview)

- `doc.GetActiveObject()` = `me.parent()` in TD
- `obj.GetDown()` = navigating into a COMP's children
- `c4d.EventAdd()` = `op('container1').cook(force=True)`
- Object hierarchy = TD's operator tree

### Week 3 Checkpoint

Ready for Week 4 when you can:
- [ ] Access objects in the active C4D document
- [ ] Traverse the object hierarchy
- [ ] Create objects and set transforms via script
- [ ] Apply materials and tags programmatically
- [ ] Explain when to call `c4d.EventAdd()`

---

## Week 4: Cinema 4D Pipeline Automation

**Goal:** Build production tools for C4D workflows  
**Primary Pillar:** Cinema 4D  
**Creative Application:** Batch rendering, asset management, scene standardization

### Why This Matters

This is where your 20 years of C4D experience becomes a superpower. You know every tedious, repetitive task in a motion design pipeline. Now you automate them. Scene prep, render settings, output management, asset organization — all scriptable.

### Concepts

| Concept | Why It Matters |
|---------|----------------|
| Render settings via script | Batch render configuration |
| File I/O for pipeline | Asset paths, output naming conventions |
| Scene validation | Pre-flight checks before rendering |
| Batch operations | Processing multiple scenes/objects |
| Command-line C4D | Headless rendering, script execution |
| Plugin structure basics | CommandData, MessageData patterns |

### Daily Breakdown

**Day 1:** Render settings access — resolution, frame range, output path  
**Day 2:** Scene validation — check for missing textures, broken references  
**Day 3:** Batch operations — process all objects matching criteria  
**Day 4:** Pipeline utility functions — path management, naming conventions  
**Day 5:** Mini-project: Pre-render validator — script that checks scene health and generates a report

### TD Analogy (Preview)

- Render settings = TD's Movie File Out TOP parameters
- Scene validation = Checking all operators are cooking without errors
- Batch operations = Iterating over all COMPs in a container
- Pipeline tools = TD's build/export scripts

### Week 4 Checkpoint

Ready for Week 5 when you can:
- [ ] Access and modify render settings from Python
- [ ] Walk a scene and find objects matching criteria
- [ ] Build a validation script with pass/fail reporting
- [ ] Organize pipeline utility functions into a reusable module

---

## Week 5: TouchDesigner Python Fundamentals

**Goal:** Write Python scripts inside TouchDesigner  
**Primary Pillar:** TouchDesigner  
**Creative Application:** Operator control, parameter automation, DAT scripting

### Why This Matters

This is where your Python skills meet TD's node-based paradigm. By now you've scripted C4D's hierarchy — TD's operator tree will feel familiar. You'll learn to reference operators, read/write parameters, and execute Python in response to events.

### Concepts

| Concept | Why It Matters |
|---------|----------------|
| `op()` and `me` | Referencing operators by name and self-reference |
| `.par` accessor | Reading and writing operator parameters |
| DAT execute scripts | Running Python on events (valueChange, onCook, etc.) |
| `parent()` and `mod()` | Navigation and module imports in TD |
| CHOP data access | Reading channel values from Python |
| TOP pixel access | Reading color data from textures |

### Daily Breakdown

**Day 1:** TD Python environment — Text DAT, `op()`, `me`, `.par`  
**Day 2:** DAT callbacks — `onValueChange`, `onCook`, timer callbacks  
**Day 3:** CHOP access — reading audio/LFO/noise data from Python  
**Day 4:** TOP access — reading pixel data, color sampling  
**Day 5:** Mini-project: Parameter controller — Python script that reads audio CHOP and drives visual parameters

### C4D Analogy

- `op('geo1')` = Finding an object by name in the Object Manager
- `.par.tx` = Accessing Position.X in the Attribute Manager
- DAT callback = Python tag triggering on frame change
- `me` = "Self" in a Python tag script
- CHOP data = Sound Effector's frequency data

### Week 5 Checkpoint

Ready for Week 6 when you can:
- [ ] Reference any operator with `op()` and navigate with `parent()`
- [ ] Read and write parameters via `.par`
- [ ] Write a DAT execute script that responds to value changes
- [ ] Access CHOP channel data from Python

---

## Week 6: Serial Communication & Hardware

**Goal:** Connect Python to physical devices  
**Primary Pillar:** Devices  
**Creative Application:** Reading sensors, controlling Arduino, hardware-driven installations

### Why This Matters

This is your differentiator. Most TD artists can't wire up an Arduino and parse its serial data. You'll learn to read sensors, send commands to microcontrollers, and build the bridge between physical and digital that installations demand.

### Concepts

| Concept | Why It Matters |
|---------|----------------|
| `pyserial` library | Reading/writing serial ports |
| Baud rates and config | Matching device settings |
| Data parsing | Converting raw bytes to usable values |
| Buffering and framing | Handling incomplete messages |
| Threading for serial | Non-blocking reads (keeping UI responsive) |
| Device manager class | Encapsulating hardware communication |

### Daily Breakdown

**Day 1:** `pyserial` basics — open port, read/write, baud rates  
**Day 2:** Parsing structured serial data (CSV, delimited, binary)  
**Day 3:** Threading for non-blocking serial reads  
**Day 4:** Error handling — disconnects, timeouts, corrupt data  
**Day 5:** Mini-project: Sensor reader class — reads Arduino data, logs values, handles errors

### C4D/TD Analogy

- Serial port = A very fast data cable carrying structured frames
- Baud rate = Frame rate for data (how fast bits arrive)
- Parsing = Reading a multi-pass EXR — you pick the channels you need
- Threading = Background render — serial reads while your main app continues

### Week 6 Checkpoint

Ready for Week 7 when you can:
- [ ] Open and configure a serial port with pyserial
- [ ] Parse incoming sensor data into Python values
- [ ] Run serial reads in a background thread
- [ ] Handle disconnection and reconnection gracefully
- [ ] Build a reusable device communication class

---

## Week 7: TouchDesigner Advanced Scripting

**Goal:** Build dynamic, scriptable TD networks  
**Primary Pillar:** TouchDesigner  
**Creative Application:** Generative networks, reusable components, installation control systems

### Why This Matters

Beyond reading parameters, Python in TD can create and destroy operators, build entire networks procedurally, and manage complex state machines. This is how production installations work — not manually placing nodes, but scripting systems that configure themselves.

### Concepts

| Concept | Why It Matters |
|---------|----------------|
| Creating operators from Python | `parent().create()` |
| Wiring connections | `.inputConnectors`, `.outputConnectors` |
| Extensions (COMP classes) | Custom Python classes attached to COMPs |
| Storage and fetch | Persistent data across cooks |
| Table DAT manipulation | Reading/writing structured data |
| Timer CHOP + Python | Scheduled/repeating tasks |

### Daily Breakdown

**Day 1:** Creating and connecting operators from Python  
**Day 2:** Extensions — custom classes on COMPs  
**Day 3:** Storage, fetch, and persistent state  
**Day 4:** Table DAT as a data structure — CRUD operations  
**Day 5:** Mini-project: Self-building visualizer — Python script that generates a complete audio-reactive network

### C4D Analogy

- `parent().create(topTOP)` = Creating objects via Script Manager
- Extensions = C4D Python tag scripts with persistent state
- Storage = User Data stored on objects
- Wiring connections = XPresso node connections
- Table DAT = A spreadsheet User Data tag

### Week 7 Checkpoint

Ready for Week 8 when you can:
- [ ] Create and connect operators from Python
- [ ] Write a COMP extension with custom methods
- [ ] Use storage for persistent state
- [ ] Manipulate Table DATs from Python
- [ ] Build a network procedurally from a config

---

## Week 8: OSC & Network Protocols

**Goal:** Send and receive data over networks  
**Primary Pillar:** Devices  
**Creative Application:** TD ↔ hardware communication, multi-machine installations, remote control

### Why This Matters

OSC (Open Sound Control) is the lingua franca of creative technology. It's how TD talks to Ableton, lighting desks, Arduino, other computers, and custom hardware. Combined with your serial skills from Week 6, you'll be able to connect anything to anything.

### Concepts

| Concept | Why It Matters |
|---------|----------------|
| OSC protocol basics | Messages, addresses, arguments |
| `python-osc` library | Sending and receiving OSC |
| UDP vs TCP | When to use each |
| OSC in TouchDesigner | OSC In/Out CHOPs, DAT callbacks |
| WebSocket basics | Bidirectional real-time communication |
| MQTT basics | Lightweight IoT messaging for installations |

### Daily Breakdown

**Day 1:** OSC fundamentals — addresses, types, bundles  
**Day 2:** `python-osc` — sending and receiving in pure Python  
**Day 3:** OSC in TD — OSC In CHOP, mapping to parameters  
**Day 4:** WebSocket basics — `websockets` library, real-time data  
**Day 5:** Mini-project: Multi-device controller — Python hub that receives OSC from multiple sources and routes to TD

### C4D/TD Analogy

- OSC address = A path like `/audio/volume` (similar to TD operator paths)
- OSC message = Sending a keyframe value to a remote parameter
- UDP = Sending a postcard (fast, no confirmation)
- TCP = Sending a registered letter (slower, guaranteed delivery)
- MQTT = A bulletin board everyone subscribes to

### Week 8 Checkpoint

Ready for Week 9 when you can:
- [ ] Send and receive OSC messages with python-osc
- [ ] Map OSC input to TD parameters
- [ ] Explain UDP vs TCP tradeoffs
- [ ] Set up basic WebSocket communication
- [ ] Route messages between multiple devices

---

## Week 9: Data Processing & Real-Time Feeds

**Goal:** Process external data for creative visualization  
**Primary Pillar:** All Three  
**Creative Application:** Data-driven art, API-fed installations, CSV/JSON data visualization

### Why This Matters

Installations increasingly pull from live data — weather APIs, social media feeds, IoT sensors, databases. This week connects your Python, C4D, and TD skills to the outside world. You'll fetch, parse, clean, and transform data for real-time creative use.

### Concepts

| Concept | Why It Matters |
|---------|----------------|
| `requests` library | Fetching data from web APIs |
| JSON API parsing | Extracting useful data from responses |
| CSV processing | `csv` module, pandas basics |
| Data normalization | Scaling raw values to usable ranges (0-1, etc.) |
| Scheduling/polling | Periodically fetching updated data |
| Error resilience | APIs fail — your installation shouldn't |

### Daily Breakdown

**Day 1:** `requests` library — GET/POST, headers, API keys  
**Day 2:** Parsing JSON APIs — extracting and transforming data  
**Day 3:** CSV processing — reading, filtering, transforming  
**Day 4:** Data normalization and mapping — `lerp`, `clamp`, `remap` functions  
**Day 5:** Mini-project: Weather-driven visualizer data pipeline — fetch weather API, normalize data, output as JSON for TD consumption

### C4D/TD Analogy

- API call = Importing a file into your project, but live
- JSON parsing = Reading a scene file's metadata
- Normalization = Remapping a gradient from arbitrary range to 0-1
- Polling = A Timer CHOP that triggers a fetch every N seconds

### Week 9 Checkpoint

Ready for Week 10 when you can:
- [ ] Fetch data from a REST API
- [ ] Parse and extract specific fields from JSON responses
- [ ] Process CSV data with filtering and transformation
- [ ] Normalize values to arbitrary ranges
- [ ] Handle API failures gracefully without crashing

---

## Week 10: Integration — Interactive Installation Prototype

**Goal:** Combine all three pillars into a working prototype  
**Primary Pillar:** All Three  
**Creative Application:** Portfolio-ready interactive installation proof of concept

### What You're Building

A complete data pipeline that demonstrates:
- External data source (API or sensor) feeding Python
- Data processing and normalization
- OSC/serial output to TouchDesigner
- TD visualization responding to live data
- C4D scene generated from the same data source
- Error handling and logging throughout
- Configuration via JSON

### Week 10: Build & Polish

**Day 1:** Architecture planning, module organization  
**Day 2:** Data pipeline — fetch, process, normalize  
**Day 3:** TD integration — OSC output, parameter mapping  
**Day 4:** C4D integration — scene generation from data  
**Day 5:** Polish — error hardening, logging, documentation

### Project Structure

```
creative-pipeline-prototype/
├── config.json
├── src/
│   ├── data_fetcher.py
│   ├── data_processor.py
│   ├── osc_sender.py
│   ├── serial_handler.py
│   └── c4d_scene_builder.py
├── td_project/
│   └── prototype.toe
├── logs/
└── README.md
```

### Integration Checkpoint

Portfolio-ready when you can:
- [ ] Run the complete pipeline on your workstation
- [ ] Show live data flowing from source → Python → TD
- [ ] Generate a C4D scene from the same data
- [ ] Recover gracefully from network/device failures
- [ ] Explain the architecture to a hiring manager
- [ ] Document the project in a README

---

## After Week 10

With this foundation complete, you're equipped to:

- **Automate C4D pipelines** for production efficiency
- **Build TD installations** with hardware integration and live data
- **Connect physical and digital** through serial, OSC, and network protocols
- **Pursue creative technologist roles** with a portfolio piece demonstrating all three pillars

### Suggested Next Steps

- Build 2-3 more portfolio pieces of increasing complexity
- Contribute to open-source TD components
- Explore GLSL shaders in TD (you asked about Lambert — revisit this)
- Dive deeper into MQTT for IoT installations
- Learn `asyncio` for advanced concurrent data handling

---

## Lesson Structure (Every Day)

1. **Refresher quiz** (3-5 questions from previous day, no notes)
2. **New concepts** introduced with examples
3. **Exercises** (you post code + output, confirm each before next)
4. **End-of-day quiz** (4-5 questions)
5. **PROGRESS.md entry** (provided in markdown table format)
6. **Git commit** command provided

---

## Resources

- Python docs: docs.python.org/3/
- Cinema 4D Python SDK: developers.maxon.net
- TouchDesigner Wiki: derivative.ca/UserGuide
- Matthew Ragan AME 394: matthewragan.com
- Interactive & Immersive HQ: interactiveimmersive.io
- python-osc: pypi.org/project/python-osc/
- pyserial: pypi.org/project/pyserial/

---

## Notes Section

### Pre-Curriculum Notes
- Completed Weeks 1-3 of shortKing Python curriculum
- Known patterns: forget `return`, forget `self.`, `=`/`==` confusion
- ~60% quiz average, improving
- Strong C4D/AE technical intuition transfers to creative coding
- C4D fluency = Pillar 1 (script what you know), TD = Pillar 2 (new environment)

---

**END OF SYLLABUS v1.1**
