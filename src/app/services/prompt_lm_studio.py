import json
import requests
import app.config as config
from app.services.prompt_wrapper import get_web_page_prompt, get_document_prompt


def prompt_lm_studio_web_page(
    prompt: str,
    model: str
):
    response = requests.post(
        f"{config.LM_STUDIO_URL}/api/v1/chat",
        headers={
            "Authorization": f"Bearer {config.API_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "model": model,
            "input": prompt,
            "integrations": [
                {
                    "type": "plugin",
                    "id": "mcp/mcp-docker",
                    "allowed_tools": [
            "fetch",
            "browser_click",
            "browser_close",
            "browser_console_messages",
            "browser_drag",
            "browser_drop",
            "browser_evaluate",
            "browser_file_upload",
            "browser_fill_form",
            "browser_handle_dialog",
            "browser_hover",
            "browser_navigate",
            "browser_navigate_back",
            "browser_network_request",
            "browser_network_requests",
            "browser_press_key",
            "browser_resize",
            "browser_run_code_unsafe",
            "browser_select_option",
            "browser_snapshot",
            "browser_tabs",
            "browser_take_screenshot",
            "browser_type",
            "browser_wait_for"
        ]
                }
            ],
            "temperature": 0,
            "stream": True,
        },
        stream=True,
    )

    if not response.ok:
        print(response.status_code)
        print(response.text)

    response.raise_for_status()

    final_text = ""
    reasoning_text = ""

    for line in response.iter_lines(decode_unicode=True):
        if not line:
            continue

        # SSE format:
        # event: ...
        # data: {...}
        if line.startswith("data: "):
            data = line[6:]

            try:
                event = json.loads(data)
            except json.JSONDecodeError:
                continue

            # Print every event so you can see what LM Studio sends
            print(event)

            # Reasoning tokens
            if event.get("type") == "reasoning.delta":
                delta = event.get("content", "")
                reasoning_text += delta
                print(delta, end="", flush=True)

            # Normal answer tokens
            elif event.get("type") == "message.delta":
                delta = event.get("content", "")
                final_text += delta
                print(delta, end="", flush=True)

    print()

    return {
        "response": final_text,
        "reasoning": reasoning_text,
    }

def prompt_lm_studio_document(
    prompt: str,
    model: str
):
    response = requests.post(
        f"{config.LM_STUDIO_URL}/api/v1/chat",
        headers={
            "Authorization": f"Bearer {config.API_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "model": model,
            "input": prompt,
            "integrations": [
                {
                    "type": "plugin",
                    "id": "mcp/mcp-docker",
                    "allowed_tools": [
                        "ocr"
                    ]
                }
            ],
            "temperature": 0,
            "stream": True,
        },
        stream=True,
    )

    if not response.ok:
        print(response.status_code)
        print(response.text)

    response.raise_for_status()

    final_text = ""
    reasoning_text = ""

    for line in response.iter_lines(decode_unicode=True):
        if not line:
            continue

        if line.startswith("data: "):
            data = line[6:]

            try:
                event = json.loads(data)
            except json.JSONDecodeError:
                continue

            print(event)

            if event.get("type") == "reasoning.delta":
                delta = event.get("content", "")
                reasoning_text += delta
                print(delta, end="", flush=True)

            elif event.get("type") == "message.delta":
                delta = event.get("content", "")
                final_text += delta
                print(delta, end="", flush=True)

    print()

    return {
        "response": final_text,
        "reasoning": reasoning_text,
    }