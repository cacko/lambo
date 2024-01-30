import logging
import typer
from lambo.config import app_config
from lambo.hue.client import Hue

app = typer.Typer()


@app.command()
def alert():
    Hue.signaling(colors=["2D2D2D", "72A5D3"])


@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    if not ctx.invoked_subcommand:
        print("test")
    


if __name__ == "__main__":
    Hue.register(hostname=app_config.hue.hostname, username=app_config.hue.username)
    app()
