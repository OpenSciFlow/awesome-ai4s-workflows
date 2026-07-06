# Model Hubs and Model Zoos

This category tracks ecosystems that distribute models or define model metadata.

OpenSciFlow can learn from these projects, but its scope is different: executable scientific workflows, local/HPC readiness, validation tests, citations, and run records.

| Project | Type | Relation to OpenSciFlow | Contact priority |
|---|---|---|---|
| Hugging Face Hub | Model and dataset hub | Model hub analogy and possible metadata integration | Low |
| BioImage Model Zoo | Scientific model zoo | Top manifest-design reference and feedback target | High |
| Google DeepMind AlphaFold | Structure prediction platform | Tool endpoint/reference for structure workflows | Low |
| ESM / ESMFold | Protein language model | Future model plugin target | Low |
| DiffDock | AI docking model | Example AI model plugin and feedback target | High |
| MatGL | Materials graph learning library | Future AI materials plugin example | Low |

For individual scientific models, see also:

- [Scientific models](scientific-models.md)

## Open questions

- What model metadata is missing from current science workflow execution records?
- How should plugin manifests record model weights, checksums, and licenses?
- How should generated reports cite models automatically?
