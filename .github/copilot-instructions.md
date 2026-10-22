# Platform guide repository

Read `AGENTS.md` explicitly, then use `catalog.json` to match the question, service scope and guide kind. Overviews route to tasks; they are not executable workflows.
Default to reference or authorized read-only mode. Do not modify Azure or customer data while maintaining documentation.
Keep instructions standalone, policy-linked, scope-aware, and explicit about unknowns. Update reader metadata in the catalog, regenerate marked cards/navigation with `python scripts/validate_docs.py --sync-navigation`, and validate local changes with the repository's Python checks. Never treat navigation synchronization as policy review or tenant validation.
