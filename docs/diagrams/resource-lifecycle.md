# 🔄 Learning resource lifecycle

```mermaid
flowchart TD
    A["Identify learning objective"] --> B["Choose topic directory"]
    B --> C["Create or update resource"]
    C --> D["Add prerequisites and usage"]
    D --> E["Review safety and licensing"]
    E --> F["Run relevant validation"]
    F --> G{"Checks acceptable?"}
    G -->|"No"| H["Fix errors and clarify instructions"]
    H --> F
    G -->|"Yes"| I["Update topic index"]
    I --> J["Submit focused contribution"]
    J --> K["Review and maintain"]
```

## Resource lifecycle checklist
- Objective is explicit.
- Prerequisites are documented.
- Inputs and outputs are safe and understandable.
- License/provenance reviewed.
- Validation command is recorded.
- Learning path and index updated.
