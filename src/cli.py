import asyncio
from pathlib import Path
from typing import Optional

import typer
from rich import print

from .app import run_server

app = typer.Typer(no_args_is_help=True)


@app.command(help="Run the MCP Rug Pull demo server over stdio.")
def serve(
        # mode: str = typer.Option(
        #     "benign",
        #     "--mode",
        #     "-m",
        #     help="Initial mode: 'benign' or 'malicious'.",
        # ),
        # auto_update: bool = typer.Option(
        #     False,
        #     "--auto-update",
        #     help="Watch a JSON config for mode changes to simulate a rug pull.",
        # ),
        # config: Optional[Path] = typer.Option(
        #     None,
        #     "--config",
        #     "-c",
        #     help="Path to config/update.json with {'mode': 'benign'|'malicious'}",
        # ),
        # poll_seconds: float = typer.Option(
        #     2.0,
        #     "--poll-seconds",
        #     help="Poll interval for config watching (seconds).",
        # ),
):
    # if mode not in {"benign", "malicious"}:
    #     print("[red]Invalid --mode. Use 'benign' or 'malicious'.[/red]")
    #     raise typer.Exit(code=2)

    asyncio.run(
        run_server(
            # initial_mode=mode,
            # auto_update=auto_update,
            # config_path=str(config) if config else None,
            # poll_seconds=poll_seconds,
        )
    )


def main() -> None:
    """
    允许 `python -m mcp_rugpull_demo` 或等价方式运行带子命令的 CLI。
    """
    app()


def single_command() -> None:
    """
    提供一个“无子命令”的入口脚本。
    用法：`mcp-rugpull-demo-serve [OPTIONS]`
    """
    typer.run(serve)