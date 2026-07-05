# Weekly AI Coding Agents Digest

**Date:** 2026-07-05

---

## Executive Summary

Minor changes were detected but none scored high enough (score ≥ 3) to warrant summarization. Details below.

## Sources Checked

- **devin-docs**: checked, minor changes ignored
- **cognition-blog**: checked, minor changes ignored
- **devin-release-notes**: checked, no significant changes
- **claude-code-docs**: no completed checks yet
- **github-copilot-docs**: summarization failed — changes detected but not summarized
- **github-copilot-coding-agent**: checked, no significant changes
- **cursor-docs**: no completed checks yet
- **factory-docs**: summarization failed — changes detected but not summarized
- **coderabbit-docs**: checked, minor changes ignored

## System Status

- 5/9 sources checked successfully
- 2 failed sources
- No secrets printed
- Digest generated successfully

## Minor Changes Ignored

### devin-docs

- **https://docs.devin.ai** (score 2, minor wording): The only change detected is an update to the subscriber count for the Cognition YouTube channel. This is a social media metric and does not relate to Devin's features, API, deployment, pricing, security, or integrations.
- **https://docs.devin.ai/admin/security** (score 1, product): The documentation regarding data usage and privacy has been significantly updated. The default policy for data training has changed from 'opt-in' to 'opt-out' for paid users, and new details regarding Zero Data Retention and Enterprise consent requirements have been added. This falls under the security and integration updates scope of the monitoring goal.
- **https://docs.devin.ai/api-reference/v1/knowledge/create-knowledge** (score 1, minor wording): The documentation for the 'KnowledgeCreatedBy' object in the API has been updated to indicate that the field can now be null. This is a functional API change regarding data types and nullability, which falls under the user's goal of tracking API changes.
- **https://docs.devin.ai/api-reference/v1/knowledge/update-knowledge** (score 1, minor wording): The documentation for the 'KnowledgeCreatedBy' object in the API reference was updated to indicate that the field can now be null. This is a functional API change regarding data types and nullability, which falls under the user's goal of tracking API changes.
- **https://docs.devin.ai/api-reference/v1/sessions/create-a-new-devin-session** (score 1, docs-only): The documentation for the 'structured_output_schema' API parameter was updated to allow a 'null' value. This is a functional API change regarding valid input types, which falls under the user's goal of tracking API changes.
- **https://docs.devin.ai/api-reference/v1/sessions/retrieve-details-about-an-existing-session** (score 1, security): The documentation for the 'PullRequestInfo' object in the API reference has been updated to indicate that the value can now be 'null'. This constitutes a technical API change regarding data types and nullability, which falls under the user's goal of tracking API changes.
- **https://docs.devin.ai/api-reference/v2/consumption/daily-consumption** (score 1, minor wording): The API documentation for the 'Consumption By User' object has been updated to indicate that it can now return a null value. This is a functional API change that developers integrating with Devin would need to handle.
- **https://docs.devin.ai/api-reference/v2/repositories/get-repository-status** (score 1, docs-only): The API documentation has been updated to reflect that several repository indexing job response fields can now return 'null'. This is a functional change to the API schema that developers integrating with Devin need to account for.
- **https://docs.devin.ai/api-reference/v2/sessions/get-enterprise-session** (score 1, minor wording): The API documentation for the 'session_analysis' object has been updated to indicate that the 'SessionAnalysisData' field can now be null. This is a functional change to the API schema that developers using the Devin API need to account for.
- **https://docs.devin.ai/api-reference/v3/audit-logs/enterprise-audit-logs** (score 1, security): The documentation was updated to include new security and governance features, specifically AI Guardrail violations in audit logs and a new telemetry setting for code snippets. These fall under the user's interest in security and feature updates.
- **https://docs.devin.ai/api-reference/v3/audit-logs/organizations-audit-logs** (score 1, product): A new API event type 'update_code_snippet_telemetry' has been added to the documentation, which falls under the user's goal of tracking API changes and integration updates.
- **New page**: https://docs.devin.ai/api-reference/v3/code-scans/enterprise-code-scans-findings
- **New page**: https://docs.devin.ai/api-reference/v3/code-scans/enterprise-code-scans-metrics
- **New page**: https://docs.devin.ai/api-reference/v3/code-scans/enterprise-code-scans-remediate
- **Removed page**: https://docs.devin.ai/api-reference/v3/consumption/organizations-consumption-daily-service-users
- **Removed page**: https://docs.devin.ai/api-reference/v3/consumption/organizations-consumption-daily
- **Removed page**: https://docs.devin.ai/api-reference/v3/consumption/organizations-consumption-daily-sessions

### cognition-blog

- **https://cognition.ai/blog** (score 1, product): Three new blog posts were added to the top of the list, covering new product announcements (Devin Security Swarm, Devin Fusion) and a new company program (Security Vulnerability Remediation Program).

### github-copilot-docs

- **https://docs.github.com/en/copilot/reference/ai-models/model-comparison** (score 1, pricing): The documentation was updated with new AI models for agent tasks and coding, a new pricing discount for the 'Auto' model selection feature, and changes to the available model versions.
- **https://docs.github.com/en/copilot/concepts/agents/enterprise-management** (score 1, pricing): The documentation was updated to include new enterprise deployment and monitoring capabilities, specifically regarding streaming audit log data for agentic activity and long-term retention.
- **https://docs.github.com/en/copilot/concepts/billing/usage-based-billing-for-organizations-and-enterprises** (score 1, pricing): The diff introduces new documentation regarding AI credit usage and expiration policies for Copilot, which falls under the user's goal of tracking enterprise deployment and pricing/billing updates.
- **https://docs.github.com/en/copilot/reference/customization-cheat-sheet** (score 2, product): The only change in the document is a formatting update to the table alignment syntax in the Markdown source. There are no changes to the features, availability, pricing, or capabilities mentioned in the goal.
- **https://docs.github.com/en/copilot/reference/copilot-feature-matrix** (score 4, product): The changes are purely mechanical formatting updates to the Markdown table syntax (changing alignment markers like ':--' to standard dashes '---'). There are no changes to the actual content, features, agent capabilities, or pricing.
- **https://docs.github.com/en/copilot/concepts/billing/usage-based-billing-for-individuals** (score 1, pricing): The diff contains significant updates to Copilot's pricing and billing structure, specifically regarding the expiration of AI credits and new agent-specific cost management features (session limits for agent tasks).
- **https://docs.github.com/en/copilot/how-tos/copilot-sdk/features/steering-and-queueing** (score 2, integration): The changes are limited to technical label updates ('aria_label navigation' to 'Code languages navigation') for accessibility or internal documentation structure. These do not represent updates to agent features, coding capabilities, pricing, or deployment options.
- **https://docs.github.com/en/copilot** (score 2, product): The only change detected is an update to the total count of documents (from 413 to 416). There are no visible changes to the content, features, pricing, or deployment options specified in the monitoring goal.
- **https://docs.github.com/en/copilot/reference/ai-models/supported-models** (score 1, product): The documentation was updated to include several new AI models (Claude Sonnet 5, Kimi-K2.7-Code, and Claude Opus 4.8 fast mode) and the retirement of an older model version. These changes directly impact the available coding agent capabilities and model integrations for Copilot.
- **https://docs.github.com/en/copilot/how-tos/copilot-sdk/setup/scaling** (score 2, deployment): The only change detected is an update to the image asset URL (cache buster/ID change). There are no updates to the documentation text, agent features, enterprise options, or pricing.
- **New page**: https://docs.github.com/en/copilot/concepts/context/spaces
- **New page**: https://docs.github.com/en/copilot/concepts/models/fedramp-models
- **New page**: https://docs.github.com/en/copilot/concepts/usage-limits
- **New page**: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/troubleshoot-cloud-agent
- **New page**: https://docs.github.com/en/copilot/how-tos/copilot-on-github/copilot-for-github-tasks/using-the-github-mcp-server-from-copilot-chat
- **New page**: https://docs.github.com/en/copilot/concepts/network-settings
- **New page**: https://docs.github.com/en/copilot/get-started/features
- **New page**: https://docs.github.com/en/copilot/how-tos/provide-context/use-mcp-in-your-ide/set-up-the-github-mcp-server?tool=vscode
- **New page**: https://docs.github.com/en/copilot/how-tos/use-ai-models/change-the-completion-model?tool=vscode
- **New page**: https://docs.github.com/en/copilot/how-tos/copilot-on-github/set-up-copilot/configure-access-to-ai-models
- **New page**: https://docs.github.com/en/copilot/concepts/agents/github-copilot-app
- **New page**: https://docs.github.com/en/copilot/tutorials/write-tests
- **New page**: https://docs.github.com/en/copilot/reference/copilot-billing/request-based-billing-legacy/what-changed-with-billing
- **New page**: https://docs.github.com/en/copilot/reference/copilot-allowlist-reference
- **New page**: https://docs.github.com/en/copilot/how-tos/copilot-cli
- **New page**: https://docs.github.com/en/copilot/how-tos/copilot-on-github/set-up-copilot/configure-automatic-review
- **New page**: https://docs.github.com/en/copilot/concepts/billing
- **New page**: https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-enterprise/review-audit-logs
- **New page**: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/changing-the-ai-model
- **New page**: https://docs.github.com/en/copilot/how-tos/copilot-sdk/features/custom-agents
- **New page**: https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/configure-secrets-and-variables
- **New page**: https://docs.github.com/en/copilot/how-tos/provide-context/use-mcp-in-your-ide/set-up-the-github-mcp-server
- **New page**: https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-mcp-usage/configure-mcp-registry
- **New page**: https://docs.github.com/en/copilot/tutorials/cloud-agent/get-the-best-results
- **New page**: https://docs.github.com/en/copilot/reference/copilot-cli-reference/acp-server
- **New page**: https://docs.github.com/en/copilot/how-tos/provide-context/use-mcp-in-your-ide/enterprise-configuration
- **New page**: https://docs.github.com/en/copilot/how-tos/github-copilot-app/managing-issues-and-pull-requests
- **New page**: https://docs.github.com/en/copilot/tutorials/migrate-a-project
- **New page**: https://docs.github.com/en/copilot/concepts/agents/copilot-cli/about-copilot-cli
- **New page**: https://docs.github.com/en/copilot/tutorials/roll-out-at-scale/drive-downstream-impact/increase-test-coverage
- **New page**: https://docs.github.com/en/copilot/tutorials/copilot-cookbook/document-code
- **New page**: https://docs.github.com/en/copilot/reference/copilot-billing/models-and-pricing
- **New page**: https://docs.github.com/en/copilot/how-tos/configure-personal-settings/authenticate-to-ghecom
- **New page**: https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-organization/manage-access/grant-access
- **New page**: https://docs.github.com/en/copilot/concepts/agents/copilot-in-jetbrains
- **New page**: https://docs.github.com/en/copilot/reference/copilot-billing/request-based-billing-legacy/monitor-premium-requests
- **New page**: https://docs.github.com/en/copilot/reference/agentic-audit-log-events
- **New page**: https://docs.github.com/en/copilot/how-tos/copilot-on-github/copilot-for-github-tasks/create-a-pr-summary
- **New page**: https://docs.github.com/en/copilot/reference/ai-models/model-hosting
- **New page**: https://docs.github.com/en/copilot/reference/copilot-billing/models-and-pricing.md
- **New page**: https://docs.github.com/en/copilot/how-tos/get-code-suggestions/get-ide-code-suggestions
- **New page**: https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-organization/use-your-own-api-keys
- **New page**: https://docs.github.com/en/copilot/reference/copilot-usage-metrics/copilot-usage-metrics
- **New page**: https://docs.github.com/en/copilot/how-tos/copilot-cli/set-up-copilot-cli/install-copilot-cli
- **New page**: https://docs.github.com/en/copilot/concepts/agents/openai-codex
- **New page**: https://docs.github.com/en/copilot/concepts/agents/about-agent-skills
- **New page**: https://docs.github.com/en/copilot/concepts/context/content-exclusion
- **New page**: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/integrate-cloud-agent-with-slack
- **New page**: https://docs.github.com/en/copilot/tutorials/customization-library/custom-agents/your-first-custom-agent
- **New page**: https://docs.github.com/en/copilot/tutorials/customization-library/custom-instructions/your-first-custom-instructions
- **New page**: https://docs.github.com/en/copilot/tutorials/customization-library/prompt-files/your-first-prompt-file
- **New page**: https://docs.github.com/en/copilot/how-tos/configure-personal-settings/configure-network-settings
- **New page**: https://docs.github.com/en/copilot/how-tos/copilot-cli/automate-copilot-cli/run-cli-programmatically
- **New page**: https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/plugins-marketplace
- **New page**: https://docs.github.com/en/copilot/get-started/what-is-github-copilot
- **New page**: https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/create-custom-agents
- **New page**: https://docs.github.com/en/copilot/how-tos/copilot-cli/use-copilot-cli/overview
- **New page**: https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers
- **New page**: https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-organization/manage-access
- **New page**: https://docs.github.com/en/copilot/how-tos/copilot-cli/set-up-copilot-cli/authenticate-copilot-cli
- **New page**: https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-enterprise
- **New page**: https://docs.github.com/en/copilot/reference/review-excluded-files
- **New page**: https://docs.github.com/en/copilot/tutorials/cloud-agent/build-guardrails
- **New page**: https://docs.github.com/en/copilot/tutorials
- **New page**: https://docs.github.com/en/copilot/how-tos/use-ai-models/change-the-chat-model
- **New page**: https://docs.github.com/en/copilot/concepts/prompting/response-customization
- **New page**: https://docs.github.com/en/copilot/reference/copilot-usage-metrics/interpret-copilot-metrics
- **New page**: https://docs.github.com/en/copilot/tutorials/roll-out-at-scale/drive-downstream-impact/accelerate-pull-requests
- **New page**: https://docs.github.com/en/copilot/how-tos/copilot-cli/automate-copilot-cli/automate-with-actions
- **Removed page**: https://docs.github.com/en/copilot/how-tos/provide-context/use-mcp-in-your-ide/change-mcp-registry
- **Removed page**: https://docs.github.com/en/copilot/reference
- **Removed page**: https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-organization/add-copilot-cloud-agent
- **Removed page**: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/use-cloud-agent-from-cli
- **Removed page**: https://docs.github.com/en/copilot/how-tos/copilot-sdk/auth
- **Removed page**: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-automations
- **Removed page**: https://docs.github.com/en/copilot/how-tos/copilot-sdk/features/fleet-mode
- **Removed page**: https://docs.github.com/en/copilot/tutorials/customization-library/custom-agents/cleanup-specialist
- **Removed page**: https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/plugins-finding-installing
- **Removed page**: https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-enterprise/manage-agents/prepare-for-custom-agents
- **Removed page**: https://docs.github.com/en/copilot/tutorials/customization-library/prompt-files/create-readme
- **Removed page**: https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-organization/configure-runner-for-coding-agent
- **Removed page**: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/integrate-cloud-agent-with-azure-boards
- **Removed page**: https://docs.github.com/en/copilot/how-tos/copilot-sdk/hooks
- **Removed page**: https://docs.github.com/en/copilot/concepts/chat
- **Removed page**: https://docs.github.com/en/copilot/tutorials/cloud-agent
- **Removed page**: https://docs.github.com/en/copilot/tutorials/customization-library/custom-instructions/issue-manager
- **Removed page**: https://docs.github.com/en/copilot/tutorials/cloud-agent/improve-a-project
- **Removed page**: https://docs.github.com/en/copilot/how-tos/copilot-sdk/hooks/hooks-overview
- **Removed page**: https://docs.github.com/en/copilot/tutorials/cloud-agent/pilot-cloud-agent
- **Removed page**: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/use-cloud-agent-in-your-ide
- **Removed page**: https://docs.github.com/en/copilot/how-tos/copilot-sdk/features/streaming-events
- **Removed page**: https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/use-hooks
- **Removed page**: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/configuring-agent-settings
- **Removed page**: https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-organization/manage-policies
- **Removed page**: https://docs.github.com/en/copilot/reference/copilot-billing/request-based-billing-legacy/model-multipliers-for-annual-plans
- **Removed page**: https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions
- **Removed page**: https://docs.github.com/en/copilot/concepts/models/auto-model-selection
- **Removed page**: https://docs.github.com/en/copilot/how-tos/use-copilot-for-common-tasks/use-copilot-in-the-cli
- **Removed page**: https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-enterprise/manage-enterprise-policies
- **Removed page**: https://docs.github.com/en/copilot/concepts/policies
- **Removed page**: https://docs.github.com/en/copilot/tutorials/budgets/optimizing-your-budget-configuration
- **Removed page**: https://docs.github.com/en/copilot/how-tos/copilot-cli/cli-best-practices
- **Removed page**: https://docs.github.com/en/copilot/how-tos/copilot-on-github/set-up-copilot/enable-copilot/set-up-a-dedicated-enterprise-for-copilot-business
- **Removed page**: https://docs.github.com/en/copilot/how-tos/copilot-on-github/use-copilot-agents/copilot-code-review
- **Removed page**: https://docs.github.com/en/copilot/tutorials/enhance-agent-mode-with-mcp
- **Removed page**: https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-config-dir-reference
- **Removed page**: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/create-automations
- **Removed page**: https://docs.github.com/en/copilot/tutorials/budgets/getting-started-with-budget-controls
- **Removed page**: https://docs.github.com/en/copilot/concepts/billing/budgets-for-usage-based-billing
- **Removed page**: https://docs.github.com/en/copilot/how-tos/copilot-sdk/troubleshooting/mcp-debugging
- **Removed page**: https://docs.github.com/en/copilot/concepts/agents/copilot-memory
- **Removed page**: https://docs.github.com/en/copilot/how-tos/copilot-sdk/features/hooks
- **Removed page**: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/create-custom-agents-in-your-ide
- **Removed page**: https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-enterprise/manage-agents/disable-automatic-commands
- **Removed page**: https://docs.github.com/en/copilot/how-tos/copilot-sdk/setup/backend-services
- **Removed page**: https://docs.github.com/en/copilot/how-tos/copilot-sdk/hooks/error-handling
- **Removed page**: https://docs.github.com/en/copilot/how-tos/copilot-sdk/setup
- **Removed page**: https://docs.github.com/en/copilot/concepts/models
- **Removed page**: https://docs.github.com/en/copilot/how-tos/copilot-sdk/setup/azure-managed-identity
- **Removed page**: https://docs.github.com/en/copilot/how-tos/copilot-cli/use-copilot-cli/delegate-tasks-to-cca
- **Removed page**: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/integrate-cloud-agent-with-teams
- **Removed page**: https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-enterprise/manage-agents/enable-copilot-code-review
- **Removed page**: https://docs.github.com/en/copilot/reference/agent-session-filters
- **Removed page**: https://docs.github.com/en/copilot/tutorials/review-ai-generated-code
- **Removed page**: https://docs.github.com/en/copilot/how-tos/copilot-sdk
- **Removed page**: https://docs.github.com/en/copilot/reference/copilot-billing/request-based-billing-legacy/github-copilot-premium-requests
- **Removed page**: https://docs.github.com/en/copilot/tutorials/optimize-ai-usage
- **Removed page**: https://docs.github.com/en/copilot/tutorials/customization-library/custom-agents
- **Removed page**: https://docs.github.com/en/copilot/tutorials/customization-library
- **Removed page**: https://docs.github.com/en/copilot/concepts/spark
- **Removed page**: https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent
- **Removed page**: https://docs.github.com/en/copilot/how-tos/copilot-sdk/setup/multi-tenancy
- **Removed page**: https://docs.github.com/en/copilot/how-tos/copilot-on-github/use-copilot-agents/review-copilot-output
- **Removed page**: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/copilot-memory/manage-as-administrator
- **Removed page**: https://docs.github.com/en/copilot/tutorials/customization-library/custom-agents/implementation-planner
- **Removed page**: https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-organization/prepare-for-custom-agents
- **Removed page**: https://docs.github.com/en/copilot/responsible-use
- **Removed page**: https://docs.github.com/en/copilot/how-tos/copilot-cli/use-copilot-cli/voice-input

### factory-docs

- **https://docs.factory.ai/api-reference/computers/create-a-computer.md** (score 5, security): The changes are limited to indentation, whitespace, and escaping characters (e.g., removing backslashes before hashes and hyphens) within the OpenAPI YAML block. There are no changes to product features, pricing, deployment options, or security protocols.
- **https://docs.factory.ai/welcome/index.md** (score 1, product): The documentation has been significantly restructured to include new product features and deployment options, specifically adding 'Droid Exec' for CI/CD automation and 'Enterprise' deployment/governance options. It also introduces new capability sections for 'Factory Missions', 'Droid Control', and 'Agent Readiness', which directly relate to product features and deployment goals.
- **https://docs.factory.ai/guides/building/droid-vps-setup** (score 2, deployment): The only changes detected are updates to the subscriber count on YouTube video embeds. The monitor goal specifically asks for changes to product features, pricing, deployment, security, and competitive positioning, and these minor counter updates do not fall into those categories.
- **https://docs.factory.ai/cli/droid-exec/overview.md** (score 5, product): The changes are purely mechanical, involving the conversion of markdown formatting to use custom UI components (Tip, Card, Steps, Warning) and fixing escaping characters. There are no changes to product features, pricing, deployment, or security policies.
- **https://docs.factory.ai/web/missions.md** (score 1, product): The documentation was updated with a new 'See also' section that introduces links to several new feature pages, including Planning & Validation, Troubleshooting, and Configuration & Reference. It also includes minor structural changes to the UI navigation descriptions.
- **https://docs.factory.ai/support.md** (score 4, product): The changes are purely formatting and UI-related, wrapping existing support links (Email, Discord, GitHub) into Card components. There are no changes to product features, pricing, deployment, security, or competitive positioning.
- **https://docs.factory.ai/enterprise/service-accounts.md** (score 1, product): The documentation for Service Accounts was updated to include a new permission requirement (owners can now create/edit accounts, not just managers) and the content was restructured into functional categories (CardGroups and Accordions) which clarifies deployment and security best practices.
- **https://docs.factory.ai/enterprise/network-and-deployment.md** (score 5, product): The changes are limited to markdown formatting fixes, such as removing unnecessary backslashes and adding UI components like CardGroups for existing text. No new product features, pricing, deployment patterns, or security details were added or modified.
- **https://docs.factory.ai/cli/user-guides/specification-mode.md** (score 5, product): The changes are purely structural and formatting-related. The content has been moved into UI components like <CardGroup>, <Card>, <Steps>, and <Note>, but the actual text describing product features, deployment, and security remains identical to the previous version. No new features, pricing, or positioning details were added.
- **https://docs.factory.ai/enterprise/models-llm-gateways-and-integrations.md** (score 5, integration): The changes are strictly limited to formatting and syntax normalization. Specifically, the diff shows a transition from escaped characters (like '\*\*\*' and '\#') to standard Markdown syntax ('***' and '#'), and a change in list indentation/bullet styles. No product features, pricing, security policies, or deployment details were modified.
- **https://docs.factory.ai/guides/power-user/evaluating-context-compression.md** (score 5, product): The changes are purely formatting and character escaping fixes. Backslashes used for escaping markdown characters (like asterisks and hashes) were removed, and a single paragraph was wrapped in an <Info> tag, but no substantive information regarding product features, pricing, or positioning was added, removed, or modified.
- **New page**: https://docs.factory.ai/features/missions/reference.md
- **New page**: https://docs.factory.ai/guides/hooks/logging-analytics
- **New page**: https://docs.factory.ai/api-reference/computers/refresh-a-computer.md
- **New page**: https://docs.factory.ai/cli/byok/baseten.md
- **New page**: https://docs.factory.ai/features/missions/troubleshooting.md
- **New page**: https://docs.factory.ai/benchmarks/terminal-bench.md
- **New page**: https://docs.factory.ai/api-reference/sessions/get-a-session.md
- **New page**: https://docs.factory.ai/cli/configuration/skills.md
- **New page**: https://docs.factory.ai/cli/features/droid-computers-byom
- **New page**: https://docs.factory.ai/changelog/1-10.md
- **New page**: https://docs.factory.ai/changelog/release-notes.md
- **New page**: https://docs.factory.ai/guides/skills/automated-qa
- **New page**: https://docs.factory.ai/cli/configuration/custom-slash-commands.md
- **New page**: https://docs.factory.ai/guides/hooks/git-workflows.md
- **New page**: https://docs.factory.ai/cli/features/droid-computers.md
- **New page**: https://docs.factory.ai/enterprise/identity-sso-and-scim.md
- **New page**: https://docs.factory.ai/reference/analytics-api.md
- **New page**: https://docs.factory.ai/cli/configuration/plugins
- **New page**: https://docs.factory.ai/cli/configuration/settings.md
- **New page**: https://docs.factory.ai/cli/byok/ollama
- **New page**: https://docs.factory.ai/cli/account/droid-shield-plus.md
- **New page**: https://docs.factory.ai/cli/droid-exec/overview
- **New page**: https://docs.factory.ai/cli/configuration/sandbox.md
- **New page**: https://docs.factory.ai/cli/configuration/hooks-guide
- **New page**: https://docs.factory.ai/enterprise/network-and-deployment
- **New page**: https://docs.factory.ai/cli/getting-started/how-to-talk-to-a-droid
- **New page**: https://docs.factory.ai/guides/power-user/setup-checklist.md
- **New page**: https://docs.factory.ai/features/missions/planning.md
- **New page**: https://docs.factory.ai/models
- **New page**: https://docs.factory.ai/web/getting-started/quickstart
- **Removed page**: https://docs.factory.ai/api-reference/organization/set-user-credits-limits.md
- **Removed page**: https://docs.factory.ai/cli/byok/groq
- **Removed page**: https://docs.factory.ai/cli/byok/google-gemini.md
- **Removed page**: https://docs.factory.ai/cli/account/security.md
- **Removed page**: https://docs.factory.ai/api-reference/sessions/list-sessions.md
- **Removed page**: https://docs.factory.ai/cli/features/droid-control
- **Removed page**: https://docs.factory.ai/guides/power-user/memory-management.md
- **Removed page**: https://docs.factory.ai/api-reference/service-accounts/create-a-service-account-api-key.md
- **Removed page**: https://docs.factory.ai/cli/features/wiki/overview
- **Removed page**: https://docs.factory.ai/api-reference/automations/list-ci-repository-owners.md
- **Removed page**: https://docs.factory.ai/cli/byok/ollama.md
- **Removed page**: https://docs.factory.ai/api-reference/sessions/add-a-message-to-a-session.md
- **Removed page**: https://docs.factory.ai/guides/building/droid-vps-setup.md
- **Removed page**: https://docs.factory.ai/api-reference/sessions/interrupt-a-session.md
- **Removed page**: https://docs.factory.ai/cli/features/droid-computers-byom.md
- **Removed page**: https://docs.factory.ai/cli/byok/baseten
- **Removed page**: https://docs.factory.ai/api-reference/computers/delete-a-computer.md
- **Removed page**: https://docs.factory.ai/guides/hooks/testing-automation
- **Removed page**: https://docs.factory.ai/cli/byok/google-gemini
- **Removed page**: https://docs.factory.ai/api-reference/computers/update-a-computer.md
- **Removed page**: https://docs.factory.ai/api-reference/wiki/list-the-latest-wiki-runs.md
- **Removed page**: https://docs.factory.ai/api-reference/organization/list-organization-users.md
- **Removed page**: https://docs.factory.ai/changelog/1-9.md
- **Removed page**: https://docs.factory.ai/api-reference/sessions/delete-a-session.md
- **Removed page**: https://docs.factory.ai/guides/skills/product-management.md
- **Removed page**: https://docs.factory.ai/cli/features/missions
- **Removed page**: https://docs.factory.ai/cli/user-guides/implementing-large-features.md
- **Removed page**: https://docs.factory.ai/api-reference/computers/get-a-computer.md
- **Removed page**: https://docs.factory.ai/api-reference/organization/list-enterprise-control-change-history.md
- **Removed page**: https://docs.factory.ai/api-reference/computers/get-a-computer-by-name.md

### coderabbit-docs

- **https://docs.coderabbit.ai/api-reference/users-list** (score 1, integration): The documentation for the API reference has changed, replacing 'Metrics Data' with 'Learnings'. This represents a change in product features or API capabilities, which falls under the monitoring goal.
- **https://docs.coderabbit.ai/api-reference/users-manage-seats** (score 1, integration): The removal of API reference links for 'Users' and 'Seat Assignment Mode' represents a change in the documented product features or administrative capabilities, which falls under the user's goal of tracking product features and integrations.
- **https://docs.coderabbit.ai/cli/codex-integration** (score 1, integration): The documentation for the CodeRabbit CLI has been updated to reflect a change in product features. Specifically, the 'interactive' mode has been replaced by a new 'light' review command, which represents a change in the available functionality and usage patterns of the tool.
- **https://docs.coderabbit.ai/cli/cursor-integration** (score 1, integration): The documentation for the CLI integration has been updated to reflect a change in product features. Specifically, the '--interactive' mode has been replaced with a new '--light' review command, and the terminology has shifted from 'Output modes' to 'Review commands'.
- **https://docs.coderabbit.ai/cli/gemini-integration** (score 1, integration): The documentation for the Gemini CLI integration has been updated to reflect a change in product features. Specifically, the '--interactive' mode has been replaced with a new '--light' review command, and a video demo has been added.
- **https://docs.coderabbit.ai/api-reference/roles-delete** (score 1, security): The documentation for the API reference has been updated to include a new required query parameter ('org_id') for deleting roles. This represents a functional change to the product's API capabilities and integration requirements, which falls under the user's goal of tracking product features and integrations.
- **https://docs.coderabbit.ai/api-reference/roles-create** (score 1, security): The documentation was updated to include a new required API parameter 'org_id' for creating roles. This represents a functional change to the product's API and integration capabilities, which falls under the user's goal of tracking product features and integrations.
- **https://docs.coderabbit.ai/api-reference/roles-get** (score 1, security): The documentation was updated to include a new required query parameter ('org_id') for the API, which falls under product features and technical integrations.
- **https://docs.coderabbit.ai/api-reference/roles-list** (score 1, security): The documentation was updated to include a new required query parameter 'org_id' for the Roles List API endpoint. This represents a functional change in how the API integration works when using workspace-scoped tokens.
- **https://docs.coderabbit.ai/api-reference/roles-update** (score 1, security): The documentation for the CodeRabbit API has been updated to include a new required field, 'org_id', for role creation and updates. This is a functional change to how integrations and workspace-scoped authentication work, which falls under the user's goal of tracking product features and integrations.
- **https://docs.coderabbit.ai/api-reference/roles-permissions** (score 1, security): The documentation has been updated to include a new required query parameter ('org_id') for API authentication when using workspace-scoped tokens. This falls under the 'product features' and 'integrations' scope of the monitoring goal as it changes how developers interact with the CodeRabbit API.
- **https://docs.coderabbit.ai** (score 2, product): The changes are limited to internal documentation URL updates and a footer navigation link change. There are no updates to product features, pricing, integrations, security, or competitive positioning as requested.
- **https://docs.coderabbit.ai/cli** (score 1, pricing): The documentation was updated to include a new CLI feature ('cr stats') and changes to existing CLI review modes and flags, which falls under tracking product features.
- **https://docs.coderabbit.ai/cli/claude-code-integration** (score 1, integration): The documentation for the CodeRabbit CLI has been updated to reflect a change in product features. Specifically, the 'interactive' mode/command has been replaced with a 'light' review policy, which represents a change in the available functionality and integration options for the CLI tool.
- **https://docs.coderabbit.ai/cli/reference** (score 1, integration): The documentation was updated to reflect changes in product features, specifically the renaming of a CLI flag and the addition of a new 'stats' command and functionality.
- **https://docs.coderabbit.ai/cli/wsl-windows** (score 1, deployment): The documentation for the CLI tool has changed a product feature/command. Specifically, the '--interactive' flag for the terminal UI has been replaced or updated to a '--light' flag for a local review policy. The subscriber count change is ignored as noise.
- **https://docs.coderabbit.ai/changelog** (score 1, pricing): The changelog contains significant updates to product features (Multi-repo ref selection, Learnings API, new security tools), pricing (Legacy plan sunset), and integrations (Amplemarket, Devin, GitLab reverse tunnel).
- **https://docs.coderabbit.ai/reference/review-commands** (score 1, pricing): The documentation was updated to reflect expanded platform support for the Autofix feature and enhanced functionality for the configuration command, both of which fall under product features and integrations.
- **https://docs.coderabbit.ai/reference/configuration** (score 1, product): The documentation was updated with several new product features and integrations, including new security scanners (SkillSpector, React Doctor), a breaking change detector (oasdiff), and new configuration options for repository linking and learning approvals. It also changed the default behavior for the Microsoft Presidio PII analyzer.
- **https://docs.coderabbit.ai/api-reference/metrics-data-api** (score 1, security): The documentation has been updated to include a new API field 'ready_for_review_at' and a new 'Learnings' API endpoint, which represents a change in product features and API capabilities.
- **New page**: https://docs.coderabbit.ai/management/plans
- **New page**: https://docs.coderabbit.ai/login?redirect=%2Fintegrations%2Fknowledge-base
- **New page**: https://docs.coderabbit.ai/llms.txt
- **New page**: https://docs.coderabbit.ai/platforms/github-com.md
- **New page**: https://docs.coderabbit.ai/login?redirect=%2Fself-hosted%2Foverview
- **New page**: https://docs.coderabbit.ai/pr-reviews/cicd-pipeline-analysis
- **New page**: https://docs.coderabbit.ai/reference/caching.md
- **New page**: https://docs.coderabbit.ai/platforms/github-enterprise-server
- **New page**: https://docs.coderabbit.ai/login?redirect=%2Fabout%2Fdata-usage
- **New page**: https://docs.coderabbit.ai/login?redirect=%2Fintegrations%2Fcode-graph-analysis
- **New page**: https://docs.coderabbit.ai/login?redirect=%2Fguides%2Fusage-cli
- **New page**: https://docs.coderabbit.ai/login?redirect=%2Fblog%2Fpre-merge-checks-built-in-and-custom-pr-enforced
- **New page**: https://docs.coderabbit.ai/getting-started/yaml-configuration
- **New page**: https://docs.coderabbit.ai/cli/cli-with-self-hosted-CodeRabbit.md
- **New page**: https://docs.coderabbit.ai/login?redirect=%2Fgetting-started%2Fconfigure-coderabbit
- **New page**: https://docs.coderabbit.ai/overview/architecture.md
- **New page**: https://docs.coderabbit.ai/management/usage-based-addon
- **New page**: https://docs.coderabbit.ai/login?redirect=%2Fplatform%2Fintegration
- **New page**: https://docs.coderabbit.ai/self-hosted/coderabbit-reverse-tunnel.md
- **New page**: https://docs.coderabbit.ai/cli/index.md
- **New page**: https://docs.coderabbit.ai/login?redirect=%2Fcli%2Foverview
- **New page**: https://docs.coderabbit.ai/login?redirect=%2Fabout%2Fdata-usage.md
- **New page**: https://docs.coderabbit.ai/integrations/issue-trackers
- **New page**: https://docs.coderabbit.ai/api-reference/learnings-list
- **Removed page**: https://docs.coderabbit.ai/slack-agent
- **Removed page**: https://docs.coderabbit.ai/pr-reviews/walkthroughs
- **Removed page**: https://docs.coderabbit.ai/cli/index
- **Removed page**: https://docs.coderabbit.ai/platforms/self-hosted-gitlab
- **Removed page**: https://docs.coderabbit.ai/early-access
- **Removed page**: https://docs.coderabbit.ai/finishing-touches/autofix
- **Removed page**: https://docs.coderabbit.ai/faq
- **Removed page**: https://docs.coderabbit.ai/configuration/yaml-validator
- **Removed page**: https://docs.coderabbit.ai/finishing-touches/custom-finishing-touches
- **Removed page**: https://docs.coderabbit.ai/configuration/example/typescript/expo
- **Removed page**: https://docs.coderabbit.ai/configuration/path-instructions
- **Removed page**: https://docs.coderabbit.ai/pr-reviews/pre-merge-checks
- **Removed page**: https://docs.coderabbit.ai/platforms/gitlab-com
- **Removed page**: https://docs.coderabbit.ai/guides/commands
- **Removed page**: https://docs.coderabbit.ai/cli/headless-cli-integration
- **Removed page**: https://docs.coderabbit.ai/configuration/ast-grep-instructions
- **Removed page**: https://docs.coderabbit.ai/configuration/central-configuration
- **Removed page**: https://docs.coderabbit.ai/configuration/auto-review
- **Removed page**: https://docs.coderabbit.ai/configuration/configuration-inheritance
- **Removed page**: https://docs.coderabbit.ai/configuration/example
- **Removed page**: https://docs.coderabbit.ai/configuration/example/other/mintlify-documentation
- **Removed page**: https://docs.coderabbit.ai/configuration/example/python/django
- **Removed page**: https://docs.coderabbit.ai/guides/code-review-overview
- **Removed page**: https://docs.coderabbit.ai/llms-full.txt

## Sales / Learning Impact

No talk track updates needed this week.

## Next Recommended Action

Review the minor changes above if any look relevant. No action required otherwise.
