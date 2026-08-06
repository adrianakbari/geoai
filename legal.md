# How to avoid "work for hire" trap
one of my concerns is that because they are paying me to implement the prototype for them, they come up and say "We pay you for the development of the software so its ours". in other words i dont want them to    limit my growth and market only to themselves by any means. in an imaginary scenario that this happens, what is an smart way to get out of it and keep my options open to sell the products to other businesses as well?

## How to Protect Yourself
1. Establish Prior Art Right Now

  Before you sign anything with Geosquare, create a dated record that GeoAI existed first. You already have this in:

  - Git commit history (dates are immutable evidence)
  - This CLAUDE.md file and your project files (file system timestamps)
  - Your conversation with Peter Paul on 24.06.2026 (they asked to integrate something that already existed — that's on record)
  - The geoai.md, todo.md, etc. — all pre-date the deal

  Action: Send yourself a timestamped email with a summary of what GeoAI is and what it can do. Or better, have a notary or lawyer make a dated declaration. This is cheap (€100–200) and establishes unambiguous prior
  ownership.

  ---
  2. Structure the Deal as Two Separate Agreements

  Never sign a single "we'll build this for you" contract. Split it into two:

  Agreement A — Technology License

  ▎ Geosquare licenses access to the GeoAI platform for €X/month.
  ▎ Geosquare receives usage rights, not ownership. The platform remains Adrian's IP.

  Agreement B — Implementation Services

  ▎ You provide integration services (API connection to their frontend, training, setup) for a fixed fee.
  ▎ This work is limited to the integration layer — the connector between GeoAI and Geosquare's frontend.

  The key principle: Geosquare can own the chat widget you build specifically for them. They cannot own the engine underneath it.

  This is exactly how every major software company works. Geosquare doesn't own Salesforce's CRM when they pay for a Salesforce implementation partner to configure it.

  ---
  3. Define "Core Platform" Explicitly in the Contract

  The contract must name exactly what is yours and what they get rights to:

  ┌────────────────────────────────────────────┬────────────────────────────┬─────────────────────┐
  │                 Component                  │         Ownership          │ What Geosquare Gets │
  ├────────────────────────────────────────────┼────────────────────────────┼─────────────────────┤
  │ NL query → GIS pipeline                    │ Your IP                    │ Usage license       │
  ├────────────────────────────────────────────┼────────────────────────────┼─────────────────────┤
  │ Data catalog + pgvector search             │ Your IP                    │ Usage license       │
  ├────────────────────────────────────────────┼────────────────────────────┼─────────────────────┤
  │ Query planner + execution engine           │ Your IP                    │ Usage license       │
  ├────────────────────────────────────────────┼────────────────────────────┼─────────────────────┤
  │ Geosquare chat widget / frontend connector │ Negotiable (can be theirs) │ Full ownership      │
  ├────────────────────────────────────────────┼────────────────────────────┼─────────────────────┤
  │ Geosquare-specific API adaptor             │ Negotiable                 │ Full ownership      │
  └────────────────────────────────────────────┴────────────────────────────┴─────────────────────┘

  Let them own the integration skin. Never let them near the engine.

  ---
  4. Never Accept Market Exclusivity

  Geosquare may try to negotiate: "You can't sell to our competitors" or "We get exclusive rights in the Dutch municipality market."

  This would effectively make you their internal software department, not an independent company.

  What you can offer instead:
  - Client-list non-compete: "We won't directly approach Geosquare's named active clients for 12 months." (Specific, limited, fair)
  - Right of first refusal: "When a new prospect comes through Geosquare, they get first shot at a joint proposal." (Rewards the relationship without locking you in)
  - Head-start exclusivity: "Geosquare gets 6 months before we approach other GIS software vendors with an identical offer." (Time-limited, not permanent)

  Never agree to:
  - Exclusivity in any geography or sector without a time limit
  - Any clause that prevents you from selling to other contractors or vendors
  - Ownership of IP that predates the contract

  ---
  5. Frame It as a Benefit to Them

  If Geosquare pushes back, use this argument:

  ▎ "Because we retain ownership of the platform, you get a continuously improving product. We're incentivized to keep developing it — every improvement we make for other clients, you benefit from too. If you owned it, you'd
  ▎ have to maintain it yourself, hire your own AI team, and it would stop evolving the moment you stopped funding it. The SaaS model protects you."

  That's not a defensive argument — it's a genuine value proposition.

  ---
  The Minimum Acceptable Deal Structure

  ┌───────────────────┬───────────────────────────────────────────────────┬─────────────────────────────────────────────────────────┐
  │       Term        │                    Acceptable                     │                      Never Accept                       │
  ├───────────────────┼───────────────────────────────────────────────────┼─────────────────────────────────────────────────────────┤
  │ IP ownership      │ You own core platform, they own integration layer │ They own anything that predates the contract            │
  ├───────────────────┼───────────────────────────────────────────────────┼─────────────────────────────────────────────────────────┤
  │ Exclusivity       │ Named client list, 12 months max                  │ Dutch market, sector, or geography exclusivity          │
  ├───────────────────┼───────────────────────────────────────────────────┼─────────────────────────────────────────────────────────┤
  │ License type      │ Usage license, renewable annually                 │ Perpetual, irrevocable license with transfer rights     │
  ├───────────────────┼───────────────────────────────────────────────────┼─────────────────────────────────────────────────────────┤
  │ Source code       │ No source code delivery                           │ Handing over source code without escrow agreement       │
  ├───────────────────┼───────────────────────────────────────────────────┼─────────────────────────────────────────────────────────┤
  │ Sublicense rights │ They cannot sublicense to third parties           │ Full sublicense rights (they could resell your product) │
  └───────────────────┴───────────────────────────────────────────────────┴─────────────────────────────────────────────────────────┘