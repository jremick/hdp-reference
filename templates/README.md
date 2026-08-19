# Templates

`hdp-starter.yaml` is a complete provider-neutral Draft 0.1 starting point. Copy
it, replace the example intent and operating facts, and preserve unknowns rather
than filling fields with guesses.

`implementation-binding.example.yaml` illustrates how an implementation can map
abstract HDP capabilities to concrete systems without making that binding part
of the core standard. The binding format is informative in Draft 0.1 and is not
covered by the HDP JSON Schema.

The `create-hdp` Agent Skill carries its own copy of the starter so the skill
remains portable when installed independently.
