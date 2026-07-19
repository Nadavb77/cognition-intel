# Weekly AI Coding Agents Digest

**Date:** 2026-07-19

---

## Executive Summary

Minor changes were detected but none scored high enough (score ≥ 3) to warrant summarization. Details below.

## Sources Checked

- **devin-docs**: checked, minor changes ignored
- **cognition-blog**: checked, minor changes ignored
- **devin-release-notes**: checked, minor changes ignored
- **claude-code-docs**: no completed checks yet
- **github-copilot-docs**: summarization failed — changes detected but not summarized
- **github-copilot-coding-agent**: checked, minor changes ignored
- **cursor-docs**: checked, minor changes ignored
- **factory-docs**: summarization failed — changes detected but not summarized
- **coderabbit-docs**: checked, minor changes ignored

## System Status

- 6/9 sources checked successfully
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

- **https://cognition.ai/blog** (score 1, product): Three new blog posts were added to the top of the list, covering company milestones, product pricing/performance comparisons, and federal compliance updates, all of which match the user's goal of tracking product announcements and company news.

### devin-release-notes

- **https://docs.devin.ai/changelog** (score 2, integration): The change shows a 'Page Not Found' error message being updated, specifically removing a link to the changelog from a 404 page. This does not represent a new release note, feature, bug fix, or changelog entry.

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

### github-copilot-coding-agent

- **https://docs.github.com/copilot/concepts/agents/coding-agent/about-coding-agent** (score 2, pricing): The only changes detected are related to the page's navigation interface (sidebar and breadcrumb controls). There are no updates to the Copilot cloud agent's capabilities, pricing, availability, or security model.

### cursor-docs

- **https://cursor.com/docs/customize-cursor** (score 1, deployment): The documentation was updated to include a new 'Mobile' capability for Cloud Agents and a new 'Team MCP servers' feature for integrations and team collaboration.
- **https://docs.cursor.com** (score 1, product): The documentation has been updated with new AI models, a new 'Mobile' section for Cloud Agents, and the removal of several older model versions. These changes directly impact the features and agent capabilities of Cursor.
- **https://cursor.com/docs/api** (score 1, product): The documentation was updated to include a new 'Bugbot API' feature, including its purpose, availability for Enterprise teams, and specific rate limits. Additionally, new Admin API endpoints for Organization Members, Daily Usage, and Spending were added.
- **https://cursor.com/learn** (score 1, product): The documentation has been updated to include a new section or interface element for 'Agent' capabilities, which is explicitly listed in the monitoring goal. It also introduces a 'Tokenizer' with a specific context limit of 200k, representing a change in technical capabilities/features.
- **https://cursor.com/docs/get-started/quickstart** (score 1, deployment): A new documentation section for 'Mobile' has been added under the Cloud Agents category, indicating a new feature or platform capability for Cursor's agents.
- **https://cursor.com/changelog** (score 1, product): The changelog was updated with several major feature releases including a new iOS mobile app, side chats, conversation search, and expanded agent capabilities like cloud agent hooks and Team MCPs.
- **https://cursor.com/help** (score 1, pricing): The documentation was updated to include several new features, a new AI model (Grok 4.5), a mobile app, and new billing options for iOS, all of which fall under the user's monitoring goal.
- **https://cursor.com/docs/agent/overview** (score 1, deployment): The documentation was updated to include a new 'Mobile' capability for Cloud Agents and removed the 'Semantic search' capability from the Agent tools section.
- **https://cursor.com/docs/agent/agents-window** (score 1, deployment): A new 'Mobile' capability has been added to the Cloud Agents documentation, which directly relates to the goal of tracking agent capabilities and features.
- **https://cursor.com/docs/agent/agent-review** (score 1, deployment): The documentation was updated to include a new 'Mobile' capability for Cloud Agents and a change in the IDE integration settings for Agent Review starting in version 3.11.
- **https://cursor.com/docs/agent/plan-mode** (score 1, deployment): A new documentation section for 'Mobile' has been added under the Cloud Agents category, indicating a new feature or platform capability for Cursor's agents.
- **https://cursor.com/docs/agent/prompting** (score 1, deployment): A new documentation section for 'Mobile' has been added under the Cloud Agents category, indicating a new feature or platform capability for Cursor's agents.
- **https://cursor.com/docs/agent/debug-mode** (score 1, deployment): A new documentation section for 'Mobile' has been added under the Cloud Agents category, indicating a new feature or platform capability for Cursor's agents.
- **https://cursor.com/docs/agent/design-mode** (score 1, deployment): A new documentation section for 'Mobile' has been added under the Cloud Agents category, indicating a new feature or platform capability for Cursor's agents.
- **https://cursor.com/docs/plugins** (score 1, integration): The documentation introduces significant new features regarding Cloud Agents, MCP (Model Context Protocol) server integration, and plugin management. Specifically, it adds a 'Mobile' section for Cloud Agents, introduces 'Default team marketplaces' for sharing MCP servers across the IDE and CLI, and updates plugin installation modes (Default Off, Default On, Required).
- **https://cursor.com/docs/rules** (score 1, deployment): A new 'Mobile' capability or feature has been added to the Cloud Agents section of the documentation. Other changes were ignored as they were technical image URL updates (cache busters).
- **https://cursor.com/docs/skills** (score 1, deployment): The documentation was updated to include a new 'Mobile' capability for Cloud Agents and a comprehensive list of 'Built-in Cursor skills' which details new agent capabilities and IDE integrations like /automate, /canvas, and /review.
- **https://cursor.com/docs/subagents** (score 1, deployment): The documentation has been updated to include a new 'Mobile' capability for Cloud Agents, a new 'Model parameters' feature for subagents allowing fine-grained control over speed and reasoning effort, and references to a new model version 'gpt-5.6-sol'.
- **https://cursor.com/docs/hooks** (score 1, deployment): The documentation was updated to include new agent capabilities, specifically adding support for several hooks in Cloud Agents and introducing a new 'Mobile' documentation section. It also details a change in how agents initialize (read-only environments).
- **https://cursor.com/docs/mcp** (score 1, deployment): The documentation has been updated with significant new features regarding Cloud Agents, MCP (Model Context Protocol) integrations, and enterprise deployment options. Specifically, it introduces mobile support for agents, team marketplaces for MCP distribution, and new OAuth redirect configurations for the desktop app.
- **https://cursor.com/docs/cloud-agent** (score 1, deployment): The documentation was updated to include a new native iOS app, expanded agent capabilities with a built-in MCP for diagnostics, and a significantly larger list of supported lifecycle hooks for cloud agents.
- **https://cursor.com/docs/cloud-agent/setup** (score 1, deployment): A new 'Mobile' capability has been added to the Cloud Agents section, and there are functional updates to how pathing and context work within the environment configuration.
- **https://cursor.com/docs/cloud-agent/capabilities** (score 1, integration): The documentation was updated to include a new 'Mobile' section for Cloud Agents and a significant new feature called 'Cursor Cloud MCP'. This new MCP server provides diagnostic capabilities for agents to inspect runs, environments, and transcripts. Additionally, new administrative controls for team-wide MCP configuration and marketplace integration were added.
- **https://cursor.com/docs/cloud-agent/choose-runtime** (score 1, deployment): A new 'Mobile' capability or feature has been added to the Cloud Agents section of the documentation.
- **https://cursor.com/docs/cloud-agent/my-machines** (score 1, deployment): A new 'Mobile' capability or feature has been added to the Cloud Agents section of the documentation.
- **https://cursor.com/docs/cloud-agent/self-hosted-pool** (score 1, deployment): A new documentation section for 'Mobile' has been added under the Cloud Agents category, indicating a new feature or platform capability for Cursor's agents.
- **https://cursor.com/docs/cloud-agent/self-hosted-cloud-run** (score 1, deployment): A new documentation section for 'Mobile' has been added under the Cloud Agents category, indicating a new feature or platform capability for Cursor's agents.
- **https://cursor.com/docs/bugbot** (score 1, deployment): The documentation has been updated with significant new features and integration details, including a new Bugbot API for enterprise teams, a new 'Mobile' section for Cloud Agents, and expanded support for Bitbucket Data Center.
- **https://cursor.com/docs/cloud-agent/automations** (score 1, deployment): The documentation was updated to include Bitbucket Cloud support for Cloud Agent automations and a new 'Mobile' documentation section. It also reorganized and expanded the list of supported source control triggers for GitHub and GitLab.
- **https://cursor.com/docs/cloud-agent/best-practices** (score 1, integration): The documentation was updated to include a new 'Mobile' capability for Cloud Agents and a significant new section regarding 'Rules' (User, Team, and Repo levels) that agents can now follow to enforce conventions.
- **https://cursor.com/docs/security-agents** (score 1, deployment): A new 'Mobile' capability or feature has been added to the Cloud Agents section of the documentation, which falls directly under the goal of tracking agent capabilities and features.
- **https://cursor.com/docs/approval-agents** (score 1, deployment): A new 'Mobile' capability or feature has been added to the Cloud Agents section of the documentation.
- **https://cursor.com/docs/cloud-agent/security-network** (score 1, deployment): The documentation was updated to include a new 'Mobile' capability for Cloud Agents and a significant restriction regarding 'Privacy Mode (Legacy)' support for agent features.
- **https://cursor.com/docs/cloud-agent/settings** (score 1, deployment): A new 'Mobile' capability or feature has been added to the Cloud Agents section of the documentation.
- **https://cursor.com/docs/cloud-agent/api/endpoints** (score 1, pricing): The Admin API documentation has been updated to include new endpoints for managing organization members and viewing organization-level usage and spending data. These are new features for team/organization management.
- **https://cursor.com/docs/integrations/slack** (score 1, product): The documentation for Cloud Agents and Slack integration has been significantly updated with new capabilities, including a new 'Mobile' section and several new command options for triggering agents on specific machines or self-hosted pools.
- **https://cursor.com/docs/integrations/microsoft-teams** (score 1, deployment): A new documentation section for 'Mobile' has been added under the Cloud Agents category, indicating a new feature or platform capability for Cursor's agents.
- **https://cursor.com/docs/integrations/jira** (score 1, product): The documentation was updated to include a new 'Mobile' capability for Cloud Agents and a new model version ('gpt-5.6-sol') for agent commands, both of which fall under the user's goal of tracking agent capabilities and features.
- **https://cursor.com/docs/integrations/linear** (score 1, deployment): A new 'Mobile' capability/feature has been added to the Cloud Agents documentation section. Other changes are just technical image hash updates which are ignored.
- **https://cursor.com/docs/integrations/notion** (score 1, deployment): A new documentation section for 'Mobile' has been added under the Cloud Agents category, indicating a new feature or platform capability for Cursor's agents.
- **https://cursor.com/docs/integrations/github** (score 1, deployment): A new documentation section for 'Mobile' has been added under the Cloud Agents category, indicating a new feature or platform capability for Cursor's agents.
- **https://cursor.com/docs/integrations/gitlab** (score 1, deployment): A new documentation section for 'Mobile' has been added under the Cloud Agents category, indicating a new feature or platform capability for Cursor's agents.
- **https://cursor.com/docs/integrations/azure-devops** (score 1, deployment): The documentation was updated to include a new 'Mobile' capability for Cloud Agents and detailed feature support/limitations for the Azure DevOps integration, which directly relates to the goal of tracking features, agent capabilities, and integrations.
- **https://cursor.com/docs/reference/sandbox** (score 1, deployment): A new documentation section for 'Mobile' has been added under the Cloud Agents category, indicating a new feature or platform capability for Cursor's agents.
- **https://cursor.com/docs/cloud-agent/api/v0** (score 1, pricing): The Admin API documentation has been updated to include new endpoints for managing organization members and viewing organization-level usage and spending data. These are new features for team/organization management.
- **https://cursor.com/docs/integrations/bitbucket** (score 1, deployment): The documentation has been updated to include support for Bitbucket Data Center (previously unsupported) and new deployment/networking options for Enterprise customers, such as AWS PrivateLink and Cloudflare Tunnels. Additionally, a new 'Mobile' capability for Cloud Agents was added to the navigation.
- **https://cursor.com/docs/integrations/jetbrains** (score 1, deployment): The documentation was updated to include a new 'Mobile' capability for Cloud Agents and removed 'Codebase understanding' and 'semantic search' from the JetBrains IDE integration features.
- **https://cursor.com/docs/integrations/xcode** (score 1, deployment): A new documentation section for 'Mobile' has been added under the Cloud Agents category, indicating a new feature or platform capability for Cursor's agents.
- **https://cursor.com/docs/reference/deeplinks** (score 1, deployment): A new documentation section for 'Mobile' has been added under the Cloud Agents category, indicating a new feature or platform capability for Cursor's agents.
- **https://cursor.com/docs/sdk/typescript** (score 1, deployment): The documentation has been updated with significant new agent capabilities and SDK features, including per-run environment variables for cloud agents, token usage tracking, and a new mobile documentation section.
- **https://cursor.com/docs/sdk/python** (score 1, deployment): The documentation was updated with significant new features for the Cursor SDK and Cloud Agents, including a new 'Mobile' section, token usage tracking capabilities, and per-run environment variables for cloud agents.
- **https://cursor.com/docs/cli/overview** (score 1, deployment): A new 'Mobile' capability or feature has been added to the Cloud Agents section of the documentation.
- **https://cursor.com/docs/cli/installation** (score 1, deployment): A new documentation section for 'Mobile' has been added under the Cloud Agents category, indicating a new feature or platform capability for Cursor's agents.
- **https://cursor.com/docs/cli/using** (score 1, deployment): A new documentation section for 'Mobile' has been added under the Cloud Agents category, indicating a new feature or platform capability for Cursor's agents.
- **https://cursor.com/docs/cli/changelog** (score 1, product): The documentation was updated with two major release changelogs (June 29 and July 6, 2026) covering new agent capabilities, model routing features, CLI integrations, and a new 'Mobile' documentation section for Cloud Agents.
- **https://cursor.com/docs/cli/shell-mode** (score 1, deployment): A new documentation section for 'Mobile' has been added under the Cloud Agents category, indicating a new feature or platform capability for Cursor's agents.
- **https://cursor.com/docs/cli/acp** (score 1, deployment): A new documentation section for 'Mobile' has been added under the Cloud Agents category, indicating a new feature or platform capability for Cursor's agents.
- **https://cursor.com/docs/cli/headless** (score 1, deployment): A new 'Mobile' capability or feature has been added to the Cloud Agents section of the documentation.
- **https://cursor.com/learn/understanding-your-codebase** (score 1, product): The documentation for the 'Semantic search' feature has been significantly revised and renamed to 'Search by meaning'. A large section explaining the technical implementation (vector embeddings), research statistics on accuracy, and the rationale for combining search tools was removed and replaced with a more concise description of how the Agent integrates these tools.
- **https://cursor.com/docs/models-and-pricing** (score 1, pricing): The documentation reflects significant changes to supported AI models, pricing structures, and agent capabilities. Specifically, it introduces new GPT-5.6 variants, Grok 4.5, and Claude Sonnet 5, while removing older versions. It also rebrands the 'Auto + Composer' usage pool to 'First-party models' and adds a new 'Mobile' capability for Cloud Agents.
- **https://cursor.com/docs/models/claude-fable-5** (score 1, product): The documentation has been updated with significant changes to supported AI models, agent capabilities, and model availability, which directly aligns with the monitoring goal.
- **https://cursor.com/docs/models/claude-opus-4-8** (score 1, deployment): The documentation has been updated with new AI models (GPT-5.6 variants and Grok 4.5), a new 'Mobile' capability for Cloud Agents, and the removal of 'Semantic search' from the Opus 4.8 agent toolset.
- **https://cursor.com/docs/models/cursor-composer-2-5** (score 1, pricing): The documentation reflects significant updates to supported AI models, agent capabilities (mobile support), and pricing structures for first-party models.
- **https://cursor.com/docs/models/gemini-3-1-pro** (score 1, deployment): The documentation has been updated with new AI models (GPT-5.6 variants and Grok 4.5), a new 'Mobile' capability for Cloud Agents, and the removal of 'Semantic search' from Gemini 3.1 Pro's supported agent tools.
- **https://cursor.com/docs/models/gemini-3-5-flash** (score 1, deployment): The documentation reflects significant updates to supported AI models, the addition of a new mobile capability for Cloud Agents, and a change in the feature set for Gemini 3.5 Flash.
- **https://cursor.com/downloads** (score 1, product): The page has been updated with significant new features including 'Composer 2.5', a new 'Terminal' agent interface, and 'Web' agent capabilities. The version has also been updated from 3.9 to 3.11, with new deployment options for Windows and Linux.
- **https://cursor.com/docs/cloud-agent/api/webhooks** (score 1, pricing): The Admin API documentation has been updated to include new endpoints for managing organization members and viewing organization-level usage and spending data. These are new features for team/organization management.
- **https://cursor.com/docs/account/teams/admin-api** (score 1, pricing): The documentation for the Admin API has been updated with new endpoints for organization management and significant clarifications regarding how 'Cursor Token Fees' are applied to specific models (Composer 2.5, Grok 4.5) and request types. This directly impacts the pricing and feature tracking goal.
- **https://cursor.com/docs/account/organizations/organization-admin-api** (score 1, pricing): The Cursor Admin API documentation has been significantly expanded with new organization-level features, including a new read-only API scope, a new endpoint for listing organization members, and new endpoints for retrieving daily usage and spending data at the organization level. The membership sync functionality was also updated to support multi-team assignments.
- **https://cursor.com/docs/account/teams/analytics-api** (score 1, pricing): The documentation was updated to include a new 'Bugbot review analytics' API endpoint, which provides detailed data on agent capabilities (Bugbot) including billed costs and finding resolutions. New organization-level admin API links were also added.
- **https://cursor.com/docs/account/teams/ai-code-tracking-api** (score 1, pricing): The Admin API documentation has been updated to include new endpoints for managing organization members and viewing organization-level usage and spending data. These are new features for team/organization management.
- **https://cursor.com/docs/account/enterprise/service-accounts** (score 1, deployment): The documentation was updated to include a new 'Mobile' capability for Cloud Agents and reflects a change in the navigation path for managing Service Accounts/API Keys.
- **https://cursor.com/docs/enterprise/organization-groups** (score 1, integration): The documentation was updated to include a new 'Mobile' capability for Cloud Agents and a new 'Team marketplace access' feature for Enterprise Organization Groups, which falls under the user's interest in agent capabilities and IDE integrations/features.
- **https://cursor.com/docs/agent/tools/browser** (score 1, deployment): A new 'Mobile' capability or feature has been added to the Cloud Agents section of the documentation. Other changes were ignored as they were mechanical image URL updates.
- **https://cursor.com/docs/configuration/worktrees** (score 1, deployment): The documentation was updated to include a new 'Mobile' capability for Cloud Agents, which falls directly under the user's goal of tracking agent capabilities and features. Other changes were minor terminology updates (changing 'Editor Window' to 'IDE').
- **https://cursor.com/docs/account/teams/scim** (score 1, deployment): A new 'Mobile' capability or feature has been added to the Cloud Agents section of the documentation.
- **https://cursor.com/docs/enterprise** (score 1, deployment): A new documentation section for 'Mobile' has been added under the Cloud Agents category, indicating a new feature or platform capability for Cursor's agents.
- **https://cursor.com/docs/enterprise/baa** (score 1, deployment): The documentation was updated to include 'Mobile' and 'Cursor for iOS' as a new feature and deployment option for Cloud Agents.
- **https://cursor.com/docs/enterprise/private-connectivity** (score 1, integration): The documentation was updated to include a new 'Mobile' capability for Cloud Agents and a new integration for Bitbucket Data Center, both of which fall under the user's interest in features, agent capabilities, and IDE integrations.
- **New page**: https://cursor.com/docs/cloud-agent/mobile
- **New page**: https://cursor.com/docs/bugbot/legacy-pricing
- **New page**: https://cursor.com/docs/models/claude-sonnet-5
- **New page**: https://cursor.com/docs/models/gpt-5-6-luna
- **New page**: https://cursor.com/docs/models/gpt-5-6-sol
- **New page**: https://cursor.com/docs/models/gpt-5-6-terra
- **New page**: https://cursor.com/docs/models/grok-4-5
- **New page**: https://cursor.com/docs/mcp/install-links
- **New page**: https://cursor.com/docs/reference/plugins
- **New page**: https://cursor.com/docs/reference/third-party-hooks
- **New page**: https://cursor.com/docs/extension-api
- **New page**: https://cursor.com/docs/cloud-agent/self-hosted-k8s
- **New page**: https://cursor.com/docs-static/cloud-agents-openapi-v0.yaml
- **New page**: https://cursor.com/docs/reference/permissions
- **New page**: https://cursor.com/docs/cli/mcp
- **Removed page**: https://cursor.com/docs/models/claude-4-6-sonnet
- **Removed page**: https://cursor.com/docs/models/gpt-5-3-codex
- **Removed page**: https://cursor.com/docs/models/grok-build-0-1
- **Removed page**: https://cursor.com/docs/enterprise/model-and-integration-management
- **Removed page**: https://cursor.com/docs/models/gpt-5-5
- **Removed page**: https://cursor.com/docs/account/enterprise/cyber-safeguards
- **Removed page**: https://cursor.com/docs/enterprise/pooled-usage
- **Removed page**: https://cursor.com/docs/account/enterprise/billing-groups
- **Removed page**: https://cursor.com/docs/enterprise/compliance-and-monitoring
- **Removed page**: https://cursor.com/docs/enterprise/endpoint-security
- **Removed page**: https://cursor.com/docs/agent/tools/search
- **Removed page**: https://cursor.com/docs/enterprise/organizations
- **Removed page**: https://cursor.com/docs/enterprise/network-configuration
- **Removed page**: https://cursor.com/docs/enterprise/privacy-and-data-governance
- **Removed page**: https://cursor.com/docs/enterprise/llm-safety-and-controls

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
