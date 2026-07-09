Autonomous Retail Customer Service Agent
========================================

Category: Agentic AI

Data Files: customers.csv, entity_activity_audit_log.csv, operations_policies.json, orders.csv, returns.csv, support_tickets.csv


PROBLEM STATEMENT
-----------------

Retail customer service spans order tracking, returns, refunds, and policy interpretation—workflows that require querying multiple systems and applying business rules consistently. Manual handling introduces delays, inconsistent resolutions, and high cost per contact.
An autonomous agent orchestrates tools: lookup order status, validate return eligibility against policy, initiate refunds, and log actions in an audit trail. Agentic architectures plan multi-step resolutions rather than single-turn chat responses.
This project supplies orders, returns, support tickets, customer profiles, operations policies, and entity activity logs. Students design an agent that completes end-to-end service tasks with policy grounding from operations_policies.json and traceability via entity_activity_audit_log.csv.


OBJECTIVES
----------

1. Design a LangGraph state machine mapping service workflows (order inquiry, return initiation, escalation) to agent nodes with shared state over orders.csv, returns.csv, and customers.csv.
2. Implement LangGraph tool nodes for order lookup, return validation, and policy retrieval from operations_policies.json with multi-step workflow orchestration and rule checks before automated resolutions.
3. Orchestrate end-to-end agent pipelines from support_tickets.csv trigger through policy grounding, tool execution, and resolution logging to entity_activity_audit_log.csv format.
4. Configure human-in-the-loop escalation nodes for denied returns, high-value orders, and ambiguous policy matches with conditional edges in the state graph.
5. Measure autonomous resolution rate, policy violation rate, and average steps-to-resolution on a test scenario set with full agent trace observability.
6. Deploy the Agentic AI service agent with documented LangGraph state graph, tool schemas, and tracing configuration for compliance review.


NOTES
-----

Technology Reference
~~~~~~~~~~~~~~~~~~
  - LangGraph state machine with multi-step agent nodes, policy-retrieval tools, conditional escalation edges, and human-in-the-loop checkpoints; end-to-end workflow from support trigger through policy validation, autonomous action, and audit logging with observability/tracing.

Dataset Descriptions
~~~~~~~~~~~~~~~~~~~~
  - customers.csv: Customer master records with demographics, signup dates, contact attributes, and account metadata.
  - entity_activity_audit_log.csv: Audit trail of system and agent actions on entities with timestamps and actor identifiers.
  - operations_policies.json: Structured policy documents (returns, retention, escalation) with policy_id, department, and content text.
  - orders.csv: Order header transactions linking customers to purchase dates, amounts, and fulfillment status.
  - returns.csv: Return requests with reason codes, approval status, resolution type, and request dates.
  - support_tickets.csv: Customer support cases with category, status, subject, and created timestamps.

How Datasets Relate and Join
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Join customers.csv to orders.csv on customer_id for purchase history features.
- Join returns.csv to orders.csv on order_id for return eligibility context.
- Use operations_policies.json as authoritative grounding source; do not rely on model parametric knowledge for policy answers.

Suggested ML / Analytics Approach
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Design a tool-using agent with explicit planning: parse user intent, select tools (SQL/CSV queries, policy retrieval, record updates), execute steps, and verify outputs against schema. Ground all policy and medical content in JSON/CSV sources. Log traces for audit.

Evaluation Metrics
~~~~~~~~~~~~~~~~~~
Task completion rate, grounded answer rate, citation accuracy, escalation rate, and SLA compliance.

Student Deliverables
~~~~~~~~~~~~~~~~~~~~
- Data exploration notebook or report documenting schema, missing values, and join diagrams for all project files.
- Implemented pipeline (Python preferred) reproducible from raw CSV/JSON/JSONL/DB files in this folder.
- Model, agent, or analytics outputs with held-out evaluation using the metrics above.
- Written summary (2-3 pages) interpreting results, limitations, and recommended production next steps.
- Artifact export appropriate to project type: scored CSV, recommendation lists, agent trace logs, dashboard screenshots, or generated report samples.

Technical Notes
~~~~~~~~~~~~~~~
- All data is synthetic and intended for education, portfolio demonstrations, and prototyping.
- Do not assume external APIs or live systems; simulate tool calls against local files.
- When using GenAI components, document prompts, retrieval configuration, and safety guardrails explicitly.
- Preserve reproducibility: set random seeds, document train/validation splits, and version any embedding models used.
