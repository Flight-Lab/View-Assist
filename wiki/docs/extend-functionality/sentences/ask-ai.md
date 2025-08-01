---
title: Ask AI
---

# Ask AI

[![Image](https://img.youtube.com/vi/2xSvFU5Xlss/mqdefault.jpg)](https://www.youtube.com/watch?v=2xSvFU5Xlss)

Detailed install video: https://www.youtube.com/watch?v=2xSvFU5Xlss

Note that this video was recorded before the integration existed so you can skip the blueprint and view install as those are now automatically provided for you

### Description

This custom sentence allows for an on demand call to OpenAI for answering questions about life, love and happiness. Seriously though, this allows the user to use LLM to get answers to questions and greatly simplifies the need for coding a lot of these things by hand. Be warned, though. LLMs are known to provide bogus answers sometimes so use with caution.

### Usage

User says "Ask AI" plus the question to be answered

### Requirements

- **View**: [Info view](../views/info)
- **Integrations**: [Open AI Conversation](https://www.home-assistant.io/integrations/openai_conversation/)
- **API Key**: Must have a paid OpenAI account. Don't worry. The price to use is very low (pennies a month). See [this video](https://www.youtube.com/watch?v=4D6bIDcVOWc) for more information for pricing and set up

Advice from Discord user vash2695 wrote "In case it hasn't been mentioned already, you should set that integration to use "gpt-4o-mini". It's substantially smarter than 3.5 while also being cheaper!"

Additionally, user Andrew Steel is reporting that this blueprint will also work with local Ollama AI using [hass-ollama-conversation](https://github.com/ej52/hass-ollama-conversation#options)

## Changelog

| Version | Description     |
| ------- | --------------- |
| v 1.0.0 | Initial release |
