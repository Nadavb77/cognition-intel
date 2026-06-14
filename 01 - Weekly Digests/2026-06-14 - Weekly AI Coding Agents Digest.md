# Weekly AI Coding Agents Digest

**Date:** 2026-06-14

---

## Executive Summary

Minor changes were detected but none scored high enough (score ≥ 3) to warrant summarization. Details below.

## Sources Checked

- **devin-docs**: checked, minor changes ignored
- **cognition-blog**: checked, minor changes ignored
- **devin-release-notes**: checked, minor changes ignored
- **claude-code-docs**: no completed checks yet
- **github-copilot-docs**: checked, minor changes ignored
- **github-copilot-coding-agent**: checked, minor changes ignored
- **cursor-docs**: no completed checks yet
- **factory-docs**: checked, minor changes ignored
- **coderabbit-docs**: checked, minor changes ignored

## System Status

- 7/9 sources checked successfully
- 0 failed sources
- No secrets printed
- Digest generated successfully

## Minor Changes Ignored

### devin-docs

- **https://docs.devin.ai/onboard-devin/knowledge-onboarding** (score 2, security): The changes are limited to minor punctuation fixes, specifically adding a comma and replacing a comma with a semicolon. The monitor goal explicitly requests to ignore minor wording or formatting fixes.
- **https://docs.devin.ai/desktop/devin-desktop-faq** (score 1, product): A new section was added to the documentation explaining the replacement of the 'surf' CLI command with 'devin-desktop', including installation and usage instructions. This is a relevant integration and deployment update.
- **https://docs.devin.ai/cli/extensibility/mcp/configuration** (score 1, integration): The documentation was updated to include new configuration fields (`oauthClientId` and `oauthClientSecret`) and a new section on 'Pre-registered OAuth clients'. This represents a functional update to how MCP integrations are configured and authenticated, which falls under the user's goal of tracking integration and API changes.
- **https://docs.devin.ai/desktop/accounts/usage** (score 1, pricing): The only change is a spelling correction from 'individial' to 'individual'. The monitor goal explicitly states to ignore minor wording or formatting fixes.
- **https://docs.devin.ai/desktop/changelog** (score 1, pricing): A new version (v3.1.7) was added to the documentation changelog, introducing several new features and integration updates, including a new Agent/Editor switch, the renaming of 'Devin CLI' to 'Devin Local', and support for '.devinignore' files. Minor hyphenation fixes in older version entries were ignored as noise.
- **New page**: https://docs.devin.ai/api-reference/v3/notes/put-enterprise-knowledge-notes-note-id
- **New page**: https://docs.devin.ai/api-reference/v3/secrets/post-organizations-secrets
- **New page**: https://docs.devin.ai/api-reference/v3/snapshot-setup/get-organizations-build-logs
- **New page**: https://docs.devin.ai/api-reference/v3/notes/get-organizations-knowledge-note
- **New page**: https://docs.devin.ai/work-with-devin/slash-commands#/implement
- **New page**: https://docs.devin.ai/api-reference/v3/idp-groups/post-organizations-members-idp-groups
- **New page**: https://docs.devin.ai/api-reference/v3/notes/delete-enterprise-knowledge-notes-note-id
- **New page**: https://docs.devin.ai/api-reference/v3/users/patch-members-users
- **New page**: https://docs.devin.ai/cli/enterprise/controls
- **New page**: https://docs.devin.ai/use-cases/examples/cobol-modernization
- **New page**: https://docs.devin.ai/api-reference/v3/idp-groups/patch-members-idp-groups
- **New page**: https://docs.devin.ai/cli/reference/terminal-compatibility
- **New page**: https://docs.devin.ai/onboard-devin/environment/migration
- **New page**: https://docs.devin.ai/api-reference/v3/snapshot-setup/post-organizations-build-pin
- **New page**: https://docs.devin.ai/api-reference/v3/sessions/get-enterprise-session-tags
- **New page**: https://docs.devin.ai/api-reference/v3/tags/get-enterprise-organizations-default-tag
- **New page**: https://docs.devin.ai/api-reference/v3/snapshot-setup/post-organizations-build-cancel
- **New page**: https://docs.devin.ai/api-reference/v3/users/list-organization-idp-users
- **New page**: https://docs.devin.ai/api-reference/v3/snapshot-setup/post-enterprise-blueprints
- **New page**: https://docs.devin.ai/api-reference/v3/repositories/put-organizations-bulk-index-repositories
- **New page**: https://docs.devin.ai/cli/reference/configuration/config-file.md
- **New page**: https://docs.devin.ai/api-reference/v3/sessions/post-organizations-session-insights-generate
- **New page**: https://docs.devin.ai/api-reference/v3/sessions/get-organizations-session
- **New page**: https://docs.devin.ai/use-cases/gallery/build-internal-tool
- **New page**: https://docs.devin.ai/api-reference/v3/metrics/metrics-searches
- **New page**: https://docs.devin.ai/windsurf/plugins/cascade/models
- **New page**: https://docs.devin.ai/api-reference/v2/organizations/organization-connections
- **New page**: https://docs.devin.ai/api-reference/v3/sessions/put-organizations-session-tags
- **New page**: https://docs.devin.ai/use-cases/tutorials/code-coverage
- **New page**: https://docs.devin.ai/api-reference/v3/sessions/post-enterprise-session-tags
- **New page**: https://docs.devin.ai/api-reference/v3/repositories/list-organizations-indexed-repositories
- **New page**: https://docs.devin.ai/api-reference/v3/organizations/get-enterprise-organization
- **New page**: https://docs.devin.ai/api-reference/v2/organizations/organization-members
- **New page**: https://docs.devin.ai/api-reference/v3/service-users/post-enterprise-service-user-api-keys
- **New page**: https://docs.devin.ai/api-reference/v3/consumption/organizations-consumption-daily-service-users
- **New page**: https://docs.devin.ai/api-reference/v3/metrics/metrics-wau
- **New page**: https://docs.devin.ai/product-guides/session-insights
- **New page**: https://docs.devin.ai/api-reference/v3/metrics/organizations-metrics-usage
- **New page**: https://docs.devin.ai/api-reference/v3/sessions/post-enterprise-sessions-messages
- **New page**: https://docs.devin.ai/api-reference/v3/queue/enterprise-queue
- **New page**: https://docs.devin.ai/cli/reference/configuration/read-config-from
- **New page**: https://docs.devin.ai/api-reference/v3/sessions/enterprise-sessions
- **New page**: https://docs.devin.ai/api-reference/v3/service-users/rotate-enterprise-service-user-api-key
- **New page**: https://docs.devin.ai/api-reference/v3/snapshot-setup/patch-organizations-blueprint
- **New page**: https://docs.devin.ai/api-reference/v3/consumption/consumption-daily-organizations
- **New page**: https://docs.devin.ai/api-reference/v3/snapshot-setup/delete-organizations-blueprint-file
- **New page**: https://docs.devin.ai/api-reference/v3/users/get-organization-user
- **New page**: https://docs.devin.ai/api-reference/v3/sessions/post-organizations-sessions
- **New page**: https://docs.devin.ai/api-reference/v3/git-connections/get-git-providers-connection-repositories
- **New page**: https://docs.devin.ai/enterprise/environment-management/best-practices
- **New page**: https://docs.devin.ai/api-reference/v3/service-users/post-members-service-users
- **New page**: https://docs.devin.ai/use-cases/gallery
- **New page**: https://docs.devin.ai/api-reference/v3/service-users/get-enterprise-service-user-api-keys
- **New page**: https://docs.devin.ai/api-reference/v3/organizations/delete-organizations
- **New page**: https://docs.devin.ai/api-reference/v3/users/organizations-members-idp-users
- **New page**: https://docs.devin.ai/api-reference/v3/consumption/organizations-consumption-daily
- **New page**: https://docs.devin.ai/cli/acp/jetbrains
- **New page**: https://docs.devin.ai/api-reference/v3/sessions/post-organizations-sessions-archive
- **New page**: https://docs.devin.ai/product-guides/scheduled-sessions
- **New page**: https://docs.devin.ai/api-reference/v2/members/user-organizations
- **New page**: https://docs.devin.ai/cli/adaptive
- **New page**: https://docs.devin.ai/api-reference/v2/sessions/list-enterprise-sessions
- **New page**: https://docs.devin.ai/use-cases/gallery/batch-parallel-research
- **New page**: https://docs.devin.ai/api-reference/v3/ip-access-list/replace-ip-access-list
- **New page**: https://docs.devin.ai/cli/models.md
- **New page**: https://docs.devin.ai/api-reference/v3/pr-reviews/post-organizations-pr-reviews
- **New page**: https://docs.devin.ai/api-reference/v3/tags/delete-organizations-tags-tag
- **New page**: https://docs.devin.ai
- **New page**: https://docs.devin.ai/api-reference/v2/organizations/update-organization-member-roles
- **New page**: https://docs.devin.ai/api-reference/v2/user-usage/get-user-usage-analysis-beta
- **New page**: https://docs.devin.ai/api-reference/v3/playbooks/get-organizations-playbook
- **New page**: https://docs.devin.ai/cli/essential-commands
- **New page**: https://docs.devin.ai/integrations/self-hosted-scm-artifacts
- **New page**: https://docs.devin.ai/enterprise/security-access/sso/azure
- **New page**: https://docs.devin.ai/enterprise/integrations/azure-devops
- **New page**: https://docs.devin.ai/api-reference/v3/git-permissions/delete-organizations-git-providers-permissions
- **New page**: https://docs.devin.ai/api-reference/v3/tags/organizations-tags
- **New page**: https://docs.devin.ai/api-reference/v2/organizations/delete-organization-permission
- **New page**: https://docs.devin.ai/integrations/bitbucket
- **New page**: https://docs.devin.ai/api-reference/v3/consumption/organizations-consumption-daily-sessions
- **New page**: https://docs.devin.ai/api-reference/v2/org-group-limits/update-org-group-limits
- **New page**: https://docs.devin.ai/api-reference/v3/service-users/delete-organizations-members-service-users
- **New page**: https://docs.devin.ai/api-reference/v3/schedules/patch-organizations-schedule
- **New page**: https://docs.devin.ai/use-cases/web-scraping
- **New page**: https://docs.devin.ai/api-reference/v3/sessions/post-enterprise-session-insights-generate
- **Removed page**: https://docs.devin.ai/api-reference/v2/api-keys/provision-service-key
- **Removed page**: https://docs.devin.ai/api-reference/v2/api-keys/list-enterprise-api-keys
- **Removed page**: https://docs.devin.ai/api-reference/v1/sessions/update-session-tags
- **Removed page**: https://docs.devin.ai/api-reference/v1/sessions/terminate-a-session
- **Removed page**: https://docs.devin.ai/api-reference/v1/sessions/retrieve-details-about-an-existing-session
- **Removed page**: https://docs.devin.ai/api-reference/v1/sessions/list-sessions
- **Removed page**: https://docs.devin.ai/api-reference/v1/secrets/list-secrets
- **Removed page**: https://docs.devin.ai/api-reference/v1/secrets/delete-secret
- **Removed page**: https://docs.devin.ai/api-reference/v1/secrets/create-secret
- **Removed page**: https://docs.devin.ai/api-reference/v1/playbooks/update-playbook
- **Removed page**: https://docs.devin.ai/api-reference/v1/playbooks/delete-playbook
- **Removed page**: https://docs.devin.ai/api-reference/v1/playbooks/get-playbook
- **Removed page**: https://docs.devin.ai/api-reference/v1/playbooks/create-playbook
- **Removed page**: https://docs.devin.ai/api-reference/v1/knowledge/delete-knowledge
- **Removed page**: https://docs.devin.ai/api-reference/v1/overview
- **Removed page**: https://docs.devin.ai/api-reference/v1/knowledge/list-knowledge
- **Removed page**: https://docs.devin.ai/api-reference/v1/knowledge/create-knowledge
- **Removed page**: https://docs.devin.ai/api-reference/personal-access-tokens
- **Removed page**: https://docs.devin.ai/api-reference/v1/attachments/upload-files-for-devin-to-work-with
- **Removed page**: https://docs.devin.ai/api-reference/v1/attachments/download-attachment-files
- **Removed page**: https://docs.devin.ai/api-reference/release-notes
- **Removed page**: https://docs.devin.ai/api-reference/getting-started/migration-guide
- **Removed page**: https://docs.devin.ai/api-reference/getting-started/teams-quickstart
- **Removed page**: https://docs.devin.ai/api-reference/getting-started/enterprise-quickstart
- **Removed page**: https://docs.devin.ai/api-reference/common-flows
- **Removed page**: https://docs.devin.ai/admin/common-issues
- **Removed page**: https://docs.devin.ai/admin/billing/enterprise
- **Removed page**: https://docs.devin.ai/admin/billing/usage
- **Removed page**: https://docs.devin.ai/admin/billing/self-serve
- **Removed page**: https://docs.devin.ai/onboard-devin/agents-md
- **Removed page**: https://docs.devin.ai/release-notes/2024
- **Removed page**: https://docs.devin.ai/release-notes/overview
- **Removed page**: https://docs.devin.ai/integrations/slack
- **Removed page**: https://docs.devin.ai/api-reference/v1/sessions/send-a-message-to-an-existing-devin-session
- **Removed page**: https://docs.devin.ai/api-reference/v2/consumption/sessions-metrics
- **Removed page**: https://docs.devin.ai/ja/api-reference/v2/members/list-roles
- **Removed page**: https://docs.devin.ai/api-reference/v2/consumption/usage-metrics
- **Removed page**: https://docs.devin.ai/api-reference/v2/consumption/searches-metrics
- **Removed page**: https://docs.devin.ai/desktop/devin-local
- **Removed page**: https://docs.devin.ai/api-reference/v2/consumption/pr-metrics
- **Removed page**: https://docs.devin.ai/api-reference/v2/consumption/daily-consumption
- **Removed page**: https://docs.devin.ai/product-guides/skills
- **Removed page**: https://docs.devin.ai/api-reference/v2/audit-logs
- **Removed page**: https://docs.devin.ai/api-reference/v2/api-keys/revoke-enterprise-api-key
- **Removed page**: https://docs.devin.ai/cli/extensibility/index
- **Removed page**: https://docs.devin.ai/zh/get-started/devin-intro
- **Removed page**: https://docs.devin.ai/desktop/getting-started
- **Removed page**: https://docs.devin.ai/llms.txt
- **Removed page**: https://docs.devin.ai/desktop/troubleshooting/windsurf-common-issues
- **Removed page**: https://docs.devin.ai/zh/onboard-devin/repo-setup
- **Removed page**: https://docs.devin.ai/zh/desktop/devin-desktop-faq
- **Removed page**: https://docs.devin.ai/api-reference/overview
- **Removed page**: https://docs.devin.ai/enterprise/security-access/security/enterprise-security
- **Removed page**: https://docs.devin.ai/desktop/models
- **Removed page**: https://docs.devin.ai/work-with-devin/deepwiki-mcp
- **Removed page**: https://docs.devin.ai/desktop/adaptive.md
- **Removed page**: https://docs.devin.ai/onboard-devin/index-repo
- **Removed page**: https://docs.devin.ai/cli
- **Removed page**: https://docs.devin.ai/desktop/releases
- **Removed page**: https://docs.devin.ai/windsurf/plugins/cascade/workflows
- **Removed page**: https://docs.devin.ai/cli/models
- **Removed page**: https://docs.devin.ai/admin/security
- **Removed page**: https://docs.devin.ai/release-notes/2026
- **Removed page**: https://docs.devin.ai/product-guides/creating-playbooks
- **Removed page**: https://docs.devin.ai/cli/reference/configuration/config-file
- **Removed page**: https://docs.devin.ai/essential-guidelines/instructing-devin-effectively
- **Removed page**: https://docs.devin.ai/desktop/acp
- **Removed page**: https://docs.devin.ai/use-cases/best-practices
- **Removed page**: https://docs.devin.ai/desktop/cascade/workflows
- **Removed page**: https://docs.devin.ai/work-with-devin/devin-mcp
- **Removed page**: https://docs.devin.ai/windsurf/plugins/getting-started
- **Removed page**: https://docs.devin.ai/onboard-devin/environment
- **Removed page**: https://docs.devin.ai/work-with-devin/ask-devin
- **Removed page**: https://docs.devin.ai/cli/subagents
- **Removed page**: https://docs.devin.ai/enterprise/getting-started/get-started
- **Removed page**: https://docs.devin.ai/work-with-devin/interactive-planning
- **Removed page**: https://docs.devin.ai/get-started/devin-intro
- **Removed page**: https://docs.devin.ai/desktop/cascade/memories
- **Removed page**: https://docs.devin.ai/cli/extensibility/skills/overview
- **Removed page**: https://docs.devin.ai/work-with-devin/deepwiki
- **Removed page**: https://docs.devin.ai/essential-guidelines/when-to-use-devin
- **Removed page**: https://docs.devin.ai/desktop/changelog-next
- **Removed page**: https://docs.devin.ai/work-with-devin/advanced-capabilities
- **Removed page**: https://docs.devin.ai/product-guides/knowledge
- **Removed page**: https://docs.devin.ai/product-guides/using-playbooks

### cognition-blog

- **https://cognition.ai/blog** (score 1, product): A new blog post was published and an existing product announcement was renamed, both of which align with the goal of tracking new posts and significant updates regarding product announcements.

### devin-release-notes

- **https://docs.devin.ai/changelog** (score 2, integration): The change involves the removal of a suggested link to a changelog from a 'Page Not Found' error page. This does not constitute a new release note, feature, bug fix, or changelog entry as requested by the monitor goal.

### github-copilot-docs

- **https://docs.github.com/en/copilot** (score 1, product): The only change detected is an update to the total document count from 405 to 407. This is a metadata counter tick and does not provide any information about the content of the documents, agent features, or other specific topics requested in the monitor goal.
- **https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/create-custom-agents** (score 1, product): The documentation updated the deployment process for enterprise-level custom agents, specifying that they are created in a designated organization's repository to be available across the entire enterprise. This directly relates to the goal of tracking enterprise deployment options and agent features.
- **https://docs.github.com/en/copilot/how-tos/copilot-cli/use-copilot-cli/overview** (score 1, product): A new section was added to the Copilot CLI documentation describing the '/settings' slash command, which allows users to interactively or programmatically configure CLI settings. This constitutes a functional update to the Copilot integration and its capabilities.
- **https://docs.github.com/en/copilot/reference/ai-models/supported-models** (score 1, product): The documentation was updated to include a new AI model, 'Claude Fable 5', and detailed its enterprise deployment requirements and data retention policies. Additionally, the main supported models table was modified to remove specific columns for 'Agent mode', 'Ask mode', and 'Edit mode', which directly relates to the goal of tracking agent features and integration updates.
- **https://docs.github.com/en/copilot/reference/copilot-billing/models-and-pricing** (score 1, pricing): The documentation was updated to include pricing and availability information for a new model, Claude Fable 5. This directly relates to the user's goal of tracking pricing and integration updates.
- **https://docs.github.com/en/copilot/concepts/context/mcp** (score 1, product): The documentation was updated to include the GitHub Copilot app as a new surface that supports Model Context Protocol (MCP) integrations. This is a significant integration update and relates to how Copilot agents can be extended.
- **https://docs.github.com/en/copilot/reference/copilot-billing/request-based-billing-legacy/monitor-premium-requests** (score 1, pricing): The documentation removed a specific notice regarding upcoming tighter usage limits for Copilot Pro, Copilot Pro+, and student plans. This is a significant change to plan-related constraints and capabilities.
- **https://docs.github.com/en/copilot/reference/ai-models/model-comparison** (score 1, product): A new model, Claude Fable 5, was added to the documentation. Its capabilities include 'autonomous coding' and 'parallel tool batching', which directly relate to the goal of tracking coding agent capabilities and integration updates.
- **https://docs.github.com/en/copilot/concepts/agents/github-copilot-app** (score 1, integration): The documentation was updated to reflect changes in access for Free users (removing the waitlist) and updated the description of agent customization features to include global instructions while removing mentions of extensions and plugins.
- **https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills** (score 1, product): The documentation was updated to include 'the GitHub Copilot app' as a supported platform for Agent skills, which is a relevant integration and agent feature update.
- **https://docs.github.com/en/copilot/concepts/agents/about-third-party-coding-agents** (score 1, product): A new section titled 'Security validation' was added to the documentation for third-party coding agents. This section details how GitHub scans agent-generated code for security issues using CodeQL, secret scanning, and dependency checks, which directly relates to the goal of tracking coding agent capabilities.
- **https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-config-dir-reference** (score 1, product): The documentation has been updated with new agent features (proactive rubber-duck subagent prompting) and new CLI integration settings (tab management and a new /settings command).
- **https://docs.github.com/en/copilot/tutorials/customize-code-review** (score 1, product): The documentation for Copilot code review was updated to remove a specific 4,000-character limit for custom instruction files. This represents a change in the documented capabilities and constraints of the coding agent features.
- **New page**: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/copilot-memory
- **New page**: https://docs.github.com/en/copilot/get-started/enterprise-ai-governance
- **New page**: https://docs.github.com/en/copilot/how-tos/copilot-on-github/use-copilot-agents/manage-and-track-agents
- **New page**: https://docs.github.com/en/copilot/how-tos/copilot-cli/use-copilot-cli/steer-remotely
- **New page**: https://docs.github.com/en/copilot/get-started/what-is-github-copilot
- **New page**: https://docs.github.com/en/copilot/how-tos/copilot-cli/set-up-copilot-cli/authenticate-copilot-cli
- **New page**: https://docs.github.com/en/copilot/how-tos/troubleshoot-copilot/troubleshoot-network-errors
- **New page**: https://docs.github.com/en/copilot/concepts/tools/ai-tools
- **New page**: https://docs.github.com/en/copilot/concepts/agents/agent-apps
- **New page**: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/integrate-cloud-agent-with-linear
- **New page**: https://docs.github.com/en/copilot/responsible-use/chat
- **New page**: https://docs.github.com/en/copilot/concepts/prompting/response-customization
- **New page**: https://docs.github.com/en/copilot/concepts/agents/hooks
- **New page**: https://docs.github.com/en/copilot/tutorials/write-tests?trk=public_post_comment-text
- **New page**: https://docs.github.com/en/copilot/tutorials/vibe-coding
- **New page**: https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-organization/manage-access/grant-access
- **New page**: https://docs.github.com/en/copilot/reference/agentic-audit-log-events
- **New page**: https://docs.github.com/en/copilot/how-tos/provide-context/use-mcp-in-your-ide/extend-copilot-chat-with-mcp
- **New page**: https://docs.github.com/en/copilot/how-tos/chat-with-copilot/chat-in-ide.md
- **New page**: https://docs.github.com/en/copilot/how-tos/administer-copilot/view-code-generation
- **New page**: https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-enterprise/manage-enterprise-policies
- **New page**: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/agent-management
- **New page**: https://docs.github.com/en/copilot/how-tos/provide-context/use-mcp-in-your-ide/use-the-github-mcp-server
- **New page**: https://docs.github.com/en/copilot/how-tos/github-copilot-app/getting-started
- **New page**: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/changing-the-ai-model
- **New page**: https://docs.github.com/en/copilot/how-tos/copilot-cli/administer-copilot-cli-for-your-enterprise
- **New page**: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/use-agent-apps
- **New page**: https://docs.github.com/en/copilot/reference/ai-models/model-hosting
- **New page**: https://docs.github.com/en/copilot/how-tos/copilot-sdk/auth/authenticate
- **New page**: https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-enterprise/manage-access/view-license-usage
- **New page**: https://docs.github.com/en/copilot/reference/copilot-feature-matrix
- **New page**: https://docs.github.com/en/copilot/how-tos
- **New page**: https://docs.github.com/en/copilot/concepts/agents/about-agent-skills
- **New page**: https://docs.github.com/en/copilot/how-tos/configure-personal-settings/configure-in-ide?tool=jetbrains
- **New page**: https://docs.github.com/en/copilot/how-tos/provide-context/use-mcp-in-your-ide
- **New page**: https://docs.github.com/en/copilot/tutorials/customization-library/custom-instructions/your-first-custom-instructions
- **New page**: https://docs.github.com/en/copilot/responsible-use/inline-suggestions
- **New page**: https://docs.github.com/en/copilot/how-tos/copilot-on-github/use-copilot-agents/research-plan-iterate
- **New page**: https://docs.github.com/en/copilot/how-tos/use-copilot-for-common-tasks/use-copilot-in-the-cli
- **New page**: https://docs.github.com/en/copilot/concepts/models/auto-model-selection
- **New page**: https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions
- **New page**: https://docs.github.com/en/copilot/reference/copilot-billing/request-based-billing-legacy/model-multipliers-for-annual-plans
- **New page**: https://docs.github.com/en/copilot/how-tos/copilot-cli/set-up-copilot-cli
- **New page**: https://docs.github.com/en/copilot/concepts/agents/copilot-cli/context-management
- **New page**: https://docs.github.com/en/copilot/concepts/agents/copilot-cli/research
- **New page**: https://docs.github.com/en/copilot/how-tos/chat-with-copilot/chat-in-ide
- **New page**: https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-organization/manage-policies
- **New page**: https://docs.github.com/en/copilot/how-tos/copilot-sdk/auth/byok
- **New page**: https://docs.github.com/en/copilot/reference/copilot-billing/request-based-billing-legacy/copilot-requests
- **New page**: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent
- **Removed page**: https://docs.github.com/en/copilot/how-tos/copilot-on-github/chat-with-copilot/chat-in-github
- **Removed page**: https://docs.github.com/en/copilot/concepts/prompting/response-customization?tool=vscode
- **Removed page**: https://docs.github.com/en/copilot/how-tos/copilot-on-github/set-up-copilot/configure-automatic-review
- **Removed page**: https://docs.github.com/en/copilot/tutorials/explore-a-codebase
- **Removed page**: https://docs.github.com/en/copilot/reference/custom-instructions-support
- **Removed page**: https://docs.github.com/en/copilot/concepts/prompting/response-customization?tool=jetbrains
- **Removed page**: https://docs.github.com/en/copilot/reference/ai-models/supported-models?m=1
- **Removed page**: https://docs.github.com/en/copilot/how-tos/chat-with-copilot/chat-in-ide?tool=vscode
- **Removed page**: https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-programmatic-reference
- **Removed page**: https://docs.github.com/en/copilot/how-tos/copilot-on-github/set-up-copilot/enable-copilot/set-up-for-teachers-and-os-maintainers
- **Removed page**: https://docs.github.com/en/copilot/reference/chat-cheat-sheet
- **Removed page**: https://docs.github.com/en/copilot/how-tos/copilot-cli/use-copilot-cli/manage-pull-requests
- **Removed page**: https://docs.github.com/en/copilot/how-tos/copilot-cli/set-up-copilot-cli/add-lsp-servers
- **Removed page**: https://docs.github.com/en/copilot/concepts/copilot-usage-metrics/copilot-metrics
- **Removed page**: https://docs.github.com/en/copilot/concepts/agents/copilot-cli/fleet
- **Removed page**: https://docs.github.com/en/copilot/tutorials/roll-out-at-scale/drive-downstream-impact/accelerate-pull-requests
- **Removed page**: https://docs.github.com/en/copilot/tutorials/budgets/optimizing-your-budget-configuration
- **Removed page**: https://docs.github.com/en/copilot/how-tos/chat-with-copilot/get-started-with-chat-in-your-ide
- **Removed page**: https://docs.github.com/en/copilot/how-tos/configure-custom-instructions-in-your-ide/add-repository-instructions-in-your-ide?tool=vscode
- **Removed page**: https://docs.github.com/en/copilot/concepts/models/fallback-and-lts-models
- **Removed page**: https://docs.github.com/en/copilot/how-tos/github-copilot-app/managing-issues-and-pull-requests
- **Removed page**: https://docs.github.com/en/copilot/reference/copilot-billing/seat-assignment
- **Removed page**: https://docs.github.com/en/copilot/how-tos/copilot-on-github/set-up-copilot/enable-copilot/set-up-a-dedicated-enterprise-for-copilot-business
- **Removed page**: https://docs.github.com/en/copilot/tutorials/customization-library/prompt-files/your-first-prompt-file
- **Removed page**: https://docs.github.com/en/copilot/tutorials/enhance-agent-mode-with-mcp
- **Removed page**: https://docs.github.com/en/copilot/concepts/agents/copilot-cli/about-custom-agents
- **Removed page**: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/integrate-cloud-agent-with-slack
- **Removed page**: https://docs.github.com/en/copilot/reference/copilot-usage-metrics/reconciling-usage-metrics
- **Removed page**: https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference
- **Removed page**: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/risks-and-mitigations
- **Removed page**: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/create-automations
- **Removed page**: https://docs.github.com/en/copilot/concepts/context/repository-indexing
- **Removed page**: https://docs.github.com/en/copilot/concepts/about-enterprise-accounts-for-copilot-business
- **Removed page**: https://docs.github.com/en/copilot/reference/copilot-billing/models-and-pricing.md
- **Removed page**: https://docs.github.com/en/copilot/concepts/agents/copilot-cli/comparing-cli-features
- **Removed page**: https://docs.github.com/en/copilot/how-tos/copilot-cli/automate-copilot-cli/schedule-prompts
- **Removed page**: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/integrate-cloud-agent-with-jira
- **Removed page**: https://docs.github.com/en/copilot/get-started/quickstart?tool=vscode
- **Removed page**: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/request-a-code-review/use-code-review
- **Removed page**: https://docs.github.com/en/copilot/how-tos/administer-copilot/view-usage-and-adoption
- **Removed page**: https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-enterprise/manage-plan/upgrade-plan
- **Removed page**: https://docs.github.com/en/copilot/reference/copilot-cli-reference/acp-server
- **Removed page**: https://docs.github.com/en/copilot/concepts/models/fedramp-models
- **Removed page**: https://docs.github.com/en/copilot/tutorials/reduce-technical-debt
- **Removed page**: https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/customize-the-agent-firewall
- **Removed page**: https://docs.github.com/en/copilot/concepts/context/spaces
- **Removed page**: https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions?tool=vscode
- **Removed page**: https://docs.github.com/en/copilot/concepts/agents/copilot-cli/autopilot
- **Removed page**: https://docs.github.com/en/copilot/how-tos/administer-copilot/download-activity-report
- **Removed page**: https://docs.github.com/en/copilot/how-tos/copilot-cli/use-copilot-cli/chronicle

### github-copilot-coding-agent

- **https://docs.github.com/copilot/concepts/agents/coding-agent/about-coding-agent** (score 1, product): A new section was added describing a new capability: the ability to share context between Copilot Chat and Copilot cloud agent sessions.

### factory-docs

- **https://docs.factory.ai/api-reference/computers/update-a-computer.md** (score 1, docs-only): The documentation was updated to include a new 'computerSource' property in the component schema. This represents a change in product features and technical capabilities, allowing components to be defined by either a template or a specific computer ID.
- **https://docs.factory.ai/api-reference/computers/create-a-computer.md** (score 1, docs-only): The documentation for the product's configuration schema has been updated to remove the 'scratch' deployment option, rename 'live-computer' to 'computer', and introduce a new 'computerSource' property. These changes represent updates to product features and deployment configurations.
- **https://docs.factory.ai/cli/configuration/mcp** (score 1, deployment): The documentation for MCP server configuration was updated with significant new details regarding OAuth security and deployment. It introduces support for disabling OAuth, Dynamic Client Registration (DCR), and Client ID Metadata Documents (CIMD).
- **https://docs.factory.ai/web/missions.md** (score 1, pricing): The 'Missions' feature is no longer labeled as being in 'Research Preview', indicating a change in the product's feature status or availability.
- **New page**: https://docs.factory.ai/enterprise/service-accounts.md
- **New page**: https://docs.factory.ai/cli/user-guides/specification-mode.md
- **New page**: https://docs.factory.ai/cli/user-guides/implementing-large-features.md
- **New page**: https://docs.factory.ai/api-reference/computers/get-a-computer.md
- **New page**: https://docs.factory.ai/api-reference/organization/list-enterprise-control-change-history.md
- **New page**: https://docs.factory.ai/api-reference/computers/get-a-computer-by-name.md
- **New page**: https://docs.factory.ai/guides/power-user/evaluating-context-compression.md
- **New page**: https://docs.factory.ai/api-reference/organization/set-user-credits-limits.md
- **New page**: https://docs.factory.ai/cli/byok/groq
- **New page**: https://docs.factory.ai/cli/byok/google-gemini.md
- **New page**: https://docs.factory.ai/cli/account/security.md
- **New page**: https://docs.factory.ai/api-reference/sessions/list-sessions.md
- **New page**: https://docs.factory.ai/cli/features/droid-control
- **New page**: https://docs.factory.ai/guides/power-user/memory-management.md
- **New page**: https://docs.factory.ai/api-reference/service-accounts/create-a-service-account-api-key.md
- **New page**: https://docs.factory.ai/cli/features/wiki/overview
- **New page**: https://docs.factory.ai/api-reference/automations/list-ci-repository-owners.md
- **New page**: https://docs.factory.ai/cli/byok/ollama.md
- **New page**: https://docs.factory.ai/api-reference/sessions/add-a-message-to-a-session.md
- **New page**: https://docs.factory.ai/guides/building/droid-vps-setup.md
- **New page**: https://docs.factory.ai/api-reference/sessions/interrupt-a-session.md
- **New page**: https://docs.factory.ai/cli/features/droid-computers-byom.md
- **New page**: https://docs.factory.ai/cli/byok/baseten
- **New page**: https://docs.factory.ai/api-reference/computers/delete-a-computer.md
- **New page**: https://docs.factory.ai/guides/hooks/testing-automation
- **New page**: https://docs.factory.ai/guides/building/droid-vps-setup
- **New page**: https://docs.factory.ai/cli/byok/google-gemini
- **Removed page**: https://docs.factory.ai/guides/skills/automated-qa
- **Removed page**: https://docs.factory.ai/changelog/1-10.md
- **Removed page**: https://docs.factory.ai/changelog/release-notes.md
- **Removed page**: https://docs.factory.ai/guides/skills/ai-data-analyst.md
- **Removed page**: https://docs.factory.ai/cli/configuration/custom-slash-commands.md
- **Removed page**: https://docs.factory.ai/cli/features/droid-computers.md
- **Removed page**: https://docs.factory.ai/guides/hooks/git-workflows.md
- **Removed page**: https://docs.factory.ai/enterprise/identity-sso-and-scim.md
- **Removed page**: https://docs.factory.ai/reference/analytics-api.md
- **Removed page**: https://docs.factory.ai/guides/droid-exec/refactor-imports.md
- **Removed page**: https://docs.factory.ai/cli/configuration/plugins
- **Removed page**: https://docs.factory.ai/cli/configuration/settings.md
- **Removed page**: https://docs.factory.ai/cli/user-guides/specification-mode
- **Removed page**: https://docs.factory.ai/cli/account/droid-shield-plus.md
- **Removed page**: https://docs.factory.ai/cli/configuration/sandbox.md
- **Removed page**: https://docs.factory.ai/cli/droid-exec/overview
- **Removed page**: https://docs.factory.ai/guides/building/droid-exec-tutorial.md
- **Removed page**: https://docs.factory.ai/cli/features/droid-computers-byom
- **Removed page**: https://docs.factory.ai/integrations/ide-integrations
- **Removed page**: https://docs.factory.ai/cli/configuration/skills.md
- **Removed page**: https://docs.factory.ai/sitemap.xml
- **Removed page**: https://docs.factory.ai/api-reference/sessions/get-a-session.md
- **Removed page**: https://docs.factory.ai/cli/configuration/hooks-guide
- **Removed page**: https://docs.factory.ai/benchmarks/terminal-bench.md
- **Removed page**: https://docs.factory.ai/guides/droid-exec/refactor-fix-lint.md
- **Removed page**: https://docs.factory.ai/enterprise/network-and-deployment
- **Removed page**: https://docs.factory.ai/api-reference/automations/list-ci-automation-jobs.md

### coderabbit-docs

- **https://docs.coderabbit.ai/cli/claude-code-integration** (score 1, integration): A new video demonstration for the Claude Code integration was added to the documentation, which directly relates to the user's goal of tracking product features and integrations.
- **https://docs.coderabbit.ai/cli/cursor-integration** (score 2, product): The only changes detected in the documentation are an update to the YouTube subscriber count and the removal of a thumbnail image. These are considered metadata counters and minor UI changes, which are excluded by the monitoring goal and general noise rules.
- **https://docs.coderabbit.ai/cli/reference** (score 1, product): The documentation reflects a change in product features for the CodeRabbit CLI. The interactive review mode has been deprecated and replaced by a new 'fast' review policy, which is a significant change in how users interact with the tool.
- **https://docs.coderabbit.ai/cli/gemini-integration** (score 1, product): The page has transitioned from a 500 error state to a full documentation page detailing a new integration with Google's Gemini CLI. This includes new product features like the agentic loop, CLI commands, and specific pricing information regarding the Pro plan requirement for certain configuration features.
- **https://docs.coderabbit.ai/cli/wsl-windows** (score 2, deployment): The only changes detected are the removal of a thumbnail image and an update to the YouTube subscriber count. These are considered minor metadata/counter updates and do not relate to product features, pricing, integrations, security, or competitive positioning.
- **https://docs.coderabbit.ai/configuration/auto-review** (score 1, product): The documentation was updated to include new guidance on managing PR review limits, which is a key aspect of product usage and feature configuration. It also clarified default behaviors for draft PRs and branch targeting.
- **https://docs.coderabbit.ai/configuration/path-instructions** (score 2, security): The changes consist only of removing redundant image captions and duplicate image references at the bottom of the page. There are no changes to product features, pricing, integrations, or other goal-relevant content.
- **https://docs.coderabbit.ai/configuration/yaml-validator** (score 2, docs-only): The changes are minor UI and wording updates to the YAML configuration editor's loading state and description. They do not reflect changes to product features, pricing, integrations, security, or competitive positioning.
- **https://docs.coderabbit.ai/faq** (score 1, security): The documentation was updated to reflect a change in product features, specifically changing 'author exclusions' to 'title exclusions' as a method for controlling automated reviews.
- **https://docs.coderabbit.ai/finishing-touches/autofix** (score 1, pricing): The documentation was updated to include Azure DevOps as a supported platform for the Autofix feature, which is a significant integration update. Additionally, a previous limitation regarding stacked pull requests on Azure DevOps was removed.
- **https://docs.coderabbit.ai/cli** (score 1, pricing): The documentation reflects significant changes to product features and integrations, specifically the removal of the interactive review mode, the addition of a new fast review policy, and a new native integration with Claude Code.
- **https://docs.coderabbit.ai/changelog** (score 1, pricing): The documentation was updated with several new product features and integrations, including expanded platform support for 'Finishing Touches', the integration of 'CodeRabbit Plan' into the VS Code extension, and a new 'Automatic Repository Linking' feature for the Knowledge Base.
- **https://docs.coderabbit.ai/finishing-touches/custom-finishing-touches** (score 1, product): CodeRabbit has expanded the 'Custom recipes' feature to support GitLab merge requests, whereas it was previously limited to GitHub. This is a significant update to product integrations and feature availability.
- **New page**: https://docs.coderabbit.ai/platforms/self-hosted-gitlab
- **New page**: https://docs.coderabbit.ai/cli/index
- **New page**: https://docs.coderabbit.ai/pr-reviews/walkthroughs
- **New page**: https://docs.coderabbit.ai/slack-agent
- **New page**: https://docs.coderabbit.ai/llms-full.txt
- **New page**: https://docs.coderabbit.ai/pr-reviews/pre-merge-checks
- **New page**: https://docs.coderabbit.ai/reference/review-commands
- **Removed page**: https://docs.coderabbit.ai/getting-started/yaml-configuration
- **Removed page**: https://docs.coderabbit.ai/finishing-touches
- **Removed page**: https://docs.coderabbit.ai/knowledge-base
- **Removed page**: https://docs.coderabbit.ai/platforms/overview
- **Removed page**: https://docs.coderabbit.ai/finishing-touches/docstrings
- **Removed page**: https://docs.coderabbit.ai/knowledge-base/mcp-context
- **Removed page**: https://docs.coderabbit.ai/overview/architecture

## Sales / Learning Impact

No talk track updates needed this week.

## Next Recommended Action

Review the minor changes above if any look relevant. No action required otherwise.
